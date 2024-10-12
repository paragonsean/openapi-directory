/*
 * FrontDoorManagementClient
 * Use these APIs to manage Azure Front Door resources through the Azure Resource Manager. You must make sure that requests made to these resources are secure.
 *
 * The version of the OpenAPI document: 2019-04-01
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
 * L7 health probe settings for a backend pool
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:16:34.178652-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class HealthProbeSettingsUpdateParameters {
  public static final String SERIALIZED_NAME_INTERVAL_IN_SECONDS = "intervalInSeconds";
  @SerializedName(SERIALIZED_NAME_INTERVAL_IN_SECONDS)
  private Integer intervalInSeconds;

  public static final String SERIALIZED_NAME_PATH = "path";
  @SerializedName(SERIALIZED_NAME_PATH)
  private String path;

  /**
   * Protocol scheme to use for this probe
   */
  @JsonAdapter(ProtocolEnum.Adapter.class)
  public enum ProtocolEnum {
    HTTP("Http"),
    
    HTTPS("Https");

    private String value;

    ProtocolEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static ProtocolEnum fromValue(String value) {
      for (ProtocolEnum b : ProtocolEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<ProtocolEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final ProtocolEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public ProtocolEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return ProtocolEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      ProtocolEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_PROTOCOL = "protocol";
  @SerializedName(SERIALIZED_NAME_PROTOCOL)
  private ProtocolEnum protocol;

  public HealthProbeSettingsUpdateParameters() {
  }

  public HealthProbeSettingsUpdateParameters intervalInSeconds(Integer intervalInSeconds) {
    this.intervalInSeconds = intervalInSeconds;
    return this;
  }

  /**
   * The number of seconds between health probes.
   * @return intervalInSeconds
   */
  @javax.annotation.Nullable
  public Integer getIntervalInSeconds() {
    return intervalInSeconds;
  }

  public void setIntervalInSeconds(Integer intervalInSeconds) {
    this.intervalInSeconds = intervalInSeconds;
  }


  public HealthProbeSettingsUpdateParameters path(String path) {
    this.path = path;
    return this;
  }

  /**
   * The path to use for the health probe. Default is /
   * @return path
   */
  @javax.annotation.Nullable
  public String getPath() {
    return path;
  }

  public void setPath(String path) {
    this.path = path;
  }


  public HealthProbeSettingsUpdateParameters protocol(ProtocolEnum protocol) {
    this.protocol = protocol;
    return this;
  }

  /**
   * Protocol scheme to use for this probe
   * @return protocol
   */
  @javax.annotation.Nullable
  public ProtocolEnum getProtocol() {
    return protocol;
  }

  public void setProtocol(ProtocolEnum protocol) {
    this.protocol = protocol;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    HealthProbeSettingsUpdateParameters healthProbeSettingsUpdateParameters = (HealthProbeSettingsUpdateParameters) o;
    return Objects.equals(this.intervalInSeconds, healthProbeSettingsUpdateParameters.intervalInSeconds) &&
        Objects.equals(this.path, healthProbeSettingsUpdateParameters.path) &&
        Objects.equals(this.protocol, healthProbeSettingsUpdateParameters.protocol);
  }

  @Override
  public int hashCode() {
    return Objects.hash(intervalInSeconds, path, protocol);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class HealthProbeSettingsUpdateParameters {\n");
    sb.append("    intervalInSeconds: ").append(toIndentedString(intervalInSeconds)).append("\n");
    sb.append("    path: ").append(toIndentedString(path)).append("\n");
    sb.append("    protocol: ").append(toIndentedString(protocol)).append("\n");
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
    openapiFields.add("intervalInSeconds");
    openapiFields.add("path");
    openapiFields.add("protocol");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to HealthProbeSettingsUpdateParameters
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!HealthProbeSettingsUpdateParameters.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in HealthProbeSettingsUpdateParameters is not found in the empty JSON string", HealthProbeSettingsUpdateParameters.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!HealthProbeSettingsUpdateParameters.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `HealthProbeSettingsUpdateParameters` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("path") != null && !jsonObj.get("path").isJsonNull()) && !jsonObj.get("path").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `path` to be a primitive type in the JSON string but got `%s`", jsonObj.get("path").toString()));
      }
      if ((jsonObj.get("protocol") != null && !jsonObj.get("protocol").isJsonNull()) && !jsonObj.get("protocol").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `protocol` to be a primitive type in the JSON string but got `%s`", jsonObj.get("protocol").toString()));
      }
      // validate the optional field `protocol`
      if (jsonObj.get("protocol") != null && !jsonObj.get("protocol").isJsonNull()) {
        ProtocolEnum.validateJsonElement(jsonObj.get("protocol"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!HealthProbeSettingsUpdateParameters.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'HealthProbeSettingsUpdateParameters' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<HealthProbeSettingsUpdateParameters> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(HealthProbeSettingsUpdateParameters.class));

       return (TypeAdapter<T>) new TypeAdapter<HealthProbeSettingsUpdateParameters>() {
           @Override
           public void write(JsonWriter out, HealthProbeSettingsUpdateParameters value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public HealthProbeSettingsUpdateParameters read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of HealthProbeSettingsUpdateParameters given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of HealthProbeSettingsUpdateParameters
   * @throws IOException if the JSON string is invalid with respect to HealthProbeSettingsUpdateParameters
   */
  public static HealthProbeSettingsUpdateParameters fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, HealthProbeSettingsUpdateParameters.class);
  }

  /**
   * Convert an instance of HealthProbeSettingsUpdateParameters to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

