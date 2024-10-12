/*
 * ContainerRegistryManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
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
import org.openapitools.client.model.AgentProperties;
import org.openapitools.client.model.Credentials;
import org.openapitools.client.model.PlatformUpdateParameters;
import org.openapitools.client.model.TaskStepUpdateParameters;
import org.openapitools.client.model.TriggerUpdateParameters;

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
 * The properties for updating a task.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:25:02.709621-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class TaskPropertiesUpdateParameters {
  public static final String SERIALIZED_NAME_AGENT_CONFIGURATION = "agentConfiguration";
  @SerializedName(SERIALIZED_NAME_AGENT_CONFIGURATION)
  private AgentProperties agentConfiguration;

  public static final String SERIALIZED_NAME_CREDENTIALS = "credentials";
  @SerializedName(SERIALIZED_NAME_CREDENTIALS)
  private Credentials credentials;

  public static final String SERIALIZED_NAME_PLATFORM = "platform";
  @SerializedName(SERIALIZED_NAME_PLATFORM)
  private PlatformUpdateParameters platform;

  /**
   * The current status of task.
   */
  @JsonAdapter(StatusEnum.Adapter.class)
  public enum StatusEnum {
    DISABLED("Disabled"),
    
    ENABLED("Enabled");

    private String value;

    StatusEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static StatusEnum fromValue(String value) {
      for (StatusEnum b : StatusEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<StatusEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final StatusEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public StatusEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return StatusEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      StatusEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private StatusEnum status;

  public static final String SERIALIZED_NAME_STEP = "step";
  @SerializedName(SERIALIZED_NAME_STEP)
  private TaskStepUpdateParameters step;

  public static final String SERIALIZED_NAME_TIMEOUT = "timeout";
  @SerializedName(SERIALIZED_NAME_TIMEOUT)
  private Integer timeout;

  public static final String SERIALIZED_NAME_TRIGGER = "trigger";
  @SerializedName(SERIALIZED_NAME_TRIGGER)
  private TriggerUpdateParameters trigger;

  public TaskPropertiesUpdateParameters() {
  }

  public TaskPropertiesUpdateParameters agentConfiguration(AgentProperties agentConfiguration) {
    this.agentConfiguration = agentConfiguration;
    return this;
  }

  /**
   * Get agentConfiguration
   * @return agentConfiguration
   */
  @javax.annotation.Nullable
  public AgentProperties getAgentConfiguration() {
    return agentConfiguration;
  }

  public void setAgentConfiguration(AgentProperties agentConfiguration) {
    this.agentConfiguration = agentConfiguration;
  }


  public TaskPropertiesUpdateParameters credentials(Credentials credentials) {
    this.credentials = credentials;
    return this;
  }

  /**
   * Get credentials
   * @return credentials
   */
  @javax.annotation.Nullable
  public Credentials getCredentials() {
    return credentials;
  }

  public void setCredentials(Credentials credentials) {
    this.credentials = credentials;
  }


  public TaskPropertiesUpdateParameters platform(PlatformUpdateParameters platform) {
    this.platform = platform;
    return this;
  }

  /**
   * Get platform
   * @return platform
   */
  @javax.annotation.Nullable
  public PlatformUpdateParameters getPlatform() {
    return platform;
  }

  public void setPlatform(PlatformUpdateParameters platform) {
    this.platform = platform;
  }


  public TaskPropertiesUpdateParameters status(StatusEnum status) {
    this.status = status;
    return this;
  }

  /**
   * The current status of task.
   * @return status
   */
  @javax.annotation.Nullable
  public StatusEnum getStatus() {
    return status;
  }

  public void setStatus(StatusEnum status) {
    this.status = status;
  }


  public TaskPropertiesUpdateParameters step(TaskStepUpdateParameters step) {
    this.step = step;
    return this;
  }

  /**
   * Get step
   * @return step
   */
  @javax.annotation.Nullable
  public TaskStepUpdateParameters getStep() {
    return step;
  }

  public void setStep(TaskStepUpdateParameters step) {
    this.step = step;
  }


  public TaskPropertiesUpdateParameters timeout(Integer timeout) {
    this.timeout = timeout;
    return this;
  }

  /**
   * Run timeout in seconds.
   * @return timeout
   */
  @javax.annotation.Nullable
  public Integer getTimeout() {
    return timeout;
  }

  public void setTimeout(Integer timeout) {
    this.timeout = timeout;
  }


  public TaskPropertiesUpdateParameters trigger(TriggerUpdateParameters trigger) {
    this.trigger = trigger;
    return this;
  }

  /**
   * Get trigger
   * @return trigger
   */
  @javax.annotation.Nullable
  public TriggerUpdateParameters getTrigger() {
    return trigger;
  }

  public void setTrigger(TriggerUpdateParameters trigger) {
    this.trigger = trigger;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TaskPropertiesUpdateParameters taskPropertiesUpdateParameters = (TaskPropertiesUpdateParameters) o;
    return Objects.equals(this.agentConfiguration, taskPropertiesUpdateParameters.agentConfiguration) &&
        Objects.equals(this.credentials, taskPropertiesUpdateParameters.credentials) &&
        Objects.equals(this.platform, taskPropertiesUpdateParameters.platform) &&
        Objects.equals(this.status, taskPropertiesUpdateParameters.status) &&
        Objects.equals(this.step, taskPropertiesUpdateParameters.step) &&
        Objects.equals(this.timeout, taskPropertiesUpdateParameters.timeout) &&
        Objects.equals(this.trigger, taskPropertiesUpdateParameters.trigger);
  }

  @Override
  public int hashCode() {
    return Objects.hash(agentConfiguration, credentials, platform, status, step, timeout, trigger);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TaskPropertiesUpdateParameters {\n");
    sb.append("    agentConfiguration: ").append(toIndentedString(agentConfiguration)).append("\n");
    sb.append("    credentials: ").append(toIndentedString(credentials)).append("\n");
    sb.append("    platform: ").append(toIndentedString(platform)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    step: ").append(toIndentedString(step)).append("\n");
    sb.append("    timeout: ").append(toIndentedString(timeout)).append("\n");
    sb.append("    trigger: ").append(toIndentedString(trigger)).append("\n");
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
    openapiFields.add("agentConfiguration");
    openapiFields.add("credentials");
    openapiFields.add("platform");
    openapiFields.add("status");
    openapiFields.add("step");
    openapiFields.add("timeout");
    openapiFields.add("trigger");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to TaskPropertiesUpdateParameters
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!TaskPropertiesUpdateParameters.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in TaskPropertiesUpdateParameters is not found in the empty JSON string", TaskPropertiesUpdateParameters.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!TaskPropertiesUpdateParameters.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TaskPropertiesUpdateParameters` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `agentConfiguration`
      if (jsonObj.get("agentConfiguration") != null && !jsonObj.get("agentConfiguration").isJsonNull()) {
        AgentProperties.validateJsonElement(jsonObj.get("agentConfiguration"));
      }
      // validate the optional field `credentials`
      if (jsonObj.get("credentials") != null && !jsonObj.get("credentials").isJsonNull()) {
        Credentials.validateJsonElement(jsonObj.get("credentials"));
      }
      // validate the optional field `platform`
      if (jsonObj.get("platform") != null && !jsonObj.get("platform").isJsonNull()) {
        PlatformUpdateParameters.validateJsonElement(jsonObj.get("platform"));
      }
      if ((jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) && !jsonObj.get("status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("status").toString()));
      }
      // validate the optional field `status`
      if (jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) {
        StatusEnum.validateJsonElement(jsonObj.get("status"));
      }
      // validate the optional field `step`
      if (jsonObj.get("step") != null && !jsonObj.get("step").isJsonNull()) {
        TaskStepUpdateParameters.validateJsonElement(jsonObj.get("step"));
      }
      // validate the optional field `trigger`
      if (jsonObj.get("trigger") != null && !jsonObj.get("trigger").isJsonNull()) {
        TriggerUpdateParameters.validateJsonElement(jsonObj.get("trigger"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TaskPropertiesUpdateParameters.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TaskPropertiesUpdateParameters' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TaskPropertiesUpdateParameters> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TaskPropertiesUpdateParameters.class));

       return (TypeAdapter<T>) new TypeAdapter<TaskPropertiesUpdateParameters>() {
           @Override
           public void write(JsonWriter out, TaskPropertiesUpdateParameters value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TaskPropertiesUpdateParameters read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of TaskPropertiesUpdateParameters given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of TaskPropertiesUpdateParameters
   * @throws IOException if the JSON string is invalid with respect to TaskPropertiesUpdateParameters
   */
  public static TaskPropertiesUpdateParameters fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TaskPropertiesUpdateParameters.class);
  }

  /**
   * Convert an instance of TaskPropertiesUpdateParameters to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

