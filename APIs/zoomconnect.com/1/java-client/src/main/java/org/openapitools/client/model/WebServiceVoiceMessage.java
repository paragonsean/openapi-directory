/*
 * www.zoomconnect.com
 * The world's greatest SMS API
 *
 * The version of the OpenAPI document: 1
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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.Link;

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
 * WebServiceVoiceMessage
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:12:22.444535-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class WebServiceVoiceMessage {
  public static final String SERIALIZED_NAME_AUDIO_FILE_URL = "audioFileUrl";
  @SerializedName(SERIALIZED_NAME_AUDIO_FILE_URL)
  private String audioFileUrl;

  public static final String SERIALIZED_NAME_CAMPAIGN = "campaign";
  @SerializedName(SERIALIZED_NAME_CAMPAIGN)
  private String campaign;

  public static final String SERIALIZED_NAME_DATE_TIME_SENT = "dateTimeSent";
  @SerializedName(SERIALIZED_NAME_DATE_TIME_SENT)
  private OffsetDateTime dateTimeSent;

  public static final String SERIALIZED_NAME_DELETED = "deleted";
  @SerializedName(SERIALIZED_NAME_DELETED)
  private Boolean deleted;

  public static final String SERIALIZED_NAME_LANGUAGE = "language";
  @SerializedName(SERIALIZED_NAME_LANGUAGE)
  private String language;

  public static final String SERIALIZED_NAME_LINKS = "links";
  @SerializedName(SERIALIZED_NAME_LINKS)
  private List<Link> links = new ArrayList<>();

  public static final String SERIALIZED_NAME_MESSAGE = "message";
  @SerializedName(SERIALIZED_NAME_MESSAGE)
  private String message;

  public static final String SERIALIZED_NAME_MESSAGE_STATUS = "messageStatus";
  @SerializedName(SERIALIZED_NAME_MESSAGE_STATUS)
  private String messageStatus;

  public static final String SERIALIZED_NAME_TO_NUMBER = "toNumber";
  @SerializedName(SERIALIZED_NAME_TO_NUMBER)
  private String toNumber;

  public static final String SERIALIZED_NAME_USER_DATA_FIELD = "userDataField";
  @SerializedName(SERIALIZED_NAME_USER_DATA_FIELD)
  private String userDataField;

  public static final String SERIALIZED_NAME_VOICE_MESSAGE_ID = "voiceMessageId";
  @SerializedName(SERIALIZED_NAME_VOICE_MESSAGE_ID)
  private String voiceMessageId;

  public WebServiceVoiceMessage() {
  }

  public WebServiceVoiceMessage audioFileUrl(String audioFileUrl) {
    this.audioFileUrl = audioFileUrl;
    return this;
  }

  /**
   * Get audioFileUrl
   * @return audioFileUrl
   */
  @javax.annotation.Nullable
  public String getAudioFileUrl() {
    return audioFileUrl;
  }

  public void setAudioFileUrl(String audioFileUrl) {
    this.audioFileUrl = audioFileUrl;
  }


  public WebServiceVoiceMessage campaign(String campaign) {
    this.campaign = campaign;
    return this;
  }

  /**
   * Get campaign
   * @return campaign
   */
  @javax.annotation.Nullable
  public String getCampaign() {
    return campaign;
  }

  public void setCampaign(String campaign) {
    this.campaign = campaign;
  }


  public WebServiceVoiceMessage dateTimeSent(OffsetDateTime dateTimeSent) {
    this.dateTimeSent = dateTimeSent;
    return this;
  }

  /**
   * Get dateTimeSent
   * @return dateTimeSent
   */
  @javax.annotation.Nullable
  public OffsetDateTime getDateTimeSent() {
    return dateTimeSent;
  }

  public void setDateTimeSent(OffsetDateTime dateTimeSent) {
    this.dateTimeSent = dateTimeSent;
  }


  public WebServiceVoiceMessage deleted(Boolean deleted) {
    this.deleted = deleted;
    return this;
  }

  /**
   * Get deleted
   * @return deleted
   */
  @javax.annotation.Nullable
  public Boolean getDeleted() {
    return deleted;
  }

  public void setDeleted(Boolean deleted) {
    this.deleted = deleted;
  }


  public WebServiceVoiceMessage language(String language) {
    this.language = language;
    return this;
  }

  /**
   * Get language
   * @return language
   */
  @javax.annotation.Nullable
  public String getLanguage() {
    return language;
  }

  public void setLanguage(String language) {
    this.language = language;
  }


  public WebServiceVoiceMessage links(List<Link> links) {
    this.links = links;
    return this;
  }

  public WebServiceVoiceMessage addLinksItem(Link linksItem) {
    if (this.links == null) {
      this.links = new ArrayList<>();
    }
    this.links.add(linksItem);
    return this;
  }

  /**
   * Get links
   * @return links
   */
  @javax.annotation.Nullable
  public List<Link> getLinks() {
    return links;
  }

  public void setLinks(List<Link> links) {
    this.links = links;
  }


  public WebServiceVoiceMessage message(String message) {
    this.message = message;
    return this;
  }

  /**
   * Get message
   * @return message
   */
  @javax.annotation.Nullable
  public String getMessage() {
    return message;
  }

  public void setMessage(String message) {
    this.message = message;
  }


  public WebServiceVoiceMessage messageStatus(String messageStatus) {
    this.messageStatus = messageStatus;
    return this;
  }

  /**
   * Get messageStatus
   * @return messageStatus
   */
  @javax.annotation.Nullable
  public String getMessageStatus() {
    return messageStatus;
  }

  public void setMessageStatus(String messageStatus) {
    this.messageStatus = messageStatus;
  }


  public WebServiceVoiceMessage toNumber(String toNumber) {
    this.toNumber = toNumber;
    return this;
  }

  /**
   * Get toNumber
   * @return toNumber
   */
  @javax.annotation.Nullable
  public String getToNumber() {
    return toNumber;
  }

  public void setToNumber(String toNumber) {
    this.toNumber = toNumber;
  }


  public WebServiceVoiceMessage userDataField(String userDataField) {
    this.userDataField = userDataField;
    return this;
  }

  /**
   * Get userDataField
   * @return userDataField
   */
  @javax.annotation.Nullable
  public String getUserDataField() {
    return userDataField;
  }

  public void setUserDataField(String userDataField) {
    this.userDataField = userDataField;
  }


  public WebServiceVoiceMessage voiceMessageId(String voiceMessageId) {
    this.voiceMessageId = voiceMessageId;
    return this;
  }

  /**
   * Get voiceMessageId
   * @return voiceMessageId
   */
  @javax.annotation.Nullable
  public String getVoiceMessageId() {
    return voiceMessageId;
  }

  public void setVoiceMessageId(String voiceMessageId) {
    this.voiceMessageId = voiceMessageId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    WebServiceVoiceMessage webServiceVoiceMessage = (WebServiceVoiceMessage) o;
    return Objects.equals(this.audioFileUrl, webServiceVoiceMessage.audioFileUrl) &&
        Objects.equals(this.campaign, webServiceVoiceMessage.campaign) &&
        Objects.equals(this.dateTimeSent, webServiceVoiceMessage.dateTimeSent) &&
        Objects.equals(this.deleted, webServiceVoiceMessage.deleted) &&
        Objects.equals(this.language, webServiceVoiceMessage.language) &&
        Objects.equals(this.links, webServiceVoiceMessage.links) &&
        Objects.equals(this.message, webServiceVoiceMessage.message) &&
        Objects.equals(this.messageStatus, webServiceVoiceMessage.messageStatus) &&
        Objects.equals(this.toNumber, webServiceVoiceMessage.toNumber) &&
        Objects.equals(this.userDataField, webServiceVoiceMessage.userDataField) &&
        Objects.equals(this.voiceMessageId, webServiceVoiceMessage.voiceMessageId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(audioFileUrl, campaign, dateTimeSent, deleted, language, links, message, messageStatus, toNumber, userDataField, voiceMessageId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class WebServiceVoiceMessage {\n");
    sb.append("    audioFileUrl: ").append(toIndentedString(audioFileUrl)).append("\n");
    sb.append("    campaign: ").append(toIndentedString(campaign)).append("\n");
    sb.append("    dateTimeSent: ").append(toIndentedString(dateTimeSent)).append("\n");
    sb.append("    deleted: ").append(toIndentedString(deleted)).append("\n");
    sb.append("    language: ").append(toIndentedString(language)).append("\n");
    sb.append("    links: ").append(toIndentedString(links)).append("\n");
    sb.append("    message: ").append(toIndentedString(message)).append("\n");
    sb.append("    messageStatus: ").append(toIndentedString(messageStatus)).append("\n");
    sb.append("    toNumber: ").append(toIndentedString(toNumber)).append("\n");
    sb.append("    userDataField: ").append(toIndentedString(userDataField)).append("\n");
    sb.append("    voiceMessageId: ").append(toIndentedString(voiceMessageId)).append("\n");
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
    openapiFields.add("audioFileUrl");
    openapiFields.add("campaign");
    openapiFields.add("dateTimeSent");
    openapiFields.add("deleted");
    openapiFields.add("language");
    openapiFields.add("links");
    openapiFields.add("message");
    openapiFields.add("messageStatus");
    openapiFields.add("toNumber");
    openapiFields.add("userDataField");
    openapiFields.add("voiceMessageId");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to WebServiceVoiceMessage
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!WebServiceVoiceMessage.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in WebServiceVoiceMessage is not found in the empty JSON string", WebServiceVoiceMessage.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!WebServiceVoiceMessage.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `WebServiceVoiceMessage` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("audioFileUrl") != null && !jsonObj.get("audioFileUrl").isJsonNull()) && !jsonObj.get("audioFileUrl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `audioFileUrl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("audioFileUrl").toString()));
      }
      if ((jsonObj.get("campaign") != null && !jsonObj.get("campaign").isJsonNull()) && !jsonObj.get("campaign").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `campaign` to be a primitive type in the JSON string but got `%s`", jsonObj.get("campaign").toString()));
      }
      if ((jsonObj.get("language") != null && !jsonObj.get("language").isJsonNull()) && !jsonObj.get("language").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `language` to be a primitive type in the JSON string but got `%s`", jsonObj.get("language").toString()));
      }
      if (jsonObj.get("links") != null && !jsonObj.get("links").isJsonNull()) {
        JsonArray jsonArraylinks = jsonObj.getAsJsonArray("links");
        if (jsonArraylinks != null) {
          // ensure the json data is an array
          if (!jsonObj.get("links").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `links` to be an array in the JSON string but got `%s`", jsonObj.get("links").toString()));
          }

          // validate the optional field `links` (array)
          for (int i = 0; i < jsonArraylinks.size(); i++) {
            Link.validateJsonElement(jsonArraylinks.get(i));
          };
        }
      }
      if ((jsonObj.get("message") != null && !jsonObj.get("message").isJsonNull()) && !jsonObj.get("message").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `message` to be a primitive type in the JSON string but got `%s`", jsonObj.get("message").toString()));
      }
      if ((jsonObj.get("messageStatus") != null && !jsonObj.get("messageStatus").isJsonNull()) && !jsonObj.get("messageStatus").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `messageStatus` to be a primitive type in the JSON string but got `%s`", jsonObj.get("messageStatus").toString()));
      }
      if ((jsonObj.get("toNumber") != null && !jsonObj.get("toNumber").isJsonNull()) && !jsonObj.get("toNumber").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `toNumber` to be a primitive type in the JSON string but got `%s`", jsonObj.get("toNumber").toString()));
      }
      if ((jsonObj.get("userDataField") != null && !jsonObj.get("userDataField").isJsonNull()) && !jsonObj.get("userDataField").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `userDataField` to be a primitive type in the JSON string but got `%s`", jsonObj.get("userDataField").toString()));
      }
      if ((jsonObj.get("voiceMessageId") != null && !jsonObj.get("voiceMessageId").isJsonNull()) && !jsonObj.get("voiceMessageId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `voiceMessageId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("voiceMessageId").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!WebServiceVoiceMessage.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'WebServiceVoiceMessage' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<WebServiceVoiceMessage> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(WebServiceVoiceMessage.class));

       return (TypeAdapter<T>) new TypeAdapter<WebServiceVoiceMessage>() {
           @Override
           public void write(JsonWriter out, WebServiceVoiceMessage value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public WebServiceVoiceMessage read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of WebServiceVoiceMessage given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of WebServiceVoiceMessage
   * @throws IOException if the JSON string is invalid with respect to WebServiceVoiceMessage
   */
  public static WebServiceVoiceMessage fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, WebServiceVoiceMessage.class);
  }

  /**
   * Convert an instance of WebServiceVoiceMessage to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

