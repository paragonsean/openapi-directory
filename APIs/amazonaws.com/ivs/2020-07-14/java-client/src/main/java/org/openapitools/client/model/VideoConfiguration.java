/*
 * Amazon Interactive Video Service
 * <p> <b>Introduction</b> </p> <p>The Amazon Interactive Video Service (IVS) API is REST compatible, using a standard HTTP API and an Amazon Web Services EventBridge event stream for responses. JSON is used for both requests and responses, including errors.</p> <p>The API is an Amazon Web Services regional service. For a list of supported regions and Amazon IVS HTTPS service endpoints, see the <a href=\"https://docs.aws.amazon.com/general/latest/gr/ivs.html\">Amazon IVS page</a> in the <i>Amazon Web Services General Reference</i>.</p> <p> <i> <b>All API request parameters and URLs are case sensitive. </b> </i> </p> <p>For a summary of notable documentation changes in each release, see <a href=\"https://docs.aws.amazon.com/ivs/latest/userguide/doc-history.html\"> Document History</a>.</p> <p> <b>Allowed Header Values</b> </p> <ul> <li> <p> <code> <b>Accept:</b> </code> application/json</p> </li> <li> <p> <code> <b>Accept-Encoding:</b> </code> gzip, deflate</p> </li> <li> <p> <code> <b>Content-Type:</b> </code>application/json</p> </li> </ul> <p> <b>Resources</b> </p> <p>The following resources contain information about your IVS live stream (see <a href=\"https://docs.aws.amazon.com/ivs/latest/userguide/getting-started.html\"> Getting Started with Amazon IVS</a>):</p> <ul> <li> <p> <b>Channel</b> — Stores configuration data related to your live stream. You first create a channel and then use the channel’s stream key to start your live stream. See the Channel endpoints for more information. </p> </li> <li> <p> <b>Stream key</b> — An identifier assigned by Amazon IVS when you create a channel, which is then used to authorize streaming. See the StreamKey endpoints for more information. <i> <b>Treat the stream key like a secret, since it allows anyone to stream to the channel.</b> </i> </p> </li> <li> <p> <b>Playback key pair</b> — Video playback may be restricted using playback-authorization tokens, which use public-key encryption. A playback key pair is the public-private pair of keys used to sign and validate the playback-authorization token. See the PlaybackKeyPair endpoints for more information.</p> </li> <li> <p> <b>Recording configuration</b> — Stores configuration related to recording a live stream and where to store the recorded content. Multiple channels can reference the same recording configuration. See the Recording Configuration endpoints for more information.</p> </li> </ul> <p> <b>Tagging</b> </p> <p>A <i>tag</i> is a metadata label that you assign to an Amazon Web Services resource. A tag comprises a <i>key</i> and a <i>value</i>, both set by you. For example, you might set a tag as <code>topic:nature</code> to label a particular video category. See <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\">Tagging Amazon Web Services Resources</a> for more information, including restrictions that apply to tags and \"Tag naming limits and requirements\"; Amazon IVS has no service-specific constraints beyond what is documented there.</p> <p>Tags can help you identify and organize your Amazon Web Services resources. For example, you can use the same tag for different resources to indicate that they are related. You can also use tags to manage access (see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html\"> Access Tags</a>). </p> <p>The Amazon IVS API has these tag-related endpoints: <a>TagResource</a>, <a>UntagResource</a>, and <a>ListTagsForResource</a>. The following resources support tagging: Channels, Stream Keys, Playback Key Pairs, and Recording Configurations.</p> <p>At most 50 tags can be applied to a resource. </p> <p> <b>Authentication versus Authorization</b> </p> <p>Note the differences between these concepts:</p> <ul> <li> <p> <i>Authentication</i> is about verifying identity. You need to be authenticated to sign Amazon IVS API requests.</p> </li> <li> <p> <i>Authorization</i> is about granting permissions. Your IAM roles need to have permissions for Amazon IVS API requests. In addition, authorization is needed to view <a href=\"https://docs.aws.amazon.com/ivs/latest/userguide/private-channels.html\">Amazon IVS private channels</a>. (Private channels are channels that are enabled for \"playback authorization.\")</p> </li> </ul> <p> <b>Authentication</b> </p> <p>All Amazon IVS API requests must be authenticated with a signature. The Amazon Web Services Command-Line Interface (CLI) and Amazon IVS Player SDKs take care of signing the underlying API calls for you. However, if your application calls the Amazon IVS API directly, it’s your responsibility to sign the requests.</p> <p>You generate a signature using valid Amazon Web Services credentials that have permission to perform the requested action. For example, you must sign PutMetadata requests with a signature generated from a user account that has the <code>ivs:PutMetadata</code> permission.</p> <p>For more information:</p> <ul> <li> <p>Authentication and generating signatures — See <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html\">Authenticating Requests (Amazon Web Services Signature Version 4)</a> in the <i>Amazon Web Services General Reference</i>.</p> </li> <li> <p>Managing Amazon IVS permissions — See <a href=\"https://docs.aws.amazon.com/ivs/latest/userguide/security-iam.html\">Identity and Access Management</a> on the Security page of the <i>Amazon IVS User Guide</i>.</p> </li> </ul> <p> <b>Amazon Resource Names (ARNs)</b> </p> <p>ARNs uniquely identify AWS resources. An ARN is required when you need to specify a resource unambiguously across all of AWS, such as in IAM policies and API calls. For more information, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names</a> in the <i>AWS General Reference</i>.</p> <p> <b>Channel Endpoints</b> </p> <ul> <li> <p> <a>CreateChannel</a> — Creates a new channel and an associated stream key to start streaming.</p> </li> <li> <p> <a>GetChannel</a> — Gets the channel configuration for the specified channel ARN.</p> </li> <li> <p> <a>BatchGetChannel</a> — Performs <a>GetChannel</a> on multiple ARNs simultaneously.</p> </li> <li> <p> <a>ListChannels</a> — Gets summary information about all channels in your account, in the Amazon Web Services region where the API request is processed. This list can be filtered to match a specified name or recording-configuration ARN. Filters are mutually exclusive and cannot be used together. If you try to use both filters, you will get an error (409 Conflict Exception).</p> </li> <li> <p> <a>UpdateChannel</a> — Updates a channel's configuration. This does not affect an ongoing stream of this channel. You must stop and restart the stream for the changes to take effect.</p> </li> <li> <p> <a>DeleteChannel</a> — Deletes the specified channel.</p> </li> </ul> <p> <b>StreamKey Endpoints</b> </p> <ul> <li> <p> <a>CreateStreamKey</a> — Creates a stream key, used to initiate a stream, for the specified channel ARN.</p> </li> <li> <p> <a>GetStreamKey</a> — Gets stream key information for the specified ARN.</p> </li> <li> <p> <a>BatchGetStreamKey</a> — Performs <a>GetStreamKey</a> on multiple ARNs simultaneously.</p> </li> <li> <p> <a>ListStreamKeys</a> — Gets summary information about stream keys for the specified channel.</p> </li> <li> <p> <a>DeleteStreamKey</a> — Deletes the stream key for the specified ARN, so it can no longer be used to stream.</p> </li> </ul> <p> <b>Stream Endpoints</b> </p> <ul> <li> <p> <a>GetStream</a> — Gets information about the active (live) stream on a specified channel.</p> </li> <li> <p> <a>GetStreamSession</a> — Gets metadata on a specified stream.</p> </li> <li> <p> <a>ListStreams</a> — Gets summary information about live streams in your account, in the Amazon Web Services region where the API request is processed.</p> </li> <li> <p> <a>ListStreamSessions</a> — Gets a summary of current and previous streams for a specified channel in your account, in the AWS region where the API request is processed.</p> </li> <li> <p> <a>StopStream</a> — Disconnects the incoming RTMPS stream for the specified channel. Can be used in conjunction with <a>DeleteStreamKey</a> to prevent further streaming to a channel.</p> </li> <li> <p> <a>PutMetadata</a> — Inserts metadata into the active stream of the specified channel. At most 5 requests per second per channel are allowed, each with a maximum 1 KB payload. (If 5 TPS is not sufficient for your needs, we recommend batching your data into a single PutMetadata call.) At most 155 requests per second per account are allowed.</p> </li> </ul> <p> <b>Private Channel Endpoints</b> </p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/ivs/latest/userguide/private-channels.html\">Setting Up Private Channels</a> in the <i>Amazon IVS User Guide</i>.</p> <ul> <li> <p> <a>ImportPlaybackKeyPair</a> — Imports the public portion of a new key pair and returns its <code>arn</code> and <code>fingerprint</code>. The <code>privateKey</code> can then be used to generate viewer authorization tokens, to grant viewers access to private channels (channels enabled for playback authorization).</p> </li> <li> <p> <a>GetPlaybackKeyPair</a> — Gets a specified playback authorization key pair and returns the <code>arn</code> and <code>fingerprint</code>. The <code>privateKey</code> held by the caller can be used to generate viewer authorization tokens, to grant viewers access to private channels.</p> </li> <li> <p> <a>ListPlaybackKeyPairs</a> — Gets summary information about playback key pairs.</p> </li> <li> <p> <a>DeletePlaybackKeyPair</a> — Deletes a specified authorization key pair. This invalidates future viewer tokens generated using the key pair’s <code>privateKey</code>.</p> </li> <li> <p> <a>StartViewerSessionRevocation</a> — Starts the process of revoking the viewer session associated with a specified channel ARN and viewer ID. Optionally, you can provide a version to revoke viewer sessions less than and including that version.</p> </li> <li> <p> <a>BatchStartViewerSessionRevocation</a> — Performs <a>StartViewerSessionRevocation</a> on multiple channel ARN and viewer ID pairs simultaneously.</p> </li> </ul> <p> <b>RecordingConfiguration Endpoints</b> </p> <ul> <li> <p> <a>CreateRecordingConfiguration</a> — Creates a new recording configuration, used to enable recording to Amazon S3.</p> </li> <li> <p> <a>GetRecordingConfiguration</a> — Gets the recording-configuration metadata for the specified ARN.</p> </li> <li> <p> <a>ListRecordingConfigurations</a> — Gets summary information about all recording configurations in your account, in the Amazon Web Services region where the API request is processed.</p> </li> <li> <p> <a>DeleteRecordingConfiguration</a> — Deletes the recording configuration for the specified ARN.</p> </li> </ul> <p> <b>Amazon Web Services Tags Endpoints</b> </p> <ul> <li> <p> <a>TagResource</a> — Adds or updates tags for the Amazon Web Services resource with the specified ARN.</p> </li> <li> <p> <a>UntagResource</a> — Removes tags from the resource with the specified ARN.</p> </li> <li> <p> <a>ListTagsForResource</a> — Gets information about Amazon Web Services tags for the specified ARN.</p> </li> </ul>
 *
 * The version of the OpenAPI document: 2020-07-14
 * Contact: mike.ralphson@gmail.com
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
 * Object specifying a stream’s video configuration, as set up by the broadcaster (usually in an encoder). This is part of the &lt;a&gt;IngestConfiguration&lt;/a&gt; object and used for monitoring stream health.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:23:27.693454-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class VideoConfiguration {
  public static final String SERIALIZED_NAME_AVC_LEVEL = "avcLevel";
  @SerializedName(SERIALIZED_NAME_AVC_LEVEL)
  private String avcLevel;

  public static final String SERIALIZED_NAME_AVC_PROFILE = "avcProfile";
  @SerializedName(SERIALIZED_NAME_AVC_PROFILE)
  private String avcProfile;

  public static final String SERIALIZED_NAME_CODEC = "codec";
  @SerializedName(SERIALIZED_NAME_CODEC)
  private String codec;

  public static final String SERIALIZED_NAME_ENCODER = "encoder";
  @SerializedName(SERIALIZED_NAME_ENCODER)
  private String encoder;

  public static final String SERIALIZED_NAME_TARGET_BITRATE = "targetBitrate";
  @SerializedName(SERIALIZED_NAME_TARGET_BITRATE)
  private Integer targetBitrate;

  public static final String SERIALIZED_NAME_TARGET_FRAMERATE = "targetFramerate";
  @SerializedName(SERIALIZED_NAME_TARGET_FRAMERATE)
  private Integer targetFramerate;

  public static final String SERIALIZED_NAME_VIDEO_HEIGHT = "videoHeight";
  @SerializedName(SERIALIZED_NAME_VIDEO_HEIGHT)
  private Integer videoHeight;

  public static final String SERIALIZED_NAME_VIDEO_WIDTH = "videoWidth";
  @SerializedName(SERIALIZED_NAME_VIDEO_WIDTH)
  private Integer videoWidth;

  public VideoConfiguration() {
  }

  public VideoConfiguration avcLevel(String avcLevel) {
    this.avcLevel = avcLevel;
    return this;
  }

  /**
   * Get avcLevel
   * @return avcLevel
   */
  @javax.annotation.Nullable
  public String getAvcLevel() {
    return avcLevel;
  }

  public void setAvcLevel(String avcLevel) {
    this.avcLevel = avcLevel;
  }


  public VideoConfiguration avcProfile(String avcProfile) {
    this.avcProfile = avcProfile;
    return this;
  }

  /**
   * Get avcProfile
   * @return avcProfile
   */
  @javax.annotation.Nullable
  public String getAvcProfile() {
    return avcProfile;
  }

  public void setAvcProfile(String avcProfile) {
    this.avcProfile = avcProfile;
  }


  public VideoConfiguration codec(String codec) {
    this.codec = codec;
    return this;
  }

  /**
   * Get codec
   * @return codec
   */
  @javax.annotation.Nullable
  public String getCodec() {
    return codec;
  }

  public void setCodec(String codec) {
    this.codec = codec;
  }


  public VideoConfiguration encoder(String encoder) {
    this.encoder = encoder;
    return this;
  }

  /**
   * Get encoder
   * @return encoder
   */
  @javax.annotation.Nullable
  public String getEncoder() {
    return encoder;
  }

  public void setEncoder(String encoder) {
    this.encoder = encoder;
  }


  public VideoConfiguration targetBitrate(Integer targetBitrate) {
    this.targetBitrate = targetBitrate;
    return this;
  }

  /**
   * Get targetBitrate
   * @return targetBitrate
   */
  @javax.annotation.Nullable
  public Integer getTargetBitrate() {
    return targetBitrate;
  }

  public void setTargetBitrate(Integer targetBitrate) {
    this.targetBitrate = targetBitrate;
  }


  public VideoConfiguration targetFramerate(Integer targetFramerate) {
    this.targetFramerate = targetFramerate;
    return this;
  }

  /**
   * Get targetFramerate
   * @return targetFramerate
   */
  @javax.annotation.Nullable
  public Integer getTargetFramerate() {
    return targetFramerate;
  }

  public void setTargetFramerate(Integer targetFramerate) {
    this.targetFramerate = targetFramerate;
  }


  public VideoConfiguration videoHeight(Integer videoHeight) {
    this.videoHeight = videoHeight;
    return this;
  }

  /**
   * Get videoHeight
   * @return videoHeight
   */
  @javax.annotation.Nullable
  public Integer getVideoHeight() {
    return videoHeight;
  }

  public void setVideoHeight(Integer videoHeight) {
    this.videoHeight = videoHeight;
  }


  public VideoConfiguration videoWidth(Integer videoWidth) {
    this.videoWidth = videoWidth;
    return this;
  }

  /**
   * Get videoWidth
   * @return videoWidth
   */
  @javax.annotation.Nullable
  public Integer getVideoWidth() {
    return videoWidth;
  }

  public void setVideoWidth(Integer videoWidth) {
    this.videoWidth = videoWidth;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    VideoConfiguration videoConfiguration = (VideoConfiguration) o;
    return Objects.equals(this.avcLevel, videoConfiguration.avcLevel) &&
        Objects.equals(this.avcProfile, videoConfiguration.avcProfile) &&
        Objects.equals(this.codec, videoConfiguration.codec) &&
        Objects.equals(this.encoder, videoConfiguration.encoder) &&
        Objects.equals(this.targetBitrate, videoConfiguration.targetBitrate) &&
        Objects.equals(this.targetFramerate, videoConfiguration.targetFramerate) &&
        Objects.equals(this.videoHeight, videoConfiguration.videoHeight) &&
        Objects.equals(this.videoWidth, videoConfiguration.videoWidth);
  }

  @Override
  public int hashCode() {
    return Objects.hash(avcLevel, avcProfile, codec, encoder, targetBitrate, targetFramerate, videoHeight, videoWidth);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class VideoConfiguration {\n");
    sb.append("    avcLevel: ").append(toIndentedString(avcLevel)).append("\n");
    sb.append("    avcProfile: ").append(toIndentedString(avcProfile)).append("\n");
    sb.append("    codec: ").append(toIndentedString(codec)).append("\n");
    sb.append("    encoder: ").append(toIndentedString(encoder)).append("\n");
    sb.append("    targetBitrate: ").append(toIndentedString(targetBitrate)).append("\n");
    sb.append("    targetFramerate: ").append(toIndentedString(targetFramerate)).append("\n");
    sb.append("    videoHeight: ").append(toIndentedString(videoHeight)).append("\n");
    sb.append("    videoWidth: ").append(toIndentedString(videoWidth)).append("\n");
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
    openapiFields.add("avcLevel");
    openapiFields.add("avcProfile");
    openapiFields.add("codec");
    openapiFields.add("encoder");
    openapiFields.add("targetBitrate");
    openapiFields.add("targetFramerate");
    openapiFields.add("videoHeight");
    openapiFields.add("videoWidth");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to VideoConfiguration
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!VideoConfiguration.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in VideoConfiguration is not found in the empty JSON string", VideoConfiguration.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!VideoConfiguration.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `VideoConfiguration` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `avcLevel`
      if (jsonObj.get("avcLevel") != null && !jsonObj.get("avcLevel").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("avcLevel"));
      }
      // validate the optional field `avcProfile`
      if (jsonObj.get("avcProfile") != null && !jsonObj.get("avcProfile").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("avcProfile"));
      }
      // validate the optional field `codec`
      if (jsonObj.get("codec") != null && !jsonObj.get("codec").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("codec"));
      }
      // validate the optional field `encoder`
      if (jsonObj.get("encoder") != null && !jsonObj.get("encoder").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("encoder"));
      }
      // validate the optional field `targetBitrate`
      if (jsonObj.get("targetBitrate") != null && !jsonObj.get("targetBitrate").isJsonNull()) {
        Integer.validateJsonElement(jsonObj.get("targetBitrate"));
      }
      // validate the optional field `targetFramerate`
      if (jsonObj.get("targetFramerate") != null && !jsonObj.get("targetFramerate").isJsonNull()) {
        Integer.validateJsonElement(jsonObj.get("targetFramerate"));
      }
      // validate the optional field `videoHeight`
      if (jsonObj.get("videoHeight") != null && !jsonObj.get("videoHeight").isJsonNull()) {
        Integer.validateJsonElement(jsonObj.get("videoHeight"));
      }
      // validate the optional field `videoWidth`
      if (jsonObj.get("videoWidth") != null && !jsonObj.get("videoWidth").isJsonNull()) {
        Integer.validateJsonElement(jsonObj.get("videoWidth"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!VideoConfiguration.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'VideoConfiguration' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<VideoConfiguration> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(VideoConfiguration.class));

       return (TypeAdapter<T>) new TypeAdapter<VideoConfiguration>() {
           @Override
           public void write(JsonWriter out, VideoConfiguration value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public VideoConfiguration read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of VideoConfiguration given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of VideoConfiguration
   * @throws IOException if the JSON string is invalid with respect to VideoConfiguration
   */
  public static VideoConfiguration fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, VideoConfiguration.class);
  }

  /**
   * Convert an instance of VideoConfiguration to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

