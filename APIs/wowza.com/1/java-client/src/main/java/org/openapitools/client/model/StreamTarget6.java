/*
 * Wowza Streaming Cloud REST API Reference Documentation
 *  # About the REST API  The Wowza Streaming Cloud<sup>TM</sup> REST API (application programming interface) offers complete programmatic control over live streams, transcoders, stream sources, and stream targets. Anything you can do in the Wowza Streaming Cloud UI can also be achieved by making HTTP-based requests to cloud-based servers through the REST API.  The Wowza Streaming Cloud REST API features *cross-origin resource sharing*, or CORS. CORS is a [W3C specification](https://www.w3.org/TR/cors/) that provides headers in HTTP requests to enable a web server to safely make a network request to another domain.  In order to protect shared resources, the Wowza Streaming Cloud REST API is subject to limits. For details, see [Wowza Streaming Cloud REST API limits](https://www.wowza.com/docs/wowza-streaming-cloud-rest-api-limits). # About this documentation This reference documentation is based on the open-source [Swagger framework](http://swagger.io/specification/). It allows you to view the operations, parameters, and request and reponse schemas for every resource. Request samples are presented in cURL (Shell) and JavaScript; some samples also include just the JSON object. Response samples are all JSON.  For more information and examples on using the Wowza Streaming Cloud REST API, see our [library of Wowza Streaming Cloud REST API technical articles](https://www.wowza.com/docs/wowza-streaming-cloud-rest-api).  # Query requirements The Wowza Streaming Cloud REST API uses HTTP requests to retrieve data from cloud-based servers. Requests must contain proper JSON, two authentication keys, and the correct version number in the base path.  ## JSON The Wowza Streaming Cloud REST API uses the [JSON API specification](http://jsonapi.org/format/) to request and return data. This means requests must include the header `Content-Type: application/json` and must include a single resource object in JSON format as primary data.  Responses include HTTP status codes that indicate whether the query was successful. If there was an error, a description explains the problem so that you can fix it and try again.  ## Authentication Requests to the Wowza Streaming Cloud REST API must be authenticated with two keys: an API key and an access key. Each key is a 64-character alphanumeric string that you can find on the **API Access** page in Wowza Streaming Cloud.  Use the `wsc-api-key` and `wsc-access-key` headers to authenticate requests, like this (in cURL):  ```bash curl -H 'wsc-api-key: [64-character-api-key-goes-here]' -H 'wsc-access-key: [64-character-access-key-goes-here]' ```  <!-- ReDoc-Inject: <security-definitions> -->  ## Version The Wowza Streaming Cloud API is currently at version 1.0.0. Use `v1` in your base path in every request, like this path to the live_streams endpoint: ``` https://api.cloud.wowza.com/api/v1/live_streams ``` ## Example query Here is a complete example POST request, in cURL, with proper JSON syntax, headers, authentication, and version information: ```bash curl -H 'wsc-api-key: [64-character-api-key-goes-here]' -H 'wsc-access-key: [64-character-access-key-goes-here]'   -H 'Content-Type: application/json' -X POST -d '{     \"live_stream\": {       \"name\": \"My live Stream\",       \"...\": \"...\"     }   }' https://api.cloud.wowza.com/api/v1/live_streams ``` 
 *
 * The version of the OpenAPI document: 1
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
 * StreamTarget6
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:01:34.965109-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class StreamTarget6 {
  public static final String SERIALIZED_NAME_BACKUP_URL = "backup_url";
  @SerializedName(SERIALIZED_NAME_BACKUP_URL)
  private String backupUrl;

  /**
   * &lt;strong&gt;The &lt;em&gt;chunk_size&lt;/em&gt; parameter is deprecated. To set the chunk size of a stream target, use the POST /stream_targets/[stream_target_id]/properties endpoint.&lt;/strong&gt; Only for targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;WowzaStreamTarget&lt;/strong&gt; and &lt;em&gt;provider&lt;/em&gt; is &lt;strong&gt;akamai_cupertino&lt;/strong&gt;. The segment duration for HLS encoding. The default is &lt;strong&gt;10&lt;/strong&gt;.
   */
  @JsonAdapter(ChunkSizeEnum.Adapter.class)
  public enum ChunkSizeEnum {
    _2("2"),
    
    _4("4"),
    
    _6("6"),
    
    _8("8"),
    
    _10("10");

    private String value;

    ChunkSizeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static ChunkSizeEnum fromValue(String value) {
      for (ChunkSizeEnum b : ChunkSizeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<ChunkSizeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final ChunkSizeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public ChunkSizeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return ChunkSizeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      ChunkSizeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_CHUNK_SIZE = "chunk_size";
  @SerializedName(SERIALIZED_NAME_CHUNK_SIZE)
  private ChunkSizeEnum chunkSize;

  public static final String SERIALIZED_NAME_ENABLED = "enabled";
  @SerializedName(SERIALIZED_NAME_ENABLED)
  private Boolean enabled;

  public static final String SERIALIZED_NAME_HDS_PLAYBACK_URL = "hds_playback_url";
  @SerializedName(SERIALIZED_NAME_HDS_PLAYBACK_URL)
  private String hdsPlaybackUrl;

  public static final String SERIALIZED_NAME_HLS_PLAYBACK_URL = "hls_playback_url";
  @SerializedName(SERIALIZED_NAME_HLS_PLAYBACK_URL)
  private String hlsPlaybackUrl;

  public static final String SERIALIZED_NAME_INGEST_IP_WHITELIST = "ingest_ip_whitelist";
  @SerializedName(SERIALIZED_NAME_INGEST_IP_WHITELIST)
  private List<String> ingestIpWhitelist = new ArrayList<>();

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_PASSWORD = "password";
  @SerializedName(SERIALIZED_NAME_PASSWORD)
  private String password;

  public static final String SERIALIZED_NAME_PRIMARY_URL = "primary_url";
  @SerializedName(SERIALIZED_NAME_PRIMARY_URL)
  private String primaryUrl;

  public static final String SERIALIZED_NAME_PROVIDER = "provider";
  @SerializedName(SERIALIZED_NAME_PROVIDER)
  private String provider;

  public static final String SERIALIZED_NAME_RTMP_PLAYBACK_URL = "rtmp_playback_url";
  @SerializedName(SERIALIZED_NAME_RTMP_PLAYBACK_URL)
  private String rtmpPlaybackUrl;

  public static final String SERIALIZED_NAME_SOURCE_URL = "source_url";
  @SerializedName(SERIALIZED_NAME_SOURCE_URL)
  private String sourceUrl;

  public static final String SERIALIZED_NAME_STREAM_NAME = "stream_name";
  @SerializedName(SERIALIZED_NAME_STREAM_NAME)
  private String streamName;

  public static final String SERIALIZED_NAME_USERNAME = "username";
  @SerializedName(SERIALIZED_NAME_USERNAME)
  private String username;

  public StreamTarget6() {
  }

  public StreamTarget6 backupUrl(String backupUrl) {
    this.backupUrl = backupUrl;
    return this;
  }

  /**
   * Only for targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;CustomStreamTarget&lt;/strong&gt;. The backup RTMP ingest URL of the target, without the preceding protocol and without the trailing slash (/).
   * @return backupUrl
   */
  @javax.annotation.Nullable
  public String getBackupUrl() {
    return backupUrl;
  }

  public void setBackupUrl(String backupUrl) {
    this.backupUrl = backupUrl;
  }


  public StreamTarget6 chunkSize(ChunkSizeEnum chunkSize) {
    this.chunkSize = chunkSize;
    return this;
  }

  /**
   * &lt;strong&gt;The &lt;em&gt;chunk_size&lt;/em&gt; parameter is deprecated. To set the chunk size of a stream target, use the POST /stream_targets/[stream_target_id]/properties endpoint.&lt;/strong&gt; Only for targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;WowzaStreamTarget&lt;/strong&gt; and &lt;em&gt;provider&lt;/em&gt; is &lt;strong&gt;akamai_cupertino&lt;/strong&gt;. The segment duration for HLS encoding. The default is &lt;strong&gt;10&lt;/strong&gt;.
   * @return chunkSize
   */
  @javax.annotation.Nullable
  public ChunkSizeEnum getChunkSize() {
    return chunkSize;
  }

  public void setChunkSize(ChunkSizeEnum chunkSize) {
    this.chunkSize = chunkSize;
  }


  public StreamTarget6 enabled(Boolean enabled) {
    this.enabled = enabled;
    return this;
  }

  /**
   * Only for targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;UltraLowLatencyStreamTarget&lt;/strong&gt;. If &lt;strong&gt;true&lt;/strong&gt; (the default), the source stream is ready to be ingested. If **false**, the source stream won&#39;t be ingested by the target&#39;s origin server.
   * @return enabled
   */
  @javax.annotation.Nullable
  public Boolean getEnabled() {
    return enabled;
  }

  public void setEnabled(Boolean enabled) {
    this.enabled = enabled;
  }


  public StreamTarget6 hdsPlaybackUrl(String hdsPlaybackUrl) {
    this.hdsPlaybackUrl = hdsPlaybackUrl;
    return this;
  }

  /**
   * Only for targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;CustomStreamTarget&lt;/strong&gt; and &lt;em&gt;provider&lt;/em&gt; is &lt;em&gt;not&lt;/em&gt; &lt;strong&gt;akamai_cupertino&lt;/strong&gt;. The web address that the target uses to play Adobe HDS streams.
   * @return hdsPlaybackUrl
   */
  @javax.annotation.Nullable
  public String getHdsPlaybackUrl() {
    return hdsPlaybackUrl;
  }

  public void setHdsPlaybackUrl(String hdsPlaybackUrl) {
    this.hdsPlaybackUrl = hdsPlaybackUrl;
  }


  public StreamTarget6 hlsPlaybackUrl(String hlsPlaybackUrl) {
    this.hlsPlaybackUrl = hlsPlaybackUrl;
    return this;
  }

  /**
   * Only for targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;CustomStreamTarget&lt;/strong&gt;. The web address that the target uses to play Apple HLS streams.
   * @return hlsPlaybackUrl
   */
  @javax.annotation.Nullable
  public String getHlsPlaybackUrl() {
    return hlsPlaybackUrl;
  }

  public void setHlsPlaybackUrl(String hlsPlaybackUrl) {
    this.hlsPlaybackUrl = hlsPlaybackUrl;
  }


  public StreamTarget6 ingestIpWhitelist(List<String> ingestIpWhitelist) {
    this.ingestIpWhitelist = ingestIpWhitelist;
    return this;
  }

  public StreamTarget6 addIngestIpWhitelistItem(String ingestIpWhitelistItem) {
    if (this.ingestIpWhitelist == null) {
      this.ingestIpWhitelist = new ArrayList<>();
    }
    this.ingestIpWhitelist.add(ingestIpWhitelistItem);
    return this;
  }

  /**
   * Only for targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;UltraLowLatencyStreamTarget&lt;/strong&gt; and &lt;em&gt;source_delivery_method&lt;/em&gt; is **push**. A list of IP addresses that can be used to connect to the target&#39;s origin server.
   * @return ingestIpWhitelist
   */
  @javax.annotation.Nullable
  public List<String> getIngestIpWhitelist() {
    return ingestIpWhitelist;
  }

  public void setIngestIpWhitelist(List<String> ingestIpWhitelist) {
    this.ingestIpWhitelist = ingestIpWhitelist;
  }


  public StreamTarget6 name(String name) {
    this.name = name;
    return this;
  }

  /**
   * A descriptive name for the stream target. Maximum 255 characters.
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public StreamTarget6 password(String password) {
    this.password = password;
    return this;
  }

  /**
   * Only for targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;CustomStreamTarget&lt;/strong&gt; and &lt;em&gt;provider&lt;/em&gt; is &lt;em&gt;not&lt;/em&gt; **akamai_cupertino**. A &lt;em&gt;username&lt;/em&gt; must also be present. The password associated with the target username for RTMP authentication.
   * @return password
   */
  @javax.annotation.Nullable
  public String getPassword() {
    return password;
  }

  public void setPassword(String password) {
    this.password = password;
  }


  public StreamTarget6 primaryUrl(String primaryUrl) {
    this.primaryUrl = primaryUrl;
    return this;
  }

  /**
   * Only for targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;CustomStreamTarget&lt;/strong&gt;. The primary RTMP ingest URL, without the preceding protocol and without the trailing slash (/).
   * @return primaryUrl
   */
  @javax.annotation.Nullable
  public String getPrimaryUrl() {
    return primaryUrl;
  }

  public void setPrimaryUrl(String primaryUrl) {
    this.primaryUrl = primaryUrl;
  }


  public StreamTarget6 provider(String provider) {
    this.provider = provider;
    return this;
  }

  /**
   * The CDN for the target. &lt;br /&gt;&lt;br /&gt;Required for targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;CustomStreamTarget&lt;/strong&gt;. Valid values for &lt;strong&gt;CustomStreamTarget&lt;/strong&gt; are &lt;strong&gt;akamai&lt;/strong&gt;, &lt;strong&gt;akamai_cupertino&lt;/strong&gt;, &lt;strong&gt;akamai_rtmp&lt;/strong&gt;, &lt;strong&gt;limelight&lt;/strong&gt;, &lt;strong&gt;rtmp&lt;/strong&gt;, and &lt;strong&gt;ustream&lt;/strong&gt;. Values can be appended with **_mock** to use in the sandbox environment. &lt;br /&gt;&lt;br /&gt;Valid values for &lt;strong&gt;WowzaStreamTarget&lt;/strong&gt; are &lt;strong&gt;akamai&lt;/strong&gt;, &lt;strong&gt;akamai_cupertino&lt;/strong&gt; (default), &lt;strong&gt;akamai_legacy_rtmp&lt;/strong&gt;, and &lt;strong&gt;wowza&lt;/strong&gt;. &lt;br /&gt;&lt;br /&gt;&lt;strong&gt;UltraLowLatencyStreamTarget&lt;/strong&gt; defaults to and must be &lt;strong&gt;wowza&lt;/strong&gt;.
   * @return provider
   */
  @javax.annotation.Nullable
  public String getProvider() {
    return provider;
  }

  public void setProvider(String provider) {
    this.provider = provider;
  }


  public StreamTarget6 rtmpPlaybackUrl(String rtmpPlaybackUrl) {
    this.rtmpPlaybackUrl = rtmpPlaybackUrl;
    return this;
  }

  /**
   * Only for targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;CustomStreamTarget&lt;/strong&gt;. The web address that the target uses to play RTMP streams.
   * @return rtmpPlaybackUrl
   */
  @javax.annotation.Nullable
  public String getRtmpPlaybackUrl() {
    return rtmpPlaybackUrl;
  }

  public void setRtmpPlaybackUrl(String rtmpPlaybackUrl) {
    this.rtmpPlaybackUrl = rtmpPlaybackUrl;
  }


  public StreamTarget6 sourceUrl(String sourceUrl) {
    this.sourceUrl = sourceUrl;
    return this;
  }

  /**
   * Only for targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;UltraLowLatencyStreamTarget&lt;/strong&gt; and &lt;em&gt;source_delivery_method&lt;/em&gt; is **pull**. The URL of a source IP camera or encoder connecting to the stream target.
   * @return sourceUrl
   */
  @javax.annotation.Nullable
  public String getSourceUrl() {
    return sourceUrl;
  }

  public void setSourceUrl(String sourceUrl) {
    this.sourceUrl = sourceUrl;
  }


  public StreamTarget6 streamName(String streamName) {
    this.streamName = streamName;
    return this;
  }

  /**
   * Only for targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;CustomStreamTarget&lt;/strong&gt;. The name of the stream as defined in the target&#39;s ingestion settings.
   * @return streamName
   */
  @javax.annotation.Nullable
  public String getStreamName() {
    return streamName;
  }

  public void setStreamName(String streamName) {
    this.streamName = streamName;
  }


  public StreamTarget6 username(String username) {
    this.username = username;
    return this;
  }

  /**
   * Only for targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;CustomStreamTarget&lt;/strong&gt; and &lt;em&gt;provider&lt;/em&gt; is &lt;em&gt;not&lt;/em&gt; **akamai_cupertino**. The username or ID that the target uses for RTMP authentication.
   * @return username
   */
  @javax.annotation.Nullable
  public String getUsername() {
    return username;
  }

  public void setUsername(String username) {
    this.username = username;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    StreamTarget6 streamTarget6 = (StreamTarget6) o;
    return Objects.equals(this.backupUrl, streamTarget6.backupUrl) &&
        Objects.equals(this.chunkSize, streamTarget6.chunkSize) &&
        Objects.equals(this.enabled, streamTarget6.enabled) &&
        Objects.equals(this.hdsPlaybackUrl, streamTarget6.hdsPlaybackUrl) &&
        Objects.equals(this.hlsPlaybackUrl, streamTarget6.hlsPlaybackUrl) &&
        Objects.equals(this.ingestIpWhitelist, streamTarget6.ingestIpWhitelist) &&
        Objects.equals(this.name, streamTarget6.name) &&
        Objects.equals(this.password, streamTarget6.password) &&
        Objects.equals(this.primaryUrl, streamTarget6.primaryUrl) &&
        Objects.equals(this.provider, streamTarget6.provider) &&
        Objects.equals(this.rtmpPlaybackUrl, streamTarget6.rtmpPlaybackUrl) &&
        Objects.equals(this.sourceUrl, streamTarget6.sourceUrl) &&
        Objects.equals(this.streamName, streamTarget6.streamName) &&
        Objects.equals(this.username, streamTarget6.username);
  }

  @Override
  public int hashCode() {
    return Objects.hash(backupUrl, chunkSize, enabled, hdsPlaybackUrl, hlsPlaybackUrl, ingestIpWhitelist, name, password, primaryUrl, provider, rtmpPlaybackUrl, sourceUrl, streamName, username);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class StreamTarget6 {\n");
    sb.append("    backupUrl: ").append(toIndentedString(backupUrl)).append("\n");
    sb.append("    chunkSize: ").append(toIndentedString(chunkSize)).append("\n");
    sb.append("    enabled: ").append(toIndentedString(enabled)).append("\n");
    sb.append("    hdsPlaybackUrl: ").append(toIndentedString(hdsPlaybackUrl)).append("\n");
    sb.append("    hlsPlaybackUrl: ").append(toIndentedString(hlsPlaybackUrl)).append("\n");
    sb.append("    ingestIpWhitelist: ").append(toIndentedString(ingestIpWhitelist)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    password: ").append(toIndentedString(password)).append("\n");
    sb.append("    primaryUrl: ").append(toIndentedString(primaryUrl)).append("\n");
    sb.append("    provider: ").append(toIndentedString(provider)).append("\n");
    sb.append("    rtmpPlaybackUrl: ").append(toIndentedString(rtmpPlaybackUrl)).append("\n");
    sb.append("    sourceUrl: ").append(toIndentedString(sourceUrl)).append("\n");
    sb.append("    streamName: ").append(toIndentedString(streamName)).append("\n");
    sb.append("    username: ").append(toIndentedString(username)).append("\n");
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
    openapiFields.add("backup_url");
    openapiFields.add("chunk_size");
    openapiFields.add("enabled");
    openapiFields.add("hds_playback_url");
    openapiFields.add("hls_playback_url");
    openapiFields.add("ingest_ip_whitelist");
    openapiFields.add("name");
    openapiFields.add("password");
    openapiFields.add("primary_url");
    openapiFields.add("provider");
    openapiFields.add("rtmp_playback_url");
    openapiFields.add("source_url");
    openapiFields.add("stream_name");
    openapiFields.add("username");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to StreamTarget6
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!StreamTarget6.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in StreamTarget6 is not found in the empty JSON string", StreamTarget6.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!StreamTarget6.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `StreamTarget6` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("backup_url") != null && !jsonObj.get("backup_url").isJsonNull()) && !jsonObj.get("backup_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `backup_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("backup_url").toString()));
      }
      if ((jsonObj.get("chunk_size") != null && !jsonObj.get("chunk_size").isJsonNull()) && !jsonObj.get("chunk_size").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `chunk_size` to be a primitive type in the JSON string but got `%s`", jsonObj.get("chunk_size").toString()));
      }
      // validate the optional field `chunk_size`
      if (jsonObj.get("chunk_size") != null && !jsonObj.get("chunk_size").isJsonNull()) {
        ChunkSizeEnum.validateJsonElement(jsonObj.get("chunk_size"));
      }
      if ((jsonObj.get("hds_playback_url") != null && !jsonObj.get("hds_playback_url").isJsonNull()) && !jsonObj.get("hds_playback_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `hds_playback_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("hds_playback_url").toString()));
      }
      if ((jsonObj.get("hls_playback_url") != null && !jsonObj.get("hls_playback_url").isJsonNull()) && !jsonObj.get("hls_playback_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `hls_playback_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("hls_playback_url").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("ingest_ip_whitelist") != null && !jsonObj.get("ingest_ip_whitelist").isJsonNull() && !jsonObj.get("ingest_ip_whitelist").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `ingest_ip_whitelist` to be an array in the JSON string but got `%s`", jsonObj.get("ingest_ip_whitelist").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("password") != null && !jsonObj.get("password").isJsonNull()) && !jsonObj.get("password").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `password` to be a primitive type in the JSON string but got `%s`", jsonObj.get("password").toString()));
      }
      if ((jsonObj.get("primary_url") != null && !jsonObj.get("primary_url").isJsonNull()) && !jsonObj.get("primary_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `primary_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("primary_url").toString()));
      }
      if ((jsonObj.get("provider") != null && !jsonObj.get("provider").isJsonNull()) && !jsonObj.get("provider").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `provider` to be a primitive type in the JSON string but got `%s`", jsonObj.get("provider").toString()));
      }
      if ((jsonObj.get("rtmp_playback_url") != null && !jsonObj.get("rtmp_playback_url").isJsonNull()) && !jsonObj.get("rtmp_playback_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `rtmp_playback_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("rtmp_playback_url").toString()));
      }
      if ((jsonObj.get("source_url") != null && !jsonObj.get("source_url").isJsonNull()) && !jsonObj.get("source_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `source_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("source_url").toString()));
      }
      if ((jsonObj.get("stream_name") != null && !jsonObj.get("stream_name").isJsonNull()) && !jsonObj.get("stream_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `stream_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("stream_name").toString()));
      }
      if ((jsonObj.get("username") != null && !jsonObj.get("username").isJsonNull()) && !jsonObj.get("username").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `username` to be a primitive type in the JSON string but got `%s`", jsonObj.get("username").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!StreamTarget6.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'StreamTarget6' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<StreamTarget6> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(StreamTarget6.class));

       return (TypeAdapter<T>) new TypeAdapter<StreamTarget6>() {
           @Override
           public void write(JsonWriter out, StreamTarget6 value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public StreamTarget6 read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of StreamTarget6 given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of StreamTarget6
   * @throws IOException if the JSON string is invalid with respect to StreamTarget6
   */
  public static StreamTarget6 fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, StreamTarget6.class);
  }

  /**
   * Convert an instance of StreamTarget6 to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

