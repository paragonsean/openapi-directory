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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

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
 * WebServiceAnalyseMessageResponse
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:12:22.444535-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class WebServiceAnalyseMessageResponse {
  public static final String SERIALIZED_NAME_CHARACTER_ANALYSIS = "characterAnalysis";
  @SerializedName(SERIALIZED_NAME_CHARACTER_ANALYSIS)
  private List<List<Object>> characterAnalysis = new ArrayList<>();

  public static final String SERIALIZED_NAME_MESSAGE_CREDIT_COST = "messageCreditCost";
  @SerializedName(SERIALIZED_NAME_MESSAGE_CREDIT_COST)
  private Double messageCreditCost;

  public static final String SERIALIZED_NAME_MESSAGE_ENCODING = "messageEncoding";
  @SerializedName(SERIALIZED_NAME_MESSAGE_ENCODING)
  private String messageEncoding;

  public static final String SERIALIZED_NAME_MESSAGE_LENGTH = "messageLength";
  @SerializedName(SERIALIZED_NAME_MESSAGE_LENGTH)
  private Integer messageLength;

  public static final String SERIALIZED_NAME_MESSAGE_LENGTH_WITHIN_MAXIMUM_ALLOWED = "messageLengthWithinMaximumAllowed";
  @SerializedName(SERIALIZED_NAME_MESSAGE_LENGTH_WITHIN_MAXIMUM_ALLOWED)
  private Boolean messageLengthWithinMaximumAllowed;

  public static final String SERIALIZED_NAME_NUMBER_OF_MESSAGES = "numberOfMessages";
  @SerializedName(SERIALIZED_NAME_NUMBER_OF_MESSAGES)
  private Integer numberOfMessages;

  public WebServiceAnalyseMessageResponse() {
  }

  public WebServiceAnalyseMessageResponse characterAnalysis(List<List<Object>> characterAnalysis) {
    this.characterAnalysis = characterAnalysis;
    return this;
  }

  public WebServiceAnalyseMessageResponse addCharacterAnalysisItem(List<Object> characterAnalysisItem) {
    if (this.characterAnalysis == null) {
      this.characterAnalysis = new ArrayList<>();
    }
    this.characterAnalysis.add(characterAnalysisItem);
    return this;
  }

  /**
   * Get characterAnalysis
   * @return characterAnalysis
   */
  @javax.annotation.Nullable
  public List<List<Object>> getCharacterAnalysis() {
    return characterAnalysis;
  }

  public void setCharacterAnalysis(List<List<Object>> characterAnalysis) {
    this.characterAnalysis = characterAnalysis;
  }


  public WebServiceAnalyseMessageResponse messageCreditCost(Double messageCreditCost) {
    this.messageCreditCost = messageCreditCost;
    return this;
  }

  /**
   * Get messageCreditCost
   * @return messageCreditCost
   */
  @javax.annotation.Nullable
  public Double getMessageCreditCost() {
    return messageCreditCost;
  }

  public void setMessageCreditCost(Double messageCreditCost) {
    this.messageCreditCost = messageCreditCost;
  }


  public WebServiceAnalyseMessageResponse messageEncoding(String messageEncoding) {
    this.messageEncoding = messageEncoding;
    return this;
  }

  /**
   * Get messageEncoding
   * @return messageEncoding
   */
  @javax.annotation.Nullable
  public String getMessageEncoding() {
    return messageEncoding;
  }

  public void setMessageEncoding(String messageEncoding) {
    this.messageEncoding = messageEncoding;
  }


  public WebServiceAnalyseMessageResponse messageLength(Integer messageLength) {
    this.messageLength = messageLength;
    return this;
  }

  /**
   * Get messageLength
   * @return messageLength
   */
  @javax.annotation.Nullable
  public Integer getMessageLength() {
    return messageLength;
  }

  public void setMessageLength(Integer messageLength) {
    this.messageLength = messageLength;
  }


  public WebServiceAnalyseMessageResponse messageLengthWithinMaximumAllowed(Boolean messageLengthWithinMaximumAllowed) {
    this.messageLengthWithinMaximumAllowed = messageLengthWithinMaximumAllowed;
    return this;
  }

  /**
   * Get messageLengthWithinMaximumAllowed
   * @return messageLengthWithinMaximumAllowed
   */
  @javax.annotation.Nullable
  public Boolean getMessageLengthWithinMaximumAllowed() {
    return messageLengthWithinMaximumAllowed;
  }

  public void setMessageLengthWithinMaximumAllowed(Boolean messageLengthWithinMaximumAllowed) {
    this.messageLengthWithinMaximumAllowed = messageLengthWithinMaximumAllowed;
  }


  public WebServiceAnalyseMessageResponse numberOfMessages(Integer numberOfMessages) {
    this.numberOfMessages = numberOfMessages;
    return this;
  }

  /**
   * Get numberOfMessages
   * @return numberOfMessages
   */
  @javax.annotation.Nullable
  public Integer getNumberOfMessages() {
    return numberOfMessages;
  }

  public void setNumberOfMessages(Integer numberOfMessages) {
    this.numberOfMessages = numberOfMessages;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    WebServiceAnalyseMessageResponse webServiceAnalyseMessageResponse = (WebServiceAnalyseMessageResponse) o;
    return Objects.equals(this.characterAnalysis, webServiceAnalyseMessageResponse.characterAnalysis) &&
        Objects.equals(this.messageCreditCost, webServiceAnalyseMessageResponse.messageCreditCost) &&
        Objects.equals(this.messageEncoding, webServiceAnalyseMessageResponse.messageEncoding) &&
        Objects.equals(this.messageLength, webServiceAnalyseMessageResponse.messageLength) &&
        Objects.equals(this.messageLengthWithinMaximumAllowed, webServiceAnalyseMessageResponse.messageLengthWithinMaximumAllowed) &&
        Objects.equals(this.numberOfMessages, webServiceAnalyseMessageResponse.numberOfMessages);
  }

  @Override
  public int hashCode() {
    return Objects.hash(characterAnalysis, messageCreditCost, messageEncoding, messageLength, messageLengthWithinMaximumAllowed, numberOfMessages);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class WebServiceAnalyseMessageResponse {\n");
    sb.append("    characterAnalysis: ").append(toIndentedString(characterAnalysis)).append("\n");
    sb.append("    messageCreditCost: ").append(toIndentedString(messageCreditCost)).append("\n");
    sb.append("    messageEncoding: ").append(toIndentedString(messageEncoding)).append("\n");
    sb.append("    messageLength: ").append(toIndentedString(messageLength)).append("\n");
    sb.append("    messageLengthWithinMaximumAllowed: ").append(toIndentedString(messageLengthWithinMaximumAllowed)).append("\n");
    sb.append("    numberOfMessages: ").append(toIndentedString(numberOfMessages)).append("\n");
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
    openapiFields.add("characterAnalysis");
    openapiFields.add("messageCreditCost");
    openapiFields.add("messageEncoding");
    openapiFields.add("messageLength");
    openapiFields.add("messageLengthWithinMaximumAllowed");
    openapiFields.add("numberOfMessages");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to WebServiceAnalyseMessageResponse
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!WebServiceAnalyseMessageResponse.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in WebServiceAnalyseMessageResponse is not found in the empty JSON string", WebServiceAnalyseMessageResponse.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!WebServiceAnalyseMessageResponse.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `WebServiceAnalyseMessageResponse` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the optional json data is an array if present
      if (jsonObj.get("characterAnalysis") != null && !jsonObj.get("characterAnalysis").isJsonNull() && !jsonObj.get("characterAnalysis").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `characterAnalysis` to be an array in the JSON string but got `%s`", jsonObj.get("characterAnalysis").toString()));
      }
      if ((jsonObj.get("messageEncoding") != null && !jsonObj.get("messageEncoding").isJsonNull()) && !jsonObj.get("messageEncoding").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `messageEncoding` to be a primitive type in the JSON string but got `%s`", jsonObj.get("messageEncoding").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!WebServiceAnalyseMessageResponse.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'WebServiceAnalyseMessageResponse' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<WebServiceAnalyseMessageResponse> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(WebServiceAnalyseMessageResponse.class));

       return (TypeAdapter<T>) new TypeAdapter<WebServiceAnalyseMessageResponse>() {
           @Override
           public void write(JsonWriter out, WebServiceAnalyseMessageResponse value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public WebServiceAnalyseMessageResponse read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of WebServiceAnalyseMessageResponse given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of WebServiceAnalyseMessageResponse
   * @throws IOException if the JSON string is invalid with respect to WebServiceAnalyseMessageResponse
   */
  public static WebServiceAnalyseMessageResponse fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, WebServiceAnalyseMessageResponse.class);
  }

  /**
   * Convert an instance of WebServiceAnalyseMessageResponse to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

