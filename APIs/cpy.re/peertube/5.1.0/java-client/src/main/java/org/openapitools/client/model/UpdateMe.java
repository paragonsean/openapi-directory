/*
 * PeerTube
 * The PeerTube API is built on HTTP(S) and is RESTful. You can use your favorite HTTP/REST library for your programming language to use PeerTube. The spec API is fully compatible with [openapi-generator](https://github.com/OpenAPITools/openapi-generator/wiki/API-client-generator-HOWTO) which generates a client SDK in the language of your choice - we generate some client SDKs automatically:  - [Python](https://framagit.org/framasoft/peertube/clients/python) - [Go](https://framagit.org/framasoft/peertube/clients/go) - [Kotlin](https://framagit.org/framasoft/peertube/clients/kotlin)  See the [REST API quick start](https://docs.joinpeertube.org/api/rest-getting-started) for a few examples of using the PeerTube API.  # Authentication  When you sign up for an account on a PeerTube instance, you are given the possibility to generate sessions on it, and authenticate there using an access token. Only __one access token can currently be used at a time__.  ## Roles  Accounts are given permissions based on their role. There are three roles on PeerTube: Administrator, Moderator, and User. See the [roles guide](https://docs.joinpeertube.org/admin/managing-users#roles) for a detail of their permissions.  # Errors  The API uses standard HTTP status codes to indicate the success or failure of the API call, completed by a [RFC7807-compliant](https://tools.ietf.org/html/rfc7807) response body.  ``` HTTP 1.1 404 Not Found Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Video not found\",   \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",   \"status\": 404,   \"title\": \"Not Found\",   \"type\": \"about:blank\" } ```  We provide error `type` values for [a growing number of cases](https://github.com/Chocobozzz/PeerTube/blob/develop/shared/models/server/server-error-code.enum.ts), but it is still optional. Types are used to disambiguate errors that bear the same status code and are non-obvious:  ``` HTTP 1.1 403 Forbidden Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Cannot get this video regarding follow constraints\",   \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",   \"status\": 403,   \"title\": \"Forbidden\",   \"type\": \"https://docs.joinpeertube.org/api/rest-reference.html#section/Errors/does_not_respect_follow_constraints\" } ```  Here a 403 error could otherwise mean that the video is private or blocklisted.  ### Validation errors  Each parameter is evaluated on its own against a set of rules before the route validator proceeds with potential testing involving parameter combinations. Errors coming from validation errors appear earlier and benefit from a more detailed error description:  ``` HTTP 1.1 400 Bad Request Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Incorrect request parameters: id\",   \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",   \"instance\": \"/api/v1/videos/9c9de5e8-0a1e-484a-b099-e80766180\",   \"invalid-params\": {     \"id\": {       \"location\": \"params\",       \"msg\": \"Invalid value\",       \"param\": \"id\",       \"value\": \"9c9de5e8-0a1e-484a-b099-e80766180\"     }   },   \"status\": 400,   \"title\": \"Bad Request\",   \"type\": \"about:blank\" } ```  Where `id` is the name of the field concerned by the error, within the route definition. `invalid-params.<field>.location` can be either 'params', 'body', 'header', 'query' or 'cookies', and `invalid-params.<field>.value` reports the value that didn't pass validation whose `invalid-params.<field>.msg` is about.  ### Deprecated error fields  Some fields could be included with previous versions. They are still included but their use is deprecated: - `error`: superseded by `detail` - `code`: superseded by `type` (which is now an URI)  # Rate limits  We are rate-limiting all endpoints of PeerTube's API. Custom values can be set by administrators:  | Endpoint (prefix: `/api/v1`) | Calls         | Time frame   | |------------------------------|---------------|--------------| | `/_*`                         | 50            | 10 seconds   | | `POST /users/token`          | 15            | 5 minutes    | | `POST /users/register`       | 2<sup>*</sup> | 5 minutes    | | `POST /users/ask-send-verify-email` | 3      | 5 minutes    |  Depending on the endpoint, <sup>*</sup>failed requests are not taken into account. A service limit is announced by a `429 Too Many Requests` status code.  You can get details about the current state of your rate limit by reading the following headers:  | Header                  | Description                                                | |-------------------------|------------------------------------------------------------| | `X-RateLimit-Limit`     | Number of max requests allowed in the current time period  | | `X-RateLimit-Remaining` | Number of remaining requests in the current time period    | | `X-RateLimit-Reset`     | Timestamp of end of current time period as UNIX timestamp  | | `Retry-After`           | Seconds to delay after the first `429` is received         |  # CORS  This API features [Cross-Origin Resource Sharing (CORS)](https://fetch.spec.whatwg.org/), allowing cross-domain communication from the browser for some routes:  | Endpoint                    | |------------------------- ---| | `/api/_*`                    | | `/download/_*`               | | `/lazy-static/_*`            | | `/.well-known/webfinger`    |  In addition, all routes serving ActivityPub are CORS-enabled for all origins. 
 *
 * The version of the OpenAPI document: 5.1.0
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
 * UpdateMe
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:13.152727-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class UpdateMe {
  public static final String SERIALIZED_NAME_AUTO_PLAY_NEXT_VIDEO = "autoPlayNextVideo";
  @SerializedName(SERIALIZED_NAME_AUTO_PLAY_NEXT_VIDEO)
  private Boolean autoPlayNextVideo;

  public static final String SERIALIZED_NAME_AUTO_PLAY_NEXT_VIDEO_PLAYLIST = "autoPlayNextVideoPlaylist";
  @SerializedName(SERIALIZED_NAME_AUTO_PLAY_NEXT_VIDEO_PLAYLIST)
  private Boolean autoPlayNextVideoPlaylist;

  public static final String SERIALIZED_NAME_AUTO_PLAY_VIDEO = "autoPlayVideo";
  @SerializedName(SERIALIZED_NAME_AUTO_PLAY_VIDEO)
  private Boolean autoPlayVideo;

  public static final String SERIALIZED_NAME_CURRENT_PASSWORD = "currentPassword";
  @SerializedName(SERIALIZED_NAME_CURRENT_PASSWORD)
  private String currentPassword;

  /**
   * new NSFW display policy
   */
  @JsonAdapter(DisplayNSFWEnum.Adapter.class)
  public enum DisplayNSFWEnum {
    TRUE("true"),
    
    FALSE("false"),
    
    BOTH("both");

    private String value;

    DisplayNSFWEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static DisplayNSFWEnum fromValue(String value) {
      for (DisplayNSFWEnum b : DisplayNSFWEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<DisplayNSFWEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final DisplayNSFWEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public DisplayNSFWEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return DisplayNSFWEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      DisplayNSFWEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_DISPLAY_N_S_F_W = "displayNSFW";
  @SerializedName(SERIALIZED_NAME_DISPLAY_N_S_F_W)
  private DisplayNSFWEnum displayNSFW;

  public static final String SERIALIZED_NAME_DISPLAY_NAME = "displayName";
  @SerializedName(SERIALIZED_NAME_DISPLAY_NAME)
  private String displayName;

  public static final String SERIALIZED_NAME_EMAIL = "email";
  @SerializedName(SERIALIZED_NAME_EMAIL)
  private String email;

  public static final String SERIALIZED_NAME_NO_ACCOUNT_SETUP_WARNING_MODAL = "noAccountSetupWarningModal";
  @SerializedName(SERIALIZED_NAME_NO_ACCOUNT_SETUP_WARNING_MODAL)
  private Boolean noAccountSetupWarningModal;

  public static final String SERIALIZED_NAME_NO_INSTANCE_CONFIG_WARNING_MODAL = "noInstanceConfigWarningModal";
  @SerializedName(SERIALIZED_NAME_NO_INSTANCE_CONFIG_WARNING_MODAL)
  private Boolean noInstanceConfigWarningModal;

  public static final String SERIALIZED_NAME_NO_WELCOME_MODAL = "noWelcomeModal";
  @SerializedName(SERIALIZED_NAME_NO_WELCOME_MODAL)
  private Boolean noWelcomeModal;

  public static final String SERIALIZED_NAME_P2P_ENABLED = "p2pEnabled";
  @SerializedName(SERIALIZED_NAME_P2P_ENABLED)
  private Boolean p2pEnabled;

  public static final String SERIALIZED_NAME_PASSWORD = "password";
  @SerializedName(SERIALIZED_NAME_PASSWORD)
  private String password;

  public static final String SERIALIZED_NAME_THEME = "theme";
  @SerializedName(SERIALIZED_NAME_THEME)
  private String theme;

  public static final String SERIALIZED_NAME_VIDEO_LANGUAGES = "videoLanguages";
  @SerializedName(SERIALIZED_NAME_VIDEO_LANGUAGES)
  private List<String> videoLanguages = new ArrayList<>();

  public static final String SERIALIZED_NAME_VIDEOS_HISTORY_ENABLED = "videosHistoryEnabled";
  @SerializedName(SERIALIZED_NAME_VIDEOS_HISTORY_ENABLED)
  private Boolean videosHistoryEnabled;

  public UpdateMe() {
  }

  public UpdateMe autoPlayNextVideo(Boolean autoPlayNextVideo) {
    this.autoPlayNextVideo = autoPlayNextVideo;
    return this;
  }

  /**
   * new preference regarding playing following videos automatically
   * @return autoPlayNextVideo
   */
  @javax.annotation.Nullable
  public Boolean getAutoPlayNextVideo() {
    return autoPlayNextVideo;
  }

  public void setAutoPlayNextVideo(Boolean autoPlayNextVideo) {
    this.autoPlayNextVideo = autoPlayNextVideo;
  }


  public UpdateMe autoPlayNextVideoPlaylist(Boolean autoPlayNextVideoPlaylist) {
    this.autoPlayNextVideoPlaylist = autoPlayNextVideoPlaylist;
    return this;
  }

  /**
   * new preference regarding playing following playlist videos automatically
   * @return autoPlayNextVideoPlaylist
   */
  @javax.annotation.Nullable
  public Boolean getAutoPlayNextVideoPlaylist() {
    return autoPlayNextVideoPlaylist;
  }

  public void setAutoPlayNextVideoPlaylist(Boolean autoPlayNextVideoPlaylist) {
    this.autoPlayNextVideoPlaylist = autoPlayNextVideoPlaylist;
  }


  public UpdateMe autoPlayVideo(Boolean autoPlayVideo) {
    this.autoPlayVideo = autoPlayVideo;
    return this;
  }

  /**
   * new preference regarding playing videos automatically
   * @return autoPlayVideo
   */
  @javax.annotation.Nullable
  public Boolean getAutoPlayVideo() {
    return autoPlayVideo;
  }

  public void setAutoPlayVideo(Boolean autoPlayVideo) {
    this.autoPlayVideo = autoPlayVideo;
  }


  public UpdateMe currentPassword(String currentPassword) {
    this.currentPassword = currentPassword;
    return this;
  }

  /**
   * Get currentPassword
   * @return currentPassword
   */
  @javax.annotation.Nullable
  public String getCurrentPassword() {
    return currentPassword;
  }

  public void setCurrentPassword(String currentPassword) {
    this.currentPassword = currentPassword;
  }


  public UpdateMe displayNSFW(DisplayNSFWEnum displayNSFW) {
    this.displayNSFW = displayNSFW;
    return this;
  }

  /**
   * new NSFW display policy
   * @return displayNSFW
   */
  @javax.annotation.Nullable
  public DisplayNSFWEnum getDisplayNSFW() {
    return displayNSFW;
  }

  public void setDisplayNSFW(DisplayNSFWEnum displayNSFW) {
    this.displayNSFW = displayNSFW;
  }


  public UpdateMe displayName(String displayName) {
    this.displayName = displayName;
    return this;
  }

  /**
   * new name of the user in its representations
   * @return displayName
   */
  @javax.annotation.Nullable
  public String getDisplayName() {
    return displayName;
  }

  public void setDisplayName(String displayName) {
    this.displayName = displayName;
  }


  public UpdateMe email(String email) {
    this.email = email;
    return this;
  }

  /**
   * new email used for login and service communications
   * @return email
   */
  @javax.annotation.Nullable
  public String getEmail() {
    return email;
  }

  public void setEmail(String email) {
    this.email = email;
  }


  public UpdateMe noAccountSetupWarningModal(Boolean noAccountSetupWarningModal) {
    this.noAccountSetupWarningModal = noAccountSetupWarningModal;
    return this;
  }

  /**
   * Get noAccountSetupWarningModal
   * @return noAccountSetupWarningModal
   */
  @javax.annotation.Nullable
  public Boolean getNoAccountSetupWarningModal() {
    return noAccountSetupWarningModal;
  }

  public void setNoAccountSetupWarningModal(Boolean noAccountSetupWarningModal) {
    this.noAccountSetupWarningModal = noAccountSetupWarningModal;
  }


  public UpdateMe noInstanceConfigWarningModal(Boolean noInstanceConfigWarningModal) {
    this.noInstanceConfigWarningModal = noInstanceConfigWarningModal;
    return this;
  }

  /**
   * Get noInstanceConfigWarningModal
   * @return noInstanceConfigWarningModal
   */
  @javax.annotation.Nullable
  public Boolean getNoInstanceConfigWarningModal() {
    return noInstanceConfigWarningModal;
  }

  public void setNoInstanceConfigWarningModal(Boolean noInstanceConfigWarningModal) {
    this.noInstanceConfigWarningModal = noInstanceConfigWarningModal;
  }


  public UpdateMe noWelcomeModal(Boolean noWelcomeModal) {
    this.noWelcomeModal = noWelcomeModal;
    return this;
  }

  /**
   * Get noWelcomeModal
   * @return noWelcomeModal
   */
  @javax.annotation.Nullable
  public Boolean getNoWelcomeModal() {
    return noWelcomeModal;
  }

  public void setNoWelcomeModal(Boolean noWelcomeModal) {
    this.noWelcomeModal = noWelcomeModal;
  }


  public UpdateMe p2pEnabled(Boolean p2pEnabled) {
    this.p2pEnabled = p2pEnabled;
    return this;
  }

  /**
   * whether to enable P2P in the player or not
   * @return p2pEnabled
   */
  @javax.annotation.Nullable
  public Boolean getP2pEnabled() {
    return p2pEnabled;
  }

  public void setP2pEnabled(Boolean p2pEnabled) {
    this.p2pEnabled = p2pEnabled;
  }


  public UpdateMe password(String password) {
    this.password = password;
    return this;
  }

  /**
   * Get password
   * @return password
   */
  @javax.annotation.Nullable
  public String getPassword() {
    return password;
  }

  public void setPassword(String password) {
    this.password = password;
  }


  public UpdateMe theme(String theme) {
    this.theme = theme;
    return this;
  }

  /**
   * Get theme
   * @return theme
   */
  @javax.annotation.Nullable
  public String getTheme() {
    return theme;
  }

  public void setTheme(String theme) {
    this.theme = theme;
  }


  public UpdateMe videoLanguages(List<String> videoLanguages) {
    this.videoLanguages = videoLanguages;
    return this;
  }

  public UpdateMe addVideoLanguagesItem(String videoLanguagesItem) {
    if (this.videoLanguages == null) {
      this.videoLanguages = new ArrayList<>();
    }
    this.videoLanguages.add(videoLanguagesItem);
    return this;
  }

  /**
   * list of languages to filter videos down to
   * @return videoLanguages
   */
  @javax.annotation.Nullable
  public List<String> getVideoLanguages() {
    return videoLanguages;
  }

  public void setVideoLanguages(List<String> videoLanguages) {
    this.videoLanguages = videoLanguages;
  }


  public UpdateMe videosHistoryEnabled(Boolean videosHistoryEnabled) {
    this.videosHistoryEnabled = videosHistoryEnabled;
    return this;
  }

  /**
   * whether to keep track of watched history or not
   * @return videosHistoryEnabled
   */
  @javax.annotation.Nullable
  public Boolean getVideosHistoryEnabled() {
    return videosHistoryEnabled;
  }

  public void setVideosHistoryEnabled(Boolean videosHistoryEnabled) {
    this.videosHistoryEnabled = videosHistoryEnabled;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    UpdateMe updateMe = (UpdateMe) o;
    return Objects.equals(this.autoPlayNextVideo, updateMe.autoPlayNextVideo) &&
        Objects.equals(this.autoPlayNextVideoPlaylist, updateMe.autoPlayNextVideoPlaylist) &&
        Objects.equals(this.autoPlayVideo, updateMe.autoPlayVideo) &&
        Objects.equals(this.currentPassword, updateMe.currentPassword) &&
        Objects.equals(this.displayNSFW, updateMe.displayNSFW) &&
        Objects.equals(this.displayName, updateMe.displayName) &&
        Objects.equals(this.email, updateMe.email) &&
        Objects.equals(this.noAccountSetupWarningModal, updateMe.noAccountSetupWarningModal) &&
        Objects.equals(this.noInstanceConfigWarningModal, updateMe.noInstanceConfigWarningModal) &&
        Objects.equals(this.noWelcomeModal, updateMe.noWelcomeModal) &&
        Objects.equals(this.p2pEnabled, updateMe.p2pEnabled) &&
        Objects.equals(this.password, updateMe.password) &&
        Objects.equals(this.theme, updateMe.theme) &&
        Objects.equals(this.videoLanguages, updateMe.videoLanguages) &&
        Objects.equals(this.videosHistoryEnabled, updateMe.videosHistoryEnabled);
  }

  @Override
  public int hashCode() {
    return Objects.hash(autoPlayNextVideo, autoPlayNextVideoPlaylist, autoPlayVideo, currentPassword, displayNSFW, displayName, email, noAccountSetupWarningModal, noInstanceConfigWarningModal, noWelcomeModal, p2pEnabled, password, theme, videoLanguages, videosHistoryEnabled);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class UpdateMe {\n");
    sb.append("    autoPlayNextVideo: ").append(toIndentedString(autoPlayNextVideo)).append("\n");
    sb.append("    autoPlayNextVideoPlaylist: ").append(toIndentedString(autoPlayNextVideoPlaylist)).append("\n");
    sb.append("    autoPlayVideo: ").append(toIndentedString(autoPlayVideo)).append("\n");
    sb.append("    currentPassword: ").append("*").append("\n");
    sb.append("    displayNSFW: ").append(toIndentedString(displayNSFW)).append("\n");
    sb.append("    displayName: ").append(toIndentedString(displayName)).append("\n");
    sb.append("    email: ").append(toIndentedString(email)).append("\n");
    sb.append("    noAccountSetupWarningModal: ").append(toIndentedString(noAccountSetupWarningModal)).append("\n");
    sb.append("    noInstanceConfigWarningModal: ").append(toIndentedString(noInstanceConfigWarningModal)).append("\n");
    sb.append("    noWelcomeModal: ").append(toIndentedString(noWelcomeModal)).append("\n");
    sb.append("    p2pEnabled: ").append(toIndentedString(p2pEnabled)).append("\n");
    sb.append("    password: ").append("*").append("\n");
    sb.append("    theme: ").append(toIndentedString(theme)).append("\n");
    sb.append("    videoLanguages: ").append(toIndentedString(videoLanguages)).append("\n");
    sb.append("    videosHistoryEnabled: ").append(toIndentedString(videosHistoryEnabled)).append("\n");
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
    openapiFields.add("autoPlayNextVideo");
    openapiFields.add("autoPlayNextVideoPlaylist");
    openapiFields.add("autoPlayVideo");
    openapiFields.add("currentPassword");
    openapiFields.add("displayNSFW");
    openapiFields.add("displayName");
    openapiFields.add("email");
    openapiFields.add("noAccountSetupWarningModal");
    openapiFields.add("noInstanceConfigWarningModal");
    openapiFields.add("noWelcomeModal");
    openapiFields.add("p2pEnabled");
    openapiFields.add("password");
    openapiFields.add("theme");
    openapiFields.add("videoLanguages");
    openapiFields.add("videosHistoryEnabled");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to UpdateMe
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!UpdateMe.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in UpdateMe is not found in the empty JSON string", UpdateMe.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!UpdateMe.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `UpdateMe` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("currentPassword") != null && !jsonObj.get("currentPassword").isJsonNull()) && !jsonObj.get("currentPassword").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `currentPassword` to be a primitive type in the JSON string but got `%s`", jsonObj.get("currentPassword").toString()));
      }
      if ((jsonObj.get("displayNSFW") != null && !jsonObj.get("displayNSFW").isJsonNull()) && !jsonObj.get("displayNSFW").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `displayNSFW` to be a primitive type in the JSON string but got `%s`", jsonObj.get("displayNSFW").toString()));
      }
      // validate the optional field `displayNSFW`
      if (jsonObj.get("displayNSFW") != null && !jsonObj.get("displayNSFW").isJsonNull()) {
        DisplayNSFWEnum.validateJsonElement(jsonObj.get("displayNSFW"));
      }
      if ((jsonObj.get("displayName") != null && !jsonObj.get("displayName").isJsonNull()) && !jsonObj.get("displayName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `displayName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("displayName").toString()));
      }
      if ((jsonObj.get("password") != null && !jsonObj.get("password").isJsonNull()) && !jsonObj.get("password").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `password` to be a primitive type in the JSON string but got `%s`", jsonObj.get("password").toString()));
      }
      if ((jsonObj.get("theme") != null && !jsonObj.get("theme").isJsonNull()) && !jsonObj.get("theme").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `theme` to be a primitive type in the JSON string but got `%s`", jsonObj.get("theme").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("videoLanguages") != null && !jsonObj.get("videoLanguages").isJsonNull() && !jsonObj.get("videoLanguages").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `videoLanguages` to be an array in the JSON string but got `%s`", jsonObj.get("videoLanguages").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!UpdateMe.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'UpdateMe' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<UpdateMe> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(UpdateMe.class));

       return (TypeAdapter<T>) new TypeAdapter<UpdateMe>() {
           @Override
           public void write(JsonWriter out, UpdateMe value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public UpdateMe read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of UpdateMe given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of UpdateMe
   * @throws IOException if the JSON string is invalid with respect to UpdateMe
   */
  public static UpdateMe fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, UpdateMe.class);
  }

  /**
   * Convert an instance of UpdateMe to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

