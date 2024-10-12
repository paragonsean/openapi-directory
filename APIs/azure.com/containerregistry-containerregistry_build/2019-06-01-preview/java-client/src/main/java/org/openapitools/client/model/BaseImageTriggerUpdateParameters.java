/*
 * ContainerRegistryManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-06-01-preview
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
 * The properties for updating base image dependency trigger.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:24:55.681670-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class BaseImageTriggerUpdateParameters {
  /**
   * The type of the auto trigger for base image dependency updates.
   */
  @JsonAdapter(BaseImageTriggerTypeEnum.Adapter.class)
  public enum BaseImageTriggerTypeEnum {
    ALL("All"),
    
    RUNTIME("Runtime");

    private String value;

    BaseImageTriggerTypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static BaseImageTriggerTypeEnum fromValue(String value) {
      for (BaseImageTriggerTypeEnum b : BaseImageTriggerTypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<BaseImageTriggerTypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final BaseImageTriggerTypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public BaseImageTriggerTypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return BaseImageTriggerTypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      BaseImageTriggerTypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_BASE_IMAGE_TRIGGER_TYPE = "baseImageTriggerType";
  @SerializedName(SERIALIZED_NAME_BASE_IMAGE_TRIGGER_TYPE)
  private BaseImageTriggerTypeEnum baseImageTriggerType;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  /**
   * The current status of trigger.
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
  private StatusEnum status = StatusEnum.ENABLED;

  public static final String SERIALIZED_NAME_UPDATE_TRIGGER_ENDPOINT = "updateTriggerEndpoint";
  @SerializedName(SERIALIZED_NAME_UPDATE_TRIGGER_ENDPOINT)
  private String updateTriggerEndpoint;

  /**
   * Type of Payload body for Base image update triggers.
   */
  @JsonAdapter(UpdateTriggerPayloadTypeEnum.Adapter.class)
  public enum UpdateTriggerPayloadTypeEnum {
    DEFAULT("Default"),
    
    TOKEN("Token");

    private String value;

    UpdateTriggerPayloadTypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static UpdateTriggerPayloadTypeEnum fromValue(String value) {
      for (UpdateTriggerPayloadTypeEnum b : UpdateTriggerPayloadTypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<UpdateTriggerPayloadTypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final UpdateTriggerPayloadTypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public UpdateTriggerPayloadTypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return UpdateTriggerPayloadTypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      UpdateTriggerPayloadTypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_UPDATE_TRIGGER_PAYLOAD_TYPE = "updateTriggerPayloadType";
  @SerializedName(SERIALIZED_NAME_UPDATE_TRIGGER_PAYLOAD_TYPE)
  private UpdateTriggerPayloadTypeEnum updateTriggerPayloadType;

  public BaseImageTriggerUpdateParameters() {
  }

  public BaseImageTriggerUpdateParameters baseImageTriggerType(BaseImageTriggerTypeEnum baseImageTriggerType) {
    this.baseImageTriggerType = baseImageTriggerType;
    return this;
  }

  /**
   * The type of the auto trigger for base image dependency updates.
   * @return baseImageTriggerType
   */
  @javax.annotation.Nullable
  public BaseImageTriggerTypeEnum getBaseImageTriggerType() {
    return baseImageTriggerType;
  }

  public void setBaseImageTriggerType(BaseImageTriggerTypeEnum baseImageTriggerType) {
    this.baseImageTriggerType = baseImageTriggerType;
  }


  public BaseImageTriggerUpdateParameters name(String name) {
    this.name = name;
    return this;
  }

  /**
   * The name of the trigger.
   * @return name
   */
  @javax.annotation.Nonnull
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public BaseImageTriggerUpdateParameters status(StatusEnum status) {
    this.status = status;
    return this;
  }

  /**
   * The current status of trigger.
   * @return status
   */
  @javax.annotation.Nullable
  public StatusEnum getStatus() {
    return status;
  }

  public void setStatus(StatusEnum status) {
    this.status = status;
  }


  public BaseImageTriggerUpdateParameters updateTriggerEndpoint(String updateTriggerEndpoint) {
    this.updateTriggerEndpoint = updateTriggerEndpoint;
    return this;
  }

  /**
   * The endpoint URL for receiving update triggers.
   * @return updateTriggerEndpoint
   */
  @javax.annotation.Nullable
  public String getUpdateTriggerEndpoint() {
    return updateTriggerEndpoint;
  }

  public void setUpdateTriggerEndpoint(String updateTriggerEndpoint) {
    this.updateTriggerEndpoint = updateTriggerEndpoint;
  }


  public BaseImageTriggerUpdateParameters updateTriggerPayloadType(UpdateTriggerPayloadTypeEnum updateTriggerPayloadType) {
    this.updateTriggerPayloadType = updateTriggerPayloadType;
    return this;
  }

  /**
   * Type of Payload body for Base image update triggers.
   * @return updateTriggerPayloadType
   */
  @javax.annotation.Nullable
  public UpdateTriggerPayloadTypeEnum getUpdateTriggerPayloadType() {
    return updateTriggerPayloadType;
  }

  public void setUpdateTriggerPayloadType(UpdateTriggerPayloadTypeEnum updateTriggerPayloadType) {
    this.updateTriggerPayloadType = updateTriggerPayloadType;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    BaseImageTriggerUpdateParameters baseImageTriggerUpdateParameters = (BaseImageTriggerUpdateParameters) o;
    return Objects.equals(this.baseImageTriggerType, baseImageTriggerUpdateParameters.baseImageTriggerType) &&
        Objects.equals(this.name, baseImageTriggerUpdateParameters.name) &&
        Objects.equals(this.status, baseImageTriggerUpdateParameters.status) &&
        Objects.equals(this.updateTriggerEndpoint, baseImageTriggerUpdateParameters.updateTriggerEndpoint) &&
        Objects.equals(this.updateTriggerPayloadType, baseImageTriggerUpdateParameters.updateTriggerPayloadType);
  }

  @Override
  public int hashCode() {
    return Objects.hash(baseImageTriggerType, name, status, updateTriggerEndpoint, updateTriggerPayloadType);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class BaseImageTriggerUpdateParameters {\n");
    sb.append("    baseImageTriggerType: ").append(toIndentedString(baseImageTriggerType)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    updateTriggerEndpoint: ").append(toIndentedString(updateTriggerEndpoint)).append("\n");
    sb.append("    updateTriggerPayloadType: ").append(toIndentedString(updateTriggerPayloadType)).append("\n");
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
    openapiFields.add("baseImageTriggerType");
    openapiFields.add("name");
    openapiFields.add("status");
    openapiFields.add("updateTriggerEndpoint");
    openapiFields.add("updateTriggerPayloadType");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("name");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to BaseImageTriggerUpdateParameters
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!BaseImageTriggerUpdateParameters.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in BaseImageTriggerUpdateParameters is not found in the empty JSON string", BaseImageTriggerUpdateParameters.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!BaseImageTriggerUpdateParameters.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `BaseImageTriggerUpdateParameters` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : BaseImageTriggerUpdateParameters.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("baseImageTriggerType") != null && !jsonObj.get("baseImageTriggerType").isJsonNull()) && !jsonObj.get("baseImageTriggerType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `baseImageTriggerType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("baseImageTriggerType").toString()));
      }
      // validate the optional field `baseImageTriggerType`
      if (jsonObj.get("baseImageTriggerType") != null && !jsonObj.get("baseImageTriggerType").isJsonNull()) {
        BaseImageTriggerTypeEnum.validateJsonElement(jsonObj.get("baseImageTriggerType"));
      }
      if (!jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) && !jsonObj.get("status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("status").toString()));
      }
      // validate the optional field `status`
      if (jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) {
        StatusEnum.validateJsonElement(jsonObj.get("status"));
      }
      if ((jsonObj.get("updateTriggerEndpoint") != null && !jsonObj.get("updateTriggerEndpoint").isJsonNull()) && !jsonObj.get("updateTriggerEndpoint").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `updateTriggerEndpoint` to be a primitive type in the JSON string but got `%s`", jsonObj.get("updateTriggerEndpoint").toString()));
      }
      if ((jsonObj.get("updateTriggerPayloadType") != null && !jsonObj.get("updateTriggerPayloadType").isJsonNull()) && !jsonObj.get("updateTriggerPayloadType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `updateTriggerPayloadType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("updateTriggerPayloadType").toString()));
      }
      // validate the optional field `updateTriggerPayloadType`
      if (jsonObj.get("updateTriggerPayloadType") != null && !jsonObj.get("updateTriggerPayloadType").isJsonNull()) {
        UpdateTriggerPayloadTypeEnum.validateJsonElement(jsonObj.get("updateTriggerPayloadType"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!BaseImageTriggerUpdateParameters.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'BaseImageTriggerUpdateParameters' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<BaseImageTriggerUpdateParameters> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(BaseImageTriggerUpdateParameters.class));

       return (TypeAdapter<T>) new TypeAdapter<BaseImageTriggerUpdateParameters>() {
           @Override
           public void write(JsonWriter out, BaseImageTriggerUpdateParameters value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public BaseImageTriggerUpdateParameters read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of BaseImageTriggerUpdateParameters given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of BaseImageTriggerUpdateParameters
   * @throws IOException if the JSON string is invalid with respect to BaseImageTriggerUpdateParameters
   */
  public static BaseImageTriggerUpdateParameters fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, BaseImageTriggerUpdateParameters.class);
  }

  /**
   * Convert an instance of BaseImageTriggerUpdateParameters to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

