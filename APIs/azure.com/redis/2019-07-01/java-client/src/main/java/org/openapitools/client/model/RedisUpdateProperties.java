/*
 * RedisManagementClient
 * REST API for Azure Redis Cache Service.
 *
 * The version of the OpenAPI document: 2019-07-01
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
import java.util.HashMap;
import java.util.Map;
import org.openapitools.client.model.Sku;

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
 * Patchable properties of the redis cache.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:52:25.405954-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class RedisUpdateProperties {
  public static final String SERIALIZED_NAME_SKU = "sku";
  @SerializedName(SERIALIZED_NAME_SKU)
  private Sku sku;

  public static final String SERIALIZED_NAME_ENABLE_NON_SSL_PORT = "enableNonSslPort";
  @SerializedName(SERIALIZED_NAME_ENABLE_NON_SSL_PORT)
  private Boolean enableNonSslPort;

  /**
   * Optional: requires clients to use a specified TLS version (or higher) to connect (e,g, &#39;1.0&#39;, &#39;1.1&#39;, &#39;1.2&#39;)
   */
  @JsonAdapter(MinimumTlsVersionEnum.Adapter.class)
  public enum MinimumTlsVersionEnum {
    _0("1.0"),
    
    _1("1.1"),
    
    _2("1.2");

    private String value;

    MinimumTlsVersionEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static MinimumTlsVersionEnum fromValue(String value) {
      for (MinimumTlsVersionEnum b : MinimumTlsVersionEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<MinimumTlsVersionEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final MinimumTlsVersionEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public MinimumTlsVersionEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return MinimumTlsVersionEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      MinimumTlsVersionEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_MINIMUM_TLS_VERSION = "minimumTlsVersion";
  @SerializedName(SERIALIZED_NAME_MINIMUM_TLS_VERSION)
  private MinimumTlsVersionEnum minimumTlsVersion;

  public static final String SERIALIZED_NAME_REDIS_CONFIGURATION = "redisConfiguration";
  @SerializedName(SERIALIZED_NAME_REDIS_CONFIGURATION)
  private Map<String, String> redisConfiguration = new HashMap<>();

  public static final String SERIALIZED_NAME_REPLICAS_PER_MASTER = "replicasPerMaster";
  @SerializedName(SERIALIZED_NAME_REPLICAS_PER_MASTER)
  private Integer replicasPerMaster;

  public static final String SERIALIZED_NAME_SHARD_COUNT = "shardCount";
  @SerializedName(SERIALIZED_NAME_SHARD_COUNT)
  private Integer shardCount;

  public static final String SERIALIZED_NAME_TENANT_SETTINGS = "tenantSettings";
  @SerializedName(SERIALIZED_NAME_TENANT_SETTINGS)
  private Map<String, String> tenantSettings = new HashMap<>();

  public RedisUpdateProperties() {
  }

  public RedisUpdateProperties sku(Sku sku) {
    this.sku = sku;
    return this;
  }

  /**
   * Get sku
   * @return sku
   */
  @javax.annotation.Nullable
  public Sku getSku() {
    return sku;
  }

  public void setSku(Sku sku) {
    this.sku = sku;
  }


  public RedisUpdateProperties enableNonSslPort(Boolean enableNonSslPort) {
    this.enableNonSslPort = enableNonSslPort;
    return this;
  }

  /**
   * Specifies whether the non-ssl Redis server port (6379) is enabled.
   * @return enableNonSslPort
   */
  @javax.annotation.Nullable
  public Boolean getEnableNonSslPort() {
    return enableNonSslPort;
  }

  public void setEnableNonSslPort(Boolean enableNonSslPort) {
    this.enableNonSslPort = enableNonSslPort;
  }


  public RedisUpdateProperties minimumTlsVersion(MinimumTlsVersionEnum minimumTlsVersion) {
    this.minimumTlsVersion = minimumTlsVersion;
    return this;
  }

  /**
   * Optional: requires clients to use a specified TLS version (or higher) to connect (e,g, &#39;1.0&#39;, &#39;1.1&#39;, &#39;1.2&#39;)
   * @return minimumTlsVersion
   */
  @javax.annotation.Nullable
  public MinimumTlsVersionEnum getMinimumTlsVersion() {
    return minimumTlsVersion;
  }

  public void setMinimumTlsVersion(MinimumTlsVersionEnum minimumTlsVersion) {
    this.minimumTlsVersion = minimumTlsVersion;
  }


  public RedisUpdateProperties redisConfiguration(Map<String, String> redisConfiguration) {
    this.redisConfiguration = redisConfiguration;
    return this;
  }

  public RedisUpdateProperties putRedisConfigurationItem(String key, String redisConfigurationItem) {
    if (this.redisConfiguration == null) {
      this.redisConfiguration = new HashMap<>();
    }
    this.redisConfiguration.put(key, redisConfigurationItem);
    return this;
  }

  /**
   * All Redis Settings. Few possible keys: rdb-backup-enabled,rdb-storage-connection-string,rdb-backup-frequency,maxmemory-delta,maxmemory-policy,notify-keyspace-events,maxmemory-samples,slowlog-log-slower-than,slowlog-max-len,list-max-ziplist-entries,list-max-ziplist-value,hash-max-ziplist-entries,hash-max-ziplist-value,set-max-intset-entries,zset-max-ziplist-entries,zset-max-ziplist-value etc.
   * @return redisConfiguration
   */
  @javax.annotation.Nullable
  public Map<String, String> getRedisConfiguration() {
    return redisConfiguration;
  }

  public void setRedisConfiguration(Map<String, String> redisConfiguration) {
    this.redisConfiguration = redisConfiguration;
  }


  public RedisUpdateProperties replicasPerMaster(Integer replicasPerMaster) {
    this.replicasPerMaster = replicasPerMaster;
    return this;
  }

  /**
   * The number of replicas to be created per master.
   * @return replicasPerMaster
   */
  @javax.annotation.Nullable
  public Integer getReplicasPerMaster() {
    return replicasPerMaster;
  }

  public void setReplicasPerMaster(Integer replicasPerMaster) {
    this.replicasPerMaster = replicasPerMaster;
  }


  public RedisUpdateProperties shardCount(Integer shardCount) {
    this.shardCount = shardCount;
    return this;
  }

  /**
   * The number of shards to be created on a Premium Cluster Cache.
   * @return shardCount
   */
  @javax.annotation.Nullable
  public Integer getShardCount() {
    return shardCount;
  }

  public void setShardCount(Integer shardCount) {
    this.shardCount = shardCount;
  }


  public RedisUpdateProperties tenantSettings(Map<String, String> tenantSettings) {
    this.tenantSettings = tenantSettings;
    return this;
  }

  public RedisUpdateProperties putTenantSettingsItem(String key, String tenantSettingsItem) {
    if (this.tenantSettings == null) {
      this.tenantSettings = new HashMap<>();
    }
    this.tenantSettings.put(key, tenantSettingsItem);
    return this;
  }

  /**
   * A dictionary of tenant settings
   * @return tenantSettings
   */
  @javax.annotation.Nullable
  public Map<String, String> getTenantSettings() {
    return tenantSettings;
  }

  public void setTenantSettings(Map<String, String> tenantSettings) {
    this.tenantSettings = tenantSettings;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    RedisUpdateProperties redisUpdateProperties = (RedisUpdateProperties) o;
    return Objects.equals(this.sku, redisUpdateProperties.sku) &&
        Objects.equals(this.enableNonSslPort, redisUpdateProperties.enableNonSslPort) &&
        Objects.equals(this.minimumTlsVersion, redisUpdateProperties.minimumTlsVersion) &&
        Objects.equals(this.redisConfiguration, redisUpdateProperties.redisConfiguration) &&
        Objects.equals(this.replicasPerMaster, redisUpdateProperties.replicasPerMaster) &&
        Objects.equals(this.shardCount, redisUpdateProperties.shardCount) &&
        Objects.equals(this.tenantSettings, redisUpdateProperties.tenantSettings);
  }

  @Override
  public int hashCode() {
    return Objects.hash(sku, enableNonSslPort, minimumTlsVersion, redisConfiguration, replicasPerMaster, shardCount, tenantSettings);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class RedisUpdateProperties {\n");
    sb.append("    sku: ").append(toIndentedString(sku)).append("\n");
    sb.append("    enableNonSslPort: ").append(toIndentedString(enableNonSslPort)).append("\n");
    sb.append("    minimumTlsVersion: ").append(toIndentedString(minimumTlsVersion)).append("\n");
    sb.append("    redisConfiguration: ").append(toIndentedString(redisConfiguration)).append("\n");
    sb.append("    replicasPerMaster: ").append(toIndentedString(replicasPerMaster)).append("\n");
    sb.append("    shardCount: ").append(toIndentedString(shardCount)).append("\n");
    sb.append("    tenantSettings: ").append(toIndentedString(tenantSettings)).append("\n");
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
    openapiFields.add("enableNonSslPort");
    openapiFields.add("minimumTlsVersion");
    openapiFields.add("redisConfiguration");
    openapiFields.add("replicasPerMaster");
    openapiFields.add("shardCount");
    openapiFields.add("tenantSettings");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to RedisUpdateProperties
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!RedisUpdateProperties.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in RedisUpdateProperties is not found in the empty JSON string", RedisUpdateProperties.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!RedisUpdateProperties.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `RedisUpdateProperties` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `sku`
      if (jsonObj.get("sku") != null && !jsonObj.get("sku").isJsonNull()) {
        Sku.validateJsonElement(jsonObj.get("sku"));
      }
      if ((jsonObj.get("minimumTlsVersion") != null && !jsonObj.get("minimumTlsVersion").isJsonNull()) && !jsonObj.get("minimumTlsVersion").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `minimumTlsVersion` to be a primitive type in the JSON string but got `%s`", jsonObj.get("minimumTlsVersion").toString()));
      }
      // validate the optional field `minimumTlsVersion`
      if (jsonObj.get("minimumTlsVersion") != null && !jsonObj.get("minimumTlsVersion").isJsonNull()) {
        MinimumTlsVersionEnum.validateJsonElement(jsonObj.get("minimumTlsVersion"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!RedisUpdateProperties.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'RedisUpdateProperties' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<RedisUpdateProperties> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(RedisUpdateProperties.class));

       return (TypeAdapter<T>) new TypeAdapter<RedisUpdateProperties>() {
           @Override
           public void write(JsonWriter out, RedisUpdateProperties value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public RedisUpdateProperties read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of RedisUpdateProperties given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of RedisUpdateProperties
   * @throws IOException if the JSON string is invalid with respect to RedisUpdateProperties
   */
  public static RedisUpdateProperties fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, RedisUpdateProperties.class);
  }

  /**
   * Convert an instance of RedisUpdateProperties to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

