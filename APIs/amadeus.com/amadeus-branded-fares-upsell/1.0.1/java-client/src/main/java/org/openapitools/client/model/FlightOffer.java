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
import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.ExtendedPrice;
import org.openapitools.client.model.FareRules;
import org.openapitools.client.model.FlightOfferSource;
import org.openapitools.client.model.Itineraries;
import org.openapitools.client.model.PricingOptions;
import org.openapitools.client.model.TravelerPricing;

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
 * FlightOffer
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:02:43.649656-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class FlightOffer {
  public static final String SERIALIZED_NAME_DISABLE_PRICING = "disablePricing";
  @SerializedName(SERIALIZED_NAME_DISABLE_PRICING)
  private Boolean disablePricing;

  public static final String SERIALIZED_NAME_FARE_RULES = "fareRules";
  @SerializedName(SERIALIZED_NAME_FARE_RULES)
  private FareRules fareRules;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_INSTANT_TICKETING_REQUIRED = "instantTicketingRequired";
  @SerializedName(SERIALIZED_NAME_INSTANT_TICKETING_REQUIRED)
  private Boolean instantTicketingRequired;

  public static final String SERIALIZED_NAME_ITINERARIES = "itineraries";
  @SerializedName(SERIALIZED_NAME_ITINERARIES)
  private List<Itineraries> itineraries = new ArrayList<>();

  public static final String SERIALIZED_NAME_LAST_TICKETING_DATE = "lastTicketingDate";
  @SerializedName(SERIALIZED_NAME_LAST_TICKETING_DATE)
  private String lastTicketingDate;

  public static final String SERIALIZED_NAME_NON_HOMOGENEOUS = "nonHomogeneous";
  @SerializedName(SERIALIZED_NAME_NON_HOMOGENEOUS)
  private Boolean nonHomogeneous;

  public static final String SERIALIZED_NAME_NUMBER_OF_BOOKABLE_SEATS = "numberOfBookableSeats";
  @SerializedName(SERIALIZED_NAME_NUMBER_OF_BOOKABLE_SEATS)
  private BigDecimal numberOfBookableSeats;

  public static final String SERIALIZED_NAME_ONE_WAY = "oneWay";
  @SerializedName(SERIALIZED_NAME_ONE_WAY)
  private Boolean oneWay;

  public static final String SERIALIZED_NAME_PAYMENT_CARD_REQUIRED = "paymentCardRequired";
  @SerializedName(SERIALIZED_NAME_PAYMENT_CARD_REQUIRED)
  private Boolean paymentCardRequired;

  public static final String SERIALIZED_NAME_PRICE = "price";
  @SerializedName(SERIALIZED_NAME_PRICE)
  private ExtendedPrice price;

  public static final String SERIALIZED_NAME_PRICING_OPTIONS = "pricingOptions";
  @SerializedName(SERIALIZED_NAME_PRICING_OPTIONS)
  private PricingOptions pricingOptions;

  public static final String SERIALIZED_NAME_SOURCE = "source";
  @SerializedName(SERIALIZED_NAME_SOURCE)
  private FlightOfferSource source;

  public static final String SERIALIZED_NAME_TRAVELER_PRICINGS = "travelerPricings";
  @SerializedName(SERIALIZED_NAME_TRAVELER_PRICINGS)
  private List<TravelerPricing> travelerPricings = new ArrayList<>();

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private String type;

  public static final String SERIALIZED_NAME_VALIDATING_AIRLINE_CODES = "validatingAirlineCodes";
  @SerializedName(SERIALIZED_NAME_VALIDATING_AIRLINE_CODES)
  private List<String> validatingAirlineCodes = new ArrayList<>();

  public FlightOffer() {
  }

  public FlightOffer disablePricing(Boolean disablePricing) {
    this.disablePricing = disablePricing;
    return this;
  }

  /**
   * BOOK step ONLY - If true, allows to book a PNR without pricing. Only for the source \&quot;GDS\&quot;
   * @return disablePricing
   */
  @javax.annotation.Nullable
  public Boolean getDisablePricing() {
    return disablePricing;
  }

  public void setDisablePricing(Boolean disablePricing) {
    this.disablePricing = disablePricing;
  }


  public FlightOffer fareRules(FareRules fareRules) {
    this.fareRules = fareRules;
    return this;
  }

  /**
   * Get fareRules
   * @return fareRules
   */
  @javax.annotation.Nullable
  public FareRules getFareRules() {
    return fareRules;
  }

  public void setFareRules(FareRules fareRules) {
    this.fareRules = fareRules;
  }


  public FlightOffer id(String id) {
    this.id = id;
    return this;
  }

  /**
   * Id of the flight offer
   * @return id
   */
  @javax.annotation.Nonnull
  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }


  public FlightOffer instantTicketingRequired(Boolean instantTicketingRequired) {
    this.instantTicketingRequired = instantTicketingRequired;
    return this;
  }

  /**
   * If true, inform that a ticketing will be required at booking step.
   * @return instantTicketingRequired
   */
  @javax.annotation.Nullable
  public Boolean getInstantTicketingRequired() {
    return instantTicketingRequired;
  }

  public void setInstantTicketingRequired(Boolean instantTicketingRequired) {
    this.instantTicketingRequired = instantTicketingRequired;
  }


  public FlightOffer itineraries(List<Itineraries> itineraries) {
    this.itineraries = itineraries;
    return this;
  }

  public FlightOffer addItinerariesItem(Itineraries itinerariesItem) {
    if (this.itineraries == null) {
      this.itineraries = new ArrayList<>();
    }
    this.itineraries.add(itinerariesItem);
    return this;
  }

  /**
   * Get itineraries
   * @return itineraries
   */
  @javax.annotation.Nullable
  public List<Itineraries> getItineraries() {
    return itineraries;
  }

  public void setItineraries(List<Itineraries> itineraries) {
    this.itineraries = itineraries;
  }


  public FlightOffer lastTicketingDate(String lastTicketingDate) {
    this.lastTicketingDate = lastTicketingDate;
    return this;
  }

  /**
   * If booked on the same day as the search (with respect to timezone), this flight offer is guaranteed to be thereafter valid for ticketing until this date (included). Unspecified when it does not make sense for this flight offer (e.g. no control over ticketing once booked). YYYY-MM-DD format, e.g. 2019-06-07
   * @return lastTicketingDate
   */
  @javax.annotation.Nullable
  public String getLastTicketingDate() {
    return lastTicketingDate;
  }

  public void setLastTicketingDate(String lastTicketingDate) {
    this.lastTicketingDate = lastTicketingDate;
  }


  public FlightOffer nonHomogeneous(Boolean nonHomogeneous) {
    this.nonHomogeneous = nonHomogeneous;
    return this;
  }

  /**
   * If true, upon completion of the booking, this pricing solution is expected to yield multiple records (a record contains booking information confirmed and stored, typically a Passenger Name Record (PNR), in the provider GDS or system)
   * @return nonHomogeneous
   */
  @javax.annotation.Nullable
  public Boolean getNonHomogeneous() {
    return nonHomogeneous;
  }

  public void setNonHomogeneous(Boolean nonHomogeneous) {
    this.nonHomogeneous = nonHomogeneous;
  }


  public FlightOffer numberOfBookableSeats(BigDecimal numberOfBookableSeats) {
    this.numberOfBookableSeats = numberOfBookableSeats;
    return this;
  }

  /**
   * Number of seats bookable in a single request. Can not be higher than 9.
   * minimum: 1
   * maximum: 9
   * @return numberOfBookableSeats
   */
  @javax.annotation.Nullable
  public BigDecimal getNumberOfBookableSeats() {
    return numberOfBookableSeats;
  }

  public void setNumberOfBookableSeats(BigDecimal numberOfBookableSeats) {
    this.numberOfBookableSeats = numberOfBookableSeats;
  }


  public FlightOffer oneWay(Boolean oneWay) {
    this.oneWay = oneWay;
    return this;
  }

  /**
   * If true, the flight offer fulfills only one originDestination and has to be combined with other oneWays to complete the whole journey.
   * @return oneWay
   */
  @javax.annotation.Nullable
  public Boolean getOneWay() {
    return oneWay;
  }

  public void setOneWay(Boolean oneWay) {
    this.oneWay = oneWay;
  }


  public FlightOffer paymentCardRequired(Boolean paymentCardRequired) {
    this.paymentCardRequired = paymentCardRequired;
    return this;
  }

  /**
   * If true, a payment card is mandatory to book this flight offer
   * @return paymentCardRequired
   */
  @javax.annotation.Nullable
  public Boolean getPaymentCardRequired() {
    return paymentCardRequired;
  }

  public void setPaymentCardRequired(Boolean paymentCardRequired) {
    this.paymentCardRequired = paymentCardRequired;
  }


  public FlightOffer price(ExtendedPrice price) {
    this.price = price;
    return this;
  }

  /**
   * Get price
   * @return price
   */
  @javax.annotation.Nullable
  public ExtendedPrice getPrice() {
    return price;
  }

  public void setPrice(ExtendedPrice price) {
    this.price = price;
  }


  public FlightOffer pricingOptions(PricingOptions pricingOptions) {
    this.pricingOptions = pricingOptions;
    return this;
  }

  /**
   * Get pricingOptions
   * @return pricingOptions
   */
  @javax.annotation.Nullable
  public PricingOptions getPricingOptions() {
    return pricingOptions;
  }

  public void setPricingOptions(PricingOptions pricingOptions) {
    this.pricingOptions = pricingOptions;
  }


  public FlightOffer source(FlightOfferSource source) {
    this.source = source;
    return this;
  }

  /**
   * Get source
   * @return source
   */
  @javax.annotation.Nullable
  public FlightOfferSource getSource() {
    return source;
  }

  public void setSource(FlightOfferSource source) {
    this.source = source;
  }


  public FlightOffer travelerPricings(List<TravelerPricing> travelerPricings) {
    this.travelerPricings = travelerPricings;
    return this;
  }

  public FlightOffer addTravelerPricingsItem(TravelerPricing travelerPricingsItem) {
    if (this.travelerPricings == null) {
      this.travelerPricings = new ArrayList<>();
    }
    this.travelerPricings.add(travelerPricingsItem);
    return this;
  }

  /**
   * Fare information for each traveler/segment
   * @return travelerPricings
   */
  @javax.annotation.Nullable
  public List<TravelerPricing> getTravelerPricings() {
    return travelerPricings;
  }

  public void setTravelerPricings(List<TravelerPricing> travelerPricings) {
    this.travelerPricings = travelerPricings;
  }


  public FlightOffer type(String type) {
    this.type = type;
    return this;
  }

  /**
   * the resource name
   * @return type
   */
  @javax.annotation.Nonnull
  public String getType() {
    return type;
  }

  public void setType(String type) {
    this.type = type;
  }


  public FlightOffer validatingAirlineCodes(List<String> validatingAirlineCodes) {
    this.validatingAirlineCodes = validatingAirlineCodes;
    return this;
  }

  public FlightOffer addValidatingAirlineCodesItem(String validatingAirlineCodesItem) {
    if (this.validatingAirlineCodes == null) {
      this.validatingAirlineCodes = new ArrayList<>();
    }
    this.validatingAirlineCodes.add(validatingAirlineCodesItem);
    return this;
  }

  /**
   * This option ensures that the system will only consider these airlines.
   * @return validatingAirlineCodes
   */
  @javax.annotation.Nullable
  public List<String> getValidatingAirlineCodes() {
    return validatingAirlineCodes;
  }

  public void setValidatingAirlineCodes(List<String> validatingAirlineCodes) {
    this.validatingAirlineCodes = validatingAirlineCodes;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    FlightOffer flightOffer = (FlightOffer) o;
    return Objects.equals(this.disablePricing, flightOffer.disablePricing) &&
        Objects.equals(this.fareRules, flightOffer.fareRules) &&
        Objects.equals(this.id, flightOffer.id) &&
        Objects.equals(this.instantTicketingRequired, flightOffer.instantTicketingRequired) &&
        Objects.equals(this.itineraries, flightOffer.itineraries) &&
        Objects.equals(this.lastTicketingDate, flightOffer.lastTicketingDate) &&
        Objects.equals(this.nonHomogeneous, flightOffer.nonHomogeneous) &&
        Objects.equals(this.numberOfBookableSeats, flightOffer.numberOfBookableSeats) &&
        Objects.equals(this.oneWay, flightOffer.oneWay) &&
        Objects.equals(this.paymentCardRequired, flightOffer.paymentCardRequired) &&
        Objects.equals(this.price, flightOffer.price) &&
        Objects.equals(this.pricingOptions, flightOffer.pricingOptions) &&
        Objects.equals(this.source, flightOffer.source) &&
        Objects.equals(this.travelerPricings, flightOffer.travelerPricings) &&
        Objects.equals(this.type, flightOffer.type) &&
        Objects.equals(this.validatingAirlineCodes, flightOffer.validatingAirlineCodes);
  }

  @Override
  public int hashCode() {
    return Objects.hash(disablePricing, fareRules, id, instantTicketingRequired, itineraries, lastTicketingDate, nonHomogeneous, numberOfBookableSeats, oneWay, paymentCardRequired, price, pricingOptions, source, travelerPricings, type, validatingAirlineCodes);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class FlightOffer {\n");
    sb.append("    disablePricing: ").append(toIndentedString(disablePricing)).append("\n");
    sb.append("    fareRules: ").append(toIndentedString(fareRules)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    instantTicketingRequired: ").append(toIndentedString(instantTicketingRequired)).append("\n");
    sb.append("    itineraries: ").append(toIndentedString(itineraries)).append("\n");
    sb.append("    lastTicketingDate: ").append(toIndentedString(lastTicketingDate)).append("\n");
    sb.append("    nonHomogeneous: ").append(toIndentedString(nonHomogeneous)).append("\n");
    sb.append("    numberOfBookableSeats: ").append(toIndentedString(numberOfBookableSeats)).append("\n");
    sb.append("    oneWay: ").append(toIndentedString(oneWay)).append("\n");
    sb.append("    paymentCardRequired: ").append(toIndentedString(paymentCardRequired)).append("\n");
    sb.append("    price: ").append(toIndentedString(price)).append("\n");
    sb.append("    pricingOptions: ").append(toIndentedString(pricingOptions)).append("\n");
    sb.append("    source: ").append(toIndentedString(source)).append("\n");
    sb.append("    travelerPricings: ").append(toIndentedString(travelerPricings)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
    sb.append("    validatingAirlineCodes: ").append(toIndentedString(validatingAirlineCodes)).append("\n");
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
    openapiFields.add("disablePricing");
    openapiFields.add("fareRules");
    openapiFields.add("id");
    openapiFields.add("instantTicketingRequired");
    openapiFields.add("itineraries");
    openapiFields.add("lastTicketingDate");
    openapiFields.add("nonHomogeneous");
    openapiFields.add("numberOfBookableSeats");
    openapiFields.add("oneWay");
    openapiFields.add("paymentCardRequired");
    openapiFields.add("price");
    openapiFields.add("pricingOptions");
    openapiFields.add("source");
    openapiFields.add("travelerPricings");
    openapiFields.add("type");
    openapiFields.add("validatingAirlineCodes");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("id");
    openapiRequiredFields.add("type");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to FlightOffer
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!FlightOffer.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in FlightOffer is not found in the empty JSON string", FlightOffer.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!FlightOffer.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `FlightOffer` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : FlightOffer.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `fareRules`
      if (jsonObj.get("fareRules") != null && !jsonObj.get("fareRules").isJsonNull()) {
        FareRules.validateJsonElement(jsonObj.get("fareRules"));
      }
      if (!jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if (jsonObj.get("itineraries") != null && !jsonObj.get("itineraries").isJsonNull()) {
        JsonArray jsonArrayitineraries = jsonObj.getAsJsonArray("itineraries");
        if (jsonArrayitineraries != null) {
          // ensure the json data is an array
          if (!jsonObj.get("itineraries").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `itineraries` to be an array in the JSON string but got `%s`", jsonObj.get("itineraries").toString()));
          }

          // validate the optional field `itineraries` (array)
          for (int i = 0; i < jsonArrayitineraries.size(); i++) {
            Itineraries.validateJsonElement(jsonArrayitineraries.get(i));
          };
        }
      }
      if ((jsonObj.get("lastTicketingDate") != null && !jsonObj.get("lastTicketingDate").isJsonNull()) && !jsonObj.get("lastTicketingDate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `lastTicketingDate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("lastTicketingDate").toString()));
      }
      // validate the optional field `price`
      if (jsonObj.get("price") != null && !jsonObj.get("price").isJsonNull()) {
        ExtendedPrice.validateJsonElement(jsonObj.get("price"));
      }
      // validate the optional field `pricingOptions`
      if (jsonObj.get("pricingOptions") != null && !jsonObj.get("pricingOptions").isJsonNull()) {
        PricingOptions.validateJsonElement(jsonObj.get("pricingOptions"));
      }
      // validate the optional field `source`
      if (jsonObj.get("source") != null && !jsonObj.get("source").isJsonNull()) {
        FlightOfferSource.validateJsonElement(jsonObj.get("source"));
      }
      if (jsonObj.get("travelerPricings") != null && !jsonObj.get("travelerPricings").isJsonNull()) {
        JsonArray jsonArraytravelerPricings = jsonObj.getAsJsonArray("travelerPricings");
        if (jsonArraytravelerPricings != null) {
          // ensure the json data is an array
          if (!jsonObj.get("travelerPricings").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `travelerPricings` to be an array in the JSON string but got `%s`", jsonObj.get("travelerPricings").toString()));
          }

          // validate the optional field `travelerPricings` (array)
          for (int i = 0; i < jsonArraytravelerPricings.size(); i++) {
            TravelerPricing.validateJsonElement(jsonArraytravelerPricings.get(i));
          };
        }
      }
      if (!jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("validatingAirlineCodes") != null && !jsonObj.get("validatingAirlineCodes").isJsonNull() && !jsonObj.get("validatingAirlineCodes").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `validatingAirlineCodes` to be an array in the JSON string but got `%s`", jsonObj.get("validatingAirlineCodes").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!FlightOffer.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'FlightOffer' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<FlightOffer> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(FlightOffer.class));

       return (TypeAdapter<T>) new TypeAdapter<FlightOffer>() {
           @Override
           public void write(JsonWriter out, FlightOffer value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public FlightOffer read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of FlightOffer given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of FlightOffer
   * @throws IOException if the JSON string is invalid with respect to FlightOffer
   */
  public static FlightOffer fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, FlightOffer.class);
  }

  /**
   * Convert an instance of FlightOffer to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

