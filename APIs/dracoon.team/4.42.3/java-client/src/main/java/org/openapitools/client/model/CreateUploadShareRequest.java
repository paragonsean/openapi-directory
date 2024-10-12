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
 * Request model for creating an Upload Share
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:04:27.439567-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CreateUploadShareRequest {
  public static final String SERIALIZED_NAME_CREATOR_LANGUAGE = "creatorLanguage";
  @Deprecated
  @SerializedName(SERIALIZED_NAME_CREATOR_LANGUAGE)
  private String creatorLanguage;

  public static final String SERIALIZED_NAME_EXPIRATION = "expiration";
  @SerializedName(SERIALIZED_NAME_EXPIRATION)
  private ObjectExpiration expiration;

  public static final String SERIALIZED_NAME_FILES_EXPIRY_PERIOD = "filesExpiryPeriod";
  @SerializedName(SERIALIZED_NAME_FILES_EXPIRY_PERIOD)
  private Integer filesExpiryPeriod;

  public static final String SERIALIZED_NAME_INTERNAL_NOTES = "internalNotes";
  @SerializedName(SERIALIZED_NAME_INTERNAL_NOTES)
  private String internalNotes;

  public static final String SERIALIZED_NAME_MAIL_BODY = "mailBody";
  @Deprecated
  @SerializedName(SERIALIZED_NAME_MAIL_BODY)
  private String mailBody;

  public static final String SERIALIZED_NAME_MAIL_RECIPIENTS = "mailRecipients";
  @Deprecated
  @SerializedName(SERIALIZED_NAME_MAIL_RECIPIENTS)
  private String mailRecipients;

  public static final String SERIALIZED_NAME_MAIL_SUBJECT = "mailSubject";
  @Deprecated
  @SerializedName(SERIALIZED_NAME_MAIL_SUBJECT)
  private String mailSubject;

  public static final String SERIALIZED_NAME_MAX_SIZE = "maxSize";
  @SerializedName(SERIALIZED_NAME_MAX_SIZE)
  private Long maxSize;

  public static final String SERIALIZED_NAME_MAX_SLOTS = "maxSlots";
  @SerializedName(SERIALIZED_NAME_MAX_SLOTS)
  private Integer maxSlots;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_NOTES = "notes";
  @SerializedName(SERIALIZED_NAME_NOTES)
  private String notes;

  public static final String SERIALIZED_NAME_NOTIFY_CREATOR = "notifyCreator";
  @Deprecated
  @SerializedName(SERIALIZED_NAME_NOTIFY_CREATOR)
  private Boolean notifyCreator = false;

  public static final String SERIALIZED_NAME_PASSWORD = "password";
  @SerializedName(SERIALIZED_NAME_PASSWORD)
  private String password;

  public static final String SERIALIZED_NAME_RECEIVER_LANGUAGE = "receiverLanguage";
  @SerializedName(SERIALIZED_NAME_RECEIVER_LANGUAGE)
  private String receiverLanguage;

  public static final String SERIALIZED_NAME_SEND_MAIL = "sendMail";
  @Deprecated
  @SerializedName(SERIALIZED_NAME_SEND_MAIL)
  private Boolean sendMail = false;

  public static final String SERIALIZED_NAME_SEND_SMS = "sendSms";
  @Deprecated
  @SerializedName(SERIALIZED_NAME_SEND_SMS)
  private Boolean sendSms = false;

  public static final String SERIALIZED_NAME_SHOW_CREATOR_NAME = "showCreatorName";
  @SerializedName(SERIALIZED_NAME_SHOW_CREATOR_NAME)
  private Boolean showCreatorName = false;

  public static final String SERIALIZED_NAME_SHOW_CREATOR_USERNAME = "showCreatorUsername";
  @SerializedName(SERIALIZED_NAME_SHOW_CREATOR_USERNAME)
  private Boolean showCreatorUsername = false;

  public static final String SERIALIZED_NAME_SHOW_UPLOADED_FILES = "showUploadedFiles";
  @SerializedName(SERIALIZED_NAME_SHOW_UPLOADED_FILES)
  private Boolean showUploadedFiles = false;

  public static final String SERIALIZED_NAME_SMS_RECIPIENTS = "smsRecipients";
  @Deprecated
  @SerializedName(SERIALIZED_NAME_SMS_RECIPIENTS)
  private String smsRecipients;

  public static final String SERIALIZED_NAME_TARGET_ID = "targetId";
  @SerializedName(SERIALIZED_NAME_TARGET_ID)
  private Long targetId;

  public static final String SERIALIZED_NAME_TEXT_MESSAGE_RECIPIENTS = "textMessageRecipients";
  @SerializedName(SERIALIZED_NAME_TEXT_MESSAGE_RECIPIENTS)
  private List<String> textMessageRecipients = new ArrayList<>();

  public CreateUploadShareRequest() {
  }

  @Deprecated
  public CreateUploadShareRequest creatorLanguage(String creatorLanguage) {
    this.creatorLanguage = creatorLanguage;
    return this;
  }

  /**
   * &amp;#128679; Deprecated since v4.20.0  Language tag for messages to creator
   * @return creatorLanguage
   * @deprecated
   */
  @Deprecated
  @javax.annotation.Nullable
  public String getCreatorLanguage() {
    return creatorLanguage;
  }

  @Deprecated
  public void setCreatorLanguage(String creatorLanguage) {
    this.creatorLanguage = creatorLanguage;
  }


  public CreateUploadShareRequest expiration(ObjectExpiration expiration) {
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


  public CreateUploadShareRequest filesExpiryPeriod(Integer filesExpiryPeriod) {
    this.filesExpiryPeriod = filesExpiryPeriod;
    return this;
  }

  /**
   * Number of days after which uploaded files expire
   * @return filesExpiryPeriod
   */
  @javax.annotation.Nullable
  public Integer getFilesExpiryPeriod() {
    return filesExpiryPeriod;
  }

  public void setFilesExpiryPeriod(Integer filesExpiryPeriod) {
    this.filesExpiryPeriod = filesExpiryPeriod;
  }


  public CreateUploadShareRequest internalNotes(String internalNotes) {
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


  @Deprecated
  public CreateUploadShareRequest mailBody(String mailBody) {
    this.mailBody = mailBody;
    return this;
  }

  /**
   * &amp;#128679; Deprecated since v4.11.0  Notification email content
   * @return mailBody
   * @deprecated
   */
  @Deprecated
  @javax.annotation.Nullable
  public String getMailBody() {
    return mailBody;
  }

  @Deprecated
  public void setMailBody(String mailBody) {
    this.mailBody = mailBody;
  }


  @Deprecated
  public CreateUploadShareRequest mailRecipients(String mailRecipients) {
    this.mailRecipients = mailRecipients;
    return this;
  }

  /**
   * &amp;#128679; Deprecated since v4.11.0  CSV string of recipient email addresses
   * @return mailRecipients
   * @deprecated
   */
  @Deprecated
  @javax.annotation.Nullable
  public String getMailRecipients() {
    return mailRecipients;
  }

  @Deprecated
  public void setMailRecipients(String mailRecipients) {
    this.mailRecipients = mailRecipients;
  }


  @Deprecated
  public CreateUploadShareRequest mailSubject(String mailSubject) {
    this.mailSubject = mailSubject;
    return this;
  }

  /**
   * &amp;#128679; Deprecated since v4.11.0  Notification email subject
   * @return mailSubject
   * @deprecated
   */
  @Deprecated
  @javax.annotation.Nullable
  public String getMailSubject() {
    return mailSubject;
  }

  @Deprecated
  public void setMailSubject(String mailSubject) {
    this.mailSubject = mailSubject;
  }


  public CreateUploadShareRequest maxSize(Long maxSize) {
    this.maxSize = maxSize;
    return this;
  }

  /**
   * Maximal total size of uploaded files (in bytes)
   * @return maxSize
   */
  @javax.annotation.Nullable
  public Long getMaxSize() {
    return maxSize;
  }

  public void setMaxSize(Long maxSize) {
    this.maxSize = maxSize;
  }


  public CreateUploadShareRequest maxSlots(Integer maxSlots) {
    this.maxSlots = maxSlots;
    return this;
  }

  /**
   * Maximal amount of files to upload
   * @return maxSlots
   */
  @javax.annotation.Nullable
  public Integer getMaxSlots() {
    return maxSlots;
  }

  public void setMaxSlots(Integer maxSlots) {
    this.maxSlots = maxSlots;
  }


  public CreateUploadShareRequest name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Alias name  (default: name of the shared node)
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public CreateUploadShareRequest notes(String notes) {
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
  public CreateUploadShareRequest notifyCreator(Boolean notifyCreator) {
    this.notifyCreator = notifyCreator;
    return this;
  }

  /**
   * &amp;#128679; Deprecated since v4.20.0  Notify creator on every upload.
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


  public CreateUploadShareRequest password(String password) {
    this.password = password;
    return this;
  }

  /**
   * Password
   * @return password
   */
  @javax.annotation.Nullable
  public String getPassword() {
    return password;
  }

  public void setPassword(String password) {
    this.password = password;
  }


  public CreateUploadShareRequest receiverLanguage(String receiverLanguage) {
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


  @Deprecated
  public CreateUploadShareRequest sendMail(Boolean sendMail) {
    this.sendMail = sendMail;
    return this;
  }

  /**
   * &amp;#128679; Deprecated since v4.11.0  Notify recipients via email  Please use &#x60;POST /shares/uploads/{share_id}/email&#x60; API instead.
   * @return sendMail
   * @deprecated
   */
  @Deprecated
  @javax.annotation.Nullable
  public Boolean getSendMail() {
    return sendMail;
  }

  @Deprecated
  public void setSendMail(Boolean sendMail) {
    this.sendMail = sendMail;
  }


  @Deprecated
  public CreateUploadShareRequest sendSms(Boolean sendSms) {
    this.sendSms = sendSms;
    return this;
  }

  /**
   * &amp;#128679; Deprecated since v4.11.0  Send share password via SMS  Please use &#x60;textMessageRecipients&#x60; attribute instead.
   * @return sendSms
   * @deprecated
   */
  @Deprecated
  @javax.annotation.Nullable
  public Boolean getSendSms() {
    return sendSms;
  }

  @Deprecated
  public void setSendSms(Boolean sendSms) {
    this.sendSms = sendSms;
  }


  public CreateUploadShareRequest showCreatorName(Boolean showCreatorName) {
    this.showCreatorName = showCreatorName;
    return this;
  }

  /**
   * &amp;#128640; Since v4.11.0  Show creator first and last name.
   * @return showCreatorName
   */
  @javax.annotation.Nullable
  public Boolean getShowCreatorName() {
    return showCreatorName;
  }

  public void setShowCreatorName(Boolean showCreatorName) {
    this.showCreatorName = showCreatorName;
  }


  public CreateUploadShareRequest showCreatorUsername(Boolean showCreatorUsername) {
    this.showCreatorUsername = showCreatorUsername;
    return this;
  }

  /**
   * &amp;#128640; Since v4.11.0  Show creator email address.
   * @return showCreatorUsername
   */
  @javax.annotation.Nullable
  public Boolean getShowCreatorUsername() {
    return showCreatorUsername;
  }

  public void setShowCreatorUsername(Boolean showCreatorUsername) {
    this.showCreatorUsername = showCreatorUsername;
  }


  public CreateUploadShareRequest showUploadedFiles(Boolean showUploadedFiles) {
    this.showUploadedFiles = showUploadedFiles;
    return this;
  }

  /**
   * Allow display of already uploaded files
   * @return showUploadedFiles
   */
  @javax.annotation.Nullable
  public Boolean getShowUploadedFiles() {
    return showUploadedFiles;
  }

  public void setShowUploadedFiles(Boolean showUploadedFiles) {
    this.showUploadedFiles = showUploadedFiles;
  }


  @Deprecated
  public CreateUploadShareRequest smsRecipients(String smsRecipients) {
    this.smsRecipients = smsRecipients;
    return this;
  }

  /**
   * &amp;#128679; Deprecated since v4.11.0  CSV string of recipient MSISDNs
   * @return smsRecipients
   * @deprecated
   */
  @Deprecated
  @javax.annotation.Nullable
  public String getSmsRecipients() {
    return smsRecipients;
  }

  @Deprecated
  public void setSmsRecipients(String smsRecipients) {
    this.smsRecipients = smsRecipients;
  }


  public CreateUploadShareRequest targetId(Long targetId) {
    this.targetId = targetId;
    return this;
  }

  /**
   * Target room or folder ID
   * @return targetId
   */
  @javax.annotation.Nonnull
  public Long getTargetId() {
    return targetId;
  }

  public void setTargetId(Long targetId) {
    this.targetId = targetId;
  }


  public CreateUploadShareRequest textMessageRecipients(List<String> textMessageRecipients) {
    this.textMessageRecipients = textMessageRecipients;
    return this;
  }

  public CreateUploadShareRequest addTextMessageRecipientsItem(String textMessageRecipientsItem) {
    if (this.textMessageRecipients == null) {
      this.textMessageRecipients = new ArrayList<>();
    }
    this.textMessageRecipients.add(textMessageRecipientsItem);
    return this;
  }

  /**
   * &amp;#128640; Since v4.11.0  List of recipient FQTNs  E.123 / E.164 Format
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
    CreateUploadShareRequest createUploadShareRequest = (CreateUploadShareRequest) o;
    return Objects.equals(this.creatorLanguage, createUploadShareRequest.creatorLanguage) &&
        Objects.equals(this.expiration, createUploadShareRequest.expiration) &&
        Objects.equals(this.filesExpiryPeriod, createUploadShareRequest.filesExpiryPeriod) &&
        Objects.equals(this.internalNotes, createUploadShareRequest.internalNotes) &&
        Objects.equals(this.mailBody, createUploadShareRequest.mailBody) &&
        Objects.equals(this.mailRecipients, createUploadShareRequest.mailRecipients) &&
        Objects.equals(this.mailSubject, createUploadShareRequest.mailSubject) &&
        Objects.equals(this.maxSize, createUploadShareRequest.maxSize) &&
        Objects.equals(this.maxSlots, createUploadShareRequest.maxSlots) &&
        Objects.equals(this.name, createUploadShareRequest.name) &&
        Objects.equals(this.notes, createUploadShareRequest.notes) &&
        Objects.equals(this.notifyCreator, createUploadShareRequest.notifyCreator) &&
        Objects.equals(this.password, createUploadShareRequest.password) &&
        Objects.equals(this.receiverLanguage, createUploadShareRequest.receiverLanguage) &&
        Objects.equals(this.sendMail, createUploadShareRequest.sendMail) &&
        Objects.equals(this.sendSms, createUploadShareRequest.sendSms) &&
        Objects.equals(this.showCreatorName, createUploadShareRequest.showCreatorName) &&
        Objects.equals(this.showCreatorUsername, createUploadShareRequest.showCreatorUsername) &&
        Objects.equals(this.showUploadedFiles, createUploadShareRequest.showUploadedFiles) &&
        Objects.equals(this.smsRecipients, createUploadShareRequest.smsRecipients) &&
        Objects.equals(this.targetId, createUploadShareRequest.targetId) &&
        Objects.equals(this.textMessageRecipients, createUploadShareRequest.textMessageRecipients);
  }

  @Override
  public int hashCode() {
    return Objects.hash(creatorLanguage, expiration, filesExpiryPeriod, internalNotes, mailBody, mailRecipients, mailSubject, maxSize, maxSlots, name, notes, notifyCreator, password, receiverLanguage, sendMail, sendSms, showCreatorName, showCreatorUsername, showUploadedFiles, smsRecipients, targetId, textMessageRecipients);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CreateUploadShareRequest {\n");
    sb.append("    creatorLanguage: ").append(toIndentedString(creatorLanguage)).append("\n");
    sb.append("    expiration: ").append(toIndentedString(expiration)).append("\n");
    sb.append("    filesExpiryPeriod: ").append(toIndentedString(filesExpiryPeriod)).append("\n");
    sb.append("    internalNotes: ").append(toIndentedString(internalNotes)).append("\n");
    sb.append("    mailBody: ").append(toIndentedString(mailBody)).append("\n");
    sb.append("    mailRecipients: ").append(toIndentedString(mailRecipients)).append("\n");
    sb.append("    mailSubject: ").append(toIndentedString(mailSubject)).append("\n");
    sb.append("    maxSize: ").append(toIndentedString(maxSize)).append("\n");
    sb.append("    maxSlots: ").append(toIndentedString(maxSlots)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    notes: ").append(toIndentedString(notes)).append("\n");
    sb.append("    notifyCreator: ").append(toIndentedString(notifyCreator)).append("\n");
    sb.append("    password: ").append(toIndentedString(password)).append("\n");
    sb.append("    receiverLanguage: ").append(toIndentedString(receiverLanguage)).append("\n");
    sb.append("    sendMail: ").append(toIndentedString(sendMail)).append("\n");
    sb.append("    sendSms: ").append(toIndentedString(sendSms)).append("\n");
    sb.append("    showCreatorName: ").append(toIndentedString(showCreatorName)).append("\n");
    sb.append("    showCreatorUsername: ").append(toIndentedString(showCreatorUsername)).append("\n");
    sb.append("    showUploadedFiles: ").append(toIndentedString(showUploadedFiles)).append("\n");
    sb.append("    smsRecipients: ").append(toIndentedString(smsRecipients)).append("\n");
    sb.append("    targetId: ").append(toIndentedString(targetId)).append("\n");
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
    openapiFields.add("creatorLanguage");
    openapiFields.add("expiration");
    openapiFields.add("filesExpiryPeriod");
    openapiFields.add("internalNotes");
    openapiFields.add("mailBody");
    openapiFields.add("mailRecipients");
    openapiFields.add("mailSubject");
    openapiFields.add("maxSize");
    openapiFields.add("maxSlots");
    openapiFields.add("name");
    openapiFields.add("notes");
    openapiFields.add("notifyCreator");
    openapiFields.add("password");
    openapiFields.add("receiverLanguage");
    openapiFields.add("sendMail");
    openapiFields.add("sendSms");
    openapiFields.add("showCreatorName");
    openapiFields.add("showCreatorUsername");
    openapiFields.add("showUploadedFiles");
    openapiFields.add("smsRecipients");
    openapiFields.add("targetId");
    openapiFields.add("textMessageRecipients");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("targetId");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CreateUploadShareRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CreateUploadShareRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CreateUploadShareRequest is not found in the empty JSON string", CreateUploadShareRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CreateUploadShareRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CreateUploadShareRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : CreateUploadShareRequest.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("creatorLanguage") != null && !jsonObj.get("creatorLanguage").isJsonNull()) && !jsonObj.get("creatorLanguage").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `creatorLanguage` to be a primitive type in the JSON string but got `%s`", jsonObj.get("creatorLanguage").toString()));
      }
      // validate the optional field `expiration`
      if (jsonObj.get("expiration") != null && !jsonObj.get("expiration").isJsonNull()) {
        ObjectExpiration.validateJsonElement(jsonObj.get("expiration"));
      }
      if ((jsonObj.get("internalNotes") != null && !jsonObj.get("internalNotes").isJsonNull()) && !jsonObj.get("internalNotes").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `internalNotes` to be a primitive type in the JSON string but got `%s`", jsonObj.get("internalNotes").toString()));
      }
      if ((jsonObj.get("mailBody") != null && !jsonObj.get("mailBody").isJsonNull()) && !jsonObj.get("mailBody").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `mailBody` to be a primitive type in the JSON string but got `%s`", jsonObj.get("mailBody").toString()));
      }
      if ((jsonObj.get("mailRecipients") != null && !jsonObj.get("mailRecipients").isJsonNull()) && !jsonObj.get("mailRecipients").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `mailRecipients` to be a primitive type in the JSON string but got `%s`", jsonObj.get("mailRecipients").toString()));
      }
      if ((jsonObj.get("mailSubject") != null && !jsonObj.get("mailSubject").isJsonNull()) && !jsonObj.get("mailSubject").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `mailSubject` to be a primitive type in the JSON string but got `%s`", jsonObj.get("mailSubject").toString()));
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
      if ((jsonObj.get("smsRecipients") != null && !jsonObj.get("smsRecipients").isJsonNull()) && !jsonObj.get("smsRecipients").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `smsRecipients` to be a primitive type in the JSON string but got `%s`", jsonObj.get("smsRecipients").toString()));
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
       if (!CreateUploadShareRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CreateUploadShareRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CreateUploadShareRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CreateUploadShareRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<CreateUploadShareRequest>() {
           @Override
           public void write(JsonWriter out, CreateUploadShareRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CreateUploadShareRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CreateUploadShareRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CreateUploadShareRequest
   * @throws IOException if the JSON string is invalid with respect to CreateUploadShareRequest
   */
  public static CreateUploadShareRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CreateUploadShareRequest.class);
  }

  /**
   * Convert an instance of CreateUploadShareRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

