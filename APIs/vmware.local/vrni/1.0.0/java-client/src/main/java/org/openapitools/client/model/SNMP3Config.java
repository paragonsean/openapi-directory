/*
 * vRealize Network Insight API Reference
 * vRealize Network Insight API Reference
 *
 * The version of the OpenAPI document: 1.0.0
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
 * SNMP3Config
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:01:28.864194-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class SNMP3Config {
  public static final String SERIALIZED_NAME_AUTHENTICATION_PASSWORD = "authentication_password";
  @SerializedName(SERIALIZED_NAME_AUTHENTICATION_PASSWORD)
  private String authenticationPassword;

  /**
   * Gets or Sets authenticationType
   */
  @JsonAdapter(AuthenticationTypeEnum.Adapter.class)
  public enum AuthenticationTypeEnum {
    NO_AUTH("NO_AUTH"),
    
    MD5("MD5"),
    
    SHA("SHA");

    private String value;

    AuthenticationTypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static AuthenticationTypeEnum fromValue(String value) {
      for (AuthenticationTypeEnum b : AuthenticationTypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<AuthenticationTypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final AuthenticationTypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public AuthenticationTypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return AuthenticationTypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      AuthenticationTypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_AUTHENTICATION_TYPE = "authentication_type";
  @SerializedName(SERIALIZED_NAME_AUTHENTICATION_TYPE)
  private AuthenticationTypeEnum authenticationType;

  public static final String SERIALIZED_NAME_CONTEXT_NAME = "context_name";
  @SerializedName(SERIALIZED_NAME_CONTEXT_NAME)
  private String contextName;

  public static final String SERIALIZED_NAME_PRIVACY_PASSWORD = "privacy_password";
  @SerializedName(SERIALIZED_NAME_PRIVACY_PASSWORD)
  private String privacyPassword;

  /**
   * Gets or Sets privacyType
   */
  @JsonAdapter(PrivacyTypeEnum.Adapter.class)
  public enum PrivacyTypeEnum {
    AES("AES"),
    
    DES("DES"),
    
    AES128("AES128"),
    
    AES192("AES192"),
    
    AES256("AES256"),
    
    _3_DES("3DES"),
    
    NO_PRIV("NO_PRIV");

    private String value;

    PrivacyTypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static PrivacyTypeEnum fromValue(String value) {
      for (PrivacyTypeEnum b : PrivacyTypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<PrivacyTypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final PrivacyTypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public PrivacyTypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return PrivacyTypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      PrivacyTypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_PRIVACY_TYPE = "privacy_type";
  @SerializedName(SERIALIZED_NAME_PRIVACY_TYPE)
  private PrivacyTypeEnum privacyType;

  public static final String SERIALIZED_NAME_USERNAME = "username";
  @SerializedName(SERIALIZED_NAME_USERNAME)
  private String username;

  public SNMP3Config() {
  }

  public SNMP3Config authenticationPassword(String authenticationPassword) {
    this.authenticationPassword = authenticationPassword;
    return this;
  }

  /**
   * Get authenticationPassword
   * @return authenticationPassword
   */
  @javax.annotation.Nullable
  public String getAuthenticationPassword() {
    return authenticationPassword;
  }

  public void setAuthenticationPassword(String authenticationPassword) {
    this.authenticationPassword = authenticationPassword;
  }


  public SNMP3Config authenticationType(AuthenticationTypeEnum authenticationType) {
    this.authenticationType = authenticationType;
    return this;
  }

  /**
   * Get authenticationType
   * @return authenticationType
   */
  @javax.annotation.Nullable
  public AuthenticationTypeEnum getAuthenticationType() {
    return authenticationType;
  }

  public void setAuthenticationType(AuthenticationTypeEnum authenticationType) {
    this.authenticationType = authenticationType;
  }


  public SNMP3Config contextName(String contextName) {
    this.contextName = contextName;
    return this;
  }

  /**
   * Get contextName
   * @return contextName
   */
  @javax.annotation.Nullable
  public String getContextName() {
    return contextName;
  }

  public void setContextName(String contextName) {
    this.contextName = contextName;
  }


  public SNMP3Config privacyPassword(String privacyPassword) {
    this.privacyPassword = privacyPassword;
    return this;
  }

  /**
   * Get privacyPassword
   * @return privacyPassword
   */
  @javax.annotation.Nullable
  public String getPrivacyPassword() {
    return privacyPassword;
  }

  public void setPrivacyPassword(String privacyPassword) {
    this.privacyPassword = privacyPassword;
  }


  public SNMP3Config privacyType(PrivacyTypeEnum privacyType) {
    this.privacyType = privacyType;
    return this;
  }

  /**
   * Get privacyType
   * @return privacyType
   */
  @javax.annotation.Nullable
  public PrivacyTypeEnum getPrivacyType() {
    return privacyType;
  }

  public void setPrivacyType(PrivacyTypeEnum privacyType) {
    this.privacyType = privacyType;
  }


  public SNMP3Config username(String username) {
    this.username = username;
    return this;
  }

  /**
   * Get username
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
    SNMP3Config snMP3Config = (SNMP3Config) o;
    return Objects.equals(this.authenticationPassword, snMP3Config.authenticationPassword) &&
        Objects.equals(this.authenticationType, snMP3Config.authenticationType) &&
        Objects.equals(this.contextName, snMP3Config.contextName) &&
        Objects.equals(this.privacyPassword, snMP3Config.privacyPassword) &&
        Objects.equals(this.privacyType, snMP3Config.privacyType) &&
        Objects.equals(this.username, snMP3Config.username);
  }

  @Override
  public int hashCode() {
    return Objects.hash(authenticationPassword, authenticationType, contextName, privacyPassword, privacyType, username);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class SNMP3Config {\n");
    sb.append("    authenticationPassword: ").append(toIndentedString(authenticationPassword)).append("\n");
    sb.append("    authenticationType: ").append(toIndentedString(authenticationType)).append("\n");
    sb.append("    contextName: ").append(toIndentedString(contextName)).append("\n");
    sb.append("    privacyPassword: ").append(toIndentedString(privacyPassword)).append("\n");
    sb.append("    privacyType: ").append(toIndentedString(privacyType)).append("\n");
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
    openapiFields.add("authentication_password");
    openapiFields.add("authentication_type");
    openapiFields.add("context_name");
    openapiFields.add("privacy_password");
    openapiFields.add("privacy_type");
    openapiFields.add("username");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to SNMP3Config
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!SNMP3Config.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in SNMP3Config is not found in the empty JSON string", SNMP3Config.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!SNMP3Config.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `SNMP3Config` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("authentication_password") != null && !jsonObj.get("authentication_password").isJsonNull()) && !jsonObj.get("authentication_password").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `authentication_password` to be a primitive type in the JSON string but got `%s`", jsonObj.get("authentication_password").toString()));
      }
      if ((jsonObj.get("authentication_type") != null && !jsonObj.get("authentication_type").isJsonNull()) && !jsonObj.get("authentication_type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `authentication_type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("authentication_type").toString()));
      }
      // validate the optional field `authentication_type`
      if (jsonObj.get("authentication_type") != null && !jsonObj.get("authentication_type").isJsonNull()) {
        AuthenticationTypeEnum.validateJsonElement(jsonObj.get("authentication_type"));
      }
      if ((jsonObj.get("context_name") != null && !jsonObj.get("context_name").isJsonNull()) && !jsonObj.get("context_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `context_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("context_name").toString()));
      }
      if ((jsonObj.get("privacy_password") != null && !jsonObj.get("privacy_password").isJsonNull()) && !jsonObj.get("privacy_password").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `privacy_password` to be a primitive type in the JSON string but got `%s`", jsonObj.get("privacy_password").toString()));
      }
      if ((jsonObj.get("privacy_type") != null && !jsonObj.get("privacy_type").isJsonNull()) && !jsonObj.get("privacy_type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `privacy_type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("privacy_type").toString()));
      }
      // validate the optional field `privacy_type`
      if (jsonObj.get("privacy_type") != null && !jsonObj.get("privacy_type").isJsonNull()) {
        PrivacyTypeEnum.validateJsonElement(jsonObj.get("privacy_type"));
      }
      if ((jsonObj.get("username") != null && !jsonObj.get("username").isJsonNull()) && !jsonObj.get("username").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `username` to be a primitive type in the JSON string but got `%s`", jsonObj.get("username").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!SNMP3Config.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'SNMP3Config' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<SNMP3Config> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(SNMP3Config.class));

       return (TypeAdapter<T>) new TypeAdapter<SNMP3Config>() {
           @Override
           public void write(JsonWriter out, SNMP3Config value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public SNMP3Config read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of SNMP3Config given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of SNMP3Config
   * @throws IOException if the JSON string is invalid with respect to SNMP3Config
   */
  public static SNMP3Config fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, SNMP3Config.class);
  }

  /**
   * Convert an instance of SNMP3Config to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

