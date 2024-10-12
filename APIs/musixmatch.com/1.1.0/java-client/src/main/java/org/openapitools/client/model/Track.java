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
 * a song in the Musixmatch database
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:43:43.628132-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Track {
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

  public static final String SERIALIZED_NAME_ALBUM_ID = "album_id";
  @SerializedName(SERIALIZED_NAME_ALBUM_ID)
  private BigDecimal albumId;

  public static final String SERIALIZED_NAME_ALBUM_NAME = "album_name";
  @SerializedName(SERIALIZED_NAME_ALBUM_NAME)
  private String albumName;

  public static final String SERIALIZED_NAME_ARTIST_ID = "artist_id";
  @SerializedName(SERIALIZED_NAME_ARTIST_ID)
  private BigDecimal artistId;

  public static final String SERIALIZED_NAME_ARTIST_MBID = "artist_mbid";
  @SerializedName(SERIALIZED_NAME_ARTIST_MBID)
  private String artistMbid;

  public static final String SERIALIZED_NAME_ARTIST_NAME = "artist_name";
  @SerializedName(SERIALIZED_NAME_ARTIST_NAME)
  private String artistName;

  public static final String SERIALIZED_NAME_COMMONTRACK_ID = "commontrack_id";
  @SerializedName(SERIALIZED_NAME_COMMONTRACK_ID)
  private BigDecimal commontrackId;

  public static final String SERIALIZED_NAME_COMMONTRACK_VANITY_ID = "commontrack_vanity_id";
  @SerializedName(SERIALIZED_NAME_COMMONTRACK_VANITY_ID)
  private String commontrackVanityId;

  public static final String SERIALIZED_NAME_EXPLICIT = "explicit";
  @SerializedName(SERIALIZED_NAME_EXPLICIT)
  private BigDecimal explicit;

  public static final String SERIALIZED_NAME_FIRST_RELEASE_DATE = "first_release_date";
  @SerializedName(SERIALIZED_NAME_FIRST_RELEASE_DATE)
  private String firstReleaseDate;

  public static final String SERIALIZED_NAME_HAS_LYRICS = "has_lyrics";
  @SerializedName(SERIALIZED_NAME_HAS_LYRICS)
  private BigDecimal hasLyrics;

  public static final String SERIALIZED_NAME_HAS_SUBTITLES = "has_subtitles";
  @SerializedName(SERIALIZED_NAME_HAS_SUBTITLES)
  private BigDecimal hasSubtitles;

  public static final String SERIALIZED_NAME_INSTRUMENTAL = "instrumental";
  @SerializedName(SERIALIZED_NAME_INSTRUMENTAL)
  private BigDecimal instrumental;

  public static final String SERIALIZED_NAME_LYRICS_ID = "lyrics_id";
  @SerializedName(SERIALIZED_NAME_LYRICS_ID)
  private BigDecimal lyricsId;

  public static final String SERIALIZED_NAME_NUM_FAVOURITE = "num_favourite";
  @SerializedName(SERIALIZED_NAME_NUM_FAVOURITE)
  private BigDecimal numFavourite;

  public static final String SERIALIZED_NAME_PRIMARY_GENRES = "primary_genres";
  @SerializedName(SERIALIZED_NAME_PRIMARY_GENRES)
  private AlbumPrimaryGenres primaryGenres;

  public static final String SERIALIZED_NAME_RESTRICTED = "restricted";
  @SerializedName(SERIALIZED_NAME_RESTRICTED)
  private BigDecimal restricted;

  public static final String SERIALIZED_NAME_SECONDARY_GENRES = "secondary_genres";
  @SerializedName(SERIALIZED_NAME_SECONDARY_GENRES)
  private AlbumPrimaryGenres secondaryGenres;

  public static final String SERIALIZED_NAME_SUBTITLE_ID = "subtitle_id";
  @SerializedName(SERIALIZED_NAME_SUBTITLE_ID)
  private BigDecimal subtitleId;

  public static final String SERIALIZED_NAME_TRACK_EDIT_URL = "track_edit_url";
  @SerializedName(SERIALIZED_NAME_TRACK_EDIT_URL)
  private String trackEditUrl;

  public static final String SERIALIZED_NAME_TRACK_ID = "track_id";
  @SerializedName(SERIALIZED_NAME_TRACK_ID)
  private BigDecimal trackId;

  public static final String SERIALIZED_NAME_TRACK_ISRC = "track_isrc";
  @SerializedName(SERIALIZED_NAME_TRACK_ISRC)
  private String trackIsrc;

  public static final String SERIALIZED_NAME_TRACK_LENGTH = "track_length";
  @SerializedName(SERIALIZED_NAME_TRACK_LENGTH)
  private BigDecimal trackLength;

  public static final String SERIALIZED_NAME_TRACK_MBID = "track_mbid";
  @SerializedName(SERIALIZED_NAME_TRACK_MBID)
  private String trackMbid;

  public static final String SERIALIZED_NAME_TRACK_NAME = "track_name";
  @SerializedName(SERIALIZED_NAME_TRACK_NAME)
  private String trackName;

  public static final String SERIALIZED_NAME_TRACK_NAME_TRANSLATION_LIST = "track_name_translation_list";
  @SerializedName(SERIALIZED_NAME_TRACK_NAME_TRANSLATION_LIST)
  private List<String> trackNameTranslationList = new ArrayList<>();

  public static final String SERIALIZED_NAME_TRACK_RATING = "track_rating";
  @SerializedName(SERIALIZED_NAME_TRACK_RATING)
  private BigDecimal trackRating;

  public static final String SERIALIZED_NAME_TRACK_SHARE_URL = "track_share_url";
  @SerializedName(SERIALIZED_NAME_TRACK_SHARE_URL)
  private String trackShareUrl;

  public static final String SERIALIZED_NAME_TRACK_SOUNDCLOUD_ID = "track_soundcloud_id";
  @SerializedName(SERIALIZED_NAME_TRACK_SOUNDCLOUD_ID)
  private BigDecimal trackSoundcloudId;

  public static final String SERIALIZED_NAME_TRACK_SPOTIFY_ID = "track_spotify_id";
  @SerializedName(SERIALIZED_NAME_TRACK_SPOTIFY_ID)
  private String trackSpotifyId;

  public static final String SERIALIZED_NAME_TRACK_XBOXMUSIC_ID = "track_xboxmusic_id";
  @SerializedName(SERIALIZED_NAME_TRACK_XBOXMUSIC_ID)
  private String trackXboxmusicId;

  public static final String SERIALIZED_NAME_UPDATED_TIME = "updated_time";
  @SerializedName(SERIALIZED_NAME_UPDATED_TIME)
  private String updatedTime;

  public Track() {
  }

  public Track albumCoverart100x100(String albumCoverart100x100) {
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


  public Track albumCoverart350x350(String albumCoverart350x350) {
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


  public Track albumCoverart500x500(String albumCoverart500x500) {
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


  public Track albumCoverart800x800(String albumCoverart800x800) {
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


  public Track albumId(BigDecimal albumId) {
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


  public Track albumName(String albumName) {
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


  public Track artistId(BigDecimal artistId) {
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


  public Track artistMbid(String artistMbid) {
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


  public Track artistName(String artistName) {
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


  public Track commontrackId(BigDecimal commontrackId) {
    this.commontrackId = commontrackId;
    return this;
  }

  /**
   * 
   * @return commontrackId
   */
  @javax.annotation.Nullable
  public BigDecimal getCommontrackId() {
    return commontrackId;
  }

  public void setCommontrackId(BigDecimal commontrackId) {
    this.commontrackId = commontrackId;
  }


  public Track commontrackVanityId(String commontrackVanityId) {
    this.commontrackVanityId = commontrackVanityId;
    return this;
  }

  /**
   * 
   * @return commontrackVanityId
   */
  @javax.annotation.Nullable
  public String getCommontrackVanityId() {
    return commontrackVanityId;
  }

  public void setCommontrackVanityId(String commontrackVanityId) {
    this.commontrackVanityId = commontrackVanityId;
  }


  public Track explicit(BigDecimal explicit) {
    this.explicit = explicit;
    return this;
  }

  /**
   * 
   * @return explicit
   */
  @javax.annotation.Nullable
  public BigDecimal getExplicit() {
    return explicit;
  }

  public void setExplicit(BigDecimal explicit) {
    this.explicit = explicit;
  }


  public Track firstReleaseDate(String firstReleaseDate) {
    this.firstReleaseDate = firstReleaseDate;
    return this;
  }

  /**
   * 
   * @return firstReleaseDate
   */
  @javax.annotation.Nullable
  public String getFirstReleaseDate() {
    return firstReleaseDate;
  }

  public void setFirstReleaseDate(String firstReleaseDate) {
    this.firstReleaseDate = firstReleaseDate;
  }


  public Track hasLyrics(BigDecimal hasLyrics) {
    this.hasLyrics = hasLyrics;
    return this;
  }

  /**
   * 
   * @return hasLyrics
   */
  @javax.annotation.Nullable
  public BigDecimal getHasLyrics() {
    return hasLyrics;
  }

  public void setHasLyrics(BigDecimal hasLyrics) {
    this.hasLyrics = hasLyrics;
  }


  public Track hasSubtitles(BigDecimal hasSubtitles) {
    this.hasSubtitles = hasSubtitles;
    return this;
  }

  /**
   * 
   * @return hasSubtitles
   */
  @javax.annotation.Nullable
  public BigDecimal getHasSubtitles() {
    return hasSubtitles;
  }

  public void setHasSubtitles(BigDecimal hasSubtitles) {
    this.hasSubtitles = hasSubtitles;
  }


  public Track instrumental(BigDecimal instrumental) {
    this.instrumental = instrumental;
    return this;
  }

  /**
   * 
   * @return instrumental
   */
  @javax.annotation.Nullable
  public BigDecimal getInstrumental() {
    return instrumental;
  }

  public void setInstrumental(BigDecimal instrumental) {
    this.instrumental = instrumental;
  }


  public Track lyricsId(BigDecimal lyricsId) {
    this.lyricsId = lyricsId;
    return this;
  }

  /**
   * 
   * @return lyricsId
   */
  @javax.annotation.Nullable
  public BigDecimal getLyricsId() {
    return lyricsId;
  }

  public void setLyricsId(BigDecimal lyricsId) {
    this.lyricsId = lyricsId;
  }


  public Track numFavourite(BigDecimal numFavourite) {
    this.numFavourite = numFavourite;
    return this;
  }

  /**
   * 
   * @return numFavourite
   */
  @javax.annotation.Nullable
  public BigDecimal getNumFavourite() {
    return numFavourite;
  }

  public void setNumFavourite(BigDecimal numFavourite) {
    this.numFavourite = numFavourite;
  }


  public Track primaryGenres(AlbumPrimaryGenres primaryGenres) {
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


  public Track restricted(BigDecimal restricted) {
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


  public Track secondaryGenres(AlbumPrimaryGenres secondaryGenres) {
    this.secondaryGenres = secondaryGenres;
    return this;
  }

  /**
   * Get secondaryGenres
   * @return secondaryGenres
   */
  @javax.annotation.Nullable
  public AlbumPrimaryGenres getSecondaryGenres() {
    return secondaryGenres;
  }

  public void setSecondaryGenres(AlbumPrimaryGenres secondaryGenres) {
    this.secondaryGenres = secondaryGenres;
  }


  public Track subtitleId(BigDecimal subtitleId) {
    this.subtitleId = subtitleId;
    return this;
  }

  /**
   * 
   * @return subtitleId
   */
  @javax.annotation.Nullable
  public BigDecimal getSubtitleId() {
    return subtitleId;
  }

  public void setSubtitleId(BigDecimal subtitleId) {
    this.subtitleId = subtitleId;
  }


  public Track trackEditUrl(String trackEditUrl) {
    this.trackEditUrl = trackEditUrl;
    return this;
  }

  /**
   * 
   * @return trackEditUrl
   */
  @javax.annotation.Nullable
  public String getTrackEditUrl() {
    return trackEditUrl;
  }

  public void setTrackEditUrl(String trackEditUrl) {
    this.trackEditUrl = trackEditUrl;
  }


  public Track trackId(BigDecimal trackId) {
    this.trackId = trackId;
    return this;
  }

  /**
   * 
   * @return trackId
   */
  @javax.annotation.Nullable
  public BigDecimal getTrackId() {
    return trackId;
  }

  public void setTrackId(BigDecimal trackId) {
    this.trackId = trackId;
  }


  public Track trackIsrc(String trackIsrc) {
    this.trackIsrc = trackIsrc;
    return this;
  }

  /**
   * 
   * @return trackIsrc
   */
  @javax.annotation.Nullable
  public String getTrackIsrc() {
    return trackIsrc;
  }

  public void setTrackIsrc(String trackIsrc) {
    this.trackIsrc = trackIsrc;
  }


  public Track trackLength(BigDecimal trackLength) {
    this.trackLength = trackLength;
    return this;
  }

  /**
   * 
   * @return trackLength
   */
  @javax.annotation.Nullable
  public BigDecimal getTrackLength() {
    return trackLength;
  }

  public void setTrackLength(BigDecimal trackLength) {
    this.trackLength = trackLength;
  }


  public Track trackMbid(String trackMbid) {
    this.trackMbid = trackMbid;
    return this;
  }

  /**
   * 
   * @return trackMbid
   */
  @javax.annotation.Nullable
  public String getTrackMbid() {
    return trackMbid;
  }

  public void setTrackMbid(String trackMbid) {
    this.trackMbid = trackMbid;
  }


  public Track trackName(String trackName) {
    this.trackName = trackName;
    return this;
  }

  /**
   * 
   * @return trackName
   */
  @javax.annotation.Nullable
  public String getTrackName() {
    return trackName;
  }

  public void setTrackName(String trackName) {
    this.trackName = trackName;
  }


  public Track trackNameTranslationList(List<String> trackNameTranslationList) {
    this.trackNameTranslationList = trackNameTranslationList;
    return this;
  }

  public Track addTrackNameTranslationListItem(String trackNameTranslationListItem) {
    if (this.trackNameTranslationList == null) {
      this.trackNameTranslationList = new ArrayList<>();
    }
    this.trackNameTranslationList.add(trackNameTranslationListItem);
    return this;
  }

  /**
   * Get trackNameTranslationList
   * @return trackNameTranslationList
   */
  @javax.annotation.Nullable
  public List<String> getTrackNameTranslationList() {
    return trackNameTranslationList;
  }

  public void setTrackNameTranslationList(List<String> trackNameTranslationList) {
    this.trackNameTranslationList = trackNameTranslationList;
  }


  public Track trackRating(BigDecimal trackRating) {
    this.trackRating = trackRating;
    return this;
  }

  /**
   * 
   * @return trackRating
   */
  @javax.annotation.Nullable
  public BigDecimal getTrackRating() {
    return trackRating;
  }

  public void setTrackRating(BigDecimal trackRating) {
    this.trackRating = trackRating;
  }


  public Track trackShareUrl(String trackShareUrl) {
    this.trackShareUrl = trackShareUrl;
    return this;
  }

  /**
   * 
   * @return trackShareUrl
   */
  @javax.annotation.Nullable
  public String getTrackShareUrl() {
    return trackShareUrl;
  }

  public void setTrackShareUrl(String trackShareUrl) {
    this.trackShareUrl = trackShareUrl;
  }


  public Track trackSoundcloudId(BigDecimal trackSoundcloudId) {
    this.trackSoundcloudId = trackSoundcloudId;
    return this;
  }

  /**
   * 
   * @return trackSoundcloudId
   */
  @javax.annotation.Nullable
  public BigDecimal getTrackSoundcloudId() {
    return trackSoundcloudId;
  }

  public void setTrackSoundcloudId(BigDecimal trackSoundcloudId) {
    this.trackSoundcloudId = trackSoundcloudId;
  }


  public Track trackSpotifyId(String trackSpotifyId) {
    this.trackSpotifyId = trackSpotifyId;
    return this;
  }

  /**
   * 
   * @return trackSpotifyId
   */
  @javax.annotation.Nullable
  public String getTrackSpotifyId() {
    return trackSpotifyId;
  }

  public void setTrackSpotifyId(String trackSpotifyId) {
    this.trackSpotifyId = trackSpotifyId;
  }


  public Track trackXboxmusicId(String trackXboxmusicId) {
    this.trackXboxmusicId = trackXboxmusicId;
    return this;
  }

  /**
   * 
   * @return trackXboxmusicId
   */
  @javax.annotation.Nullable
  public String getTrackXboxmusicId() {
    return trackXboxmusicId;
  }

  public void setTrackXboxmusicId(String trackXboxmusicId) {
    this.trackXboxmusicId = trackXboxmusicId;
  }


  public Track updatedTime(String updatedTime) {
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
    Track track = (Track) o;
    return Objects.equals(this.albumCoverart100x100, track.albumCoverart100x100) &&
        Objects.equals(this.albumCoverart350x350, track.albumCoverart350x350) &&
        Objects.equals(this.albumCoverart500x500, track.albumCoverart500x500) &&
        Objects.equals(this.albumCoverart800x800, track.albumCoverart800x800) &&
        Objects.equals(this.albumId, track.albumId) &&
        Objects.equals(this.albumName, track.albumName) &&
        Objects.equals(this.artistId, track.artistId) &&
        Objects.equals(this.artistMbid, track.artistMbid) &&
        Objects.equals(this.artistName, track.artistName) &&
        Objects.equals(this.commontrackId, track.commontrackId) &&
        Objects.equals(this.commontrackVanityId, track.commontrackVanityId) &&
        Objects.equals(this.explicit, track.explicit) &&
        Objects.equals(this.firstReleaseDate, track.firstReleaseDate) &&
        Objects.equals(this.hasLyrics, track.hasLyrics) &&
        Objects.equals(this.hasSubtitles, track.hasSubtitles) &&
        Objects.equals(this.instrumental, track.instrumental) &&
        Objects.equals(this.lyricsId, track.lyricsId) &&
        Objects.equals(this.numFavourite, track.numFavourite) &&
        Objects.equals(this.primaryGenres, track.primaryGenres) &&
        Objects.equals(this.restricted, track.restricted) &&
        Objects.equals(this.secondaryGenres, track.secondaryGenres) &&
        Objects.equals(this.subtitleId, track.subtitleId) &&
        Objects.equals(this.trackEditUrl, track.trackEditUrl) &&
        Objects.equals(this.trackId, track.trackId) &&
        Objects.equals(this.trackIsrc, track.trackIsrc) &&
        Objects.equals(this.trackLength, track.trackLength) &&
        Objects.equals(this.trackMbid, track.trackMbid) &&
        Objects.equals(this.trackName, track.trackName) &&
        Objects.equals(this.trackNameTranslationList, track.trackNameTranslationList) &&
        Objects.equals(this.trackRating, track.trackRating) &&
        Objects.equals(this.trackShareUrl, track.trackShareUrl) &&
        Objects.equals(this.trackSoundcloudId, track.trackSoundcloudId) &&
        Objects.equals(this.trackSpotifyId, track.trackSpotifyId) &&
        Objects.equals(this.trackXboxmusicId, track.trackXboxmusicId) &&
        Objects.equals(this.updatedTime, track.updatedTime);
  }

  @Override
  public int hashCode() {
    return Objects.hash(albumCoverart100x100, albumCoverart350x350, albumCoverart500x500, albumCoverart800x800, albumId, albumName, artistId, artistMbid, artistName, commontrackId, commontrackVanityId, explicit, firstReleaseDate, hasLyrics, hasSubtitles, instrumental, lyricsId, numFavourite, primaryGenres, restricted, secondaryGenres, subtitleId, trackEditUrl, trackId, trackIsrc, trackLength, trackMbid, trackName, trackNameTranslationList, trackRating, trackShareUrl, trackSoundcloudId, trackSpotifyId, trackXboxmusicId, updatedTime);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Track {\n");
    sb.append("    albumCoverart100x100: ").append(toIndentedString(albumCoverart100x100)).append("\n");
    sb.append("    albumCoverart350x350: ").append(toIndentedString(albumCoverart350x350)).append("\n");
    sb.append("    albumCoverart500x500: ").append(toIndentedString(albumCoverart500x500)).append("\n");
    sb.append("    albumCoverart800x800: ").append(toIndentedString(albumCoverart800x800)).append("\n");
    sb.append("    albumId: ").append(toIndentedString(albumId)).append("\n");
    sb.append("    albumName: ").append(toIndentedString(albumName)).append("\n");
    sb.append("    artistId: ").append(toIndentedString(artistId)).append("\n");
    sb.append("    artistMbid: ").append(toIndentedString(artistMbid)).append("\n");
    sb.append("    artistName: ").append(toIndentedString(artistName)).append("\n");
    sb.append("    commontrackId: ").append(toIndentedString(commontrackId)).append("\n");
    sb.append("    commontrackVanityId: ").append(toIndentedString(commontrackVanityId)).append("\n");
    sb.append("    explicit: ").append(toIndentedString(explicit)).append("\n");
    sb.append("    firstReleaseDate: ").append(toIndentedString(firstReleaseDate)).append("\n");
    sb.append("    hasLyrics: ").append(toIndentedString(hasLyrics)).append("\n");
    sb.append("    hasSubtitles: ").append(toIndentedString(hasSubtitles)).append("\n");
    sb.append("    instrumental: ").append(toIndentedString(instrumental)).append("\n");
    sb.append("    lyricsId: ").append(toIndentedString(lyricsId)).append("\n");
    sb.append("    numFavourite: ").append(toIndentedString(numFavourite)).append("\n");
    sb.append("    primaryGenres: ").append(toIndentedString(primaryGenres)).append("\n");
    sb.append("    restricted: ").append(toIndentedString(restricted)).append("\n");
    sb.append("    secondaryGenres: ").append(toIndentedString(secondaryGenres)).append("\n");
    sb.append("    subtitleId: ").append(toIndentedString(subtitleId)).append("\n");
    sb.append("    trackEditUrl: ").append(toIndentedString(trackEditUrl)).append("\n");
    sb.append("    trackId: ").append(toIndentedString(trackId)).append("\n");
    sb.append("    trackIsrc: ").append(toIndentedString(trackIsrc)).append("\n");
    sb.append("    trackLength: ").append(toIndentedString(trackLength)).append("\n");
    sb.append("    trackMbid: ").append(toIndentedString(trackMbid)).append("\n");
    sb.append("    trackName: ").append(toIndentedString(trackName)).append("\n");
    sb.append("    trackNameTranslationList: ").append(toIndentedString(trackNameTranslationList)).append("\n");
    sb.append("    trackRating: ").append(toIndentedString(trackRating)).append("\n");
    sb.append("    trackShareUrl: ").append(toIndentedString(trackShareUrl)).append("\n");
    sb.append("    trackSoundcloudId: ").append(toIndentedString(trackSoundcloudId)).append("\n");
    sb.append("    trackSpotifyId: ").append(toIndentedString(trackSpotifyId)).append("\n");
    sb.append("    trackXboxmusicId: ").append(toIndentedString(trackXboxmusicId)).append("\n");
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
    openapiFields.add("album_coverart_100x100");
    openapiFields.add("album_coverart_350x350");
    openapiFields.add("album_coverart_500x500");
    openapiFields.add("album_coverart_800x800");
    openapiFields.add("album_id");
    openapiFields.add("album_name");
    openapiFields.add("artist_id");
    openapiFields.add("artist_mbid");
    openapiFields.add("artist_name");
    openapiFields.add("commontrack_id");
    openapiFields.add("commontrack_vanity_id");
    openapiFields.add("explicit");
    openapiFields.add("first_release_date");
    openapiFields.add("has_lyrics");
    openapiFields.add("has_subtitles");
    openapiFields.add("instrumental");
    openapiFields.add("lyrics_id");
    openapiFields.add("num_favourite");
    openapiFields.add("primary_genres");
    openapiFields.add("restricted");
    openapiFields.add("secondary_genres");
    openapiFields.add("subtitle_id");
    openapiFields.add("track_edit_url");
    openapiFields.add("track_id");
    openapiFields.add("track_isrc");
    openapiFields.add("track_length");
    openapiFields.add("track_mbid");
    openapiFields.add("track_name");
    openapiFields.add("track_name_translation_list");
    openapiFields.add("track_rating");
    openapiFields.add("track_share_url");
    openapiFields.add("track_soundcloud_id");
    openapiFields.add("track_spotify_id");
    openapiFields.add("track_xboxmusic_id");
    openapiFields.add("updated_time");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Track
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Track.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Track is not found in the empty JSON string", Track.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Track.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Track` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
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
      if ((jsonObj.get("album_name") != null && !jsonObj.get("album_name").isJsonNull()) && !jsonObj.get("album_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `album_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("album_name").toString()));
      }
      if ((jsonObj.get("artist_mbid") != null && !jsonObj.get("artist_mbid").isJsonNull()) && !jsonObj.get("artist_mbid").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `artist_mbid` to be a primitive type in the JSON string but got `%s`", jsonObj.get("artist_mbid").toString()));
      }
      if ((jsonObj.get("artist_name") != null && !jsonObj.get("artist_name").isJsonNull()) && !jsonObj.get("artist_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `artist_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("artist_name").toString()));
      }
      if ((jsonObj.get("commontrack_vanity_id") != null && !jsonObj.get("commontrack_vanity_id").isJsonNull()) && !jsonObj.get("commontrack_vanity_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `commontrack_vanity_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("commontrack_vanity_id").toString()));
      }
      if ((jsonObj.get("first_release_date") != null && !jsonObj.get("first_release_date").isJsonNull()) && !jsonObj.get("first_release_date").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `first_release_date` to be a primitive type in the JSON string but got `%s`", jsonObj.get("first_release_date").toString()));
      }
      // validate the optional field `primary_genres`
      if (jsonObj.get("primary_genres") != null && !jsonObj.get("primary_genres").isJsonNull()) {
        AlbumPrimaryGenres.validateJsonElement(jsonObj.get("primary_genres"));
      }
      // validate the optional field `secondary_genres`
      if (jsonObj.get("secondary_genres") != null && !jsonObj.get("secondary_genres").isJsonNull()) {
        AlbumPrimaryGenres.validateJsonElement(jsonObj.get("secondary_genres"));
      }
      if ((jsonObj.get("track_edit_url") != null && !jsonObj.get("track_edit_url").isJsonNull()) && !jsonObj.get("track_edit_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `track_edit_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("track_edit_url").toString()));
      }
      if ((jsonObj.get("track_isrc") != null && !jsonObj.get("track_isrc").isJsonNull()) && !jsonObj.get("track_isrc").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `track_isrc` to be a primitive type in the JSON string but got `%s`", jsonObj.get("track_isrc").toString()));
      }
      if ((jsonObj.get("track_mbid") != null && !jsonObj.get("track_mbid").isJsonNull()) && !jsonObj.get("track_mbid").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `track_mbid` to be a primitive type in the JSON string but got `%s`", jsonObj.get("track_mbid").toString()));
      }
      if ((jsonObj.get("track_name") != null && !jsonObj.get("track_name").isJsonNull()) && !jsonObj.get("track_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `track_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("track_name").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("track_name_translation_list") != null && !jsonObj.get("track_name_translation_list").isJsonNull() && !jsonObj.get("track_name_translation_list").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `track_name_translation_list` to be an array in the JSON string but got `%s`", jsonObj.get("track_name_translation_list").toString()));
      }
      if ((jsonObj.get("track_share_url") != null && !jsonObj.get("track_share_url").isJsonNull()) && !jsonObj.get("track_share_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `track_share_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("track_share_url").toString()));
      }
      if ((jsonObj.get("track_spotify_id") != null && !jsonObj.get("track_spotify_id").isJsonNull()) && !jsonObj.get("track_spotify_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `track_spotify_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("track_spotify_id").toString()));
      }
      if ((jsonObj.get("track_xboxmusic_id") != null && !jsonObj.get("track_xboxmusic_id").isJsonNull()) && !jsonObj.get("track_xboxmusic_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `track_xboxmusic_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("track_xboxmusic_id").toString()));
      }
      if ((jsonObj.get("updated_time") != null && !jsonObj.get("updated_time").isJsonNull()) && !jsonObj.get("updated_time").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `updated_time` to be a primitive type in the JSON string but got `%s`", jsonObj.get("updated_time").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Track.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Track' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Track> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Track.class));

       return (TypeAdapter<T>) new TypeAdapter<Track>() {
           @Override
           public void write(JsonWriter out, Track value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Track read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Track given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Track
   * @throws IOException if the JSON string is invalid with respect to Track
   */
  public static Track fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Track.class);
  }

  /**
   * Convert an instance of Track to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

