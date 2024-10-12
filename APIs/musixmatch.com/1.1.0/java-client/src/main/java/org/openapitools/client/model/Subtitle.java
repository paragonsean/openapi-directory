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
 * a synchronized lyrics subtitle in the Musixmatch database.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:43:43.628132-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Subtitle {
  public static final String SERIALIZED_NAME_HTML_TRACKING_URL = "html_tracking_url";
  @SerializedName(SERIALIZED_NAME_HTML_TRACKING_URL)
  private String htmlTrackingUrl;

  public static final String SERIALIZED_NAME_LYRICS_COPYRIGHT = "lyrics_copyright";
  @SerializedName(SERIALIZED_NAME_LYRICS_COPYRIGHT)
  private String lyricsCopyright;

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

  public static final String SERIALIZED_NAME_SUBTITLE_BODY = "subtitle_body";
  @SerializedName(SERIALIZED_NAME_SUBTITLE_BODY)
  private String subtitleBody;

  public static final String SERIALIZED_NAME_SUBTITLE_ID = "subtitle_id";
  @SerializedName(SERIALIZED_NAME_SUBTITLE_ID)
  private BigDecimal subtitleId;

  public static final String SERIALIZED_NAME_SUBTITLE_LANGUAGE = "subtitle_language";
  @SerializedName(SERIALIZED_NAME_SUBTITLE_LANGUAGE)
  private String subtitleLanguage;

  public static final String SERIALIZED_NAME_SUBTITLE_LANGUAGE_DESCRIPTION = "subtitle_language_description";
  @SerializedName(SERIALIZED_NAME_SUBTITLE_LANGUAGE_DESCRIPTION)
  private String subtitleLanguageDescription;

  public static final String SERIALIZED_NAME_SUBTITLE_LENGTH = "subtitle_length";
  @SerializedName(SERIALIZED_NAME_SUBTITLE_LENGTH)
  private BigDecimal subtitleLength;

  public static final String SERIALIZED_NAME_UPDATED_TIME = "updated_time";
  @SerializedName(SERIALIZED_NAME_UPDATED_TIME)
  private String updatedTime;

  public static final String SERIALIZED_NAME_WRITER_LIST = "writer_list";
  @SerializedName(SERIALIZED_NAME_WRITER_LIST)
  private List<String> writerList = new ArrayList<>();

  public Subtitle() {
  }

  public Subtitle htmlTrackingUrl(String htmlTrackingUrl) {
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


  public Subtitle lyricsCopyright(String lyricsCopyright) {
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


  public Subtitle pixelTrackingUrl(String pixelTrackingUrl) {
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


  public Subtitle publisherList(List<String> publisherList) {
    this.publisherList = publisherList;
    return this;
  }

  public Subtitle addPublisherListItem(String publisherListItem) {
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


  public Subtitle restricted(BigDecimal restricted) {
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


  public Subtitle scriptTrackingUrl(String scriptTrackingUrl) {
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


  public Subtitle subtitleBody(String subtitleBody) {
    this.subtitleBody = subtitleBody;
    return this;
  }

  /**
   * 
   * @return subtitleBody
   */
  @javax.annotation.Nullable
  public String getSubtitleBody() {
    return subtitleBody;
  }

  public void setSubtitleBody(String subtitleBody) {
    this.subtitleBody = subtitleBody;
  }


  public Subtitle subtitleId(BigDecimal subtitleId) {
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


  public Subtitle subtitleLanguage(String subtitleLanguage) {
    this.subtitleLanguage = subtitleLanguage;
    return this;
  }

  /**
   * 
   * @return subtitleLanguage
   */
  @javax.annotation.Nullable
  public String getSubtitleLanguage() {
    return subtitleLanguage;
  }

  public void setSubtitleLanguage(String subtitleLanguage) {
    this.subtitleLanguage = subtitleLanguage;
  }


  public Subtitle subtitleLanguageDescription(String subtitleLanguageDescription) {
    this.subtitleLanguageDescription = subtitleLanguageDescription;
    return this;
  }

  /**
   * 
   * @return subtitleLanguageDescription
   */
  @javax.annotation.Nullable
  public String getSubtitleLanguageDescription() {
    return subtitleLanguageDescription;
  }

  public void setSubtitleLanguageDescription(String subtitleLanguageDescription) {
    this.subtitleLanguageDescription = subtitleLanguageDescription;
  }


  public Subtitle subtitleLength(BigDecimal subtitleLength) {
    this.subtitleLength = subtitleLength;
    return this;
  }

  /**
   * 
   * @return subtitleLength
   */
  @javax.annotation.Nullable
  public BigDecimal getSubtitleLength() {
    return subtitleLength;
  }

  public void setSubtitleLength(BigDecimal subtitleLength) {
    this.subtitleLength = subtitleLength;
  }


  public Subtitle updatedTime(String updatedTime) {
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


  public Subtitle writerList(List<String> writerList) {
    this.writerList = writerList;
    return this;
  }

  public Subtitle addWriterListItem(String writerListItem) {
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
    Subtitle subtitle = (Subtitle) o;
    return Objects.equals(this.htmlTrackingUrl, subtitle.htmlTrackingUrl) &&
        Objects.equals(this.lyricsCopyright, subtitle.lyricsCopyright) &&
        Objects.equals(this.pixelTrackingUrl, subtitle.pixelTrackingUrl) &&
        Objects.equals(this.publisherList, subtitle.publisherList) &&
        Objects.equals(this.restricted, subtitle.restricted) &&
        Objects.equals(this.scriptTrackingUrl, subtitle.scriptTrackingUrl) &&
        Objects.equals(this.subtitleBody, subtitle.subtitleBody) &&
        Objects.equals(this.subtitleId, subtitle.subtitleId) &&
        Objects.equals(this.subtitleLanguage, subtitle.subtitleLanguage) &&
        Objects.equals(this.subtitleLanguageDescription, subtitle.subtitleLanguageDescription) &&
        Objects.equals(this.subtitleLength, subtitle.subtitleLength) &&
        Objects.equals(this.updatedTime, subtitle.updatedTime) &&
        Objects.equals(this.writerList, subtitle.writerList);
  }

  @Override
  public int hashCode() {
    return Objects.hash(htmlTrackingUrl, lyricsCopyright, pixelTrackingUrl, publisherList, restricted, scriptTrackingUrl, subtitleBody, subtitleId, subtitleLanguage, subtitleLanguageDescription, subtitleLength, updatedTime, writerList);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Subtitle {\n");
    sb.append("    htmlTrackingUrl: ").append(toIndentedString(htmlTrackingUrl)).append("\n");
    sb.append("    lyricsCopyright: ").append(toIndentedString(lyricsCopyright)).append("\n");
    sb.append("    pixelTrackingUrl: ").append(toIndentedString(pixelTrackingUrl)).append("\n");
    sb.append("    publisherList: ").append(toIndentedString(publisherList)).append("\n");
    sb.append("    restricted: ").append(toIndentedString(restricted)).append("\n");
    sb.append("    scriptTrackingUrl: ").append(toIndentedString(scriptTrackingUrl)).append("\n");
    sb.append("    subtitleBody: ").append(toIndentedString(subtitleBody)).append("\n");
    sb.append("    subtitleId: ").append(toIndentedString(subtitleId)).append("\n");
    sb.append("    subtitleLanguage: ").append(toIndentedString(subtitleLanguage)).append("\n");
    sb.append("    subtitleLanguageDescription: ").append(toIndentedString(subtitleLanguageDescription)).append("\n");
    sb.append("    subtitleLength: ").append(toIndentedString(subtitleLength)).append("\n");
    sb.append("    updatedTime: ").append(toIndentedString(updatedTime)).append("\n");
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
    openapiFields.add("html_tracking_url");
    openapiFields.add("lyrics_copyright");
    openapiFields.add("pixel_tracking_url");
    openapiFields.add("publisher_list");
    openapiFields.add("restricted");
    openapiFields.add("script_tracking_url");
    openapiFields.add("subtitle_body");
    openapiFields.add("subtitle_id");
    openapiFields.add("subtitle_language");
    openapiFields.add("subtitle_language_description");
    openapiFields.add("subtitle_length");
    openapiFields.add("updated_time");
    openapiFields.add("writer_list");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Subtitle
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Subtitle.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Subtitle is not found in the empty JSON string", Subtitle.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Subtitle.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Subtitle` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("html_tracking_url") != null && !jsonObj.get("html_tracking_url").isJsonNull()) && !jsonObj.get("html_tracking_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `html_tracking_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("html_tracking_url").toString()));
      }
      if ((jsonObj.get("lyrics_copyright") != null && !jsonObj.get("lyrics_copyright").isJsonNull()) && !jsonObj.get("lyrics_copyright").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `lyrics_copyright` to be a primitive type in the JSON string but got `%s`", jsonObj.get("lyrics_copyright").toString()));
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
      if ((jsonObj.get("subtitle_body") != null && !jsonObj.get("subtitle_body").isJsonNull()) && !jsonObj.get("subtitle_body").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `subtitle_body` to be a primitive type in the JSON string but got `%s`", jsonObj.get("subtitle_body").toString()));
      }
      if ((jsonObj.get("subtitle_language") != null && !jsonObj.get("subtitle_language").isJsonNull()) && !jsonObj.get("subtitle_language").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `subtitle_language` to be a primitive type in the JSON string but got `%s`", jsonObj.get("subtitle_language").toString()));
      }
      if ((jsonObj.get("subtitle_language_description") != null && !jsonObj.get("subtitle_language_description").isJsonNull()) && !jsonObj.get("subtitle_language_description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `subtitle_language_description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("subtitle_language_description").toString()));
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
       if (!Subtitle.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Subtitle' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Subtitle> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Subtitle.class));

       return (TypeAdapter<T>) new TypeAdapter<Subtitle>() {
           @Override
           public void write(JsonWriter out, Subtitle value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Subtitle read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Subtitle given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Subtitle
   * @throws IOException if the JSON string is invalid with respect to Subtitle
   */
  public static Subtitle fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Subtitle.class);
  }

  /**
   * Convert an instance of Subtitle to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

