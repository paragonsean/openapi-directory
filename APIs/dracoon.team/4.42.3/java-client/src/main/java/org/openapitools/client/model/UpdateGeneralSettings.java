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
import java.util.Arrays;
import org.openapitools.client.model.UpdateAuthTokenRestrictions;

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
 * Request model for updating general settings
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:04:27.439567-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class UpdateGeneralSettings {
  public static final String SERIALIZED_NAME_AUTH_TOKEN_RESTRICTIONS = "authTokenRestrictions";
  @SerializedName(SERIALIZED_NAME_AUTH_TOKEN_RESTRICTIONS)
  private UpdateAuthTokenRestrictions authTokenRestrictions;

  public static final String SERIALIZED_NAME_CRYPTO_ENABLED = "cryptoEnabled";
  @SerializedName(SERIALIZED_NAME_CRYPTO_ENABLED)
  private Boolean cryptoEnabled;

  public static final String SERIALIZED_NAME_EMAIL_NOTIFICATION_BUTTON_ENABLED = "emailNotificationButtonEnabled";
  @SerializedName(SERIALIZED_NAME_EMAIL_NOTIFICATION_BUTTON_ENABLED)
  private Boolean emailNotificationButtonEnabled;

  public static final String SERIALIZED_NAME_EULA_ENABLED = "eulaEnabled";
  @SerializedName(SERIALIZED_NAME_EULA_ENABLED)
  private Boolean eulaEnabled;

  public static final String SERIALIZED_NAME_HIDE_LOGIN_INPUT_FIELDS = "hideLoginInputFields";
  @Deprecated
  @SerializedName(SERIALIZED_NAME_HIDE_LOGIN_INPUT_FIELDS)
  private Boolean hideLoginInputFields;

  public static final String SERIALIZED_NAME_MEDIA_SERVER_ENABLED = "mediaServerEnabled";
  @Deprecated
  @SerializedName(SERIALIZED_NAME_MEDIA_SERVER_ENABLED)
  private Boolean mediaServerEnabled;

  public static final String SERIALIZED_NAME_S3_TAGS_ENABLED = "s3TagsEnabled";
  @SerializedName(SERIALIZED_NAME_S3_TAGS_ENABLED)
  private Boolean s3TagsEnabled;

  public static final String SERIALIZED_NAME_SHARE_PASSWORD_SMS_ENABLED = "sharePasswordSmsEnabled";
  @SerializedName(SERIALIZED_NAME_SHARE_PASSWORD_SMS_ENABLED)
  private Boolean sharePasswordSmsEnabled;

  public static final String SERIALIZED_NAME_WEAK_PASSWORD_ENABLED = "weakPasswordEnabled";
  @Deprecated
  @SerializedName(SERIALIZED_NAME_WEAK_PASSWORD_ENABLED)
  private Boolean weakPasswordEnabled;

  public UpdateGeneralSettings() {
  }

  public UpdateGeneralSettings authTokenRestrictions(UpdateAuthTokenRestrictions authTokenRestrictions) {
    this.authTokenRestrictions = authTokenRestrictions;
    return this;
  }

  /**
   * Get authTokenRestrictions
   * @return authTokenRestrictions
   */
  @javax.annotation.Nullable
  public UpdateAuthTokenRestrictions getAuthTokenRestrictions() {
    return authTokenRestrictions;
  }

  public void setAuthTokenRestrictions(UpdateAuthTokenRestrictions authTokenRestrictions) {
    this.authTokenRestrictions = authTokenRestrictions;
  }


  public UpdateGeneralSettings cryptoEnabled(Boolean cryptoEnabled) {
    this.cryptoEnabled = cryptoEnabled;
    return this;
  }

  /**
   * Activation status of client-side encryption.  Can only be enabled once; disabling is not possible.
   * @return cryptoEnabled
   */
  @javax.annotation.Nullable
  public Boolean getCryptoEnabled() {
    return cryptoEnabled;
  }

  public void setCryptoEnabled(Boolean cryptoEnabled) {
    this.cryptoEnabled = cryptoEnabled;
  }


  public UpdateGeneralSettings emailNotificationButtonEnabled(Boolean emailNotificationButtonEnabled) {
    this.emailNotificationButtonEnabled = emailNotificationButtonEnabled;
    return this;
  }

  /**
   * Enable email notification button
   * @return emailNotificationButtonEnabled
   */
  @javax.annotation.Nullable
  public Boolean getEmailNotificationButtonEnabled() {
    return emailNotificationButtonEnabled;
  }

  public void setEmailNotificationButtonEnabled(Boolean emailNotificationButtonEnabled) {
    this.emailNotificationButtonEnabled = emailNotificationButtonEnabled;
  }


  public UpdateGeneralSettings eulaEnabled(Boolean eulaEnabled) {
    this.eulaEnabled = eulaEnabled;
    return this;
  }

  /**
   * Each user has to confirm the EULA at first login.
   * @return eulaEnabled
   */
  @javax.annotation.Nullable
  public Boolean getEulaEnabled() {
    return eulaEnabled;
  }

  public void setEulaEnabled(Boolean eulaEnabled) {
    this.eulaEnabled = eulaEnabled;
  }


  @Deprecated
  public UpdateGeneralSettings hideLoginInputFields(Boolean hideLoginInputFields) {
    this.hideLoginInputFields = hideLoginInputFields;
    return this;
  }

  /**
   * &amp;#128679; Deprecated since v4.13.0  Defines if login fields should be hidden
   * @return hideLoginInputFields
   * @deprecated
   */
  @Deprecated
  @javax.annotation.Nullable
  public Boolean getHideLoginInputFields() {
    return hideLoginInputFields;
  }

  @Deprecated
  public void setHideLoginInputFields(Boolean hideLoginInputFields) {
    this.hideLoginInputFields = hideLoginInputFields;
  }


  @Deprecated
  public UpdateGeneralSettings mediaServerEnabled(Boolean mediaServerEnabled) {
    this.mediaServerEnabled = mediaServerEnabled;
    return this;
  }

  /**
   * &amp;#128679; Deprecated since v4.12.0  Determines if the media server is enabled
   * @return mediaServerEnabled
   * @deprecated
   */
  @Deprecated
  @javax.annotation.Nullable
  public Boolean getMediaServerEnabled() {
    return mediaServerEnabled;
  }

  @Deprecated
  public void setMediaServerEnabled(Boolean mediaServerEnabled) {
    this.mediaServerEnabled = mediaServerEnabled;
  }


  public UpdateGeneralSettings s3TagsEnabled(Boolean s3TagsEnabled) {
    this.s3TagsEnabled = s3TagsEnabled;
    return this;
  }

  /**
   * &amp;#128640; Since v4.9.0  Defines if S3 tags are enabled
   * @return s3TagsEnabled
   */
  @javax.annotation.Nullable
  public Boolean getS3TagsEnabled() {
    return s3TagsEnabled;
  }

  public void setS3TagsEnabled(Boolean s3TagsEnabled) {
    this.s3TagsEnabled = s3TagsEnabled;
  }


  public UpdateGeneralSettings sharePasswordSmsEnabled(Boolean sharePasswordSmsEnabled) {
    this.sharePasswordSmsEnabled = sharePasswordSmsEnabled;
    return this;
  }

  /**
   * Allow sending of share passwords via SMS
   * @return sharePasswordSmsEnabled
   */
  @javax.annotation.Nullable
  public Boolean getSharePasswordSmsEnabled() {
    return sharePasswordSmsEnabled;
  }

  public void setSharePasswordSmsEnabled(Boolean sharePasswordSmsEnabled) {
    this.sharePasswordSmsEnabled = sharePasswordSmsEnabled;
  }


  @Deprecated
  public UpdateGeneralSettings weakPasswordEnabled(Boolean weakPasswordEnabled) {
    this.weakPasswordEnabled = weakPasswordEnabled;
    return this;
  }

  /**
   * &amp;#128679; Deprecated since v4.14.0  Allow weak password  * A weak password has to fulfill the following criteria:     * is at least 8 characters long     * contains letters and numbers  * A strong password has to fulfill the following criteria in addition:     * contains at least one special character     * contains upper and lower case characters  Please use &#x60;PUT /system/config/policies/passwords&#x60; API to change configured password policies.
   * @return weakPasswordEnabled
   * @deprecated
   */
  @Deprecated
  @javax.annotation.Nullable
  public Boolean getWeakPasswordEnabled() {
    return weakPasswordEnabled;
  }

  @Deprecated
  public void setWeakPasswordEnabled(Boolean weakPasswordEnabled) {
    this.weakPasswordEnabled = weakPasswordEnabled;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    UpdateGeneralSettings updateGeneralSettings = (UpdateGeneralSettings) o;
    return Objects.equals(this.authTokenRestrictions, updateGeneralSettings.authTokenRestrictions) &&
        Objects.equals(this.cryptoEnabled, updateGeneralSettings.cryptoEnabled) &&
        Objects.equals(this.emailNotificationButtonEnabled, updateGeneralSettings.emailNotificationButtonEnabled) &&
        Objects.equals(this.eulaEnabled, updateGeneralSettings.eulaEnabled) &&
        Objects.equals(this.hideLoginInputFields, updateGeneralSettings.hideLoginInputFields) &&
        Objects.equals(this.mediaServerEnabled, updateGeneralSettings.mediaServerEnabled) &&
        Objects.equals(this.s3TagsEnabled, updateGeneralSettings.s3TagsEnabled) &&
        Objects.equals(this.sharePasswordSmsEnabled, updateGeneralSettings.sharePasswordSmsEnabled) &&
        Objects.equals(this.weakPasswordEnabled, updateGeneralSettings.weakPasswordEnabled);
  }

  @Override
  public int hashCode() {
    return Objects.hash(authTokenRestrictions, cryptoEnabled, emailNotificationButtonEnabled, eulaEnabled, hideLoginInputFields, mediaServerEnabled, s3TagsEnabled, sharePasswordSmsEnabled, weakPasswordEnabled);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class UpdateGeneralSettings {\n");
    sb.append("    authTokenRestrictions: ").append(toIndentedString(authTokenRestrictions)).append("\n");
    sb.append("    cryptoEnabled: ").append(toIndentedString(cryptoEnabled)).append("\n");
    sb.append("    emailNotificationButtonEnabled: ").append(toIndentedString(emailNotificationButtonEnabled)).append("\n");
    sb.append("    eulaEnabled: ").append(toIndentedString(eulaEnabled)).append("\n");
    sb.append("    hideLoginInputFields: ").append(toIndentedString(hideLoginInputFields)).append("\n");
    sb.append("    mediaServerEnabled: ").append(toIndentedString(mediaServerEnabled)).append("\n");
    sb.append("    s3TagsEnabled: ").append(toIndentedString(s3TagsEnabled)).append("\n");
    sb.append("    sharePasswordSmsEnabled: ").append(toIndentedString(sharePasswordSmsEnabled)).append("\n");
    sb.append("    weakPasswordEnabled: ").append(toIndentedString(weakPasswordEnabled)).append("\n");
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
    openapiFields.add("authTokenRestrictions");
    openapiFields.add("cryptoEnabled");
    openapiFields.add("emailNotificationButtonEnabled");
    openapiFields.add("eulaEnabled");
    openapiFields.add("hideLoginInputFields");
    openapiFields.add("mediaServerEnabled");
    openapiFields.add("s3TagsEnabled");
    openapiFields.add("sharePasswordSmsEnabled");
    openapiFields.add("weakPasswordEnabled");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to UpdateGeneralSettings
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!UpdateGeneralSettings.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in UpdateGeneralSettings is not found in the empty JSON string", UpdateGeneralSettings.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!UpdateGeneralSettings.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `UpdateGeneralSettings` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `authTokenRestrictions`
      if (jsonObj.get("authTokenRestrictions") != null && !jsonObj.get("authTokenRestrictions").isJsonNull()) {
        UpdateAuthTokenRestrictions.validateJsonElement(jsonObj.get("authTokenRestrictions"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!UpdateGeneralSettings.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'UpdateGeneralSettings' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<UpdateGeneralSettings> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(UpdateGeneralSettings.class));

       return (TypeAdapter<T>) new TypeAdapter<UpdateGeneralSettings>() {
           @Override
           public void write(JsonWriter out, UpdateGeneralSettings value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public UpdateGeneralSettings read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of UpdateGeneralSettings given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of UpdateGeneralSettings
   * @throws IOException if the JSON string is invalid with respect to UpdateGeneralSettings
   */
  public static UpdateGeneralSettings fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, UpdateGeneralSettings.class);
  }

  /**
   * Convert an instance of UpdateGeneralSettings to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

