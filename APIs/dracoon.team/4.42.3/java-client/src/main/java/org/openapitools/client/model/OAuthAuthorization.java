/*
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
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
import java.time.OffsetDateTime;
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
 * OAuth authorization
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:04:27.439567-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class OAuthAuthorization {
  public static final String SERIALIZED_NAME_CLIENT_ID = "clientId";
  @SerializedName(SERIALIZED_NAME_CLIENT_ID)
  private String clientId;

  public static final String SERIALIZED_NAME_CLIENT_NAME = "clientName";
  @SerializedName(SERIALIZED_NAME_CLIENT_NAME)
  private String clientName;

  public static final String SERIALIZED_NAME_CREATED_AT = "createdAt";
  @SerializedName(SERIALIZED_NAME_CREATED_AT)
  private OffsetDateTime createdAt;

  public static final String SERIALIZED_NAME_EXPIRES_AT = "expiresAt";
  @SerializedName(SERIALIZED_NAME_EXPIRES_AT)
  private OffsetDateTime expiresAt;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Long id;

  public static final String SERIALIZED_NAME_IS_CURRENT_AUTHORIZATION = "isCurrentAuthorization";
  @SerializedName(SERIALIZED_NAME_IS_CURRENT_AUTHORIZATION)
  private Boolean isCurrentAuthorization;

  public static final String SERIALIZED_NAME_IS_STANDARD = "isStandard";
  @SerializedName(SERIALIZED_NAME_IS_STANDARD)
  private Boolean isStandard;

  public static final String SERIALIZED_NAME_USED_AT = "usedAt";
  @SerializedName(SERIALIZED_NAME_USED_AT)
  private OffsetDateTime usedAt;

  /**
   * &amp;#128640; Since v4.12.0  User agent category.
   */
  @JsonAdapter(UserAgentCategoryEnum.Adapter.class)
  public enum UserAgentCategoryEnum {
    BROWSER("browser"),
    
    NATIVE("native"),
    
    UNKNOWN("unknown");

    private String value;

    UserAgentCategoryEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static UserAgentCategoryEnum fromValue(String value) {
      for (UserAgentCategoryEnum b : UserAgentCategoryEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<UserAgentCategoryEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final UserAgentCategoryEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public UserAgentCategoryEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return UserAgentCategoryEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      UserAgentCategoryEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_USER_AGENT_CATEGORY = "userAgentCategory";
  @SerializedName(SERIALIZED_NAME_USER_AGENT_CATEGORY)
  private UserAgentCategoryEnum userAgentCategory;

  public static final String SERIALIZED_NAME_USER_AGENT_INFO = "userAgentInfo";
  @SerializedName(SERIALIZED_NAME_USER_AGENT_INFO)
  private String userAgentInfo;

  public static final String SERIALIZED_NAME_USER_AGENT_OS = "userAgentOs";
  @SerializedName(SERIALIZED_NAME_USER_AGENT_OS)
  private String userAgentOs;

  public static final String SERIALIZED_NAME_USER_AGENT_TYPE = "userAgentType";
  @SerializedName(SERIALIZED_NAME_USER_AGENT_TYPE)
  private String userAgentType;

  public OAuthAuthorization() {
  }

  public OAuthAuthorization clientId(String clientId) {
    this.clientId = clientId;
    return this;
  }

  /**
   * ID of the OAuth client
   * @return clientId
   */
  @javax.annotation.Nonnull
  public String getClientId() {
    return clientId;
  }

  public void setClientId(String clientId) {
    this.clientId = clientId;
  }


  public OAuthAuthorization clientName(String clientName) {
    this.clientName = clientName;
    return this;
  }

  /**
   * Name, which is shown at the client configuration and authorization.
   * @return clientName
   */
  @javax.annotation.Nonnull
  public String getClientName() {
    return clientName;
  }

  public void setClientName(String clientName) {
    this.clientName = clientName;
  }


  public OAuthAuthorization createdAt(OffsetDateTime createdAt) {
    this.createdAt = createdAt;
    return this;
  }

  /**
   * &amp;#128640; Since v4.13.0  Creation date of the authorization
   * @return createdAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getCreatedAt() {
    return createdAt;
  }

  public void setCreatedAt(OffsetDateTime createdAt) {
    this.createdAt = createdAt;
  }


  public OAuthAuthorization expiresAt(OffsetDateTime expiresAt) {
    this.expiresAt = expiresAt;
    return this;
  }

  /**
   * Expiration date of the authorization
   * @return expiresAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getExpiresAt() {
    return expiresAt;
  }

  public void setExpiresAt(OffsetDateTime expiresAt) {
    this.expiresAt = expiresAt;
  }


  public OAuthAuthorization id(Long id) {
    this.id = id;
    return this;
  }

  /**
   * &amp;#128640; Since v4.12.0  ID of the OAuth authorization
   * @return id
   */
  @javax.annotation.Nullable
  public Long getId() {
    return id;
  }

  public void setId(Long id) {
    this.id = id;
  }


  public OAuthAuthorization isCurrentAuthorization(Boolean isCurrentAuthorization) {
    this.isCurrentAuthorization = isCurrentAuthorization;
    return this;
  }

  /**
   * &amp;#128640; Since v4.25.0  Determines whether authorization matches the one from Authorization Header
   * @return isCurrentAuthorization
   */
  @javax.annotation.Nullable
  public Boolean getIsCurrentAuthorization() {
    return isCurrentAuthorization;
  }

  public void setIsCurrentAuthorization(Boolean isCurrentAuthorization) {
    this.isCurrentAuthorization = isCurrentAuthorization;
  }


  public OAuthAuthorization isStandard(Boolean isStandard) {
    this.isStandard = isStandard;
    return this;
  }

  /**
   * &amp;#128640; Since v4.12.0  Determines whether client is a standard client.
   * @return isStandard
   */
  @javax.annotation.Nullable
  public Boolean getIsStandard() {
    return isStandard;
  }

  public void setIsStandard(Boolean isStandard) {
    this.isStandard = isStandard;
  }


  public OAuthAuthorization usedAt(OffsetDateTime usedAt) {
    this.usedAt = usedAt;
    return this;
  }

  /**
   * &amp;#128640; Since v4.13.0  Usage date of the authorization  (Time of last usage.)
   * @return usedAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getUsedAt() {
    return usedAt;
  }

  public void setUsedAt(OffsetDateTime usedAt) {
    this.usedAt = usedAt;
  }


  public OAuthAuthorization userAgentCategory(UserAgentCategoryEnum userAgentCategory) {
    this.userAgentCategory = userAgentCategory;
    return this;
  }

  /**
   * &amp;#128640; Since v4.12.0  User agent category.
   * @return userAgentCategory
   */
  @javax.annotation.Nonnull
  public UserAgentCategoryEnum getUserAgentCategory() {
    return userAgentCategory;
  }

  public void setUserAgentCategory(UserAgentCategoryEnum userAgentCategory) {
    this.userAgentCategory = userAgentCategory;
  }


  public OAuthAuthorization userAgentInfo(String userAgentInfo) {
    this.userAgentInfo = userAgentInfo;
    return this;
  }

  /**
   * &amp;#128640; Since v4.12.0  User agent info.
   * @return userAgentInfo
   */
  @javax.annotation.Nullable
  public String getUserAgentInfo() {
    return userAgentInfo;
  }

  public void setUserAgentInfo(String userAgentInfo) {
    this.userAgentInfo = userAgentInfo;
  }


  public OAuthAuthorization userAgentOs(String userAgentOs) {
    this.userAgentOs = userAgentOs;
    return this;
  }

  /**
   * &amp;#128640; Since v4.12.0  User agent OS.
   * @return userAgentOs
   */
  @javax.annotation.Nullable
  public String getUserAgentOs() {
    return userAgentOs;
  }

  public void setUserAgentOs(String userAgentOs) {
    this.userAgentOs = userAgentOs;
  }


  public OAuthAuthorization userAgentType(String userAgentType) {
    this.userAgentType = userAgentType;
    return this;
  }

  /**
   * &amp;#128640; Since v4.12.0  User agent type.
   * @return userAgentType
   */
  @javax.annotation.Nullable
  public String getUserAgentType() {
    return userAgentType;
  }

  public void setUserAgentType(String userAgentType) {
    this.userAgentType = userAgentType;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    OAuthAuthorization oauthAuthorization = (OAuthAuthorization) o;
    return Objects.equals(this.clientId, oauthAuthorization.clientId) &&
        Objects.equals(this.clientName, oauthAuthorization.clientName) &&
        Objects.equals(this.createdAt, oauthAuthorization.createdAt) &&
        Objects.equals(this.expiresAt, oauthAuthorization.expiresAt) &&
        Objects.equals(this.id, oauthAuthorization.id) &&
        Objects.equals(this.isCurrentAuthorization, oauthAuthorization.isCurrentAuthorization) &&
        Objects.equals(this.isStandard, oauthAuthorization.isStandard) &&
        Objects.equals(this.usedAt, oauthAuthorization.usedAt) &&
        Objects.equals(this.userAgentCategory, oauthAuthorization.userAgentCategory) &&
        Objects.equals(this.userAgentInfo, oauthAuthorization.userAgentInfo) &&
        Objects.equals(this.userAgentOs, oauthAuthorization.userAgentOs) &&
        Objects.equals(this.userAgentType, oauthAuthorization.userAgentType);
  }

  @Override
  public int hashCode() {
    return Objects.hash(clientId, clientName, createdAt, expiresAt, id, isCurrentAuthorization, isStandard, usedAt, userAgentCategory, userAgentInfo, userAgentOs, userAgentType);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class OAuthAuthorization {\n");
    sb.append("    clientId: ").append(toIndentedString(clientId)).append("\n");
    sb.append("    clientName: ").append(toIndentedString(clientName)).append("\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    expiresAt: ").append(toIndentedString(expiresAt)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    isCurrentAuthorization: ").append(toIndentedString(isCurrentAuthorization)).append("\n");
    sb.append("    isStandard: ").append(toIndentedString(isStandard)).append("\n");
    sb.append("    usedAt: ").append(toIndentedString(usedAt)).append("\n");
    sb.append("    userAgentCategory: ").append(toIndentedString(userAgentCategory)).append("\n");
    sb.append("    userAgentInfo: ").append(toIndentedString(userAgentInfo)).append("\n");
    sb.append("    userAgentOs: ").append(toIndentedString(userAgentOs)).append("\n");
    sb.append("    userAgentType: ").append(toIndentedString(userAgentType)).append("\n");
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
    openapiFields.add("clientId");
    openapiFields.add("clientName");
    openapiFields.add("createdAt");
    openapiFields.add("expiresAt");
    openapiFields.add("id");
    openapiFields.add("isCurrentAuthorization");
    openapiFields.add("isStandard");
    openapiFields.add("usedAt");
    openapiFields.add("userAgentCategory");
    openapiFields.add("userAgentInfo");
    openapiFields.add("userAgentOs");
    openapiFields.add("userAgentType");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("clientId");
    openapiRequiredFields.add("clientName");
    openapiRequiredFields.add("userAgentCategory");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to OAuthAuthorization
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!OAuthAuthorization.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in OAuthAuthorization is not found in the empty JSON string", OAuthAuthorization.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!OAuthAuthorization.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `OAuthAuthorization` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : OAuthAuthorization.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("clientId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `clientId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("clientId").toString()));
      }
      if (!jsonObj.get("clientName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `clientName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("clientName").toString()));
      }
      if (!jsonObj.get("userAgentCategory").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `userAgentCategory` to be a primitive type in the JSON string but got `%s`", jsonObj.get("userAgentCategory").toString()));
      }
      // validate the required field `userAgentCategory`
      UserAgentCategoryEnum.validateJsonElement(jsonObj.get("userAgentCategory"));
      if ((jsonObj.get("userAgentInfo") != null && !jsonObj.get("userAgentInfo").isJsonNull()) && !jsonObj.get("userAgentInfo").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `userAgentInfo` to be a primitive type in the JSON string but got `%s`", jsonObj.get("userAgentInfo").toString()));
      }
      if ((jsonObj.get("userAgentOs") != null && !jsonObj.get("userAgentOs").isJsonNull()) && !jsonObj.get("userAgentOs").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `userAgentOs` to be a primitive type in the JSON string but got `%s`", jsonObj.get("userAgentOs").toString()));
      }
      if ((jsonObj.get("userAgentType") != null && !jsonObj.get("userAgentType").isJsonNull()) && !jsonObj.get("userAgentType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `userAgentType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("userAgentType").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!OAuthAuthorization.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'OAuthAuthorization' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<OAuthAuthorization> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(OAuthAuthorization.class));

       return (TypeAdapter<T>) new TypeAdapter<OAuthAuthorization>() {
           @Override
           public void write(JsonWriter out, OAuthAuthorization value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public OAuthAuthorization read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of OAuthAuthorization given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of OAuthAuthorization
   * @throws IOException if the JSON string is invalid with respect to OAuthAuthorization
   */
  public static OAuthAuthorization fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, OAuthAuthorization.class);
  }

  /**
   * Convert an instance of OAuthAuthorization to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

