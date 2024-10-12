/*
 * Otoroshi Admin API
 * Admin API of the Otoroshi reverse proxy
 *
 * The version of the OpenAPI document: 1.5.0-dev
 * Contact: oss@maif.fr
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
 * The configuration of the circuit breaker for a service descriptor
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:11:27.562730-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ClientConfig {
  public static final String SERIALIZED_NAME_BACKOFF_FACTOR = "backoffFactor";
  @SerializedName(SERIALIZED_NAME_BACKOFF_FACTOR)
  private Integer backoffFactor;

  public static final String SERIALIZED_NAME_CALL_TIMEOUT = "callTimeout";
  @SerializedName(SERIALIZED_NAME_CALL_TIMEOUT)
  private Integer callTimeout;

  public static final String SERIALIZED_NAME_GLOBAL_TIMEOUT = "globalTimeout";
  @SerializedName(SERIALIZED_NAME_GLOBAL_TIMEOUT)
  private Integer globalTimeout;

  public static final String SERIALIZED_NAME_MAX_ERRORS = "maxErrors";
  @SerializedName(SERIALIZED_NAME_MAX_ERRORS)
  private Integer maxErrors;

  public static final String SERIALIZED_NAME_RETRIES = "retries";
  @SerializedName(SERIALIZED_NAME_RETRIES)
  private Integer retries;

  public static final String SERIALIZED_NAME_RETRY_INITIAL_DELAY = "retryInitialDelay";
  @SerializedName(SERIALIZED_NAME_RETRY_INITIAL_DELAY)
  private Integer retryInitialDelay;

  public static final String SERIALIZED_NAME_SAMPLE_INTERVAL = "sampleInterval";
  @SerializedName(SERIALIZED_NAME_SAMPLE_INTERVAL)
  private Integer sampleInterval;

  public static final String SERIALIZED_NAME_USE_CIRCUIT_BREAKER = "useCircuitBreaker";
  @SerializedName(SERIALIZED_NAME_USE_CIRCUIT_BREAKER)
  private Boolean useCircuitBreaker;

  public ClientConfig() {
  }

  public ClientConfig backoffFactor(Integer backoffFactor) {
    this.backoffFactor = backoffFactor;
    return this;
  }

  /**
   * Specify the factor to multiply the delay for each retry
   * @return backoffFactor
   */
  @javax.annotation.Nonnull
  public Integer getBackoffFactor() {
    return backoffFactor;
  }

  public void setBackoffFactor(Integer backoffFactor) {
    this.backoffFactor = backoffFactor;
  }


  public ClientConfig callTimeout(Integer callTimeout) {
    this.callTimeout = callTimeout;
    return this;
  }

  /**
   * Specify how long each call should last at most in milliseconds
   * @return callTimeout
   */
  @javax.annotation.Nonnull
  public Integer getCallTimeout() {
    return callTimeout;
  }

  public void setCallTimeout(Integer callTimeout) {
    this.callTimeout = callTimeout;
  }


  public ClientConfig globalTimeout(Integer globalTimeout) {
    this.globalTimeout = globalTimeout;
    return this;
  }

  /**
   * Specify how long the global call (with retries) should last at most in milliseconds
   * @return globalTimeout
   */
  @javax.annotation.Nonnull
  public Integer getGlobalTimeout() {
    return globalTimeout;
  }

  public void setGlobalTimeout(Integer globalTimeout) {
    this.globalTimeout = globalTimeout;
  }


  public ClientConfig maxErrors(Integer maxErrors) {
    this.maxErrors = maxErrors;
    return this;
  }

  /**
   * Specify how many errors can pass before opening the circuit breaker
   * @return maxErrors
   */
  @javax.annotation.Nonnull
  public Integer getMaxErrors() {
    return maxErrors;
  }

  public void setMaxErrors(Integer maxErrors) {
    this.maxErrors = maxErrors;
  }


  public ClientConfig retries(Integer retries) {
    this.retries = retries;
    return this;
  }

  /**
   * Specify how many times the client will try to fetch the result of the request after an error before giving up.
   * @return retries
   */
  @javax.annotation.Nonnull
  public Integer getRetries() {
    return retries;
  }

  public void setRetries(Integer retries) {
    this.retries = retries;
  }


  public ClientConfig retryInitialDelay(Integer retryInitialDelay) {
    this.retryInitialDelay = retryInitialDelay;
    return this;
  }

  /**
   * Specify the delay between two retries. Each retry, the delay is multiplied by the backoff factor
   * @return retryInitialDelay
   */
  @javax.annotation.Nonnull
  public Integer getRetryInitialDelay() {
    return retryInitialDelay;
  }

  public void setRetryInitialDelay(Integer retryInitialDelay) {
    this.retryInitialDelay = retryInitialDelay;
  }


  public ClientConfig sampleInterval(Integer sampleInterval) {
    this.sampleInterval = sampleInterval;
    return this;
  }

  /**
   * Specify the sliding window time for the circuit breaker in milliseconds, after this time, error count will be reseted
   * @return sampleInterval
   */
  @javax.annotation.Nonnull
  public Integer getSampleInterval() {
    return sampleInterval;
  }

  public void setSampleInterval(Integer sampleInterval) {
    this.sampleInterval = sampleInterval;
  }


  public ClientConfig useCircuitBreaker(Boolean useCircuitBreaker) {
    this.useCircuitBreaker = useCircuitBreaker;
    return this;
  }

  /**
   * Use a circuit breaker to avoid cascading failure when calling chains of services. Highly recommended !
   * @return useCircuitBreaker
   */
  @javax.annotation.Nonnull
  public Boolean getUseCircuitBreaker() {
    return useCircuitBreaker;
  }

  public void setUseCircuitBreaker(Boolean useCircuitBreaker) {
    this.useCircuitBreaker = useCircuitBreaker;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ClientConfig clientConfig = (ClientConfig) o;
    return Objects.equals(this.backoffFactor, clientConfig.backoffFactor) &&
        Objects.equals(this.callTimeout, clientConfig.callTimeout) &&
        Objects.equals(this.globalTimeout, clientConfig.globalTimeout) &&
        Objects.equals(this.maxErrors, clientConfig.maxErrors) &&
        Objects.equals(this.retries, clientConfig.retries) &&
        Objects.equals(this.retryInitialDelay, clientConfig.retryInitialDelay) &&
        Objects.equals(this.sampleInterval, clientConfig.sampleInterval) &&
        Objects.equals(this.useCircuitBreaker, clientConfig.useCircuitBreaker);
  }

  @Override
  public int hashCode() {
    return Objects.hash(backoffFactor, callTimeout, globalTimeout, maxErrors, retries, retryInitialDelay, sampleInterval, useCircuitBreaker);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ClientConfig {\n");
    sb.append("    backoffFactor: ").append(toIndentedString(backoffFactor)).append("\n");
    sb.append("    callTimeout: ").append(toIndentedString(callTimeout)).append("\n");
    sb.append("    globalTimeout: ").append(toIndentedString(globalTimeout)).append("\n");
    sb.append("    maxErrors: ").append(toIndentedString(maxErrors)).append("\n");
    sb.append("    retries: ").append(toIndentedString(retries)).append("\n");
    sb.append("    retryInitialDelay: ").append(toIndentedString(retryInitialDelay)).append("\n");
    sb.append("    sampleInterval: ").append(toIndentedString(sampleInterval)).append("\n");
    sb.append("    useCircuitBreaker: ").append(toIndentedString(useCircuitBreaker)).append("\n");
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
    openapiFields.add("backoffFactor");
    openapiFields.add("callTimeout");
    openapiFields.add("globalTimeout");
    openapiFields.add("maxErrors");
    openapiFields.add("retries");
    openapiFields.add("retryInitialDelay");
    openapiFields.add("sampleInterval");
    openapiFields.add("useCircuitBreaker");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("backoffFactor");
    openapiRequiredFields.add("callTimeout");
    openapiRequiredFields.add("globalTimeout");
    openapiRequiredFields.add("maxErrors");
    openapiRequiredFields.add("retries");
    openapiRequiredFields.add("retryInitialDelay");
    openapiRequiredFields.add("sampleInterval");
    openapiRequiredFields.add("useCircuitBreaker");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ClientConfig
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ClientConfig.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ClientConfig is not found in the empty JSON string", ClientConfig.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ClientConfig.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ClientConfig` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : ClientConfig.openapiRequiredFields) {
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
       if (!ClientConfig.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ClientConfig' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ClientConfig> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ClientConfig.class));

       return (TypeAdapter<T>) new TypeAdapter<ClientConfig>() {
           @Override
           public void write(JsonWriter out, ClientConfig value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ClientConfig read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ClientConfig given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ClientConfig
   * @throws IOException if the JSON string is invalid with respect to ClientConfig
   */
  public static ClientConfig fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ClientConfig.class);
  }

  /**
   * Convert an instance of ClientConfig to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

