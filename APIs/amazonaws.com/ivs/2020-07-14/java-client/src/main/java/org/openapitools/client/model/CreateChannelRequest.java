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
import java.util.HashMap;
import java.util.Map;

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
 * CreateChannelRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:23:27.693454-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CreateChannelRequest {
  public static final String SERIALIZED_NAME_AUTHORIZED = "authorized";
  @SerializedName(SERIALIZED_NAME_AUTHORIZED)
  private Boolean authorized;

  public static final String SERIALIZED_NAME_INSECURE_INGEST = "insecureIngest";
  @SerializedName(SERIALIZED_NAME_INSECURE_INGEST)
  private Boolean insecureIngest;

  /**
   * Channel latency mode. Use &lt;code&gt;NORMAL&lt;/code&gt; to broadcast and deliver live video up to Full HD. Use &lt;code&gt;LOW&lt;/code&gt; for near-real-time interaction with viewers. (Note: In the Amazon IVS console, &lt;code&gt;LOW&lt;/code&gt; and &lt;code&gt;NORMAL&lt;/code&gt; correspond to Ultra-low and Standard, respectively.) Default: &lt;code&gt;LOW&lt;/code&gt;.
   */
  @JsonAdapter(LatencyModeEnum.Adapter.class)
  public enum LatencyModeEnum {
    NORMAL("NORMAL"),
    
    LOW("LOW");

    private String value;

    LatencyModeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static LatencyModeEnum fromValue(String value) {
      for (LatencyModeEnum b : LatencyModeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<LatencyModeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final LatencyModeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public LatencyModeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return LatencyModeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      LatencyModeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_LATENCY_MODE = "latencyMode";
  @SerializedName(SERIALIZED_NAME_LATENCY_MODE)
  private LatencyModeEnum latencyMode;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  /**
   * Optional transcode preset for the channel. This is selectable only for &lt;code&gt;ADVANCED_HD&lt;/code&gt; and &lt;code&gt;ADVANCED_SD&lt;/code&gt; channel types. For those channel types, the default &lt;code&gt;preset&lt;/code&gt; is &lt;code&gt;HIGHER_BANDWIDTH_DELIVERY&lt;/code&gt;. For other channel types (&lt;code&gt;BASIC&lt;/code&gt; and &lt;code&gt;STANDARD&lt;/code&gt;), &lt;code&gt;preset&lt;/code&gt; is the empty string (&lt;code&gt;\&quot;\&quot;&lt;/code&gt;).
   */
  @JsonAdapter(PresetEnum.Adapter.class)
  public enum PresetEnum {
    HIGHER_BANDWIDTH_DELIVERY("HIGHER_BANDWIDTH_DELIVERY"),
    
    CONSTRAINED_BANDWIDTH_DELIVERY("CONSTRAINED_BANDWIDTH_DELIVERY");

    private String value;

    PresetEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static PresetEnum fromValue(String value) {
      for (PresetEnum b : PresetEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<PresetEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final PresetEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public PresetEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return PresetEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      PresetEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_PRESET = "preset";
  @SerializedName(SERIALIZED_NAME_PRESET)
  private PresetEnum preset;

  public static final String SERIALIZED_NAME_RECORDING_CONFIGURATION_ARN = "recordingConfigurationArn";
  @SerializedName(SERIALIZED_NAME_RECORDING_CONFIGURATION_ARN)
  private String recordingConfigurationArn;

  public static final String SERIALIZED_NAME_TAGS = "tags";
  @SerializedName(SERIALIZED_NAME_TAGS)
  private Map<String, String> tags = new HashMap<>();

  /**
   * &lt;p&gt;Channel type, which determines the allowable resolution and bitrate. &lt;i&gt;If you exceed the allowable input resolution or bitrate, the stream probably will disconnect immediately.&lt;/i&gt; Some types generate multiple qualities (renditions) from the original input; this automatically gives viewers the best experience for their devices and network conditions. Some types provide transcoded video; transcoding allows higher playback quality across a range of download speeds. Default: &lt;code&gt;STANDARD&lt;/code&gt;. Valid values:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;BASIC&lt;/code&gt;: Video is transmuxed: Amazon IVS delivers the original input quality to viewers. The viewer’s video-quality choice is limited to the original input. Input resolution can be up to 1080p and bitrate can be up to 1.5 Mbps for 480p and up to 3.5 Mbps for resolutions between 480p and 1080p. Original audio is passed through.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;STANDARD&lt;/code&gt;: Video is transcoded: multiple qualities are generated from the original input, to automatically give viewers the best experience for their devices and network conditions. Transcoding allows higher playback quality across a range of download speeds. Resolution can be up to 1080p and bitrate can be up to 8.5 Mbps. Audio is transcoded only for renditions 360p and below; above that, audio is passed through. This is the default when you create a channel.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ADVANCED_SD&lt;/code&gt;: Video is transcoded; multiple qualities are generated from the original input, to automatically give viewers the best experience for their devices and network conditions. Input resolution can be up to 1080p and bitrate can be up to 8.5 Mbps; output is capped at SD quality (480p). You can select an optional transcode preset (see below). Audio for all renditions is transcoded, and an audio-only rendition is available.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ADVANCED_HD&lt;/code&gt;: Video is transcoded; multiple qualities are generated from the original input, to automatically give viewers the best experience for their devices and network conditions. Input resolution can be up to 1080p and bitrate can be up to 8.5 Mbps; output is capped at HD quality (720p). You can select an optional transcode preset (see below). Audio for all renditions is transcoded, and an audio-only rendition is available.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Optional &lt;i&gt;transcode presets&lt;/i&gt; (available for the &lt;code&gt;ADVANCED&lt;/code&gt; types) allow you to trade off available download bandwidth and video quality, to optimize the viewing experience. There are two presets:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;i&gt;Constrained bandwidth delivery&lt;/i&gt; uses a lower bitrate for each quality level. Use it if you have low download bandwidth and/or simple video content (e.g., talking heads)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;i&gt;Higher bandwidth delivery&lt;/i&gt; uses a higher bitrate for each quality level. Use it if you have high download bandwidth and/or complex video content (e.g., flashes and quick scene changes).&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
   */
  @JsonAdapter(TypeEnum.Adapter.class)
  public enum TypeEnum {
    BASIC("BASIC"),
    
    STANDARD("STANDARD"),
    
    ADVANCED_SD("ADVANCED_SD"),
    
    ADVANCED_HD("ADVANCED_HD");

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

  public CreateChannelRequest() {
  }

  public CreateChannelRequest authorized(Boolean authorized) {
    this.authorized = authorized;
    return this;
  }

  /**
   * Whether the channel is private (enabled for playback authorization). Default: &lt;code&gt;false&lt;/code&gt;.
   * @return authorized
   */
  @javax.annotation.Nullable
  public Boolean getAuthorized() {
    return authorized;
  }

  public void setAuthorized(Boolean authorized) {
    this.authorized = authorized;
  }


  public CreateChannelRequest insecureIngest(Boolean insecureIngest) {
    this.insecureIngest = insecureIngest;
    return this;
  }

  /**
   * Whether the channel allows insecure RTMP ingest. Default: &lt;code&gt;false&lt;/code&gt;.
   * @return insecureIngest
   */
  @javax.annotation.Nullable
  public Boolean getInsecureIngest() {
    return insecureIngest;
  }

  public void setInsecureIngest(Boolean insecureIngest) {
    this.insecureIngest = insecureIngest;
  }


  public CreateChannelRequest latencyMode(LatencyModeEnum latencyMode) {
    this.latencyMode = latencyMode;
    return this;
  }

  /**
   * Channel latency mode. Use &lt;code&gt;NORMAL&lt;/code&gt; to broadcast and deliver live video up to Full HD. Use &lt;code&gt;LOW&lt;/code&gt; for near-real-time interaction with viewers. (Note: In the Amazon IVS console, &lt;code&gt;LOW&lt;/code&gt; and &lt;code&gt;NORMAL&lt;/code&gt; correspond to Ultra-low and Standard, respectively.) Default: &lt;code&gt;LOW&lt;/code&gt;.
   * @return latencyMode
   */
  @javax.annotation.Nullable
  public LatencyModeEnum getLatencyMode() {
    return latencyMode;
  }

  public void setLatencyMode(LatencyModeEnum latencyMode) {
    this.latencyMode = latencyMode;
  }


  public CreateChannelRequest name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Channel name.
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public CreateChannelRequest preset(PresetEnum preset) {
    this.preset = preset;
    return this;
  }

  /**
   * Optional transcode preset for the channel. This is selectable only for &lt;code&gt;ADVANCED_HD&lt;/code&gt; and &lt;code&gt;ADVANCED_SD&lt;/code&gt; channel types. For those channel types, the default &lt;code&gt;preset&lt;/code&gt; is &lt;code&gt;HIGHER_BANDWIDTH_DELIVERY&lt;/code&gt;. For other channel types (&lt;code&gt;BASIC&lt;/code&gt; and &lt;code&gt;STANDARD&lt;/code&gt;), &lt;code&gt;preset&lt;/code&gt; is the empty string (&lt;code&gt;\&quot;\&quot;&lt;/code&gt;).
   * @return preset
   */
  @javax.annotation.Nullable
  public PresetEnum getPreset() {
    return preset;
  }

  public void setPreset(PresetEnum preset) {
    this.preset = preset;
  }


  public CreateChannelRequest recordingConfigurationArn(String recordingConfigurationArn) {
    this.recordingConfigurationArn = recordingConfigurationArn;
    return this;
  }

  /**
   * Recording-configuration ARN. Default: \&quot;\&quot; (empty string, recording is disabled).
   * @return recordingConfigurationArn
   */
  @javax.annotation.Nullable
  public String getRecordingConfigurationArn() {
    return recordingConfigurationArn;
  }

  public void setRecordingConfigurationArn(String recordingConfigurationArn) {
    this.recordingConfigurationArn = recordingConfigurationArn;
  }


  public CreateChannelRequest tags(Map<String, String> tags) {
    this.tags = tags;
    return this;
  }

  public CreateChannelRequest putTagsItem(String key, String tagsItem) {
    if (this.tags == null) {
      this.tags = new HashMap<>();
    }
    this.tags.put(key, tagsItem);
    return this;
  }

  /**
   * Array of 1-50 maps, each of the form &lt;code&gt;string:string (key:value)&lt;/code&gt;. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\&quot;&gt;Tagging Amazon Web Services Resources&lt;/a&gt; for more information, including restrictions that apply to tags and \&quot;Tag naming limits and requirements\&quot;; Amazon IVS has no service-specific constraints beyond what is documented there.
   * @return tags
   */
  @javax.annotation.Nullable
  public Map<String, String> getTags() {
    return tags;
  }

  public void setTags(Map<String, String> tags) {
    this.tags = tags;
  }


  public CreateChannelRequest type(TypeEnum type) {
    this.type = type;
    return this;
  }

  /**
   * &lt;p&gt;Channel type, which determines the allowable resolution and bitrate. &lt;i&gt;If you exceed the allowable input resolution or bitrate, the stream probably will disconnect immediately.&lt;/i&gt; Some types generate multiple qualities (renditions) from the original input; this automatically gives viewers the best experience for their devices and network conditions. Some types provide transcoded video; transcoding allows higher playback quality across a range of download speeds. Default: &lt;code&gt;STANDARD&lt;/code&gt;. Valid values:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;BASIC&lt;/code&gt;: Video is transmuxed: Amazon IVS delivers the original input quality to viewers. The viewer’s video-quality choice is limited to the original input. Input resolution can be up to 1080p and bitrate can be up to 1.5 Mbps for 480p and up to 3.5 Mbps for resolutions between 480p and 1080p. Original audio is passed through.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;STANDARD&lt;/code&gt;: Video is transcoded: multiple qualities are generated from the original input, to automatically give viewers the best experience for their devices and network conditions. Transcoding allows higher playback quality across a range of download speeds. Resolution can be up to 1080p and bitrate can be up to 8.5 Mbps. Audio is transcoded only for renditions 360p and below; above that, audio is passed through. This is the default when you create a channel.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ADVANCED_SD&lt;/code&gt;: Video is transcoded; multiple qualities are generated from the original input, to automatically give viewers the best experience for their devices and network conditions. Input resolution can be up to 1080p and bitrate can be up to 8.5 Mbps; output is capped at SD quality (480p). You can select an optional transcode preset (see below). Audio for all renditions is transcoded, and an audio-only rendition is available.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ADVANCED_HD&lt;/code&gt;: Video is transcoded; multiple qualities are generated from the original input, to automatically give viewers the best experience for their devices and network conditions. Input resolution can be up to 1080p and bitrate can be up to 8.5 Mbps; output is capped at HD quality (720p). You can select an optional transcode preset (see below). Audio for all renditions is transcoded, and an audio-only rendition is available.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Optional &lt;i&gt;transcode presets&lt;/i&gt; (available for the &lt;code&gt;ADVANCED&lt;/code&gt; types) allow you to trade off available download bandwidth and video quality, to optimize the viewing experience. There are two presets:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;i&gt;Constrained bandwidth delivery&lt;/i&gt; uses a lower bitrate for each quality level. Use it if you have low download bandwidth and/or simple video content (e.g., talking heads)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;i&gt;Higher bandwidth delivery&lt;/i&gt; uses a higher bitrate for each quality level. Use it if you have high download bandwidth and/or complex video content (e.g., flashes and quick scene changes).&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
   * @return type
   */
  @javax.annotation.Nullable
  public TypeEnum getType() {
    return type;
  }

  public void setType(TypeEnum type) {
    this.type = type;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CreateChannelRequest createChannelRequest = (CreateChannelRequest) o;
    return Objects.equals(this.authorized, createChannelRequest.authorized) &&
        Objects.equals(this.insecureIngest, createChannelRequest.insecureIngest) &&
        Objects.equals(this.latencyMode, createChannelRequest.latencyMode) &&
        Objects.equals(this.name, createChannelRequest.name) &&
        Objects.equals(this.preset, createChannelRequest.preset) &&
        Objects.equals(this.recordingConfigurationArn, createChannelRequest.recordingConfigurationArn) &&
        Objects.equals(this.tags, createChannelRequest.tags) &&
        Objects.equals(this.type, createChannelRequest.type);
  }

  @Override
  public int hashCode() {
    return Objects.hash(authorized, insecureIngest, latencyMode, name, preset, recordingConfigurationArn, tags, type);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CreateChannelRequest {\n");
    sb.append("    authorized: ").append(toIndentedString(authorized)).append("\n");
    sb.append("    insecureIngest: ").append(toIndentedString(insecureIngest)).append("\n");
    sb.append("    latencyMode: ").append(toIndentedString(latencyMode)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    preset: ").append(toIndentedString(preset)).append("\n");
    sb.append("    recordingConfigurationArn: ").append(toIndentedString(recordingConfigurationArn)).append("\n");
    sb.append("    tags: ").append(toIndentedString(tags)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
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
    openapiFields.add("authorized");
    openapiFields.add("insecureIngest");
    openapiFields.add("latencyMode");
    openapiFields.add("name");
    openapiFields.add("preset");
    openapiFields.add("recordingConfigurationArn");
    openapiFields.add("tags");
    openapiFields.add("type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CreateChannelRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CreateChannelRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CreateChannelRequest is not found in the empty JSON string", CreateChannelRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CreateChannelRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CreateChannelRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("latencyMode") != null && !jsonObj.get("latencyMode").isJsonNull()) && !jsonObj.get("latencyMode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `latencyMode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("latencyMode").toString()));
      }
      // validate the optional field `latencyMode`
      if (jsonObj.get("latencyMode") != null && !jsonObj.get("latencyMode").isJsonNull()) {
        LatencyModeEnum.validateJsonElement(jsonObj.get("latencyMode"));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("preset") != null && !jsonObj.get("preset").isJsonNull()) && !jsonObj.get("preset").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `preset` to be a primitive type in the JSON string but got `%s`", jsonObj.get("preset").toString()));
      }
      // validate the optional field `preset`
      if (jsonObj.get("preset") != null && !jsonObj.get("preset").isJsonNull()) {
        PresetEnum.validateJsonElement(jsonObj.get("preset"));
      }
      if ((jsonObj.get("recordingConfigurationArn") != null && !jsonObj.get("recordingConfigurationArn").isJsonNull()) && !jsonObj.get("recordingConfigurationArn").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `recordingConfigurationArn` to be a primitive type in the JSON string but got `%s`", jsonObj.get("recordingConfigurationArn").toString()));
      }
      if ((jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) && !jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
      // validate the optional field `type`
      if (jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) {
        TypeEnum.validateJsonElement(jsonObj.get("type"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CreateChannelRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CreateChannelRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CreateChannelRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CreateChannelRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<CreateChannelRequest>() {
           @Override
           public void write(JsonWriter out, CreateChannelRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CreateChannelRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CreateChannelRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CreateChannelRequest
   * @throws IOException if the JSON string is invalid with respect to CreateChannelRequest
   */
  public static CreateChannelRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CreateChannelRequest.class);
  }

  /**
   * Convert an instance of CreateChannelRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

