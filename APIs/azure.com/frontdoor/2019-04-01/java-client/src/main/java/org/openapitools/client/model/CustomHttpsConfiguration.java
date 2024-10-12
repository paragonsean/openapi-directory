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
import org.openapitools.client.model.FrontDoorCertificateSourceParameters;
import org.openapitools.client.model.KeyVaultCertificateSourceParameters;

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
 * Https settings for a domain
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:16:34.178652-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CustomHttpsConfiguration {
  /**
   * Defines the source of the SSL certificate
   */
  @JsonAdapter(CertificateSourceEnum.Adapter.class)
  public enum CertificateSourceEnum {
    AZURE_KEY_VAULT("AzureKeyVault"),
    
    FRONT_DOOR("FrontDoor");

    private String value;

    CertificateSourceEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static CertificateSourceEnum fromValue(String value) {
      for (CertificateSourceEnum b : CertificateSourceEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<CertificateSourceEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final CertificateSourceEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public CertificateSourceEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return CertificateSourceEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      CertificateSourceEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_CERTIFICATE_SOURCE = "certificateSource";
  @SerializedName(SERIALIZED_NAME_CERTIFICATE_SOURCE)
  private CertificateSourceEnum certificateSource;

  public static final String SERIALIZED_NAME_FRONT_DOOR_CERTIFICATE_SOURCE_PARAMETERS = "frontDoorCertificateSourceParameters";
  @SerializedName(SERIALIZED_NAME_FRONT_DOOR_CERTIFICATE_SOURCE_PARAMETERS)
  private FrontDoorCertificateSourceParameters frontDoorCertificateSourceParameters;

  public static final String SERIALIZED_NAME_KEY_VAULT_CERTIFICATE_SOURCE_PARAMETERS = "keyVaultCertificateSourceParameters";
  @SerializedName(SERIALIZED_NAME_KEY_VAULT_CERTIFICATE_SOURCE_PARAMETERS)
  private KeyVaultCertificateSourceParameters keyVaultCertificateSourceParameters;

  /**
   * Defines the TLS extension protocol that is used for secure delivery
   */
  @JsonAdapter(ProtocolTypeEnum.Adapter.class)
  public enum ProtocolTypeEnum {
    SERVER_NAME_INDICATION("ServerNameIndication");

    private String value;

    ProtocolTypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static ProtocolTypeEnum fromValue(String value) {
      for (ProtocolTypeEnum b : ProtocolTypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<ProtocolTypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final ProtocolTypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public ProtocolTypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return ProtocolTypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      ProtocolTypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_PROTOCOL_TYPE = "protocolType";
  @SerializedName(SERIALIZED_NAME_PROTOCOL_TYPE)
  private ProtocolTypeEnum protocolType;

  public CustomHttpsConfiguration() {
  }

  public CustomHttpsConfiguration certificateSource(CertificateSourceEnum certificateSource) {
    this.certificateSource = certificateSource;
    return this;
  }

  /**
   * Defines the source of the SSL certificate
   * @return certificateSource
   */
  @javax.annotation.Nullable
  public CertificateSourceEnum getCertificateSource() {
    return certificateSource;
  }

  public void setCertificateSource(CertificateSourceEnum certificateSource) {
    this.certificateSource = certificateSource;
  }


  public CustomHttpsConfiguration frontDoorCertificateSourceParameters(FrontDoorCertificateSourceParameters frontDoorCertificateSourceParameters) {
    this.frontDoorCertificateSourceParameters = frontDoorCertificateSourceParameters;
    return this;
  }

  /**
   * Get frontDoorCertificateSourceParameters
   * @return frontDoorCertificateSourceParameters
   */
  @javax.annotation.Nullable
  public FrontDoorCertificateSourceParameters getFrontDoorCertificateSourceParameters() {
    return frontDoorCertificateSourceParameters;
  }

  public void setFrontDoorCertificateSourceParameters(FrontDoorCertificateSourceParameters frontDoorCertificateSourceParameters) {
    this.frontDoorCertificateSourceParameters = frontDoorCertificateSourceParameters;
  }


  public CustomHttpsConfiguration keyVaultCertificateSourceParameters(KeyVaultCertificateSourceParameters keyVaultCertificateSourceParameters) {
    this.keyVaultCertificateSourceParameters = keyVaultCertificateSourceParameters;
    return this;
  }

  /**
   * Get keyVaultCertificateSourceParameters
   * @return keyVaultCertificateSourceParameters
   */
  @javax.annotation.Nullable
  public KeyVaultCertificateSourceParameters getKeyVaultCertificateSourceParameters() {
    return keyVaultCertificateSourceParameters;
  }

  public void setKeyVaultCertificateSourceParameters(KeyVaultCertificateSourceParameters keyVaultCertificateSourceParameters) {
    this.keyVaultCertificateSourceParameters = keyVaultCertificateSourceParameters;
  }


  public CustomHttpsConfiguration protocolType(ProtocolTypeEnum protocolType) {
    this.protocolType = protocolType;
    return this;
  }

  /**
   * Defines the TLS extension protocol that is used for secure delivery
   * @return protocolType
   */
  @javax.annotation.Nullable
  public ProtocolTypeEnum getProtocolType() {
    return protocolType;
  }

  public void setProtocolType(ProtocolTypeEnum protocolType) {
    this.protocolType = protocolType;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CustomHttpsConfiguration customHttpsConfiguration = (CustomHttpsConfiguration) o;
    return Objects.equals(this.certificateSource, customHttpsConfiguration.certificateSource) &&
        Objects.equals(this.frontDoorCertificateSourceParameters, customHttpsConfiguration.frontDoorCertificateSourceParameters) &&
        Objects.equals(this.keyVaultCertificateSourceParameters, customHttpsConfiguration.keyVaultCertificateSourceParameters) &&
        Objects.equals(this.protocolType, customHttpsConfiguration.protocolType);
  }

  @Override
  public int hashCode() {
    return Objects.hash(certificateSource, frontDoorCertificateSourceParameters, keyVaultCertificateSourceParameters, protocolType);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CustomHttpsConfiguration {\n");
    sb.append("    certificateSource: ").append(toIndentedString(certificateSource)).append("\n");
    sb.append("    frontDoorCertificateSourceParameters: ").append(toIndentedString(frontDoorCertificateSourceParameters)).append("\n");
    sb.append("    keyVaultCertificateSourceParameters: ").append(toIndentedString(keyVaultCertificateSourceParameters)).append("\n");
    sb.append("    protocolType: ").append(toIndentedString(protocolType)).append("\n");
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
    openapiFields.add("certificateSource");
    openapiFields.add("frontDoorCertificateSourceParameters");
    openapiFields.add("keyVaultCertificateSourceParameters");
    openapiFields.add("protocolType");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CustomHttpsConfiguration
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CustomHttpsConfiguration.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CustomHttpsConfiguration is not found in the empty JSON string", CustomHttpsConfiguration.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CustomHttpsConfiguration.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CustomHttpsConfiguration` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("certificateSource") != null && !jsonObj.get("certificateSource").isJsonNull()) && !jsonObj.get("certificateSource").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `certificateSource` to be a primitive type in the JSON string but got `%s`", jsonObj.get("certificateSource").toString()));
      }
      // validate the optional field `certificateSource`
      if (jsonObj.get("certificateSource") != null && !jsonObj.get("certificateSource").isJsonNull()) {
        CertificateSourceEnum.validateJsonElement(jsonObj.get("certificateSource"));
      }
      // validate the optional field `frontDoorCertificateSourceParameters`
      if (jsonObj.get("frontDoorCertificateSourceParameters") != null && !jsonObj.get("frontDoorCertificateSourceParameters").isJsonNull()) {
        FrontDoorCertificateSourceParameters.validateJsonElement(jsonObj.get("frontDoorCertificateSourceParameters"));
      }
      // validate the optional field `keyVaultCertificateSourceParameters`
      if (jsonObj.get("keyVaultCertificateSourceParameters") != null && !jsonObj.get("keyVaultCertificateSourceParameters").isJsonNull()) {
        KeyVaultCertificateSourceParameters.validateJsonElement(jsonObj.get("keyVaultCertificateSourceParameters"));
      }
      if ((jsonObj.get("protocolType") != null && !jsonObj.get("protocolType").isJsonNull()) && !jsonObj.get("protocolType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `protocolType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("protocolType").toString()));
      }
      // validate the optional field `protocolType`
      if (jsonObj.get("protocolType") != null && !jsonObj.get("protocolType").isJsonNull()) {
        ProtocolTypeEnum.validateJsonElement(jsonObj.get("protocolType"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CustomHttpsConfiguration.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CustomHttpsConfiguration' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CustomHttpsConfiguration> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CustomHttpsConfiguration.class));

       return (TypeAdapter<T>) new TypeAdapter<CustomHttpsConfiguration>() {
           @Override
           public void write(JsonWriter out, CustomHttpsConfiguration value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CustomHttpsConfiguration read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CustomHttpsConfiguration given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CustomHttpsConfiguration
   * @throws IOException if the JSON string is invalid with respect to CustomHttpsConfiguration
   */
  public static CustomHttpsConfiguration fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CustomHttpsConfiguration.class);
  }

  /**
   * Convert an instance of CustomHttpsConfiguration to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

