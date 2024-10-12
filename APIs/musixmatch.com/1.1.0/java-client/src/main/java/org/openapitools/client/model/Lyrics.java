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
 * a Lyrics in the Musixmatch database.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:43:43.628132-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Lyrics {
  public static final String SERIALIZED_NAME_ACTION_REQUESTED = "action_requested";
  @SerializedName(SERIALIZED_NAME_ACTION_REQUESTED)
  private String actionRequested;

  public static final String SERIALIZED_NAME_CAN_EDIT = "can_edit";
  @SerializedName(SERIALIZED_NAME_CAN_EDIT)
  private BigDecimal canEdit;

  public static final String SERIALIZED_NAME_EXPLICIT = "explicit";
  @SerializedName(SERIALIZED_NAME_EXPLICIT)
  private BigDecimal explicit;

  public static final String SERIALIZED_NAME_HTML_TRACKING_URL = "html_tracking_url";
  @SerializedName(SERIALIZED_NAME_HTML_TRACKING_URL)
  private String htmlTrackingUrl;

  public static final String SERIALIZED_NAME_INSTRUMENTAL = "instrumental";
  @SerializedName(SERIALIZED_NAME_INSTRUMENTAL)
  private BigDecimal instrumental;

  public static final String SERIALIZED_NAME_LOCKED = "locked";
  @SerializedName(SERIALIZED_NAME_LOCKED)
  private BigDecimal locked;

  public static final String SERIALIZED_NAME_LYRICS_BODY = "lyrics_body";
  @SerializedName(SERIALIZED_NAME_LYRICS_BODY)
  private String lyricsBody;

  public static final String SERIALIZED_NAME_LYRICS_COPYRIGHT = "lyrics_copyright";
  @SerializedName(SERIALIZED_NAME_LYRICS_COPYRIGHT)
  private String lyricsCopyright;

  public static final String SERIALIZED_NAME_LYRICS_ID = "lyrics_id";
  @SerializedName(SERIALIZED_NAME_LYRICS_ID)
  private BigDecimal lyricsId;

  public static final String SERIALIZED_NAME_LYRICS_LANGUAGE = "lyrics_language";
  @SerializedName(SERIALIZED_NAME_LYRICS_LANGUAGE)
  private String lyricsLanguage;

  public static final String SERIALIZED_NAME_LYRICS_LANGUAGE_DESCRIPTION = "lyrics_language_description";
  @SerializedName(SERIALIZED_NAME_LYRICS_LANGUAGE_DESCRIPTION)
  private String lyricsLanguageDescription;

  public static final String SERIALIZED_NAME_PIXEL_TRACKING_URL = "pixel_tracking_url";
  @SerializedName(SERIALIZED_NAME_PIXEL_TRACKING_URL)
  private String pixelTrackingUrl;

  public static final String SERIALIZED_NAME_PUBLISHER_LIST = "publisher_list";
  @SerializedName(SERIALIZED_NAME_PUBLISHER_LIST)
  private List<String> publisherList = new ArrayList<>();

  public static final String SERIALIZED_NAME_RESTRICTED = "restricted";
  @SerializedName(SERIALIZED_NAME_RESTRICTED)
  private BigDecimal restricted;

  public static final String SERIALIZED_NAME_SCRIPT_TRACKING_URL = "script_tracking_url";
  @SerializedName(SERIALIZED_NAME_SCRIPT_TRACKING_URL)
  private String scriptTrackingUrl;

  public static final String SERIALIZED_NAME_UPDATED_TIME = "updated_time";
  @SerializedName(SERIALIZED_NAME_UPDATED_TIME)
  private String updatedTime;

  public static final String SERIALIZED_NAME_VERIFIED = "verified";
  @SerializedName(SERIALIZED_NAME_VERIFIED)
  private BigDecimal verified;

  public static final String SERIALIZED_NAME_WRITER_LIST = "writer_list";
  @SerializedName(SERIALIZED_NAME_WRITER_LIST)
  private List<String> writerList = new ArrayList<>();

  public Lyrics() {
  }

  public Lyrics actionRequested(String actionRequested) {
    this.actionRequested = actionRequested;
    return this;
  }

  /**
   * 
   * @return actionRequested
   */
  @javax.annotation.Nullable
  public String getActionRequested() {
    return actionRequested;
  }

  public void setActionRequested(String actionRequested) {
    this.actionRequested = actionRequested;
  }


  public Lyrics canEdit(BigDecimal canEdit) {
    this.canEdit = canEdit;
    return this;
  }

  /**
   * 
   * @return canEdit
   */
  @javax.annotation.Nullable
  public BigDecimal getCanEdit() {
    return canEdit;
  }

  public void setCanEdit(BigDecimal canEdit) {
    this.canEdit = canEdit;
  }


  public Lyrics explicit(BigDecimal explicit) {
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


  public Lyrics htmlTrackingUrl(String htmlTrackingUrl) {
    this.htmlTrackingUrl = htmlTrackingUrl;
    return this;
  }

  /**
   * 
   * @return htmlTrackingUrl
   */
  @javax.annotation.Nullable
  public String getHtmlTrackingUrl() {
    return htmlTrackingUrl;
  }

  public void setHtmlTrackingUrl(String htmlTrackingUrl) {
    this.htmlTrackingUrl = htmlTrackingUrl;
  }


  public Lyrics instrumental(BigDecimal instrumental) {
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


  public Lyrics locked(BigDecimal locked) {
    this.locked = locked;
    return this;
  }

  /**
   * 
   * @return locked
   */
  @javax.annotation.Nullable
  public BigDecimal getLocked() {
    return locked;
  }

  public void setLocked(BigDecimal locked) {
    this.locked = locked;
  }


  public Lyrics lyricsBody(String lyricsBody) {
    this.lyricsBody = lyricsBody;
    return this;
  }

  /**
   * 
   * @return lyricsBody
   */
  @javax.annotation.Nullable
  public String getLyricsBody() {
    return lyricsBody;
  }

  public void setLyricsBody(String lyricsBody) {
    this.lyricsBody = lyricsBody;
  }


  public Lyrics lyricsCopyright(String lyricsCopyright) {
    this.lyricsCopyright = lyricsCopyright;
    return this;
  }

  /**
   * 
   * @return lyricsCopyright
   */
  @javax.annotation.Nullable
  public String getLyricsCopyright() {
    return lyricsCopyright;
  }

  public void setLyricsCopyright(String lyricsCopyright) {
    this.lyricsCopyright = lyricsCopyright;
  }


  public Lyrics lyricsId(BigDecimal lyricsId) {
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


  public Lyrics lyricsLanguage(String lyricsLanguage) {
    this.lyricsLanguage = lyricsLanguage;
    return this;
  }

  /**
   * 
   * @return lyricsLanguage
   */
  @javax.annotation.Nullable
  public String getLyricsLanguage() {
    return lyricsLanguage;
  }

  public void setLyricsLanguage(String lyricsLanguage) {
    this.lyricsLanguage = lyricsLanguage;
  }


  public Lyrics lyricsLanguageDescription(String lyricsLanguageDescription) {
    this.lyricsLanguageDescription = lyricsLanguageDescription;
    return this;
  }

  /**
   * 
   * @return lyricsLanguageDescription
   */
  @javax.annotation.Nullable
  public String getLyricsLanguageDescription() {
    return lyricsLanguageDescription;
  }

  public void setLyricsLanguageDescription(String lyricsLanguageDescription) {
    this.lyricsLanguageDescription = lyricsLanguageDescription;
  }


  public Lyrics pixelTrackingUrl(String pixelTrackingUrl) {
    this.pixelTrackingUrl = pixelTrackingUrl;
    return this;
  }

  /**
   * 
   * @return pixelTrackingUrl
   */
  @javax.annotation.Nullable
  public String getPixelTrackingUrl() {
    return pixelTrackingUrl;
  }

  public void setPixelTrackingUrl(String pixelTrackingUrl) {
    this.pixelTrackingUrl = pixelTrackingUrl;
  }


  public Lyrics publisherList(List<String> publisherList) {
    this.publisherList = publisherList;
    return this;
  }

  public Lyrics addPublisherListItem(String publisherListItem) {
    if (this.publisherList == null) {
      this.publisherList = new ArrayList<>();
    }
    this.publisherList.add(publisherListItem);
    return this;
  }

  /**
   * Get publisherList
   * @return publisherList
   */
  @javax.annotation.Nullable
  public List<String> getPublisherList() {
    return publisherList;
  }

  public void setPublisherList(List<String> publisherList) {
    this.publisherList = publisherList;
  }


  public Lyrics restricted(BigDecimal restricted) {
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


  public Lyrics scriptTrackingUrl(String scriptTrackingUrl) {
    this.scriptTrackingUrl = scriptTrackingUrl;
    return this;
  }

  /**
   * 
   * @return scriptTrackingUrl
   */
  @javax.annotation.Nullable
  public String getScriptTrackingUrl() {
    return scriptTrackingUrl;
  }

  public void setScriptTrackingUrl(String scriptTrackingUrl) {
    this.scriptTrackingUrl = scriptTrackingUrl;
  }


  public Lyrics updatedTime(String updatedTime) {
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


  public Lyrics verified(BigDecimal verified) {
    this.verified = verified;
    return this;
  }

  /**
   * 
   * @return verified
   */
  @javax.annotation.Nullable
  public BigDecimal getVerified() {
    return verified;
  }

  public void setVerified(BigDecimal verified) {
    this.verified = verified;
  }


  public Lyrics writerList(List<String> writerList) {
    this.writerList = writerList;
    return this;
  }

  public Lyrics addWriterListItem(String writerListItem) {
    if (this.writerList == null) {
      this.writerList = new ArrayList<>();
    }
    this.writerList.add(writerListItem);
    return this;
  }

  /**
   * Get writerList
   * @return writerList
   */
  @javax.annotation.Nullable
  public List<String> getWriterList() {
    return writerList;
  }

  public void setWriterList(List<String> writerList) {
    this.writerList = writerList;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Lyrics lyrics = (Lyrics) o;
    return Objects.equals(this.actionRequested, lyrics.actionRequested) &&
        Objects.equals(this.canEdit, lyrics.canEdit) &&
        Objects.equals(this.explicit, lyrics.explicit) &&
        Objects.equals(this.htmlTrackingUrl, lyrics.htmlTrackingUrl) &&
        Objects.equals(this.instrumental, lyrics.instrumental) &&
        Objects.equals(this.locked, lyrics.locked) &&
        Objects.equals(this.lyricsBody, lyrics.lyricsBody) &&
        Objects.equals(this.lyricsCopyright, lyrics.lyricsCopyright) &&
        Objects.equals(this.lyricsId, lyrics.lyricsId) &&
        Objects.equals(this.lyricsLanguage, lyrics.lyricsLanguage) &&
        Objects.equals(this.lyricsLanguageDescription, lyrics.lyricsLanguageDescription) &&
        Objects.equals(this.pixelTrackingUrl, lyrics.pixelTrackingUrl) &&
        Objects.equals(this.publisherList, lyrics.publisherList) &&
        Objects.equals(this.restricted, lyrics.restricted) &&
        Objects.equals(this.scriptTrackingUrl, lyrics.scriptTrackingUrl) &&
        Objects.equals(this.updatedTime, lyrics.updatedTime) &&
        Objects.equals(this.verified, lyrics.verified) &&
        Objects.equals(this.writerList, lyrics.writerList);
  }

  @Override
  public int hashCode() {
    return Objects.hash(actionRequested, canEdit, explicit, htmlTrackingUrl, instrumental, locked, lyricsBody, lyricsCopyright, lyricsId, lyricsLanguage, lyricsLanguageDescription, pixelTrackingUrl, publisherList, restricted, scriptTrackingUrl, updatedTime, verified, writerList);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Lyrics {\n");
    sb.append("    actionRequested: ").append(toIndentedString(actionRequested)).append("\n");
    sb.append("    canEdit: ").append(toIndentedString(canEdit)).append("\n");
    sb.append("    explicit: ").append(toIndentedString(explicit)).append("\n");
    sb.append("    htmlTrackingUrl: ").append(toIndentedString(htmlTrackingUrl)).append("\n");
    sb.append("    instrumental: ").append(toIndentedString(instrumental)).append("\n");
    sb.append("    locked: ").append(toIndentedString(locked)).append("\n");
    sb.append("    lyricsBody: ").append(toIndentedString(lyricsBody)).append("\n");
    sb.append("    lyricsCopyright: ").append(toIndentedString(lyricsCopyright)).append("\n");
    sb.append("    lyricsId: ").append(toIndentedString(lyricsId)).append("\n");
    sb.append("    lyricsLanguage: ").append(toIndentedString(lyricsLanguage)).append("\n");
    sb.append("    lyricsLanguageDescription: ").append(toIndentedString(lyricsLanguageDescription)).append("\n");
    sb.append("    pixelTrackingUrl: ").append(toIndentedString(pixelTrackingUrl)).append("\n");
    sb.append("    publisherList: ").append(toIndentedString(publisherList)).append("\n");
    sb.append("    restricted: ").append(toIndentedString(restricted)).append("\n");
    sb.append("    scriptTrackingUrl: ").append(toIndentedString(scriptTrackingUrl)).append("\n");
    sb.append("    updatedTime: ").append(toIndentedString(updatedTime)).append("\n");
    sb.append("    verified: ").append(toIndentedString(verified)).append("\n");
    sb.append("    writerList: ").append(toIndentedString(writerList)).append("\n");
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
    openapiFields.add("action_requested");
    openapiFields.add("can_edit");
    openapiFields.add("explicit");
    openapiFields.add("html_tracking_url");
    openapiFields.add("instrumental");
    openapiFields.add("locked");
    openapiFields.add("lyrics_body");
    openapiFields.add("lyrics_copyright");
    openapiFields.add("lyrics_id");
    openapiFields.add("lyrics_language");
    openapiFields.add("lyrics_language_description");
    openapiFields.add("pixel_tracking_url");
    openapiFields.add("publisher_list");
    openapiFields.add("restricted");
    openapiFields.add("script_tracking_url");
    openapiFields.add("updated_time");
    openapiFields.add("verified");
    openapiFields.add("writer_list");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Lyrics
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Lyrics.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Lyrics is not found in the empty JSON string", Lyrics.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Lyrics.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Lyrics` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("action_requested") != null && !jsonObj.get("action_requested").isJsonNull()) && !jsonObj.get("action_requested").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `action_requested` to be a primitive type in the JSON string but got `%s`", jsonObj.get("action_requested").toString()));
      }
      if ((jsonObj.get("html_tracking_url") != null && !jsonObj.get("html_tracking_url").isJsonNull()) && !jsonObj.get("html_tracking_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `html_tracking_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("html_tracking_url").toString()));
      }
      if ((jsonObj.get("lyrics_body") != null && !jsonObj.get("lyrics_body").isJsonNull()) && !jsonObj.get("lyrics_body").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `lyrics_body` to be a primitive type in the JSON string but got `%s`", jsonObj.get("lyrics_body").toString()));
      }
      if ((jsonObj.get("lyrics_copyright") != null && !jsonObj.get("lyrics_copyright").isJsonNull()) && !jsonObj.get("lyrics_copyright").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `lyrics_copyright` to be a primitive type in the JSON string but got `%s`", jsonObj.get("lyrics_copyright").toString()));
      }
      if ((jsonObj.get("lyrics_language") != null && !jsonObj.get("lyrics_language").isJsonNull()) && !jsonObj.get("lyrics_language").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `lyrics_language` to be a primitive type in the JSON string but got `%s`", jsonObj.get("lyrics_language").toString()));
      }
      if ((jsonObj.get("lyrics_language_description") != null && !jsonObj.get("lyrics_language_description").isJsonNull()) && !jsonObj.get("lyrics_language_description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `lyrics_language_description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("lyrics_language_description").toString()));
      }
      if ((jsonObj.get("pixel_tracking_url") != null && !jsonObj.get("pixel_tracking_url").isJsonNull()) && !jsonObj.get("pixel_tracking_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `pixel_tracking_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("pixel_tracking_url").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("publisher_list") != null && !jsonObj.get("publisher_list").isJsonNull() && !jsonObj.get("publisher_list").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `publisher_list` to be an array in the JSON string but got `%s`", jsonObj.get("publisher_list").toString()));
      }
      if ((jsonObj.get("script_tracking_url") != null && !jsonObj.get("script_tracking_url").isJsonNull()) && !jsonObj.get("script_tracking_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `script_tracking_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("script_tracking_url").toString()));
      }
      if ((jsonObj.get("updated_time") != null && !jsonObj.get("updated_time").isJsonNull()) && !jsonObj.get("updated_time").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `updated_time` to be a primitive type in the JSON string but got `%s`", jsonObj.get("updated_time").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("writer_list") != null && !jsonObj.get("writer_list").isJsonNull() && !jsonObj.get("writer_list").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `writer_list` to be an array in the JSON string but got `%s`", jsonObj.get("writer_list").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Lyrics.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Lyrics' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Lyrics> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Lyrics.class));

       return (TypeAdapter<T>) new TypeAdapter<Lyrics>() {
           @Override
           public void write(JsonWriter out, Lyrics value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Lyrics read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Lyrics given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Lyrics
   * @throws IOException if the JSON string is invalid with respect to Lyrics
   */
  public static Lyrics fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Lyrics.class);
  }

  /**
   * Convert an instance of Lyrics to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

