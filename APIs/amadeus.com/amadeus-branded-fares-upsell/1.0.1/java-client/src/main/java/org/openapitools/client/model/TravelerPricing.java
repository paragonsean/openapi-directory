/*
 * Branded Fares Upsell
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.0.1
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
import org.openapitools.client.model.FareDetailsBySegment;
import org.openapitools.client.model.Price;
import org.openapitools.client.model.TravelerPricingFareOption;
import org.openapitools.client.model.TravelerType;

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
 * TravelerPricing
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:02:43.649656-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class TravelerPricing {
  public static final String SERIALIZED_NAME_ASSOCIATED_ADULT_ID = "associatedAdultId";
  @SerializedName(SERIALIZED_NAME_ASSOCIATED_ADULT_ID)
  private String associatedAdultId;

  public static final String SERIALIZED_NAME_FARE_DETAILS_BY_SEGMENT = "fareDetailsBySegment";
  @SerializedName(SERIALIZED_NAME_FARE_DETAILS_BY_SEGMENT)
  private List<FareDetailsBySegment> fareDetailsBySegment = new ArrayList<>();

  public static final String SERIALIZED_NAME_FARE_OPTION = "fareOption";
  @SerializedName(SERIALIZED_NAME_FARE_OPTION)
  private TravelerPricingFareOption fareOption;

  public static final String SERIALIZED_NAME_PRICE = "price";
  @SerializedName(SERIALIZED_NAME_PRICE)
  private Price price;

  public static final String SERIALIZED_NAME_TRAVELER_ID = "travelerId";
  @SerializedName(SERIALIZED_NAME_TRAVELER_ID)
  private String travelerId;

  public static final String SERIALIZED_NAME_TRAVELER_TYPE = "travelerType";
  @SerializedName(SERIALIZED_NAME_TRAVELER_TYPE)
  private TravelerType travelerType;

  public TravelerPricing() {
  }

  public TravelerPricing associatedAdultId(String associatedAdultId) {
    this.associatedAdultId = associatedAdultId;
    return this;
  }

  /**
   * if type&#x3D;\&quot;HELD_INFANT\&quot;, corresponds to the adult traveler&#39;s id who will share the seat
   * @return associatedAdultId
   */
  @javax.annotation.Nullable
  public String getAssociatedAdultId() {
    return associatedAdultId;
  }

  public void setAssociatedAdultId(String associatedAdultId) {
    this.associatedAdultId = associatedAdultId;
  }


  public TravelerPricing fareDetailsBySegment(List<FareDetailsBySegment> fareDetailsBySegment) {
    this.fareDetailsBySegment = fareDetailsBySegment;
    return this;
  }

  public TravelerPricing addFareDetailsBySegmentItem(FareDetailsBySegment fareDetailsBySegmentItem) {
    if (this.fareDetailsBySegment == null) {
      this.fareDetailsBySegment = new ArrayList<>();
    }
    this.fareDetailsBySegment.add(fareDetailsBySegmentItem);
    return this;
  }

  /**
   * Get fareDetailsBySegment
   * @return fareDetailsBySegment
   */
  @javax.annotation.Nonnull
  public List<FareDetailsBySegment> getFareDetailsBySegment() {
    return fareDetailsBySegment;
  }

  public void setFareDetailsBySegment(List<FareDetailsBySegment> fareDetailsBySegment) {
    this.fareDetailsBySegment = fareDetailsBySegment;
  }


  public TravelerPricing fareOption(TravelerPricingFareOption fareOption) {
    this.fareOption = fareOption;
    return this;
  }

  /**
   * Get fareOption
   * @return fareOption
   */
  @javax.annotation.Nonnull
  public TravelerPricingFareOption getFareOption() {
    return fareOption;
  }

  public void setFareOption(TravelerPricingFareOption fareOption) {
    this.fareOption = fareOption;
  }


  public TravelerPricing price(Price price) {
    this.price = price;
    return this;
  }

  /**
   * Get price
   * @return price
   */
  @javax.annotation.Nullable
  public Price getPrice() {
    return price;
  }

  public void setPrice(Price price) {
    this.price = price;
  }


  public TravelerPricing travelerId(String travelerId) {
    this.travelerId = travelerId;
    return this;
  }

  /**
   * Id of the traveler
   * @return travelerId
   */
  @javax.annotation.Nonnull
  public String getTravelerId() {
    return travelerId;
  }

  public void setTravelerId(String travelerId) {
    this.travelerId = travelerId;
  }


  public TravelerPricing travelerType(TravelerType travelerType) {
    this.travelerType = travelerType;
    return this;
  }

  /**
   * Get travelerType
   * @return travelerType
   */
  @javax.annotation.Nonnull
  public TravelerType getTravelerType() {
    return travelerType;
  }

  public void setTravelerType(TravelerType travelerType) {
    this.travelerType = travelerType;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TravelerPricing travelerPricing = (TravelerPricing) o;
    return Objects.equals(this.associatedAdultId, travelerPricing.associatedAdultId) &&
        Objects.equals(this.fareDetailsBySegment, travelerPricing.fareDetailsBySegment) &&
        Objects.equals(this.fareOption, travelerPricing.fareOption) &&
        Objects.equals(this.price, travelerPricing.price) &&
        Objects.equals(this.travelerId, travelerPricing.travelerId) &&
        Objects.equals(this.travelerType, travelerPricing.travelerType);
  }

  @Override
  public int hashCode() {
    return Objects.hash(associatedAdultId, fareDetailsBySegment, fareOption, price, travelerId, travelerType);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TravelerPricing {\n");
    sb.append("    associatedAdultId: ").append(toIndentedString(associatedAdultId)).append("\n");
    sb.append("    fareDetailsBySegment: ").append(toIndentedString(fareDetailsBySegment)).append("\n");
    sb.append("    fareOption: ").append(toIndentedString(fareOption)).append("\n");
    sb.append("    price: ").append(toIndentedString(price)).append("\n");
    sb.append("    travelerId: ").append(toIndentedString(travelerId)).append("\n");
    sb.append("    travelerType: ").append(toIndentedString(travelerType)).append("\n");
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
    openapiFields.add("associatedAdultId");
    openapiFields.add("fareDetailsBySegment");
    openapiFields.add("fareOption");
    openapiFields.add("price");
    openapiFields.add("travelerId");
    openapiFields.add("travelerType");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("fareDetailsBySegment");
    openapiRequiredFields.add("fareOption");
    openapiRequiredFields.add("travelerId");
    openapiRequiredFields.add("travelerType");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to TravelerPricing
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!TravelerPricing.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in TravelerPricing is not found in the empty JSON string", TravelerPricing.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!TravelerPricing.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TravelerPricing` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : TravelerPricing.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("associatedAdultId") != null && !jsonObj.get("associatedAdultId").isJsonNull()) && !jsonObj.get("associatedAdultId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `associatedAdultId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("associatedAdultId").toString()));
      }
      // ensure the json data is an array
      if (!jsonObj.get("fareDetailsBySegment").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `fareDetailsBySegment` to be an array in the JSON string but got `%s`", jsonObj.get("fareDetailsBySegment").toString()));
      }

      JsonArray jsonArrayfareDetailsBySegment = jsonObj.getAsJsonArray("fareDetailsBySegment");
      // validate the required field `fareDetailsBySegment` (array)
      for (int i = 0; i < jsonArrayfareDetailsBySegment.size(); i++) {
        FareDetailsBySegment.validateJsonElement(jsonArrayfareDetailsBySegment.get(i));
      };
      // validate the required field `fareOption`
      TravelerPricingFareOption.validateJsonElement(jsonObj.get("fareOption"));
      // validate the optional field `price`
      if (jsonObj.get("price") != null && !jsonObj.get("price").isJsonNull()) {
        Price.validateJsonElement(jsonObj.get("price"));
      }
      if (!jsonObj.get("travelerId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `travelerId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("travelerId").toString()));
      }
      // validate the required field `travelerType`
      TravelerType.validateJsonElement(jsonObj.get("travelerType"));
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TravelerPricing.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TravelerPricing' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TravelerPricing> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TravelerPricing.class));

       return (TypeAdapter<T>) new TypeAdapter<TravelerPricing>() {
           @Override
           public void write(JsonWriter out, TravelerPricing value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TravelerPricing read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of TravelerPricing given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of TravelerPricing
   * @throws IOException if the JSON string is invalid with respect to TravelerPricing
   */
  public static TravelerPricing fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TravelerPricing.class);
  }

  /**
   * Convert an instance of TravelerPricing to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

