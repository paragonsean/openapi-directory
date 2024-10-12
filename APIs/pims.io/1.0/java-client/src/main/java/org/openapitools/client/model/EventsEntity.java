/*
 * Pims
 *  Hereafter is the documentation of the private API of [Pims: Pointages Intelligents pour le Monde du Spectacle](https://pims.io). This API is designed for 3rd-party softwares, editors and partners. Its main purpose is to give access the core data of a Pims customer (i.e. events, ticket counts and promotions).  ## Authentication The API uses [basic access authentication](https://en.wikipedia.org/wiki/Basic_access_authentication), meaning you will need a username and password to get authorized.  As each customer in Pims has its own domain (e.g. caramba.pims.io, gdp.pims.io...), each credentials will be valid for one domain/customer only. If you need dedicated credentials for one domain, please contact us. (In any case, we will need an explicit agreement from the customer before we create these credentials.)  <div class=\"info\"> To make your life easy, you can try all endpoints with the public credentials below, pointing to our [demo domain](https://demo.pims.io):   <ul>     <li>Base path: `https://demo.pims.io/api`</li>     <li>Username: `demo`</li>     <li>Password: `q83792db2GCvgYVdKpU3yG3R`</li>   </ul> </div>  ## Response format The API returns JSON and matches the [HAL specification](http://stateless.co/hal_specification.html). The `Content-Type` of each response will be `application/hal+json`, unless an error occurs.  Please note that this documentation describes all responses “as if” they were plain JSON. The specificities of HAL are ignored on purpose, in order to remain compact and avoid repetition. <div style=\"-webkit-column-count: 2; -moz-column-count: 2; column-count: 2; -webkit-column-rule: 1px dotted #e0e0e0; -moz-column-rule: 1px dotted #e0e0e0; column-rule: 1px dotted #e0e0e0;\">  <div style=\"display: inline-block; width:100%;\">   <strong>So when you read in the doc:</strong> <pre><code class=\"lang-json\">{  <span class=\"token string\">\"id\"</span>: <span class=\"token number\">123</span>,  <span class=\"token string\">\"property1\"</span>: <span class=\"token string\">\"Lorem ipsum\"</span>,  <span class=\"token string\">\"object\"</span>: {   <span class=\"token string\">\"id\"</span>: <span class=\"token number\">456</span>,   <span class=\"token string\">\"property2\"</span>: <span class=\"token number\">7.89</span>  } }</code></pre>  </div>  <div style=\"display: inline-block; width:100%;\">   <strong>... you'll get in the Real World®:</strong> <pre><code class=\"lang-json\">{  <span class=\"token string\">\"id\"</span>: <span class=\"token number\">123</span>,  <span class=\"token string\">\"property2\"</span>: <span class=\"token string\">\"Lorem ipsum\"</span>,  <span class=\"token string\">\"_embedded\"</span>: {   <span class=\"token string\">\"object\"</span>: {    <span class=\"token string\">\"id\"</span>: <span class=\"token number\">456</span>,    <span class=\"token string\">\"property2\"</span>: <span class=\"token number\">7.89</span>,    <span class=\"token string\">\"_links\"</span>: {     <span class=\"token string\">\"self\"</span>: {      <span class=\"token string\">\"href\"</span>: <span class=\"token string\">\"https://api.mydomain.com/other-item/456\"</span>     }    }   }  }  <span class=\"token string\">\"_links\"</span>: {   <span class=\"token string\">\"self\"</span>: {    <span class=\"token string\">\"href\"</span>: <span class=\"token string\">\"https://api.mydomain.com/item/123\"</span>   }  } }</code></pre>  </div> </div>  ### Errors Errors return JSON too and tries to match the [Problem Details for HTTP APIs specification](https://tools.ietf.org/html/rfc7807). If it does not match this spec, that's either a bug or a compatibility issue. Please contact us to solve the problem.  The `Content-Type` of errors will be `application/problem+json`. The content will match the following JSON: ```json {  \"type\": \"https://tools.ietf.org/html/rfc2616#section-10\",     \"title\": \"Not Found\",  \"status\": 404,     \"detail\": \"Entity not found\" } ```  ## Versioning The API is fully versionned, using an URL-versioning scheme: `https://demo.pims.io/api/v1/events`, `https://demo.pims.io/api/v2/events`,...  The version part of the URL is optional, and will be completed with the last stable version if omitted.  ## Pagination All responses corresponding to a collection of resources (e.g. `/venues` or `/series/:id/events`) are paginated. When so, you will only get the first 25 resources you asked for.  If you need to get more resources in one call, you can use the `page_size` query parameter. E.g. `/venues?page_size=50` to get the 50 first venues.  Also note that with HAL, the navigation in paginated responses is a piece of cake, as you can see below: ```json {  \"_links\": {   \"self\": {    \"href\": \"https://demo.pims.io/api/v1/events?page=1\"   },   \"first\": {    \"href\": \"https://demo.pims.io/api/v1/events\"   },   \"last\": {    \"href\": \"https://demo.pims.io/api/v1/events?page=14\"   },   \"next\": {    \"href\": \"https://demo.pims.io/api/v1/events?page=2\"   }  },  \"_embedded\": {    ... // data content goes here  },  \"page_count\": 14,  \"page_size\": 25,  \"total_items\": 331,  \"page\": 1 } ```  ## Filtering and sorting Every textual filter (e.g. `/events?label=U2`) and/or sort (e.g. `/events?sort=label`) performed with the API uses UTF8_UNICODE_CI collation, meaning it is: - Case insensitive: “Chloé” will be considered the same as “CHLOÉ”; - Diacritic insensitive: “Chloé” will be considered the same as “Chloe”.  When performing a sort, it will always be *ascending* by default. To make it *descending*, just use a minus sign (`-`) in front of the parameter value (e.g. `/events?sort=-label`).  ## I18n In responses, some labels can be translated (e.g. promotion types, event input types, etc.). These translatable labels are clearly indicated in the documentation below.  By default, they will be displayed in English, but you can change this behaviour via the `Accept-Language` header. E.g., use `fr` as a value for French.  ## PHP SDK We provide a simple yet convenient SDK for the PHP language, see [the Github page of the project](https://github.com/pimssas/pims-api-client-php).  ## And now? Generaly, you will start by [fetching one or more events](#tag/Events). An <span class=\"definition\">event</span> can be anything that occurs in one venue at one given date and time: a concert, a play, a match, a conference, etc. Additionnally, you can explore the [series](#tag/Series): a <span class=\"definition\">series</span> is just a group of events (e.g. a tour or a festival).  Once you retrieved the events you were interested in, you can look for the sales (<span class=\"definition\">ticket counts</span>): - Get a quick overview with [`/events/:id/ticket-counts`](#operation/fetchAllTicketCounts) - Or get a full insight by calling these endpoints:     1. [`/events/:id/categories`](#operation/fetchAllEventsCategories)     2. [`/events/:id/channels`](#operation/fetchAllEventsChannels)     3. [`/events/:id/ticket-counts/detailed`](#operation/fetchAllDetailedTicketCounts)  Eventually, you may also want to fetch the [promotions](#tag/Promotions). A <span class=\"definition\">promotion</span> can be anything meant to leverage the sales: ads, marketing campaigns, buzz or news around the event, etc. A promotion can be linked to any combination of events and/or series.
 *
 * The version of the OpenAPI document: 1.0
 * Contact: support@pims.io
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
import java.time.LocalDate;
import java.util.Arrays;
import org.openapitools.client.model.EventsEntityContract;
import org.openapitools.client.model.EventsEntityInputType;
import org.openapitools.client.model.VenuesEntity;

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
 * EventsEntity
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:12:11.901875-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class EventsEntity {
  public static final String SERIALIZED_NAME_BREAK_EVEN = "break_even";
  @SerializedName(SERIALIZED_NAME_BREAK_EVEN)
  private Integer breakEven;

  public static final String SERIALIZED_NAME_CANCELLATION_DATE = "cancellation_date";
  @SerializedName(SERIALIZED_NAME_CANCELLATION_DATE)
  private LocalDate cancellationDate;

  public static final String SERIALIZED_NAME_CONTRACT = "contract";
  @SerializedName(SERIALIZED_NAME_CONTRACT)
  private EventsEntityContract contract;

  public static final String SERIALIZED_NAME_COSTING_CAPACITY = "costing_capacity";
  @SerializedName(SERIALIZED_NAME_COSTING_CAPACITY)
  private Integer costingCapacity;

  public static final String SERIALIZED_NAME_CREATION_TIMESTAMP = "creation_timestamp";
  @SerializedName(SERIALIZED_NAME_CREATION_TIMESTAMP)
  private Long creationTimestamp;

  public static final String SERIALIZED_NAME_CURRENCY = "currency";
  @SerializedName(SERIALIZED_NAME_CURRENCY)
  private String currency;

  public static final String SERIALIZED_NAME_DATETIME = "datetime";
  @SerializedName(SERIALIZED_NAME_DATETIME)
  private String datetime;

  public static final String SERIALIZED_NAME_FREE = "free";
  @SerializedName(SERIALIZED_NAME_FREE)
  private Boolean free;

  public static final String SERIALIZED_NAME_GENERAL_SALES_DATE = "general_sales_date";
  @SerializedName(SERIALIZED_NAME_GENERAL_SALES_DATE)
  private LocalDate generalSalesDate;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_INPUT_TYPE = "input_type";
  @SerializedName(SERIALIZED_NAME_INPUT_TYPE)
  private EventsEntityInputType inputType;

  public static final String SERIALIZED_NAME_LABEL = "label";
  @SerializedName(SERIALIZED_NAME_LABEL)
  private String label;

  public static final String SERIALIZED_NAME_LAST_UPDATE_TIMESTAMP = "last_update_timestamp";
  @SerializedName(SERIALIZED_NAME_LAST_UPDATE_TIMESTAMP)
  private Long lastUpdateTimestamp;

  public static final String SERIALIZED_NAME_MAX_CAPACITY = "max_capacity";
  @SerializedName(SERIALIZED_NAME_MAX_CAPACITY)
  private Integer maxCapacity;

  public static final String SERIALIZED_NAME_PRESALES_DATE = "presales_date";
  @SerializedName(SERIALIZED_NAME_PRESALES_DATE)
  private LocalDate presalesDate;

  public static final String SERIALIZED_NAME_SERIES_ID = "series_id";
  @SerializedName(SERIALIZED_NAME_SERIES_ID)
  private Integer seriesId;

  public static final String SERIALIZED_NAME_SOLD_OUT_DATE = "sold_out_date";
  @SerializedName(SERIALIZED_NAME_SOLD_OUT_DATE)
  private LocalDate soldOutDate;

  public static final String SERIALIZED_NAME_VENUE = "venue";
  @SerializedName(SERIALIZED_NAME_VENUE)
  private VenuesEntity venue;

  public EventsEntity() {
  }

  public EventsEntity breakEven(Integer breakEven) {
    this.breakEven = breakEven;
    return this;
  }

  /**
   * Value of the break-even for the event.
   * minimum: 0
   * @return breakEven
   */
  @javax.annotation.Nullable
  public Integer getBreakEven() {
    return breakEven;
  }

  public void setBreakEven(Integer breakEven) {
    this.breakEven = breakEven;
  }


  public EventsEntity cancellationDate(LocalDate cancellationDate) {
    this.cancellationDate = cancellationDate;
    return this;
  }

  /**
   * Date the event was canceled.
   * @return cancellationDate
   */
  @javax.annotation.Nullable
  public LocalDate getCancellationDate() {
    return cancellationDate;
  }

  public void setCancellationDate(LocalDate cancellationDate) {
    this.cancellationDate = cancellationDate;
  }


  public EventsEntity contract(EventsEntityContract contract) {
    this.contract = contract;
    return this;
  }

  /**
   * Get contract
   * @return contract
   */
  @javax.annotation.Nonnull
  public EventsEntityContract getContract() {
    return contract;
  }

  public void setContract(EventsEntityContract contract) {
    this.contract = contract;
  }


  public EventsEntity costingCapacity(Integer costingCapacity) {
    this.costingCapacity = costingCapacity;
    return this;
  }

  /**
   * Costing capacity of the event.
   * minimum: 0
   * @return costingCapacity
   */
  @javax.annotation.Nullable
  public Integer getCostingCapacity() {
    return costingCapacity;
  }

  public void setCostingCapacity(Integer costingCapacity) {
    this.costingCapacity = costingCapacity;
  }


  public EventsEntity creationTimestamp(Long creationTimestamp) {
    this.creationTimestamp = creationTimestamp;
    return this;
  }

  /**
   * Timestamp for when the venue was created in the customer&#39;s database.
   * @return creationTimestamp
   */
  @javax.annotation.Nonnull
  public Long getCreationTimestamp() {
    return creationTimestamp;
  }

  public void setCreationTimestamp(Long creationTimestamp) {
    this.creationTimestamp = creationTimestamp;
  }


  public EventsEntity currency(String currency) {
    this.currency = currency;
    return this;
  }

  /**
   * Currency of the prices.
   * @return currency
   */
  @javax.annotation.Nullable
  public String getCurrency() {
    return currency;
  }

  public void setCurrency(String currency) {
    this.currency = currency;
  }


  public EventsEntity datetime(String datetime) {
    this.datetime = datetime;
    return this;
  }

  /**
   * Datetime of the event (relative to the timezone of the venue).
   * @return datetime
   */
  @javax.annotation.Nonnull
  public String getDatetime() {
    return datetime;
  }

  public void setDatetime(String datetime) {
    this.datetime = datetime;
  }


  public EventsEntity free(Boolean free) {
    this.free = free;
    return this;
  }

  /**
   * Whether this event is free or not.
   * @return free
   */
  @javax.annotation.Nonnull
  public Boolean getFree() {
    return free;
  }

  public void setFree(Boolean free) {
    this.free = free;
  }


  public EventsEntity generalSalesDate(LocalDate generalSalesDate) {
    this.generalSalesDate = generalSalesDate;
    return this;
  }

  /**
   * Date the event went on general sales (relative to the timezone of the venue).
   * @return generalSalesDate
   */
  @javax.annotation.Nullable
  public LocalDate getGeneralSalesDate() {
    return generalSalesDate;
  }

  public void setGeneralSalesDate(LocalDate generalSalesDate) {
    this.generalSalesDate = generalSalesDate;
  }


  public EventsEntity id(Integer id) {
    this.id = id;
    return this;
  }

  /**
   * Unique ID of the event.
   * @return id
   */
  @javax.annotation.Nonnull
  public Integer getId() {
    return id;
  }

  public void setId(Integer id) {
    this.id = id;
  }


  public EventsEntity inputType(EventsEntityInputType inputType) {
    this.inputType = inputType;
    return this;
  }

  /**
   * Get inputType
   * @return inputType
   */
  @javax.annotation.Nonnull
  public EventsEntityInputType getInputType() {
    return inputType;
  }

  public void setInputType(EventsEntityInputType inputType) {
    this.inputType = inputType;
  }


  public EventsEntity label(String label) {
    this.label = label;
    return this;
  }

  /**
   * Label of the event.
   * @return label
   */
  @javax.annotation.Nonnull
  public String getLabel() {
    return label;
  }

  public void setLabel(String label) {
    this.label = label;
  }


  public EventsEntity lastUpdateTimestamp(Long lastUpdateTimestamp) {
    this.lastUpdateTimestamp = lastUpdateTimestamp;
    return this;
  }

  /**
   * Timestamp for when the venue was last updated in the customer&#39;s database.
   * @return lastUpdateTimestamp
   */
  @javax.annotation.Nonnull
  public Long getLastUpdateTimestamp() {
    return lastUpdateTimestamp;
  }

  public void setLastUpdateTimestamp(Long lastUpdateTimestamp) {
    this.lastUpdateTimestamp = lastUpdateTimestamp;
  }


  public EventsEntity maxCapacity(Integer maxCapacity) {
    this.maxCapacity = maxCapacity;
    return this;
  }

  /**
   * Maximum capacity for the venue in which the event occurs.
   * minimum: 0
   * @return maxCapacity
   */
  @javax.annotation.Nullable
  public Integer getMaxCapacity() {
    return maxCapacity;
  }

  public void setMaxCapacity(Integer maxCapacity) {
    this.maxCapacity = maxCapacity;
  }


  public EventsEntity presalesDate(LocalDate presalesDate) {
    this.presalesDate = presalesDate;
    return this;
  }

  /**
   * Date the event went on presales (relative to the timezone of the venue).
   * @return presalesDate
   */
  @javax.annotation.Nullable
  public LocalDate getPresalesDate() {
    return presalesDate;
  }

  public void setPresalesDate(LocalDate presalesDate) {
    this.presalesDate = presalesDate;
  }


  public EventsEntity seriesId(Integer seriesId) {
    this.seriesId = seriesId;
    return this;
  }

  /**
   * ID of the series the event belongs to.
   * @return seriesId
   */
  @javax.annotation.Nullable
  public Integer getSeriesId() {
    return seriesId;
  }

  public void setSeriesId(Integer seriesId) {
    this.seriesId = seriesId;
  }


  public EventsEntity soldOutDate(LocalDate soldOutDate) {
    this.soldOutDate = soldOutDate;
    return this;
  }

  /**
   * Date the event was sold out.
   * @return soldOutDate
   */
  @javax.annotation.Nullable
  public LocalDate getSoldOutDate() {
    return soldOutDate;
  }

  public void setSoldOutDate(LocalDate soldOutDate) {
    this.soldOutDate = soldOutDate;
  }


  public EventsEntity venue(VenuesEntity venue) {
    this.venue = venue;
    return this;
  }

  /**
   * Get venue
   * @return venue
   */
  @javax.annotation.Nonnull
  public VenuesEntity getVenue() {
    return venue;
  }

  public void setVenue(VenuesEntity venue) {
    this.venue = venue;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    EventsEntity eventsEntity = (EventsEntity) o;
    return Objects.equals(this.breakEven, eventsEntity.breakEven) &&
        Objects.equals(this.cancellationDate, eventsEntity.cancellationDate) &&
        Objects.equals(this.contract, eventsEntity.contract) &&
        Objects.equals(this.costingCapacity, eventsEntity.costingCapacity) &&
        Objects.equals(this.creationTimestamp, eventsEntity.creationTimestamp) &&
        Objects.equals(this.currency, eventsEntity.currency) &&
        Objects.equals(this.datetime, eventsEntity.datetime) &&
        Objects.equals(this.free, eventsEntity.free) &&
        Objects.equals(this.generalSalesDate, eventsEntity.generalSalesDate) &&
        Objects.equals(this.id, eventsEntity.id) &&
        Objects.equals(this.inputType, eventsEntity.inputType) &&
        Objects.equals(this.label, eventsEntity.label) &&
        Objects.equals(this.lastUpdateTimestamp, eventsEntity.lastUpdateTimestamp) &&
        Objects.equals(this.maxCapacity, eventsEntity.maxCapacity) &&
        Objects.equals(this.presalesDate, eventsEntity.presalesDate) &&
        Objects.equals(this.seriesId, eventsEntity.seriesId) &&
        Objects.equals(this.soldOutDate, eventsEntity.soldOutDate) &&
        Objects.equals(this.venue, eventsEntity.venue);
  }

  @Override
  public int hashCode() {
    return Objects.hash(breakEven, cancellationDate, contract, costingCapacity, creationTimestamp, currency, datetime, free, generalSalesDate, id, inputType, label, lastUpdateTimestamp, maxCapacity, presalesDate, seriesId, soldOutDate, venue);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class EventsEntity {\n");
    sb.append("    breakEven: ").append(toIndentedString(breakEven)).append("\n");
    sb.append("    cancellationDate: ").append(toIndentedString(cancellationDate)).append("\n");
    sb.append("    contract: ").append(toIndentedString(contract)).append("\n");
    sb.append("    costingCapacity: ").append(toIndentedString(costingCapacity)).append("\n");
    sb.append("    creationTimestamp: ").append(toIndentedString(creationTimestamp)).append("\n");
    sb.append("    currency: ").append(toIndentedString(currency)).append("\n");
    sb.append("    datetime: ").append(toIndentedString(datetime)).append("\n");
    sb.append("    free: ").append(toIndentedString(free)).append("\n");
    sb.append("    generalSalesDate: ").append(toIndentedString(generalSalesDate)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    inputType: ").append(toIndentedString(inputType)).append("\n");
    sb.append("    label: ").append(toIndentedString(label)).append("\n");
    sb.append("    lastUpdateTimestamp: ").append(toIndentedString(lastUpdateTimestamp)).append("\n");
    sb.append("    maxCapacity: ").append(toIndentedString(maxCapacity)).append("\n");
    sb.append("    presalesDate: ").append(toIndentedString(presalesDate)).append("\n");
    sb.append("    seriesId: ").append(toIndentedString(seriesId)).append("\n");
    sb.append("    soldOutDate: ").append(toIndentedString(soldOutDate)).append("\n");
    sb.append("    venue: ").append(toIndentedString(venue)).append("\n");
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
    openapiFields.add("break_even");
    openapiFields.add("cancellation_date");
    openapiFields.add("contract");
    openapiFields.add("costing_capacity");
    openapiFields.add("creation_timestamp");
    openapiFields.add("currency");
    openapiFields.add("datetime");
    openapiFields.add("free");
    openapiFields.add("general_sales_date");
    openapiFields.add("id");
    openapiFields.add("input_type");
    openapiFields.add("label");
    openapiFields.add("last_update_timestamp");
    openapiFields.add("max_capacity");
    openapiFields.add("presales_date");
    openapiFields.add("series_id");
    openapiFields.add("sold_out_date");
    openapiFields.add("venue");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("contract");
    openapiRequiredFields.add("creation_timestamp");
    openapiRequiredFields.add("datetime");
    openapiRequiredFields.add("free");
    openapiRequiredFields.add("id");
    openapiRequiredFields.add("input_type");
    openapiRequiredFields.add("label");
    openapiRequiredFields.add("last_update_timestamp");
    openapiRequiredFields.add("series_id");
    openapiRequiredFields.add("venue");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to EventsEntity
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!EventsEntity.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in EventsEntity is not found in the empty JSON string", EventsEntity.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!EventsEntity.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `EventsEntity` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : EventsEntity.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the required field `contract`
      EventsEntityContract.validateJsonElement(jsonObj.get("contract"));
      if ((jsonObj.get("currency") != null && !jsonObj.get("currency").isJsonNull()) && !jsonObj.get("currency").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `currency` to be a primitive type in the JSON string but got `%s`", jsonObj.get("currency").toString()));
      }
      if (!jsonObj.get("datetime").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `datetime` to be a primitive type in the JSON string but got `%s`", jsonObj.get("datetime").toString()));
      }
      // validate the required field `input_type`
      EventsEntityInputType.validateJsonElement(jsonObj.get("input_type"));
      if (!jsonObj.get("label").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `label` to be a primitive type in the JSON string but got `%s`", jsonObj.get("label").toString()));
      }
      // validate the required field `venue`
      VenuesEntity.validateJsonElement(jsonObj.get("venue"));
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!EventsEntity.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'EventsEntity' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<EventsEntity> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(EventsEntity.class));

       return (TypeAdapter<T>) new TypeAdapter<EventsEntity>() {
           @Override
           public void write(JsonWriter out, EventsEntity value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public EventsEntity read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of EventsEntity given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of EventsEntity
   * @throws IOException if the JSON string is invalid with respect to EventsEntity
   */
  public static EventsEntity fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, EventsEntity.class);
  }

  /**
   * Convert an instance of EventsEntity to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

