/*
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
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
import org.openapitools.client.model.AppleConnectionSecretRequestAllOfData;

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
 * SharedConnectionRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class SharedConnectionRequest {
  /**
   * credential type of the shared connection. Values can be credentials|certificate
   */
  @JsonAdapter(CredentialTypeEnum.Adapter.class)
  public enum CredentialTypeEnum {
    CREDENTIALS("credentials"),
    
    CERTIFICATE("certificate"),
    
    KEY("key");

    private String value;

    CredentialTypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static CredentialTypeEnum fromValue(String value) {
      for (CredentialTypeEnum b : CredentialTypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<CredentialTypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final CredentialTypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public CredentialTypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return CredentialTypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      CredentialTypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_CREDENTIAL_TYPE = "credentialType";
  @SerializedName(SERIALIZED_NAME_CREDENTIAL_TYPE)
  private CredentialTypeEnum credentialType = CredentialTypeEnum.CREDENTIALS;

  public static final String SERIALIZED_NAME_DATA = "data";
  @SerializedName(SERIALIZED_NAME_DATA)
  private AppleConnectionSecretRequestAllOfData data;

  public static final String SERIALIZED_NAME_DISPLAY_NAME = "displayName";
  @SerializedName(SERIALIZED_NAME_DISPLAY_NAME)
  private String displayName;

  /**
   * service type of shared connection can be apple|gitlab|googleplay|jira|applecertificate
   */
  @JsonAdapter(ServiceTypeEnum.Adapter.class)
  public enum ServiceTypeEnum {
    APPLE("apple"),
    
    JIRA("jira"),
    
    GOOGLEPLAY("googleplay"),
    
    GITLAB("gitlab");

    private String value;

    ServiceTypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static ServiceTypeEnum fromValue(String value) {
      for (ServiceTypeEnum b : ServiceTypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<ServiceTypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final ServiceTypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public ServiceTypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return ServiceTypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      ServiceTypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_SERVICE_TYPE = "serviceType";
  @SerializedName(SERIALIZED_NAME_SERVICE_TYPE)
  protected ServiceTypeEnum serviceType;

  public SharedConnectionRequest() {
  }

  public SharedConnectionRequest credentialType(CredentialTypeEnum credentialType) {
    this.credentialType = credentialType;
    return this;
  }

  /**
   * credential type of the shared connection. Values can be credentials|certificate
   * @return credentialType
   */
  @javax.annotation.Nullable
  public CredentialTypeEnum getCredentialType() {
    return credentialType;
  }

  public void setCredentialType(CredentialTypeEnum credentialType) {
    this.credentialType = credentialType;
  }


  public SharedConnectionRequest data(AppleConnectionSecretRequestAllOfData data) {
    this.data = data;
    return this;
  }

  /**
   * Get data
   * @return data
   */
  @javax.annotation.Nullable
  public AppleConnectionSecretRequestAllOfData getData() {
    return data;
  }

  public void setData(AppleConnectionSecretRequestAllOfData data) {
    this.data = data;
  }


  public SharedConnectionRequest displayName(String displayName) {
    this.displayName = displayName;
    return this;
  }

  /**
   * display name of shared connection
   * @return displayName
   */
  @javax.annotation.Nullable
  public String getDisplayName() {
    return displayName;
  }

  public void setDisplayName(String displayName) {
    this.displayName = displayName;
  }


  public SharedConnectionRequest serviceType(ServiceTypeEnum serviceType) {
    this.serviceType = serviceType;
    return this;
  }

  /**
   * service type of shared connection can be apple|gitlab|googleplay|jira|applecertificate
   * @return serviceType
   */
  @javax.annotation.Nonnull
  public ServiceTypeEnum getServiceType() {
    return serviceType;
  }

  public void setServiceType(ServiceTypeEnum serviceType) {
    this.serviceType = serviceType;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    SharedConnectionRequest sharedConnectionRequest = (SharedConnectionRequest) o;
    return Objects.equals(this.credentialType, sharedConnectionRequest.credentialType) &&
        Objects.equals(this.data, sharedConnectionRequest.data) &&
        Objects.equals(this.displayName, sharedConnectionRequest.displayName) &&
        Objects.equals(this.serviceType, sharedConnectionRequest.serviceType);
  }

  @Override
  public int hashCode() {
    return Objects.hash(credentialType, data, displayName, serviceType);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class SharedConnectionRequest {\n");
    sb.append("    credentialType: ").append(toIndentedString(credentialType)).append("\n");
    sb.append("    data: ").append(toIndentedString(data)).append("\n");
    sb.append("    displayName: ").append(toIndentedString(displayName)).append("\n");
    sb.append("    serviceType: ").append(toIndentedString(serviceType)).append("\n");
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
    openapiFields.add("credentialType");
    openapiFields.add("data");
    openapiFields.add("displayName");
    openapiFields.add("serviceType");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("serviceType");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to SharedConnectionRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!SharedConnectionRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in SharedConnectionRequest is not found in the empty JSON string", SharedConnectionRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!SharedConnectionRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `SharedConnectionRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : SharedConnectionRequest.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!SharedConnectionRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'SharedConnectionRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<SharedConnectionRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(SharedConnectionRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<SharedConnectionRequest>() {
           @Override
           public void write(JsonWriter out, SharedConnectionRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public SharedConnectionRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of SharedConnectionRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of SharedConnectionRequest
   * @throws IOException if the JSON string is invalid with respect to SharedConnectionRequest
   */
  public static SharedConnectionRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, SharedConnectionRequest.class);
  }

  /**
   * Convert an instance of SharedConnectionRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

