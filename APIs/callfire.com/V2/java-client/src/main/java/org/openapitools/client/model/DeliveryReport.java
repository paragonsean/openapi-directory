/*
 * CallFire API Documentation
 * CallFire
 *
 * The version of the OpenAPI document: V2
 * Contact: support@callfire.com
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
 * ~
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:59:09.684594-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class DeliveryReport {
  public static final String SERIALIZED_NAME_CAMPAIGN_ID = "campaignId";
  @SerializedName(SERIALIZED_NAME_CAMPAIGN_ID)
  private Long campaignId;

  public static final String SERIALIZED_NAME_CARRIER = "carrier";
  @SerializedName(SERIALIZED_NAME_CARRIER)
  private String carrier;

  /**
   * ~
   */
  @JsonAdapter(DeliveryCategoryEnum.Adapter.class)
  public enum DeliveryCategoryEnum {
    NO_DATA("NO_DATA"),
    
    OPTED_OUT("OPTED_OUT"),
    
    BOUNCED("BOUNCED"),
    
    NO_CREDITS("NO_CREDITS"),
    
    DELIVERED("DELIVERED");

    private String value;

    DeliveryCategoryEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static DeliveryCategoryEnum fromValue(String value) {
      for (DeliveryCategoryEnum b : DeliveryCategoryEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<DeliveryCategoryEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final DeliveryCategoryEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public DeliveryCategoryEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return DeliveryCategoryEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      DeliveryCategoryEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_DELIVERY_CATEGORY = "deliveryCategory";
  @SerializedName(SERIALIZED_NAME_DELIVERY_CATEGORY)
  private DeliveryCategoryEnum deliveryCategory;

  /**
   * ~
   */
  @JsonAdapter(DeliveryStateEnum.Adapter.class)
  public enum DeliveryStateEnum {
    DELIVERED("DELIVERED"),
    
    UNSENT_OPTED_OUT_GLOBAL("UNSENT_OPTED_OUT_GLOBAL"),
    
    UNSENT_OPTED_OUT_LOCAL("UNSENT_OPTED_OUT_LOCAL"),
    
    UNSENT_NO_CREDITS("UNSENT_NO_CREDITS"),
    
    GATEWAY_REJECTED("GATEWAY_REJECTED"),
    
    CARRIER_REJECTED("CARRIER_REJECTED"),
    
    NOT_DELIVERED("NOT_DELIVERED"),
    
    UNSENT_INVALID_NUMBER("UNSENT_INVALID_NUMBER"),
    
    UNSENT_BAD_DATA("UNSENT_BAD_DATA"),
    
    UNSENT_FORCE_STOPPED("UNSENT_FORCE_STOPPED"),
    
    UNSENT_PERIOD_LIMIT("UNSENT_PERIOD_LIMIT"),
    
    UNSENT_INTERNATIONAL("UNSENT_INTERNATIONAL"),
    
    UNSENT_INVALID_TIMEZONE_OR_DNC("UNSENT_INVALID_TIMEZONE_OR_DNC"),
    
    UNSENT_ALREADY_SCRUBBED("UNSENT_ALREADY_SCRUBBED"),
    
    UNSENT_SYSTEM_ERROR("UNSENT_SYSTEM_ERROR"),
    
    UNSENT_NO_WIRELESS_CARRIER("UNSENT_NO_WIRELESS_CARRIER"),
    
    UNSENT_MESSAGE_TOO_LONG("UNSENT_MESSAGE_TOO_LONG"),
    
    UNSENT_MESSAGE_BLOCKED("UNSENT_MESSAGE_BLOCKED"),
    
    UNSENT_QUEUE_LIMIT_REACHED("UNSENT_QUEUE_LIMIT_REACHED"),
    
    UNSENT_TOKEN_LIMIT_REACHED("UNSENT_TOKEN_LIMIT_REACHED"),
    
    UNSENT_TIME_LIMIT_REACHED("UNSENT_TIME_LIMIT_REACHED"),
    
    UNSENT_SCHEDULER_CAPACITY_EXCEEDED("UNSENT_SCHEDULER_CAPACITY_EXCEEDED"),
    
    SPAM_DETECTED("SPAM_DETECTED"),
    
    UNSENT_NO_GATEWAY("UNSENT_NO_GATEWAY"),
    
    UNSENT_DAILY_LIMIT_REACHED("UNSENT_DAILY_LIMIT_REACHED"),
    
    ORIGINATED("ORIGINATED"),
    
    SUBMITTED("SUBMITTED"),
    
    FORWARDED("FORWARDED"),
    
    NOT_GIVEN("NOT_GIVEN"),
    
    UNKNOWN("UNKNOWN"),
    
    RETRY_MMS_AS_SMS("RETRY_MMS_AS_SMS"),
    
    QUEUED("QUEUED"),
    
    QUEUED_TRANSCODE("QUEUED_TRANSCODE"),
    
    ORIGINAL("ORIGINAL"),
    
    DUPE("DUPE"),
    
    TRUNCATED("TRUNCATED"),
    
    REQUEUED_RATE_LIMITED("REQUEUED_RATE_LIMITED"),
    
    BUFFERED("BUFFERED"),
    
    RATE_LIMIT_EXCEEDED("RATE_LIMIT_EXCEEDED"),
    
    SERVICE_UNAVAILABLE("SERVICE_UNAVAILABLE"),
    
    SEND_MMS_AS_SMS("SEND_MMS_AS_SMS"),
    
    REQUEUED_RECOVERABLE_ERROR("REQUEUED_RECOVERABLE_ERROR"),
    
    SEND_WITH_ADDITIONAL_SPID("SEND_WITH_ADDITIONAL_SPID"),
    
    UNSENT_FREE_TRIAL("UNSENT_FREE_TRIAL");

    private String value;

    DeliveryStateEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static DeliveryStateEnum fromValue(String value) {
      for (DeliveryStateEnum b : DeliveryStateEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<DeliveryStateEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final DeliveryStateEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public DeliveryStateEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return DeliveryStateEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      DeliveryStateEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_DELIVERY_STATE = "deliveryState";
  @SerializedName(SERIALIZED_NAME_DELIVERY_STATE)
  private DeliveryStateEnum deliveryState;

  public static final String SERIALIZED_NAME_FROM_NUMBER = "fromNumber";
  @SerializedName(SERIALIZED_NAME_FROM_NUMBER)
  private String fromNumber;

  public static final String SERIALIZED_NAME_MESSAGE_TEXT = "messageText";
  @SerializedName(SERIALIZED_NAME_MESSAGE_TEXT)
  private String messageText;

  public static final String SERIALIZED_NAME_TO_NUMBER = "toNumber";
  @SerializedName(SERIALIZED_NAME_TO_NUMBER)
  private String toNumber;

  public static final String SERIALIZED_NAME_UPDATED = "updated";
  @SerializedName(SERIALIZED_NAME_UPDATED)
  private OffsetDateTime updated;

  public DeliveryReport() {
  }

  public DeliveryReport campaignId(Long campaignId) {
    this.campaignId = campaignId;
    return this;
  }

  /**
   * ~
   * @return campaignId
   */
  @javax.annotation.Nullable
  public Long getCampaignId() {
    return campaignId;
  }

  public void setCampaignId(Long campaignId) {
    this.campaignId = campaignId;
  }


  public DeliveryReport carrier(String carrier) {
    this.carrier = carrier;
    return this;
  }

  /**
   * ~
   * @return carrier
   */
  @javax.annotation.Nullable
  public String getCarrier() {
    return carrier;
  }

  public void setCarrier(String carrier) {
    this.carrier = carrier;
  }


  public DeliveryReport deliveryCategory(DeliveryCategoryEnum deliveryCategory) {
    this.deliveryCategory = deliveryCategory;
    return this;
  }

  /**
   * ~
   * @return deliveryCategory
   */
  @javax.annotation.Nullable
  public DeliveryCategoryEnum getDeliveryCategory() {
    return deliveryCategory;
  }

  public void setDeliveryCategory(DeliveryCategoryEnum deliveryCategory) {
    this.deliveryCategory = deliveryCategory;
  }


  public DeliveryReport deliveryState(DeliveryStateEnum deliveryState) {
    this.deliveryState = deliveryState;
    return this;
  }

  /**
   * ~
   * @return deliveryState
   */
  @javax.annotation.Nullable
  public DeliveryStateEnum getDeliveryState() {
    return deliveryState;
  }

  public void setDeliveryState(DeliveryStateEnum deliveryState) {
    this.deliveryState = deliveryState;
  }


  public DeliveryReport fromNumber(String fromNumber) {
    this.fromNumber = fromNumber;
    return this;
  }

  /**
   * ~
   * @return fromNumber
   */
  @javax.annotation.Nullable
  public String getFromNumber() {
    return fromNumber;
  }

  public void setFromNumber(String fromNumber) {
    this.fromNumber = fromNumber;
  }


  public DeliveryReport messageText(String messageText) {
    this.messageText = messageText;
    return this;
  }

  /**
   * ~
   * @return messageText
   */
  @javax.annotation.Nullable
  public String getMessageText() {
    return messageText;
  }

  public void setMessageText(String messageText) {
    this.messageText = messageText;
  }


  public DeliveryReport toNumber(String toNumber) {
    this.toNumber = toNumber;
    return this;
  }

  /**
   * ~
   * @return toNumber
   */
  @javax.annotation.Nullable
  public String getToNumber() {
    return toNumber;
  }

  public void setToNumber(String toNumber) {
    this.toNumber = toNumber;
  }


  public DeliveryReport updated(OffsetDateTime updated) {
    this.updated = updated;
    return this;
  }

  /**
   * ~
   * @return updated
   */
  @javax.annotation.Nullable
  public OffsetDateTime getUpdated() {
    return updated;
  }

  public void setUpdated(OffsetDateTime updated) {
    this.updated = updated;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    DeliveryReport deliveryReport = (DeliveryReport) o;
    return Objects.equals(this.campaignId, deliveryReport.campaignId) &&
        Objects.equals(this.carrier, deliveryReport.carrier) &&
        Objects.equals(this.deliveryCategory, deliveryReport.deliveryCategory) &&
        Objects.equals(this.deliveryState, deliveryReport.deliveryState) &&
        Objects.equals(this.fromNumber, deliveryReport.fromNumber) &&
        Objects.equals(this.messageText, deliveryReport.messageText) &&
        Objects.equals(this.toNumber, deliveryReport.toNumber) &&
        Objects.equals(this.updated, deliveryReport.updated);
  }

  @Override
  public int hashCode() {
    return Objects.hash(campaignId, carrier, deliveryCategory, deliveryState, fromNumber, messageText, toNumber, updated);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class DeliveryReport {\n");
    sb.append("    campaignId: ").append(toIndentedString(campaignId)).append("\n");
    sb.append("    carrier: ").append(toIndentedString(carrier)).append("\n");
    sb.append("    deliveryCategory: ").append(toIndentedString(deliveryCategory)).append("\n");
    sb.append("    deliveryState: ").append(toIndentedString(deliveryState)).append("\n");
    sb.append("    fromNumber: ").append(toIndentedString(fromNumber)).append("\n");
    sb.append("    messageText: ").append(toIndentedString(messageText)).append("\n");
    sb.append("    toNumber: ").append(toIndentedString(toNumber)).append("\n");
    sb.append("    updated: ").append(toIndentedString(updated)).append("\n");
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
    openapiFields.add("campaignId");
    openapiFields.add("carrier");
    openapiFields.add("deliveryCategory");
    openapiFields.add("deliveryState");
    openapiFields.add("fromNumber");
    openapiFields.add("messageText");
    openapiFields.add("toNumber");
    openapiFields.add("updated");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to DeliveryReport
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!DeliveryReport.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in DeliveryReport is not found in the empty JSON string", DeliveryReport.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!DeliveryReport.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `DeliveryReport` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("carrier") != null && !jsonObj.get("carrier").isJsonNull()) && !jsonObj.get("carrier").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `carrier` to be a primitive type in the JSON string but got `%s`", jsonObj.get("carrier").toString()));
      }
      if ((jsonObj.get("deliveryCategory") != null && !jsonObj.get("deliveryCategory").isJsonNull()) && !jsonObj.get("deliveryCategory").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `deliveryCategory` to be a primitive type in the JSON string but got `%s`", jsonObj.get("deliveryCategory").toString()));
      }
      // validate the optional field `deliveryCategory`
      if (jsonObj.get("deliveryCategory") != null && !jsonObj.get("deliveryCategory").isJsonNull()) {
        DeliveryCategoryEnum.validateJsonElement(jsonObj.get("deliveryCategory"));
      }
      if ((jsonObj.get("deliveryState") != null && !jsonObj.get("deliveryState").isJsonNull()) && !jsonObj.get("deliveryState").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `deliveryState` to be a primitive type in the JSON string but got `%s`", jsonObj.get("deliveryState").toString()));
      }
      // validate the optional field `deliveryState`
      if (jsonObj.get("deliveryState") != null && !jsonObj.get("deliveryState").isJsonNull()) {
        DeliveryStateEnum.validateJsonElement(jsonObj.get("deliveryState"));
      }
      if ((jsonObj.get("fromNumber") != null && !jsonObj.get("fromNumber").isJsonNull()) && !jsonObj.get("fromNumber").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `fromNumber` to be a primitive type in the JSON string but got `%s`", jsonObj.get("fromNumber").toString()));
      }
      if ((jsonObj.get("messageText") != null && !jsonObj.get("messageText").isJsonNull()) && !jsonObj.get("messageText").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `messageText` to be a primitive type in the JSON string but got `%s`", jsonObj.get("messageText").toString()));
      }
      if ((jsonObj.get("toNumber") != null && !jsonObj.get("toNumber").isJsonNull()) && !jsonObj.get("toNumber").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `toNumber` to be a primitive type in the JSON string but got `%s`", jsonObj.get("toNumber").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!DeliveryReport.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'DeliveryReport' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<DeliveryReport> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(DeliveryReport.class));

       return (TypeAdapter<T>) new TypeAdapter<DeliveryReport>() {
           @Override
           public void write(JsonWriter out, DeliveryReport value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public DeliveryReport read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of DeliveryReport given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of DeliveryReport
   * @throws IOException if the JSON string is invalid with respect to DeliveryReport
   */
  public static DeliveryReport fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, DeliveryReport.class);
  }

  /**
   * Convert an instance of DeliveryReport to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

