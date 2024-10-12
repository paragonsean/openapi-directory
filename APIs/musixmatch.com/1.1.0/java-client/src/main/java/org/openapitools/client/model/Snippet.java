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
 * Snippet of lyrics text in the Musixmatch database.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:43:43.628132-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Snippet {
  public static final String SERIALIZED_NAME_HTML_TRACKING_URL = "html_tracking_url";
  @SerializedName(SERIALIZED_NAME_HTML_TRACKING_URL)
  private String htmlTrackingUrl;

  public static final String SERIALIZED_NAME_INSTRUMENTAL = "instrumental";
  @SerializedName(SERIALIZED_NAME_INSTRUMENTAL)
  private BigDecimal instrumental;

  public static final String SERIALIZED_NAME_PIXEL_TRACKING_URL = "pixel_tracking_url";
  @SerializedName(SERIALIZED_NAME_PIXEL_TRACKING_URL)
  private String pixelTrackingUrl;

  public static final String SERIALIZED_NAME_RESTRICTED = "restricted";
  @SerializedName(SERIALIZED_NAME_RESTRICTED)
  private BigDecimal restricted;

  public static final String SERIALIZED_NAME_SCRIPT_TRACKING_URL = "script_tracking_url";
  @SerializedName(SERIALIZED_NAME_SCRIPT_TRACKING_URL)
  private String scriptTrackingUrl;

  public static final String SERIALIZED_NAME_SNIPPET_BODY = "snippet_body";
  @SerializedName(SERIALIZED_NAME_SNIPPET_BODY)
  private String snippetBody;

  public static final String SERIALIZED_NAME_SNIPPET_ID = "snippet_id";
  @SerializedName(SERIALIZED_NAME_SNIPPET_ID)
  private BigDecimal snippetId;

  public static final String SERIALIZED_NAME_SNIPPET_LANGUAGE = "snippet_language";
  @SerializedName(SERIALIZED_NAME_SNIPPET_LANGUAGE)
  private String snippetLanguage;

  public static final String SERIALIZED_NAME_UPDATED_TIME = "updated_time";
  @SerializedName(SERIALIZED_NAME_UPDATED_TIME)
  private String updatedTime;

  public Snippet() {
  }

  public Snippet htmlTrackingUrl(String htmlTrackingUrl) {
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


  public Snippet instrumental(BigDecimal instrumental) {
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


  public Snippet pixelTrackingUrl(String pixelTrackingUrl) {
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


  public Snippet restricted(BigDecimal restricted) {
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


  public Snippet scriptTrackingUrl(String scriptTrackingUrl) {
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


  public Snippet snippetBody(String snippetBody) {
    this.snippetBody = snippetBody;
    return this;
  }

  /**
   * 
   * @return snippetBody
   */
  @javax.annotation.Nullable
  public String getSnippetBody() {
    return snippetBody;
  }

  public void setSnippetBody(String snippetBody) {
    this.snippetBody = snippetBody;
  }


  public Snippet snippetId(BigDecimal snippetId) {
    this.snippetId = snippetId;
    return this;
  }

  /**
   * 
   * @return snippetId
   */
  @javax.annotation.Nullable
  public BigDecimal getSnippetId() {
    return snippetId;
  }

  public void setSnippetId(BigDecimal snippetId) {
    this.snippetId = snippetId;
  }


  public Snippet snippetLanguage(String snippetLanguage) {
    this.snippetLanguage = snippetLanguage;
    return this;
  }

  /**
   * 
   * @return snippetLanguage
   */
  @javax.annotation.Nullable
  public String getSnippetLanguage() {
    return snippetLanguage;
  }

  public void setSnippetLanguage(String snippetLanguage) {
    this.snippetLanguage = snippetLanguage;
  }


  public Snippet updatedTime(String updatedTime) {
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
    Snippet snippet = (Snippet) o;
    return Objects.equals(this.htmlTrackingUrl, snippet.htmlTrackingUrl) &&
        Objects.equals(this.instrumental, snippet.instrumental) &&
        Objects.equals(this.pixelTrackingUrl, snippet.pixelTrackingUrl) &&
        Objects.equals(this.restricted, snippet.restricted) &&
        Objects.equals(this.scriptTrackingUrl, snippet.scriptTrackingUrl) &&
        Objects.equals(this.snippetBody, snippet.snippetBody) &&
        Objects.equals(this.snippetId, snippet.snippetId) &&
        Objects.equals(this.snippetLanguage, snippet.snippetLanguage) &&
        Objects.equals(this.updatedTime, snippet.updatedTime);
  }

  @Override
  public int hashCode() {
    return Objects.hash(htmlTrackingUrl, instrumental, pixelTrackingUrl, restricted, scriptTrackingUrl, snippetBody, snippetId, snippetLanguage, updatedTime);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Snippet {\n");
    sb.append("    htmlTrackingUrl: ").append(toIndentedString(htmlTrackingUrl)).append("\n");
    sb.append("    instrumental: ").append(toIndentedString(instrumental)).append("\n");
    sb.append("    pixelTrackingUrl: ").append(toIndentedString(pixelTrackingUrl)).append("\n");
    sb.append("    restricted: ").append(toIndentedString(restricted)).append("\n");
    sb.append("    scriptTrackingUrl: ").append(toIndentedString(scriptTrackingUrl)).append("\n");
    sb.append("    snippetBody: ").append(toIndentedString(snippetBody)).append("\n");
    sb.append("    snippetId: ").append(toIndentedString(snippetId)).append("\n");
    sb.append("    snippetLanguage: ").append(toIndentedString(snippetLanguage)).append("\n");
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
    openapiFields.add("html_tracking_url");
    openapiFields.add("instrumental");
    openapiFields.add("pixel_tracking_url");
    openapiFields.add("restricted");
    openapiFields.add("script_tracking_url");
    openapiFields.add("snippet_body");
    openapiFields.add("snippet_id");
    openapiFields.add("snippet_language");
    openapiFields.add("updated_time");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Snippet
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Snippet.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Snippet is not found in the empty JSON string", Snippet.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Snippet.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Snippet` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("html_tracking_url") != null && !jsonObj.get("html_tracking_url").isJsonNull()) && !jsonObj.get("html_tracking_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `html_tracking_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("html_tracking_url").toString()));
      }
      if ((jsonObj.get("pixel_tracking_url") != null && !jsonObj.get("pixel_tracking_url").isJsonNull()) && !jsonObj.get("pixel_tracking_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `pixel_tracking_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("pixel_tracking_url").toString()));
      }
      if ((jsonObj.get("script_tracking_url") != null && !jsonObj.get("script_tracking_url").isJsonNull()) && !jsonObj.get("script_tracking_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `script_tracking_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("script_tracking_url").toString()));
      }
      if ((jsonObj.get("snippet_body") != null && !jsonObj.get("snippet_body").isJsonNull()) && !jsonObj.get("snippet_body").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `snippet_body` to be a primitive type in the JSON string but got `%s`", jsonObj.get("snippet_body").toString()));
      }
      if ((jsonObj.get("snippet_language") != null && !jsonObj.get("snippet_language").isJsonNull()) && !jsonObj.get("snippet_language").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `snippet_language` to be a primitive type in the JSON string but got `%s`", jsonObj.get("snippet_language").toString()));
      }
      if ((jsonObj.get("updated_time") != null && !jsonObj.get("updated_time").isJsonNull()) && !jsonObj.get("updated_time").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `updated_time` to be a primitive type in the JSON string but got `%s`", jsonObj.get("updated_time").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Snippet.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Snippet' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Snippet> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Snippet.class));

       return (TypeAdapter<T>) new TypeAdapter<Snippet>() {
           @Override
           public void write(JsonWriter out, Snippet value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Snippet read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Snippet given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Snippet
   * @throws IOException if the JSON string is invalid with respect to Snippet
   */
  public static Snippet fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Snippet.class);
  }

  /**
   * Convert an instance of Snippet to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

