/*
 * FrontDoorManagementClient
 * Use these APIs to manage Azure Front Door resources through the Azure Resource Manager. You must make sure that requests made to these resources are secure.
 *
 * The version of the OpenAPI document: 2019-05-01
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
 * Backend address of a frontDoor load balancer.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:16:31.612735-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Backend {
  public static final String SERIALIZED_NAME_ADDRESS = "address";
  @SerializedName(SERIALIZED_NAME_ADDRESS)
  private String address;

  public static final String SERIALIZED_NAME_BACKEND_HOST_HEADER = "backendHostHeader";
  @SerializedName(SERIALIZED_NAME_BACKEND_HOST_HEADER)
  private String backendHostHeader;

  /**
   * Whether to enable use of this backend. Permitted values are &#39;Enabled&#39; or &#39;Disabled&#39;
   */
  @JsonAdapter(EnabledStateEnum.Adapter.class)
  public enum EnabledStateEnum {
    ENABLED("Enabled"),
    
    DISABLED("Disabled");

    private String value;

    EnabledStateEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static EnabledStateEnum fromValue(String value) {
      for (EnabledStateEnum b : EnabledStateEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<EnabledStateEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final EnabledStateEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public EnabledStateEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return EnabledStateEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      EnabledStateEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_ENABLED_STATE = "enabledState";
  @SerializedName(SERIALIZED_NAME_ENABLED_STATE)
  private EnabledStateEnum enabledState;

  public static final String SERIALIZED_NAME_HTTP_PORT = "httpPort";
  @SerializedName(SERIALIZED_NAME_HTTP_PORT)
  private Integer httpPort;

  public static final String SERIALIZED_NAME_HTTPS_PORT = "httpsPort";
  @SerializedName(SERIALIZED_NAME_HTTPS_PORT)
  private Integer httpsPort;

  public static final String SERIALIZED_NAME_PRIORITY = "priority";
  @SerializedName(SERIALIZED_NAME_PRIORITY)
  private Integer priority;

  public static final String SERIALIZED_NAME_WEIGHT = "weight";
  @SerializedName(SERIALIZED_NAME_WEIGHT)
  private Integer weight;

  public Backend() {
  }

  public Backend address(String address) {
    this.address = address;
    return this;
  }

  /**
   * Location of the backend (IP address or FQDN)
   * @return address
   */
  @javax.annotation.Nullable
  public String getAddress() {
    return address;
  }

  public void setAddress(String address) {
    this.address = address;
  }


  public Backend backendHostHeader(String backendHostHeader) {
    this.backendHostHeader = backendHostHeader;
    return this;
  }

  /**
   * The value to use as the host header sent to the backend. If blank or unspecified, this defaults to the incoming host.
   * @return backendHostHeader
   */
  @javax.annotation.Nullable
  public String getBackendHostHeader() {
    return backendHostHeader;
  }

  public void setBackendHostHeader(String backendHostHeader) {
    this.backendHostHeader = backendHostHeader;
  }


  public Backend enabledState(EnabledStateEnum enabledState) {
    this.enabledState = enabledState;
    return this;
  }

  /**
   * Whether to enable use of this backend. Permitted values are &#39;Enabled&#39; or &#39;Disabled&#39;
   * @return enabledState
   */
  @javax.annotation.Nullable
  public EnabledStateEnum getEnabledState() {
    return enabledState;
  }

  public void setEnabledState(EnabledStateEnum enabledState) {
    this.enabledState = enabledState;
  }


  public Backend httpPort(Integer httpPort) {
    this.httpPort = httpPort;
    return this;
  }

  /**
   * The HTTP TCP port number. Must be between 1 and 65535.
   * minimum: 1
   * maximum: 65535
   * @return httpPort
   */
  @javax.annotation.Nullable
  public Integer getHttpPort() {
    return httpPort;
  }

  public void setHttpPort(Integer httpPort) {
    this.httpPort = httpPort;
  }


  public Backend httpsPort(Integer httpsPort) {
    this.httpsPort = httpsPort;
    return this;
  }

  /**
   * The HTTPS TCP port number. Must be between 1 and 65535.
   * minimum: 1
   * maximum: 65535
   * @return httpsPort
   */
  @javax.annotation.Nullable
  public Integer getHttpsPort() {
    return httpsPort;
  }

  public void setHttpsPort(Integer httpsPort) {
    this.httpsPort = httpsPort;
  }


  public Backend priority(Integer priority) {
    this.priority = priority;
    return this;
  }

  /**
   * Priority to use for load balancing. Higher priorities will not be used for load balancing if any lower priority backend is healthy.
   * minimum: 1
   * maximum: 5
   * @return priority
   */
  @javax.annotation.Nullable
  public Integer getPriority() {
    return priority;
  }

  public void setPriority(Integer priority) {
    this.priority = priority;
  }


  public Backend weight(Integer weight) {
    this.weight = weight;
    return this;
  }

  /**
   * Weight of this endpoint for load balancing purposes.
   * minimum: 1
   * maximum: 1000
   * @return weight
   */
  @javax.annotation.Nullable
  public Integer getWeight() {
    return weight;
  }

  public void setWeight(Integer weight) {
    this.weight = weight;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Backend backend = (Backend) o;
    return Objects.equals(this.address, backend.address) &&
        Objects.equals(this.backendHostHeader, backend.backendHostHeader) &&
        Objects.equals(this.enabledState, backend.enabledState) &&
        Objects.equals(this.httpPort, backend.httpPort) &&
        Objects.equals(this.httpsPort, backend.httpsPort) &&
        Objects.equals(this.priority, backend.priority) &&
        Objects.equals(this.weight, backend.weight);
  }

  @Override
  public int hashCode() {
    return Objects.hash(address, backendHostHeader, enabledState, httpPort, httpsPort, priority, weight);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Backend {\n");
    sb.append("    address: ").append(toIndentedString(address)).append("\n");
    sb.append("    backendHostHeader: ").append(toIndentedString(backendHostHeader)).append("\n");
    sb.append("    enabledState: ").append(toIndentedString(enabledState)).append("\n");
    sb.append("    httpPort: ").append(toIndentedString(httpPort)).append("\n");
    sb.append("    httpsPort: ").append(toIndentedString(httpsPort)).append("\n");
    sb.append("    priority: ").append(toIndentedString(priority)).append("\n");
    sb.append("    weight: ").append(toIndentedString(weight)).append("\n");
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
    openapiFields.add("address");
    openapiFields.add("backendHostHeader");
    openapiFields.add("enabledState");
    openapiFields.add("httpPort");
    openapiFields.add("httpsPort");
    openapiFields.add("priority");
    openapiFields.add("weight");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Backend
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Backend.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Backend is not found in the empty JSON string", Backend.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Backend.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Backend` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("address") != null && !jsonObj.get("address").isJsonNull()) && !jsonObj.get("address").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `address` to be a primitive type in the JSON string but got `%s`", jsonObj.get("address").toString()));
      }
      if ((jsonObj.get("backendHostHeader") != null && !jsonObj.get("backendHostHeader").isJsonNull()) && !jsonObj.get("backendHostHeader").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `backendHostHeader` to be a primitive type in the JSON string but got `%s`", jsonObj.get("backendHostHeader").toString()));
      }
      if ((jsonObj.get("enabledState") != null && !jsonObj.get("enabledState").isJsonNull()) && !jsonObj.get("enabledState").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `enabledState` to be a primitive type in the JSON string but got `%s`", jsonObj.get("enabledState").toString()));
      }
      // validate the optional field `enabledState`
      if (jsonObj.get("enabledState") != null && !jsonObj.get("enabledState").isJsonNull()) {
        EnabledStateEnum.validateJsonElement(jsonObj.get("enabledState"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Backend.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Backend' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Backend> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Backend.class));

       return (TypeAdapter<T>) new TypeAdapter<Backend>() {
           @Override
           public void write(JsonWriter out, Backend value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Backend read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Backend given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Backend
   * @throws IOException if the JSON string is invalid with respect to Backend
   */
  public static Backend fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Backend.class);
  }

  /**
   * Convert an instance of Backend to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

