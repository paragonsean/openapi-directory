/*
 * Fire Financial Services Business API
 * The fire.com API allows you to deeply integrate Business Account features into your application or back-office systems.  The API provides read access to your profile, accounts and transactions, event-driven notifications of activity on the account and payment initiation via batches. Each feature has its own HTTP endpoint and every endpoint has its own permission.   The API exposes 3 main areas of functionality: financial functions, service information and service configuration. ## Financial Functions These functions provide access to your account details, transactions, payee accounts, payment initiation etc. ## Service Functions These provide information about the fees and limits applied to your account. ## Service configuration These provide information about your service configs - applications, webhooks, API tokens, etc. 
 *
 * The version of the OpenAPI document: 1.0
 * Contact: api@fire.com
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
 * Details of the card used (if applicable)
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:07.131817-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class RelatedCard {
  public static final String SERIALIZED_NAME_ALIAS = "alias";
  @SerializedName(SERIALIZED_NAME_ALIAS)
  private String alias;

  public static final String SERIALIZED_NAME_CARD_ID = "cardId";
  @SerializedName(SERIALIZED_NAME_CARD_ID)
  private Long cardId;

  public static final String SERIALIZED_NAME_EMBOSS_BUSINESS_NAME = "embossBusinessName";
  @SerializedName(SERIALIZED_NAME_EMBOSS_BUSINESS_NAME)
  private String embossBusinessName;

  public static final String SERIALIZED_NAME_EMBOSS_CARD_NAME = "embossCardName";
  @SerializedName(SERIALIZED_NAME_EMBOSS_CARD_NAME)
  private String embossCardName;

  public static final String SERIALIZED_NAME_EXPIRY_DATE = "expiryDate";
  @SerializedName(SERIALIZED_NAME_EXPIRY_DATE)
  private OffsetDateTime expiryDate;

  public static final String SERIALIZED_NAME_MASKED_PAN = "maskedPan";
  @SerializedName(SERIALIZED_NAME_MASKED_PAN)
  private String maskedPan;

  public static final String SERIALIZED_NAME_PROVIDER = "provider";
  @SerializedName(SERIALIZED_NAME_PROVIDER)
  private String provider;

  public RelatedCard() {
  }

  public RelatedCard alias(String alias) {
    this.alias = alias;
    return this;
  }

  /**
   * Get alias
   * @return alias
   */
  @javax.annotation.Nullable
  public String getAlias() {
    return alias;
  }

  public void setAlias(String alias) {
    this.alias = alias;
  }


  public RelatedCard cardId(Long cardId) {
    this.cardId = cardId;
    return this;
  }

  /**
   * Get cardId
   * @return cardId
   */
  @javax.annotation.Nullable
  public Long getCardId() {
    return cardId;
  }

  public void setCardId(Long cardId) {
    this.cardId = cardId;
  }


  public RelatedCard embossBusinessName(String embossBusinessName) {
    this.embossBusinessName = embossBusinessName;
    return this;
  }

  /**
   * Get embossBusinessName
   * @return embossBusinessName
   */
  @javax.annotation.Nullable
  public String getEmbossBusinessName() {
    return embossBusinessName;
  }

  public void setEmbossBusinessName(String embossBusinessName) {
    this.embossBusinessName = embossBusinessName;
  }


  public RelatedCard embossCardName(String embossCardName) {
    this.embossCardName = embossCardName;
    return this;
  }

  /**
   * Get embossCardName
   * @return embossCardName
   */
  @javax.annotation.Nullable
  public String getEmbossCardName() {
    return embossCardName;
  }

  public void setEmbossCardName(String embossCardName) {
    this.embossCardName = embossCardName;
  }


  public RelatedCard expiryDate(OffsetDateTime expiryDate) {
    this.expiryDate = expiryDate;
    return this;
  }

  /**
   * Get expiryDate
   * @return expiryDate
   */
  @javax.annotation.Nullable
  public OffsetDateTime getExpiryDate() {
    return expiryDate;
  }

  public void setExpiryDate(OffsetDateTime expiryDate) {
    this.expiryDate = expiryDate;
  }


  public RelatedCard maskedPan(String maskedPan) {
    this.maskedPan = maskedPan;
    return this;
  }

  /**
   * Get maskedPan
   * @return maskedPan
   */
  @javax.annotation.Nullable
  public String getMaskedPan() {
    return maskedPan;
  }

  public void setMaskedPan(String maskedPan) {
    this.maskedPan = maskedPan;
  }


  public RelatedCard provider(String provider) {
    this.provider = provider;
    return this;
  }

  /**
   * Get provider
   * @return provider
   */
  @javax.annotation.Nullable
  public String getProvider() {
    return provider;
  }

  public void setProvider(String provider) {
    this.provider = provider;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    RelatedCard relatedCard = (RelatedCard) o;
    return Objects.equals(this.alias, relatedCard.alias) &&
        Objects.equals(this.cardId, relatedCard.cardId) &&
        Objects.equals(this.embossBusinessName, relatedCard.embossBusinessName) &&
        Objects.equals(this.embossCardName, relatedCard.embossCardName) &&
        Objects.equals(this.expiryDate, relatedCard.expiryDate) &&
        Objects.equals(this.maskedPan, relatedCard.maskedPan) &&
        Objects.equals(this.provider, relatedCard.provider);
  }

  @Override
  public int hashCode() {
    return Objects.hash(alias, cardId, embossBusinessName, embossCardName, expiryDate, maskedPan, provider);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class RelatedCard {\n");
    sb.append("    alias: ").append(toIndentedString(alias)).append("\n");
    sb.append("    cardId: ").append(toIndentedString(cardId)).append("\n");
    sb.append("    embossBusinessName: ").append(toIndentedString(embossBusinessName)).append("\n");
    sb.append("    embossCardName: ").append(toIndentedString(embossCardName)).append("\n");
    sb.append("    expiryDate: ").append(toIndentedString(expiryDate)).append("\n");
    sb.append("    maskedPan: ").append(toIndentedString(maskedPan)).append("\n");
    sb.append("    provider: ").append(toIndentedString(provider)).append("\n");
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
    openapiFields.add("alias");
    openapiFields.add("cardId");
    openapiFields.add("embossBusinessName");
    openapiFields.add("embossCardName");
    openapiFields.add("expiryDate");
    openapiFields.add("maskedPan");
    openapiFields.add("provider");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to RelatedCard
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!RelatedCard.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in RelatedCard is not found in the empty JSON string", RelatedCard.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!RelatedCard.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `RelatedCard` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("alias") != null && !jsonObj.get("alias").isJsonNull()) && !jsonObj.get("alias").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `alias` to be a primitive type in the JSON string but got `%s`", jsonObj.get("alias").toString()));
      }
      if ((jsonObj.get("embossBusinessName") != null && !jsonObj.get("embossBusinessName").isJsonNull()) && !jsonObj.get("embossBusinessName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `embossBusinessName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("embossBusinessName").toString()));
      }
      if ((jsonObj.get("embossCardName") != null && !jsonObj.get("embossCardName").isJsonNull()) && !jsonObj.get("embossCardName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `embossCardName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("embossCardName").toString()));
      }
      if ((jsonObj.get("maskedPan") != null && !jsonObj.get("maskedPan").isJsonNull()) && !jsonObj.get("maskedPan").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `maskedPan` to be a primitive type in the JSON string but got `%s`", jsonObj.get("maskedPan").toString()));
      }
      if ((jsonObj.get("provider") != null && !jsonObj.get("provider").isJsonNull()) && !jsonObj.get("provider").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `provider` to be a primitive type in the JSON string but got `%s`", jsonObj.get("provider").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!RelatedCard.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'RelatedCard' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<RelatedCard> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(RelatedCard.class));

       return (TypeAdapter<T>) new TypeAdapter<RelatedCard>() {
           @Override
           public void write(JsonWriter out, RelatedCard value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public RelatedCard read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of RelatedCard given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of RelatedCard
   * @throws IOException if the JSON string is invalid with respect to RelatedCard
   */
  public static RelatedCard fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, RelatedCard.class);
  }

  /**
   * Convert an instance of RelatedCard to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

