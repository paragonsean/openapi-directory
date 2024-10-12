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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.AlbumPrimaryGenres;
import org.openapitools.client.model.AlbumSecondaryGenres;
import org.openapitools.client.model.ArtistArtistAliasListInner;
import org.openapitools.client.model.ArtistArtistCredits;
import org.openapitools.client.model.ArtistArtistNameTranslationListInner;

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
 * a artist in the Musixmatch database.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:43:43.628132-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Artist {
  public static final String SERIALIZED_NAME_ARTIST_ALIAS_LIST = "artist_alias_list";
  @SerializedName(SERIALIZED_NAME_ARTIST_ALIAS_LIST)
  private List<ArtistArtistAliasListInner> artistAliasList = new ArrayList<>();

  public static final String SERIALIZED_NAME_ARTIST_COMMENT = "artist_comment";
  @SerializedName(SERIALIZED_NAME_ARTIST_COMMENT)
  private String artistComment;

  public static final String SERIALIZED_NAME_ARTIST_COUNTRY = "artist_country";
  @SerializedName(SERIALIZED_NAME_ARTIST_COUNTRY)
  private String artistCountry;

  public static final String SERIALIZED_NAME_ARTIST_CREDITS = "artist_credits";
  @SerializedName(SERIALIZED_NAME_ARTIST_CREDITS)
  private ArtistArtistCredits artistCredits;

  public static final String SERIALIZED_NAME_ARTIST_EDIT_URL = "artist_edit_url";
  @SerializedName(SERIALIZED_NAME_ARTIST_EDIT_URL)
  private String artistEditUrl;

  public static final String SERIALIZED_NAME_ARTIST_ID = "artist_id";
  @SerializedName(SERIALIZED_NAME_ARTIST_ID)
  private BigDecimal artistId;

  public static final String SERIALIZED_NAME_ARTIST_MBID = "artist_mbid";
  @SerializedName(SERIALIZED_NAME_ARTIST_MBID)
  private String artistMbid;

  public static final String SERIALIZED_NAME_ARTIST_NAME = "artist_name";
  @SerializedName(SERIALIZED_NAME_ARTIST_NAME)
  private String artistName;

  public static final String SERIALIZED_NAME_ARTIST_NAME_TRANSLATION_LIST = "artist_name_translation_list";
  @SerializedName(SERIALIZED_NAME_ARTIST_NAME_TRANSLATION_LIST)
  private List<ArtistArtistNameTranslationListInner> artistNameTranslationList = new ArrayList<>();

  public static final String SERIALIZED_NAME_ARTIST_RATING = "artist_rating";
  @SerializedName(SERIALIZED_NAME_ARTIST_RATING)
  private BigDecimal artistRating;

  public static final String SERIALIZED_NAME_ARTIST_SHARE_URL = "artist_share_url";
  @SerializedName(SERIALIZED_NAME_ARTIST_SHARE_URL)
  private String artistShareUrl;

  public static final String SERIALIZED_NAME_ARTIST_TWITTER_URL = "artist_twitter_url";
  @SerializedName(SERIALIZED_NAME_ARTIST_TWITTER_URL)
  private String artistTwitterUrl;

  public static final String SERIALIZED_NAME_ARTIST_VANITY_ID = "artist_vanity_id";
  @SerializedName(SERIALIZED_NAME_ARTIST_VANITY_ID)
  private String artistVanityId;

  public static final String SERIALIZED_NAME_MANAGED = "managed";
  @SerializedName(SERIALIZED_NAME_MANAGED)
  private BigDecimal managed;

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

  public Artist() {
  }

  public Artist artistAliasList(List<ArtistArtistAliasListInner> artistAliasList) {
    this.artistAliasList = artistAliasList;
    return this;
  }

  public Artist addArtistAliasListItem(ArtistArtistAliasListInner artistAliasListItem) {
    if (this.artistAliasList == null) {
      this.artistAliasList = new ArrayList<>();
    }
    this.artistAliasList.add(artistAliasListItem);
    return this;
  }

  /**
   * Get artistAliasList
   * @return artistAliasList
   */
  @javax.annotation.Nullable
  public List<ArtistArtistAliasListInner> getArtistAliasList() {
    return artistAliasList;
  }

  public void setArtistAliasList(List<ArtistArtistAliasListInner> artistAliasList) {
    this.artistAliasList = artistAliasList;
  }


  public Artist artistComment(String artistComment) {
    this.artistComment = artistComment;
    return this;
  }

  /**
   * 
   * @return artistComment
   */
  @javax.annotation.Nullable
  public String getArtistComment() {
    return artistComment;
  }

  public void setArtistComment(String artistComment) {
    this.artistComment = artistComment;
  }


  public Artist artistCountry(String artistCountry) {
    this.artistCountry = artistCountry;
    return this;
  }

  /**
   * 
   * @return artistCountry
   */
  @javax.annotation.Nullable
  public String getArtistCountry() {
    return artistCountry;
  }

  public void setArtistCountry(String artistCountry) {
    this.artistCountry = artistCountry;
  }


  public Artist artistCredits(ArtistArtistCredits artistCredits) {
    this.artistCredits = artistCredits;
    return this;
  }

  /**
   * Get artistCredits
   * @return artistCredits
   */
  @javax.annotation.Nullable
  public ArtistArtistCredits getArtistCredits() {
    return artistCredits;
  }

  public void setArtistCredits(ArtistArtistCredits artistCredits) {
    this.artistCredits = artistCredits;
  }


  public Artist artistEditUrl(String artistEditUrl) {
    this.artistEditUrl = artistEditUrl;
    return this;
  }

  /**
   * 
   * @return artistEditUrl
   */
  @javax.annotation.Nullable
  public String getArtistEditUrl() {
    return artistEditUrl;
  }

  public void setArtistEditUrl(String artistEditUrl) {
    this.artistEditUrl = artistEditUrl;
  }


  public Artist artistId(BigDecimal artistId) {
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


  public Artist artistMbid(String artistMbid) {
    this.artistMbid = artistMbid;
    return this;
  }

  /**
   * 
   * @return artistMbid
   */
  @javax.annotation.Nullable
  public String getArtistMbid() {
    return artistMbid;
  }

  public void setArtistMbid(String artistMbid) {
    this.artistMbid = artistMbid;
  }


  public Artist artistName(String artistName) {
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


  public Artist artistNameTranslationList(List<ArtistArtistNameTranslationListInner> artistNameTranslationList) {
    this.artistNameTranslationList = artistNameTranslationList;
    return this;
  }

  public Artist addArtistNameTranslationListItem(ArtistArtistNameTranslationListInner artistNameTranslationListItem) {
    if (this.artistNameTranslationList == null) {
      this.artistNameTranslationList = new ArrayList<>();
    }
    this.artistNameTranslationList.add(artistNameTranslationListItem);
    return this;
  }

  /**
   * Get artistNameTranslationList
   * @return artistNameTranslationList
   */
  @javax.annotation.Nullable
  public List<ArtistArtistNameTranslationListInner> getArtistNameTranslationList() {
    return artistNameTranslationList;
  }

  public void setArtistNameTranslationList(List<ArtistArtistNameTranslationListInner> artistNameTranslationList) {
    this.artistNameTranslationList = artistNameTranslationList;
  }


  public Artist artistRating(BigDecimal artistRating) {
    this.artistRating = artistRating;
    return this;
  }

  /**
   * 
   * @return artistRating
   */
  @javax.annotation.Nullable
  public BigDecimal getArtistRating() {
    return artistRating;
  }

  public void setArtistRating(BigDecimal artistRating) {
    this.artistRating = artistRating;
  }


  public Artist artistShareUrl(String artistShareUrl) {
    this.artistShareUrl = artistShareUrl;
    return this;
  }

  /**
   * 
   * @return artistShareUrl
   */
  @javax.annotation.Nullable
  public String getArtistShareUrl() {
    return artistShareUrl;
  }

  public void setArtistShareUrl(String artistShareUrl) {
    this.artistShareUrl = artistShareUrl;
  }


  public Artist artistTwitterUrl(String artistTwitterUrl) {
    this.artistTwitterUrl = artistTwitterUrl;
    return this;
  }

  /**
   * 
   * @return artistTwitterUrl
   */
  @javax.annotation.Nullable
  public String getArtistTwitterUrl() {
    return artistTwitterUrl;
  }

  public void setArtistTwitterUrl(String artistTwitterUrl) {
    this.artistTwitterUrl = artistTwitterUrl;
  }


  public Artist artistVanityId(String artistVanityId) {
    this.artistVanityId = artistVanityId;
    return this;
  }

  /**
   * 
   * @return artistVanityId
   */
  @javax.annotation.Nullable
  public String getArtistVanityId() {
    return artistVanityId;
  }

  public void setArtistVanityId(String artistVanityId) {
    this.artistVanityId = artistVanityId;
  }


  public Artist managed(BigDecimal managed) {
    this.managed = managed;
    return this;
  }

  /**
   * 
   * @return managed
   */
  @javax.annotation.Nullable
  public BigDecimal getManaged() {
    return managed;
  }

  public void setManaged(BigDecimal managed) {
    this.managed = managed;
  }


  public Artist primaryGenres(AlbumPrimaryGenres primaryGenres) {
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


  public Artist restricted(BigDecimal restricted) {
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


  public Artist secondaryGenres(AlbumSecondaryGenres secondaryGenres) {
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


  public Artist updatedTime(String updatedTime) {
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
    Artist artist = (Artist) o;
    return Objects.equals(this.artistAliasList, artist.artistAliasList) &&
        Objects.equals(this.artistComment, artist.artistComment) &&
        Objects.equals(this.artistCountry, artist.artistCountry) &&
        Objects.equals(this.artistCredits, artist.artistCredits) &&
        Objects.equals(this.artistEditUrl, artist.artistEditUrl) &&
        Objects.equals(this.artistId, artist.artistId) &&
        Objects.equals(this.artistMbid, artist.artistMbid) &&
        Objects.equals(this.artistName, artist.artistName) &&
        Objects.equals(this.artistNameTranslationList, artist.artistNameTranslationList) &&
        Objects.equals(this.artistRating, artist.artistRating) &&
        Objects.equals(this.artistShareUrl, artist.artistShareUrl) &&
        Objects.equals(this.artistTwitterUrl, artist.artistTwitterUrl) &&
        Objects.equals(this.artistVanityId, artist.artistVanityId) &&
        Objects.equals(this.managed, artist.managed) &&
        Objects.equals(this.primaryGenres, artist.primaryGenres) &&
        Objects.equals(this.restricted, artist.restricted) &&
        Objects.equals(this.secondaryGenres, artist.secondaryGenres) &&
        Objects.equals(this.updatedTime, artist.updatedTime);
  }

  @Override
  public int hashCode() {
    return Objects.hash(artistAliasList, artistComment, artistCountry, artistCredits, artistEditUrl, artistId, artistMbid, artistName, artistNameTranslationList, artistRating, artistShareUrl, artistTwitterUrl, artistVanityId, managed, primaryGenres, restricted, secondaryGenres, updatedTime);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Artist {\n");
    sb.append("    artistAliasList: ").append(toIndentedString(artistAliasList)).append("\n");
    sb.append("    artistComment: ").append(toIndentedString(artistComment)).append("\n");
    sb.append("    artistCountry: ").append(toIndentedString(artistCountry)).append("\n");
    sb.append("    artistCredits: ").append(toIndentedString(artistCredits)).append("\n");
    sb.append("    artistEditUrl: ").append(toIndentedString(artistEditUrl)).append("\n");
    sb.append("    artistId: ").append(toIndentedString(artistId)).append("\n");
    sb.append("    artistMbid: ").append(toIndentedString(artistMbid)).append("\n");
    sb.append("    artistName: ").append(toIndentedString(artistName)).append("\n");
    sb.append("    artistNameTranslationList: ").append(toIndentedString(artistNameTranslationList)).append("\n");
    sb.append("    artistRating: ").append(toIndentedString(artistRating)).append("\n");
    sb.append("    artistShareUrl: ").append(toIndentedString(artistShareUrl)).append("\n");
    sb.append("    artistTwitterUrl: ").append(toIndentedString(artistTwitterUrl)).append("\n");
    sb.append("    artistVanityId: ").append(toIndentedString(artistVanityId)).append("\n");
    sb.append("    managed: ").append(toIndentedString(managed)).append("\n");
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
    openapiFields.add("artist_alias_list");
    openapiFields.add("artist_comment");
    openapiFields.add("artist_country");
    openapiFields.add("artist_credits");
    openapiFields.add("artist_edit_url");
    openapiFields.add("artist_id");
    openapiFields.add("artist_mbid");
    openapiFields.add("artist_name");
    openapiFields.add("artist_name_translation_list");
    openapiFields.add("artist_rating");
    openapiFields.add("artist_share_url");
    openapiFields.add("artist_twitter_url");
    openapiFields.add("artist_vanity_id");
    openapiFields.add("managed");
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
   * @throws IOException if the JSON Element is invalid with respect to Artist
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Artist.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Artist is not found in the empty JSON string", Artist.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Artist.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Artist` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("artist_alias_list") != null && !jsonObj.get("artist_alias_list").isJsonNull()) {
        JsonArray jsonArrayartistAliasList = jsonObj.getAsJsonArray("artist_alias_list");
        if (jsonArrayartistAliasList != null) {
          // ensure the json data is an array
          if (!jsonObj.get("artist_alias_list").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `artist_alias_list` to be an array in the JSON string but got `%s`", jsonObj.get("artist_alias_list").toString()));
          }

          // validate the optional field `artist_alias_list` (array)
          for (int i = 0; i < jsonArrayartistAliasList.size(); i++) {
            ArtistArtistAliasListInner.validateJsonElement(jsonArrayartistAliasList.get(i));
          };
        }
      }
      if ((jsonObj.get("artist_comment") != null && !jsonObj.get("artist_comment").isJsonNull()) && !jsonObj.get("artist_comment").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `artist_comment` to be a primitive type in the JSON string but got `%s`", jsonObj.get("artist_comment").toString()));
      }
      if ((jsonObj.get("artist_country") != null && !jsonObj.get("artist_country").isJsonNull()) && !jsonObj.get("artist_country").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `artist_country` to be a primitive type in the JSON string but got `%s`", jsonObj.get("artist_country").toString()));
      }
      // validate the optional field `artist_credits`
      if (jsonObj.get("artist_credits") != null && !jsonObj.get("artist_credits").isJsonNull()) {
        ArtistArtistCredits.validateJsonElement(jsonObj.get("artist_credits"));
      }
      if ((jsonObj.get("artist_edit_url") != null && !jsonObj.get("artist_edit_url").isJsonNull()) && !jsonObj.get("artist_edit_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `artist_edit_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("artist_edit_url").toString()));
      }
      if ((jsonObj.get("artist_mbid") != null && !jsonObj.get("artist_mbid").isJsonNull()) && !jsonObj.get("artist_mbid").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `artist_mbid` to be a primitive type in the JSON string but got `%s`", jsonObj.get("artist_mbid").toString()));
      }
      if ((jsonObj.get("artist_name") != null && !jsonObj.get("artist_name").isJsonNull()) && !jsonObj.get("artist_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `artist_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("artist_name").toString()));
      }
      if (jsonObj.get("artist_name_translation_list") != null && !jsonObj.get("artist_name_translation_list").isJsonNull()) {
        JsonArray jsonArrayartistNameTranslationList = jsonObj.getAsJsonArray("artist_name_translation_list");
        if (jsonArrayartistNameTranslationList != null) {
          // ensure the json data is an array
          if (!jsonObj.get("artist_name_translation_list").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `artist_name_translation_list` to be an array in the JSON string but got `%s`", jsonObj.get("artist_name_translation_list").toString()));
          }

          // validate the optional field `artist_name_translation_list` (array)
          for (int i = 0; i < jsonArrayartistNameTranslationList.size(); i++) {
            ArtistArtistNameTranslationListInner.validateJsonElement(jsonArrayartistNameTranslationList.get(i));
          };
        }
      }
      if ((jsonObj.get("artist_share_url") != null && !jsonObj.get("artist_share_url").isJsonNull()) && !jsonObj.get("artist_share_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `artist_share_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("artist_share_url").toString()));
      }
      if ((jsonObj.get("artist_twitter_url") != null && !jsonObj.get("artist_twitter_url").isJsonNull()) && !jsonObj.get("artist_twitter_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `artist_twitter_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("artist_twitter_url").toString()));
      }
      if ((jsonObj.get("artist_vanity_id") != null && !jsonObj.get("artist_vanity_id").isJsonNull()) && !jsonObj.get("artist_vanity_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `artist_vanity_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("artist_vanity_id").toString()));
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
       if (!Artist.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Artist' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Artist> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Artist.class));

       return (TypeAdapter<T>) new TypeAdapter<Artist>() {
           @Override
           public void write(JsonWriter out, Artist value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Artist read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Artist given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Artist
   * @throws IOException if the JSON string is invalid with respect to Artist
   */
  public static Artist fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Artist.class);
  }

  /**
   * Convert an instance of Artist to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

