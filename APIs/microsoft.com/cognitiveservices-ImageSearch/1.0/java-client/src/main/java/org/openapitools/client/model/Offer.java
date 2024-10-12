/*
 * Image Search Client
 * The Image Search API lets you send a search query to Bing and get back a list of relevant images. This section provides technical details about the query parameters and headers that you use to request images and the JSON response objects that contain them. For examples that show how to make requests, see [Searching the Web for Images](https://docs.microsoft.com/azure/cognitive-services/bing-image-search/search-the-web).
 *
 * The version of the OpenAPI document: 1.0
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
import org.openapitools.client.model.AggregateRating;
import org.openapitools.client.model.ImageObject;
import org.openapitools.client.model.Organization;
import org.openapitools.client.model.Thing;

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
 * Defines a merchant&#39;s offer.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:10:59.700770-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Offer extends Thing {
  public static final String SERIALIZED_NAME_AGGREGATE_RATING = "aggregateRating";
  @SerializedName(SERIALIZED_NAME_AGGREGATE_RATING)
  private AggregateRating aggregateRating;

  /**
   * The item&#39;s availability. The following are the possible values: Discontinued, InStock, InStoreOnly, LimitedAvailability, OnlineOnly, OutOfStock, PreOrder, SoldOut
   */
  @JsonAdapter(AvailabilityEnum.Adapter.class)
  public enum AvailabilityEnum {
    DISCONTINUED("Discontinued"),
    
    IN_STOCK("InStock"),
    
    IN_STORE_ONLY("InStoreOnly"),
    
    LIMITED_AVAILABILITY("LimitedAvailability"),
    
    ONLINE_ONLY("OnlineOnly"),
    
    OUT_OF_STOCK("OutOfStock"),
    
    PRE_ORDER("PreOrder"),
    
    SOLD_OUT("SoldOut");

    private String value;

    AvailabilityEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static AvailabilityEnum fromValue(String value) {
      for (AvailabilityEnum b : AvailabilityEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<AvailabilityEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final AvailabilityEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public AvailabilityEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return AvailabilityEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      AvailabilityEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_AVAILABILITY = "availability";
  @SerializedName(SERIALIZED_NAME_AVAILABILITY)
  private AvailabilityEnum availability;

  public static final String SERIALIZED_NAME_LAST_UPDATED = "lastUpdated";
  @SerializedName(SERIALIZED_NAME_LAST_UPDATED)
  private String lastUpdated;

  public static final String SERIALIZED_NAME_PRICE = "price";
  @SerializedName(SERIALIZED_NAME_PRICE)
  private Float price;

  /**
   * The monetary currency. For example, USD.
   */
  @JsonAdapter(PriceCurrencyEnum.Adapter.class)
  public enum PriceCurrencyEnum {
    USD("USD"),
    
    CAD("CAD"),
    
    GBP("GBP"),
    
    EUR("EUR"),
    
    COP("COP"),
    
    JPY("JPY"),
    
    CNY("CNY"),
    
    AUD("AUD"),
    
    INR("INR"),
    
    AED("AED"),
    
    AFN("AFN"),
    
    ALL("ALL"),
    
    AMD("AMD"),
    
    ANG("ANG"),
    
    AOA("AOA"),
    
    ARS("ARS"),
    
    AWG("AWG"),
    
    AZN("AZN"),
    
    BAM("BAM"),
    
    BBD("BBD"),
    
    BDT("BDT"),
    
    BGN("BGN"),
    
    BHD("BHD"),
    
    BIF("BIF"),
    
    BMD("BMD"),
    
    BND("BND"),
    
    BOB("BOB"),
    
    BOV("BOV"),
    
    BRL("BRL"),
    
    BSD("BSD"),
    
    BTN("BTN"),
    
    BWP("BWP"),
    
    BYR("BYR"),
    
    BZD("BZD"),
    
    CDF("CDF"),
    
    CHE("CHE"),
    
    CHF("CHF"),
    
    CHW("CHW"),
    
    CLF("CLF"),
    
    CLP("CLP"),
    
    COU("COU"),
    
    CRC("CRC"),
    
    CUC("CUC"),
    
    CUP("CUP"),
    
    CVE("CVE"),
    
    CZK("CZK"),
    
    DJF("DJF"),
    
    DKK("DKK"),
    
    DOP("DOP"),
    
    DZD("DZD"),
    
    EGP("EGP"),
    
    ERN("ERN"),
    
    ETB("ETB"),
    
    FJD("FJD"),
    
    FKP("FKP"),
    
    GEL("GEL"),
    
    GHS("GHS"),
    
    GIP("GIP"),
    
    GMD("GMD"),
    
    GNF("GNF"),
    
    GTQ("GTQ"),
    
    GYD("GYD"),
    
    HKD("HKD"),
    
    HNL("HNL"),
    
    HRK("HRK"),
    
    HTG("HTG"),
    
    HUF("HUF"),
    
    IDR("IDR"),
    
    ILS("ILS"),
    
    IQD("IQD"),
    
    IRR("IRR"),
    
    ISK("ISK"),
    
    JMD("JMD"),
    
    JOD("JOD"),
    
    KES("KES"),
    
    KGS("KGS"),
    
    KHR("KHR"),
    
    KMF("KMF"),
    
    KPW("KPW"),
    
    KRW("KRW"),
    
    KWD("KWD"),
    
    KYD("KYD"),
    
    KZT("KZT"),
    
    LAK("LAK"),
    
    LBP("LBP"),
    
    LKR("LKR"),
    
    LRD("LRD"),
    
    LSL("LSL"),
    
    LYD("LYD"),
    
    MAD("MAD"),
    
    MDL("MDL"),
    
    MGA("MGA"),
    
    MKD("MKD"),
    
    MMK("MMK"),
    
    MNT("MNT"),
    
    MOP("MOP"),
    
    MRO("MRO"),
    
    MUR("MUR"),
    
    MVR("MVR"),
    
    MWK("MWK"),
    
    MXN("MXN"),
    
    MXV("MXV"),
    
    MYR("MYR"),
    
    MZN("MZN"),
    
    NAD("NAD"),
    
    NGN("NGN"),
    
    NIO("NIO"),
    
    NOK("NOK"),
    
    NPR("NPR"),
    
    NZD("NZD"),
    
    OMR("OMR"),
    
    PAB("PAB"),
    
    PEN("PEN"),
    
    PGK("PGK"),
    
    PHP("PHP"),
    
    PKR("PKR"),
    
    PLN("PLN"),
    
    PYG("PYG"),
    
    QAR("QAR"),
    
    RON("RON"),
    
    RSD("RSD"),
    
    RUB("RUB"),
    
    RWF("RWF"),
    
    SAR("SAR"),
    
    SBD("SBD"),
    
    SCR("SCR"),
    
    SDG("SDG"),
    
    SEK("SEK"),
    
    SGD("SGD"),
    
    SHP("SHP"),
    
    SLL("SLL"),
    
    SOS("SOS"),
    
    SRD("SRD"),
    
    SSP("SSP"),
    
    STD("STD"),
    
    SYP("SYP"),
    
    SZL("SZL"),
    
    THB("THB"),
    
    TJS("TJS"),
    
    TMT("TMT"),
    
    TND("TND"),
    
    TOP("TOP"),
    
    TRY("TRY"),
    
    TTD("TTD"),
    
    TWD("TWD"),
    
    TZS("TZS"),
    
    UAH("UAH"),
    
    UGX("UGX"),
    
    UYU("UYU"),
    
    UZS("UZS"),
    
    VEF("VEF"),
    
    VND("VND"),
    
    VUV("VUV"),
    
    WST("WST"),
    
    XAF("XAF"),
    
    XCD("XCD"),
    
    XOF("XOF"),
    
    XPF("XPF"),
    
    YER("YER"),
    
    ZAR("ZAR"),
    
    ZMW("ZMW");

    private String value;

    PriceCurrencyEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static PriceCurrencyEnum fromValue(String value) {
      for (PriceCurrencyEnum b : PriceCurrencyEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<PriceCurrencyEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final PriceCurrencyEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public PriceCurrencyEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return PriceCurrencyEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      PriceCurrencyEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_PRICE_CURRENCY = "priceCurrency";
  @SerializedName(SERIALIZED_NAME_PRICE_CURRENCY)
  private PriceCurrencyEnum priceCurrency = PriceCurrencyEnum.USD;

  public static final String SERIALIZED_NAME_SELLER = "seller";
  @SerializedName(SERIALIZED_NAME_SELLER)
  private Organization seller;

  public Offer() {
    this.type = this.getClass().getSimpleName();
  }

  public Offer(
     AvailabilityEnum availability, 
     String lastUpdated, 
     Float price, 
     PriceCurrencyEnum priceCurrency, 
     String alternateName, 
     String bingId, 
     String description, 
     String name, 
     String url, 
     String readLink, 
     String webSearchUrl, 
     String id
  ) {
    this();
    this.availability = availability;
    this.lastUpdated = lastUpdated;
    this.price = price;
    this.priceCurrency = priceCurrency;
    this.alternateName = alternateName;
    this.bingId = bingId;
    this.description = description;
    this.name = name;
    this.url = url;
    this.readLink = readLink;
    this.webSearchUrl = webSearchUrl;
    this.id = id;
  }

  public Offer aggregateRating(AggregateRating aggregateRating) {
    this.aggregateRating = aggregateRating;
    return this;
  }

  /**
   * Get aggregateRating
   * @return aggregateRating
   */
  @javax.annotation.Nullable
  public AggregateRating getAggregateRating() {
    return aggregateRating;
  }

  public void setAggregateRating(AggregateRating aggregateRating) {
    this.aggregateRating = aggregateRating;
  }


  /**
   * The item&#39;s availability. The following are the possible values: Discontinued, InStock, InStoreOnly, LimitedAvailability, OnlineOnly, OutOfStock, PreOrder, SoldOut
   * @return availability
   */
  @javax.annotation.Nullable
  public AvailabilityEnum getAvailability() {
    return availability;
  }



  /**
   * The last date that the offer was updated. The date is in the form YYYY-MM-DD.
   * @return lastUpdated
   */
  @javax.annotation.Nullable
  public String getLastUpdated() {
    return lastUpdated;
  }



  /**
   * The item&#39;s price.
   * @return price
   */
  @javax.annotation.Nullable
  public Float getPrice() {
    return price;
  }



  /**
   * The monetary currency. For example, USD.
   * @return priceCurrency
   */
  @javax.annotation.Nullable
  public PriceCurrencyEnum getPriceCurrency() {
    return priceCurrency;
  }



  public Offer seller(Organization seller) {
    this.seller = seller;
    return this;
  }

  /**
   * Get seller
   * @return seller
   */
  @javax.annotation.Nullable
  public Organization getSeller() {
    return seller;
  }

  public void setSeller(Organization seller) {
    this.seller = seller;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Offer offer = (Offer) o;
    return Objects.equals(this.aggregateRating, offer.aggregateRating) &&
        Objects.equals(this.availability, offer.availability) &&
        Objects.equals(this.lastUpdated, offer.lastUpdated) &&
        Objects.equals(this.price, offer.price) &&
        Objects.equals(this.priceCurrency, offer.priceCurrency) &&
        Objects.equals(this.seller, offer.seller) &&
        super.equals(o);
  }

  @Override
  public int hashCode() {
    return Objects.hash(aggregateRating, availability, lastUpdated, price, priceCurrency, seller, super.hashCode());
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Offer {\n");
    sb.append("    ").append(toIndentedString(super.toString())).append("\n");
    sb.append("    aggregateRating: ").append(toIndentedString(aggregateRating)).append("\n");
    sb.append("    availability: ").append(toIndentedString(availability)).append("\n");
    sb.append("    lastUpdated: ").append(toIndentedString(lastUpdated)).append("\n");
    sb.append("    price: ").append(toIndentedString(price)).append("\n");
    sb.append("    priceCurrency: ").append(toIndentedString(priceCurrency)).append("\n");
    sb.append("    seller: ").append(toIndentedString(seller)).append("\n");
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
    openapiFields.add("alternateName");
    openapiFields.add("bingId");
    openapiFields.add("description");
    openapiFields.add("image");
    openapiFields.add("name");
    openapiFields.add("url");
    openapiFields.add("readLink");
    openapiFields.add("webSearchUrl");
    openapiFields.add("id");
    openapiFields.add("_type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("_type");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Offer
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Offer.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Offer is not found in the empty JSON string", Offer.openapiRequiredFields.toString()));
        }
      }

      String discriminatorValue = jsonElement.getAsJsonObject().get("_type").getAsString();
      switch (discriminatorValue) {
        case "AggregateOffer":
          AggregateOffer.validateJsonElement(jsonElement);
          break;
        default:
          throw new IllegalArgumentException(String.format("The value of the `_type` field `%s` does not match any key defined in the discriminator's mapping.", discriminatorValue));
      }
  }


  /**
   * Create an instance of Offer given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Offer
   * @throws IOException if the JSON string is invalid with respect to Offer
   */
  public static Offer fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Offer.class);
  }

  /**
   * Convert an instance of Offer to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

