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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.ObjectExpiration;

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
 * Request model for updating a Download Share
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:04:27.439567-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class UpdateDownloadShareRequest {
  public static final String SERIALIZED_NAME_DEFAULT_COUNTRY = "defaultCountry";
  @SerializedName(SERIALIZED_NAME_DEFAULT_COUNTRY)
  private String defaultCountry;

  public static final String SERIALIZED_NAME_EXPIRATION = "expiration";
  @SerializedName(SERIALIZED_NAME_EXPIRATION)
  private ObjectExpiration expiration;

  public static final String SERIALIZED_NAME_INTERNAL_NOTES = "internalNotes";
  @SerializedName(SERIALIZED_NAME_INTERNAL_NOTES)
  private String internalNotes;

  public static final String SERIALIZED_NAME_MAX_DOWNLOADS = "maxDownloads";
  @SerializedName(SERIALIZED_NAME_MAX_DOWNLOADS)
  private Integer maxDownloads;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_NOTES = "notes";
  @SerializedName(SERIALIZED_NAME_NOTES)
  private String notes;

  public static final String SERIALIZED_NAME_NOTIFY_CREATOR = "notifyCreator";
  @Deprecated
  @SerializedName(SERIALIZED_NAME_NOTIFY_CREATOR)
  private Boolean notifyCreator;

  public static final String SERIALIZED_NAME_PASSWORD = "password";
  @SerializedName(SERIALIZED_NAME_PASSWORD)
  private String password;

  public static final String SERIALIZED_NAME_RECEIVER_LANGUAGE = "receiverLanguage";
  @SerializedName(SERIALIZED_NAME_RECEIVER_LANGUAGE)
  private String receiverLanguage;

  public static final String SERIALIZED_NAME_RESET_MAX_DOWNLOADS = "resetMaxDownloads";
  @SerializedName(SERIALIZED_NAME_RESET_MAX_DOWNLOADS)
  private Boolean resetMaxDownloads;

  public static final String SERIALIZED_NAME_RESET_PASSWORD = "resetPassword";
  @SerializedName(SERIALIZED_NAME_RESET_PASSWORD)
  private Boolean resetPassword;

  public static final String SERIALIZED_NAME_SHOW_CREATOR_NAME = "showCreatorName";
  @SerializedName(SERIALIZED_NAME_SHOW_CREATOR_NAME)
  private Boolean showCreatorName;

  public static final String SERIALIZED_NAME_SHOW_CREATOR_USERNAME = "showCreatorUsername";
  @SerializedName(SERIALIZED_NAME_SHOW_CREATOR_USERNAME)
  private Boolean showCreatorUsername;

  public static final String SERIALIZED_NAME_TEXT_MESSAGE_RECIPIENTS = "textMessageRecipients";
  @SerializedName(SERIALIZED_NAME_TEXT_MESSAGE_RECIPIENTS)
  private List<String> textMessageRecipients = new ArrayList<>();

  public UpdateDownloadShareRequest() {
  }

  public UpdateDownloadShareRequest defaultCountry(String defaultCountry) {
    this.defaultCountry = defaultCountry;
    return this;
  }

  /**
   * Country shorthand symbol (cf. ISO 3166-2)
   * @return defaultCountry
   */
  @javax.annotation.Nullable
  public String getDefaultCountry() {
    return defaultCountry;
  }

  public void setDefaultCountry(String defaultCountry) {
    this.defaultCountry = defaultCountry;
  }


  public UpdateDownloadShareRequest expiration(ObjectExpiration expiration) {
    this.expiration = expiration;
    return this;
  }

  /**
   * Get expiration
   * @return expiration
   */
  @javax.annotation.Nullable
  public ObjectExpiration getExpiration() {
    return expiration;
  }

  public void setExpiration(ObjectExpiration expiration) {
    this.expiration = expiration;
  }


  public UpdateDownloadShareRequest internalNotes(String internalNotes) {
    this.internalNotes = internalNotes;
    return this;
  }

  /**
   * &amp;#128640; Since v4.11.0  Internal notes
   * @return internalNotes
   */
  @javax.annotation.Nullable
  public String getInternalNotes() {
    return internalNotes;
  }

  public void setInternalNotes(String internalNotes) {
    this.internalNotes = internalNotes;
  }


  public UpdateDownloadShareRequest maxDownloads(Integer maxDownloads) {
    this.maxDownloads = maxDownloads;
    return this;
  }

  /**
   * Max allowed downloads
   * @return maxDownloads
   */
  @javax.annotation.Nullable
  public Integer getMaxDownloads() {
    return maxDownloads;
  }

  public void setMaxDownloads(Integer maxDownloads) {
    this.maxDownloads = maxDownloads;
  }


  public UpdateDownloadShareRequest name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Alias name
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public UpdateDownloadShareRequest notes(String notes) {
    this.notes = notes;
    return this;
  }

  /**
   * User notes
   * @return notes
   */
  @javax.annotation.Nullable
  public String getNotes() {
    return notes;
  }

  public void setNotes(String notes) {
    this.notes = notes;
  }


  @Deprecated
  public UpdateDownloadShareRequest notifyCreator(Boolean notifyCreator) {
    this.notifyCreator = notifyCreator;
    return this;
  }

  /**
   * &amp;#128679; Deprecated since v4.20.0  Notify creator on every download.
   * @return notifyCreator
   * @deprecated
   */
  @Deprecated
  @javax.annotation.Nullable
  public Boolean getNotifyCreator() {
    return notifyCreator;
  }

  @Deprecated
  public void setNotifyCreator(Boolean notifyCreator) {
    this.notifyCreator = notifyCreator;
  }


  public UpdateDownloadShareRequest password(String password) {
    this.password = password;
    return this;
  }

  /**
   * Access password, not allowed for encrypted shares
   * @return password
   */
  @javax.annotation.Nullable
  public String getPassword() {
    return password;
  }

  public void setPassword(String password) {
    this.password = password;
  }


  public UpdateDownloadShareRequest receiverLanguage(String receiverLanguage) {
    this.receiverLanguage = receiverLanguage;
    return this;
  }

  /**
   * Language tag for messages to receiver
   * @return receiverLanguage
   */
  @javax.annotation.Nullable
  public String getReceiverLanguage() {
    return receiverLanguage;
  }

  public void setReceiverLanguage(String receiverLanguage) {
    this.receiverLanguage = receiverLanguage;
  }


  public UpdateDownloadShareRequest resetMaxDownloads(Boolean resetMaxDownloads) {
    this.resetMaxDownloads = resetMaxDownloads;
    return this;
  }

  /**
   * Set &#39;true&#39; to reset &#39;maxDownloads&#39; for Download Share.
   * @return resetMaxDownloads
   */
  @javax.annotation.Nullable
  public Boolean getResetMaxDownloads() {
    return resetMaxDownloads;
  }

  public void setResetMaxDownloads(Boolean resetMaxDownloads) {
    this.resetMaxDownloads = resetMaxDownloads;
  }


  public UpdateDownloadShareRequest resetPassword(Boolean resetPassword) {
    this.resetPassword = resetPassword;
    return this;
  }

  /**
   * Set &#39;true&#39; to reset &#39;password&#39; for Download Share.
   * @return resetPassword
   */
  @javax.annotation.Nullable
  public Boolean getResetPassword() {
    return resetPassword;
  }

  public void setResetPassword(Boolean resetPassword) {
    this.resetPassword = resetPassword;
  }


  public UpdateDownloadShareRequest showCreatorName(Boolean showCreatorName) {
    this.showCreatorName = showCreatorName;
    return this;
  }

  /**
   * Show creator first and last name.
   * @return showCreatorName
   */
  @javax.annotation.Nullable
  public Boolean getShowCreatorName() {
    return showCreatorName;
  }

  public void setShowCreatorName(Boolean showCreatorName) {
    this.showCreatorName = showCreatorName;
  }


  public UpdateDownloadShareRequest showCreatorUsername(Boolean showCreatorUsername) {
    this.showCreatorUsername = showCreatorUsername;
    return this;
  }

  /**
   * Show creator email address.
   * @return showCreatorUsername
   */
  @javax.annotation.Nullable
  public Boolean getShowCreatorUsername() {
    return showCreatorUsername;
  }

  public void setShowCreatorUsername(Boolean showCreatorUsername) {
    this.showCreatorUsername = showCreatorUsername;
  }


  public UpdateDownloadShareRequest textMessageRecipients(List<String> textMessageRecipients) {
    this.textMessageRecipients = textMessageRecipients;
    return this;
  }

  public UpdateDownloadShareRequest addTextMessageRecipientsItem(String textMessageRecipientsItem) {
    if (this.textMessageRecipients == null) {
      this.textMessageRecipients = new ArrayList<>();
    }
    this.textMessageRecipients.add(textMessageRecipientsItem);
    return this;
  }

  /**
   * List of recipient FQTNs  E.123 / E.164 Format
   * @return textMessageRecipients
   */
  @javax.annotation.Nullable
  public List<String> getTextMessageRecipients() {
    return textMessageRecipients;
  }

  public void setTextMessageRecipients(List<String> textMessageRecipients) {
    this.textMessageRecipients = textMessageRecipients;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    UpdateDownloadShareRequest updateDownloadShareRequest = (UpdateDownloadShareRequest) o;
    return Objects.equals(this.defaultCountry, updateDownloadShareRequest.defaultCountry) &&
        Objects.equals(this.expiration, updateDownloadShareRequest.expiration) &&
        Objects.equals(this.internalNotes, updateDownloadShareRequest.internalNotes) &&
        Objects.equals(this.maxDownloads, updateDownloadShareRequest.maxDownloads) &&
        Objects.equals(this.name, updateDownloadShareRequest.name) &&
        Objects.equals(this.notes, updateDownloadShareRequest.notes) &&
        Objects.equals(this.notifyCreator, updateDownloadShareRequest.notifyCreator) &&
        Objects.equals(this.password, updateDownloadShareRequest.password) &&
        Objects.equals(this.receiverLanguage, updateDownloadShareRequest.receiverLanguage) &&
        Objects.equals(this.resetMaxDownloads, updateDownloadShareRequest.resetMaxDownloads) &&
        Objects.equals(this.resetPassword, updateDownloadShareRequest.resetPassword) &&
        Objects.equals(this.showCreatorName, updateDownloadShareRequest.showCreatorName) &&
        Objects.equals(this.showCreatorUsername, updateDownloadShareRequest.showCreatorUsername) &&
        Objects.equals(this.textMessageRecipients, updateDownloadShareRequest.textMessageRecipients);
  }

  @Override
  public int hashCode() {
    return Objects.hash(defaultCountry, expiration, internalNotes, maxDownloads, name, notes, notifyCreator, password, receiverLanguage, resetMaxDownloads, resetPassword, showCreatorName, showCreatorUsername, textMessageRecipients);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class UpdateDownloadShareRequest {\n");
    sb.append("    defaultCountry: ").append(toIndentedString(defaultCountry)).append("\n");
    sb.append("    expiration: ").append(toIndentedString(expiration)).append("\n");
    sb.append("    internalNotes: ").append(toIndentedString(internalNotes)).append("\n");
    sb.append("    maxDownloads: ").append(toIndentedString(maxDownloads)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    notes: ").append(toIndentedString(notes)).append("\n");
    sb.append("    notifyCreator: ").append(toIndentedString(notifyCreator)).append("\n");
    sb.append("    password: ").append(toIndentedString(password)).append("\n");
    sb.append("    receiverLanguage: ").append(toIndentedString(receiverLanguage)).append("\n");
    sb.append("    resetMaxDownloads: ").append(toIndentedString(resetMaxDownloads)).append("\n");
    sb.append("    resetPassword: ").append(toIndentedString(resetPassword)).append("\n");
    sb.append("    showCreatorName: ").append(toIndentedString(showCreatorName)).append("\n");
    sb.append("    showCreatorUsername: ").append(toIndentedString(showCreatorUsername)).append("\n");
    sb.append("    textMessageRecipients: ").append(toIndentedString(textMessageRecipients)).append("\n");
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
    openapiFields.add("defaultCountry");
    openapiFields.add("expiration");
    openapiFields.add("internalNotes");
    openapiFields.add("maxDownloads");
    openapiFields.add("name");
    openapiFields.add("notes");
    openapiFields.add("notifyCreator");
    openapiFields.add("password");
    openapiFields.add("receiverLanguage");
    openapiFields.add("resetMaxDownloads");
    openapiFields.add("resetPassword");
    openapiFields.add("showCreatorName");
    openapiFields.add("showCreatorUsername");
    openapiFields.add("textMessageRecipients");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to UpdateDownloadShareRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!UpdateDownloadShareRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in UpdateDownloadShareRequest is not found in the empty JSON string", UpdateDownloadShareRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!UpdateDownloadShareRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `UpdateDownloadShareRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("defaultCountry") != null && !jsonObj.get("defaultCountry").isJsonNull()) && !jsonObj.get("defaultCountry").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `defaultCountry` to be a primitive type in the JSON string but got `%s`", jsonObj.get("defaultCountry").toString()));
      }
      // validate the optional field `expiration`
      if (jsonObj.get("expiration") != null && !jsonObj.get("expiration").isJsonNull()) {
        ObjectExpiration.validateJsonElement(jsonObj.get("expiration"));
      }
      if ((jsonObj.get("internalNotes") != null && !jsonObj.get("internalNotes").isJsonNull()) && !jsonObj.get("internalNotes").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `internalNotes` to be a primitive type in the JSON string but got `%s`", jsonObj.get("internalNotes").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("notes") != null && !jsonObj.get("notes").isJsonNull()) && !jsonObj.get("notes").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `notes` to be a primitive type in the JSON string but got `%s`", jsonObj.get("notes").toString()));
      }
      if ((jsonObj.get("password") != null && !jsonObj.get("password").isJsonNull()) && !jsonObj.get("password").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `password` to be a primitive type in the JSON string but got `%s`", jsonObj.get("password").toString()));
      }
      if ((jsonObj.get("receiverLanguage") != null && !jsonObj.get("receiverLanguage").isJsonNull()) && !jsonObj.get("receiverLanguage").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `receiverLanguage` to be a primitive type in the JSON string but got `%s`", jsonObj.get("receiverLanguage").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("textMessageRecipients") != null && !jsonObj.get("textMessageRecipients").isJsonNull() && !jsonObj.get("textMessageRecipients").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `textMessageRecipients` to be an array in the JSON string but got `%s`", jsonObj.get("textMessageRecipients").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!UpdateDownloadShareRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'UpdateDownloadShareRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<UpdateDownloadShareRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(UpdateDownloadShareRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<UpdateDownloadShareRequest>() {
           @Override
           public void write(JsonWriter out, UpdateDownloadShareRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public UpdateDownloadShareRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of UpdateDownloadShareRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of UpdateDownloadShareRequest
   * @throws IOException if the JSON string is invalid with respect to UpdateDownloadShareRequest
   */
  public static UpdateDownloadShareRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, UpdateDownloadShareRequest.class);
  }

  /**
   * Convert an instance of UpdateDownloadShareRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

