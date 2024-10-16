/*
 * Google Home
 * # Google Home Local API This is an unofficial documentation of the local API used by the Home app to communicate with GH devices. [GitHub Repo](https://github.com/rithvikvibhu/GHLocalApi)  [![GitHub stars](https://img.shields.io/github/stars/rithvikvibhu/GHLocalApi)](https://github.com/rithvikvibhu/GHLocalApi/stargazers) [![GitHub license](https://img.shields.io/github/license/rithvikvibhu/GHLocalApi)](https://github.com/rithvikvibhu/GHLocalApi/blob/master/LICENSE.md)  ## Getting Started  Requests must be made over HTTPS, port 8443, so the base URL for these endpoints is: `https://<google-home-ip>:8443/setup/`  Get the IP of Google Home from the Google Home app (Device Settings -> End of the list) or from your router.  GET requests are simple, in the browser kind.   POST requests need to set the header (when there's a body): `content-type: application/json`  ## Authentication  Since June 2019, most requests (with exceptions like `/setup/eureka_info`) need a local authorization token.  There are 3 kinds of tokens involved here:  ### Local Authorization Token This token must be sent in all requests in the header `cast-local-authorization-token`. It is short-lived (~1 day) and may change unexpectedly (with a sync, change in homegraph, etc.) ##### Get this token - With access to an android device, [get this token directly by either method](https://gist.github.com/rithvikvibhu/1a0f4937af957ef6a78453e3be482c1f). - Without a device, or to integrate it with a script, use an access token to get the homegraph and extract the token. To get an access token, read the next section. Check the example section for more info.  ### Access Token This is a standard google oauth2 access token. It is in the form `ya29.***`. This gives access to the Google Home Foyer API. These expire in an hour. Use this to get the homegraph (and then the local authorization token above). ##### Get this token To get this access token, either a Google account username/password or a Google Master Token is needed. More info in the gist. Use the script [from this gist](https://gist.github.com/rithvikvibhu/952f83ea656c6782fbd0f1645059055d).  ### Master Token This is in the form `aas_et/_***` and can be used to request access tokens. ##### Get this token The same [script in the gist](https://gist.github.com/rithvikvibhu/952f83ea656c6782fbd0f1645059055d) that gets the access token can also get the master token. Needs Google account creds.  ## Example  Here's the whole flow from just a pair of username/password to using the local API.  Prerequisites: - [grpcurl](https://github.com/fullstorydev/grpcurl) - [Proto files](https://drive.google.com/drive/folders/1RvnN3y-G23pd2SWHmfV_7sef8QU5GNF4?usp=sharing) (preserve folder structure)  ### 1. Get an access token with the script - Download get_tokens.py - Fill in username and password ```sh python3 get_tokens.py # Note down the access token printed. ```  ### 2. Use the access token and get home graph - This prints the json and uses jq to parse and filter out the fields deviceName and localAuthToken - This will give a list of all devices and their local auth tokens ```sh ./grpcurl -H 'authorization: Bearer ya29.a0Af****' \\  -import-path /path/to/protos \\  -proto /path/to/protos/google/internal/home/foyer/v1.proto \\  googlehomefoyer-pa.googleapis.com:443 \\  google.internal.home.foyer.v1.StructuresService/GetHomeGraph | jq '.home.devices[] | {deviceName, localAuthToken}' # Note down the local auth token for the device you want. ```  ### 3. Make the call to the local device using the local auth token ```sh curl -H \"cast-local-authorization-token: LOCAL_AUTH_TOKEN\" --verbose --insecure https://192.168.0.18:8443/setup/bluetooth/status ```
 *
 * The version of the OpenAPI document: 2.0
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
 * OptIn
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:31.661536-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class OptIn {
  public static final String SERIALIZED_NAME_AUDIO_HDR = "audio_hdr";
  @SerializedName(SERIALIZED_NAME_AUDIO_HDR)
  private Boolean audioHdr;

  public static final String SERIALIZED_NAME_AUDIO_SURROUND_MODE = "audio_surround_mode";
  @SerializedName(SERIALIZED_NAME_AUDIO_SURROUND_MODE)
  private Integer audioSurroundMode;

  public static final String SERIALIZED_NAME_AUTOPLAY_ON_SIGNAL = "autoplay_on_signal";
  @SerializedName(SERIALIZED_NAME_AUTOPLAY_ON_SIGNAL)
  private Boolean autoplayOnSignal;

  public static final String SERIALIZED_NAME_CLOUD_IPC = "cloud_ipc";
  @SerializedName(SERIALIZED_NAME_CLOUD_IPC)
  private Boolean cloudIpc;

  public static final String SERIALIZED_NAME_HDMI_PREFER50HZ = "hdmi_prefer_50hz";
  @SerializedName(SERIALIZED_NAME_HDMI_PREFER50HZ)
  private Boolean hdmiPrefer50hz;

  public static final String SERIALIZED_NAME_HDMI_PREFER_HIGH_FPS = "hdmi_prefer_high_fps";
  @SerializedName(SERIALIZED_NAME_HDMI_PREFER_HIGH_FPS)
  private Boolean hdmiPreferHighFps;

  public static final String SERIALIZED_NAME_MANAGED_MODE = "managed_mode";
  @SerializedName(SERIALIZED_NAME_MANAGED_MODE)
  private Boolean managedMode;

  public static final String SERIALIZED_NAME_OPENCAST = "opencast";
  @SerializedName(SERIALIZED_NAME_OPENCAST)
  private Boolean opencast;

  public static final String SERIALIZED_NAME_PREVIEW_CHANNEL = "preview_channel";
  @SerializedName(SERIALIZED_NAME_PREVIEW_CHANNEL)
  private Boolean previewChannel;

  public static final String SERIALIZED_NAME_REMOTE_DUCKING = "remote_ducking";
  @SerializedName(SERIALIZED_NAME_REMOTE_DUCKING)
  private Boolean remoteDucking;

  public static final String SERIALIZED_NAME_STATS = "stats";
  @SerializedName(SERIALIZED_NAME_STATS)
  private Boolean stats;

  public static final String SERIALIZED_NAME_UI_FLIPPED = "ui_flipped";
  @SerializedName(SERIALIZED_NAME_UI_FLIPPED)
  private Boolean uiFlipped;

  public static final String SERIALIZED_NAME_WPA3_SUPPORT_ENABLED = "wpa3_support_enabled";
  @SerializedName(SERIALIZED_NAME_WPA3_SUPPORT_ENABLED)
  private Boolean wpa3SupportEnabled;

  public OptIn() {
  }

  public OptIn audioHdr(Boolean audioHdr) {
    this.audioHdr = audioHdr;
    return this;
  }

  /**
   * Get audioHdr
   * @return audioHdr
   */
  @javax.annotation.Nonnull
  public Boolean getAudioHdr() {
    return audioHdr;
  }

  public void setAudioHdr(Boolean audioHdr) {
    this.audioHdr = audioHdr;
  }


  public OptIn audioSurroundMode(Integer audioSurroundMode) {
    this.audioSurroundMode = audioSurroundMode;
    return this;
  }

  /**
   * Get audioSurroundMode
   * @return audioSurroundMode
   */
  @javax.annotation.Nonnull
  public Integer getAudioSurroundMode() {
    return audioSurroundMode;
  }

  public void setAudioSurroundMode(Integer audioSurroundMode) {
    this.audioSurroundMode = audioSurroundMode;
  }


  public OptIn autoplayOnSignal(Boolean autoplayOnSignal) {
    this.autoplayOnSignal = autoplayOnSignal;
    return this;
  }

  /**
   * Get autoplayOnSignal
   * @return autoplayOnSignal
   */
  @javax.annotation.Nonnull
  public Boolean getAutoplayOnSignal() {
    return autoplayOnSignal;
  }

  public void setAutoplayOnSignal(Boolean autoplayOnSignal) {
    this.autoplayOnSignal = autoplayOnSignal;
  }


  public OptIn cloudIpc(Boolean cloudIpc) {
    this.cloudIpc = cloudIpc;
    return this;
  }

  /**
   * Get cloudIpc
   * @return cloudIpc
   */
  @javax.annotation.Nonnull
  public Boolean getCloudIpc() {
    return cloudIpc;
  }

  public void setCloudIpc(Boolean cloudIpc) {
    this.cloudIpc = cloudIpc;
  }


  public OptIn hdmiPrefer50hz(Boolean hdmiPrefer50hz) {
    this.hdmiPrefer50hz = hdmiPrefer50hz;
    return this;
  }

  /**
   * Get hdmiPrefer50hz
   * @return hdmiPrefer50hz
   */
  @javax.annotation.Nonnull
  public Boolean getHdmiPrefer50hz() {
    return hdmiPrefer50hz;
  }

  public void setHdmiPrefer50hz(Boolean hdmiPrefer50hz) {
    this.hdmiPrefer50hz = hdmiPrefer50hz;
  }


  public OptIn hdmiPreferHighFps(Boolean hdmiPreferHighFps) {
    this.hdmiPreferHighFps = hdmiPreferHighFps;
    return this;
  }

  /**
   * Get hdmiPreferHighFps
   * @return hdmiPreferHighFps
   */
  @javax.annotation.Nonnull
  public Boolean getHdmiPreferHighFps() {
    return hdmiPreferHighFps;
  }

  public void setHdmiPreferHighFps(Boolean hdmiPreferHighFps) {
    this.hdmiPreferHighFps = hdmiPreferHighFps;
  }


  public OptIn managedMode(Boolean managedMode) {
    this.managedMode = managedMode;
    return this;
  }

  /**
   * Get managedMode
   * @return managedMode
   */
  @javax.annotation.Nonnull
  public Boolean getManagedMode() {
    return managedMode;
  }

  public void setManagedMode(Boolean managedMode) {
    this.managedMode = managedMode;
  }


  public OptIn opencast(Boolean opencast) {
    this.opencast = opencast;
    return this;
  }

  /**
   * Get opencast
   * @return opencast
   */
  @javax.annotation.Nonnull
  public Boolean getOpencast() {
    return opencast;
  }

  public void setOpencast(Boolean opencast) {
    this.opencast = opencast;
  }


  public OptIn previewChannel(Boolean previewChannel) {
    this.previewChannel = previewChannel;
    return this;
  }

  /**
   * Get previewChannel
   * @return previewChannel
   */
  @javax.annotation.Nonnull
  public Boolean getPreviewChannel() {
    return previewChannel;
  }

  public void setPreviewChannel(Boolean previewChannel) {
    this.previewChannel = previewChannel;
  }


  public OptIn remoteDucking(Boolean remoteDucking) {
    this.remoteDucking = remoteDucking;
    return this;
  }

  /**
   * Get remoteDucking
   * @return remoteDucking
   */
  @javax.annotation.Nonnull
  public Boolean getRemoteDucking() {
    return remoteDucking;
  }

  public void setRemoteDucking(Boolean remoteDucking) {
    this.remoteDucking = remoteDucking;
  }


  public OptIn stats(Boolean stats) {
    this.stats = stats;
    return this;
  }

  /**
   * Get stats
   * @return stats
   */
  @javax.annotation.Nonnull
  public Boolean getStats() {
    return stats;
  }

  public void setStats(Boolean stats) {
    this.stats = stats;
  }


  public OptIn uiFlipped(Boolean uiFlipped) {
    this.uiFlipped = uiFlipped;
    return this;
  }

  /**
   * Get uiFlipped
   * @return uiFlipped
   */
  @javax.annotation.Nonnull
  public Boolean getUiFlipped() {
    return uiFlipped;
  }

  public void setUiFlipped(Boolean uiFlipped) {
    this.uiFlipped = uiFlipped;
  }


  public OptIn wpa3SupportEnabled(Boolean wpa3SupportEnabled) {
    this.wpa3SupportEnabled = wpa3SupportEnabled;
    return this;
  }

  /**
   * Get wpa3SupportEnabled
   * @return wpa3SupportEnabled
   */
  @javax.annotation.Nonnull
  public Boolean getWpa3SupportEnabled() {
    return wpa3SupportEnabled;
  }

  public void setWpa3SupportEnabled(Boolean wpa3SupportEnabled) {
    this.wpa3SupportEnabled = wpa3SupportEnabled;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    OptIn optIn = (OptIn) o;
    return Objects.equals(this.audioHdr, optIn.audioHdr) &&
        Objects.equals(this.audioSurroundMode, optIn.audioSurroundMode) &&
        Objects.equals(this.autoplayOnSignal, optIn.autoplayOnSignal) &&
        Objects.equals(this.cloudIpc, optIn.cloudIpc) &&
        Objects.equals(this.hdmiPrefer50hz, optIn.hdmiPrefer50hz) &&
        Objects.equals(this.hdmiPreferHighFps, optIn.hdmiPreferHighFps) &&
        Objects.equals(this.managedMode, optIn.managedMode) &&
        Objects.equals(this.opencast, optIn.opencast) &&
        Objects.equals(this.previewChannel, optIn.previewChannel) &&
        Objects.equals(this.remoteDucking, optIn.remoteDucking) &&
        Objects.equals(this.stats, optIn.stats) &&
        Objects.equals(this.uiFlipped, optIn.uiFlipped) &&
        Objects.equals(this.wpa3SupportEnabled, optIn.wpa3SupportEnabled);
  }

  @Override
  public int hashCode() {
    return Objects.hash(audioHdr, audioSurroundMode, autoplayOnSignal, cloudIpc, hdmiPrefer50hz, hdmiPreferHighFps, managedMode, opencast, previewChannel, remoteDucking, stats, uiFlipped, wpa3SupportEnabled);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class OptIn {\n");
    sb.append("    audioHdr: ").append(toIndentedString(audioHdr)).append("\n");
    sb.append("    audioSurroundMode: ").append(toIndentedString(audioSurroundMode)).append("\n");
    sb.append("    autoplayOnSignal: ").append(toIndentedString(autoplayOnSignal)).append("\n");
    sb.append("    cloudIpc: ").append(toIndentedString(cloudIpc)).append("\n");
    sb.append("    hdmiPrefer50hz: ").append(toIndentedString(hdmiPrefer50hz)).append("\n");
    sb.append("    hdmiPreferHighFps: ").append(toIndentedString(hdmiPreferHighFps)).append("\n");
    sb.append("    managedMode: ").append(toIndentedString(managedMode)).append("\n");
    sb.append("    opencast: ").append(toIndentedString(opencast)).append("\n");
    sb.append("    previewChannel: ").append(toIndentedString(previewChannel)).append("\n");
    sb.append("    remoteDucking: ").append(toIndentedString(remoteDucking)).append("\n");
    sb.append("    stats: ").append(toIndentedString(stats)).append("\n");
    sb.append("    uiFlipped: ").append(toIndentedString(uiFlipped)).append("\n");
    sb.append("    wpa3SupportEnabled: ").append(toIndentedString(wpa3SupportEnabled)).append("\n");
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
    openapiFields.add("audio_hdr");
    openapiFields.add("audio_surround_mode");
    openapiFields.add("autoplay_on_signal");
    openapiFields.add("cloud_ipc");
    openapiFields.add("hdmi_prefer_50hz");
    openapiFields.add("hdmi_prefer_high_fps");
    openapiFields.add("managed_mode");
    openapiFields.add("opencast");
    openapiFields.add("preview_channel");
    openapiFields.add("remote_ducking");
    openapiFields.add("stats");
    openapiFields.add("ui_flipped");
    openapiFields.add("wpa3_support_enabled");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("audio_hdr");
    openapiRequiredFields.add("audio_surround_mode");
    openapiRequiredFields.add("autoplay_on_signal");
    openapiRequiredFields.add("cloud_ipc");
    openapiRequiredFields.add("hdmi_prefer_50hz");
    openapiRequiredFields.add("hdmi_prefer_high_fps");
    openapiRequiredFields.add("managed_mode");
    openapiRequiredFields.add("opencast");
    openapiRequiredFields.add("preview_channel");
    openapiRequiredFields.add("remote_ducking");
    openapiRequiredFields.add("stats");
    openapiRequiredFields.add("ui_flipped");
    openapiRequiredFields.add("wpa3_support_enabled");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to OptIn
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!OptIn.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in OptIn is not found in the empty JSON string", OptIn.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!OptIn.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `OptIn` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : OptIn.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!OptIn.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'OptIn' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<OptIn> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(OptIn.class));

       return (TypeAdapter<T>) new TypeAdapter<OptIn>() {
           @Override
           public void write(JsonWriter out, OptIn value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public OptIn read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of OptIn given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of OptIn
   * @throws IOException if the JSON string is invalid with respect to OptIn
   */
  public static OptIn fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, OptIn.class);
  }

  /**
   * Convert an instance of OptIn to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

