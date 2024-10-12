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
import java.util.Arrays;
import org.openapitools.jackson.nullable.JsonNullable;

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
 * TicketCountsDetailedEntityEventChannelsInnerEventCategoriesInnerEventPriceRangesInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:12:11.901875-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class TicketCountsDetailedEntityEventChannelsInnerEventCategoriesInnerEventPriceRangesInner {
  public static final String SERIALIZED_NAME_CURRENCY = "currency";
  @SerializedName(SERIALIZED_NAME_CURRENCY)
  private String currency;

  public static final String SERIALIZED_NAME_GROSS = "gross";
  @SerializedName(SERIALIZED_NAME_GROSS)
  private Float gross;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_RESERVATIONS = "reservations";
  @SerializedName(SERIALIZED_NAME_RESERVATIONS)
  private Integer reservations;

  public static final String SERIALIZED_NAME_SALES = "sales";
  @SerializedName(SERIALIZED_NAME_SALES)
  private Integer sales;

  public TicketCountsDetailedEntityEventChannelsInnerEventCategoriesInnerEventPriceRangesInner() {
  }

  public TicketCountsDetailedEntityEventChannelsInnerEventCategoriesInnerEventPriceRangesInner currency(String currency) {
    this.currency = currency;
    return this;
  }

  /**
   * Currency of the gross (&lt;a href&#x3D;&#39;https://en.wikipedia.org/wiki/ISO_4217#Active_codes&#39;&gt;ISO 4212 alphabetic code&lt;/a&gt;).
   * @return currency
   */
  @javax.annotation.Nonnull
  public String getCurrency() {
    return currency;
  }

  public void setCurrency(String currency) {
    this.currency = currency;
  }


  public TicketCountsDetailedEntityEventChannelsInnerEventCategoriesInnerEventPriceRangesInner gross(Float gross) {
    this.gross = gross;
    return this;
  }

  /**
   * Gross (&#x3D; income for the sold tickets for the current channel/category/price range, including VAT but excluding all commissions).
   * minimum: 0
   * @return gross
   */
  @javax.annotation.Nullable
  public Float getGross() {
    return gross;
  }

  public void setGross(Float gross) {
    this.gross = gross;
  }


  public TicketCountsDetailedEntityEventChannelsInnerEventCategoriesInnerEventPriceRangesInner id(Integer id) {
    this.id = id;
    return this;
  }

  /**
   * ID of the event price range.
   * @return id
   */
  @javax.annotation.Nonnull
  public Integer getId() {
    return id;
  }

  public void setId(Integer id) {
    this.id = id;
  }


  public TicketCountsDetailedEntityEventChannelsInnerEventCategoriesInnerEventPriceRangesInner reservations(Integer reservations) {
    this.reservations = reservations;
    return this;
  }

  /**
   * Detailed ticket reservations (&#x3D; number of reserved tickets for the current channel/category/price range). *This field may be omitted according to the customer configuration.*
   * minimum: 0
   * @return reservations
   */
  @javax.annotation.Nullable
  public Integer getReservations() {
    return reservations;
  }

  public void setReservations(Integer reservations) {
    this.reservations = reservations;
  }


  public TicketCountsDetailedEntityEventChannelsInnerEventCategoriesInnerEventPriceRangesInner sales(Integer sales) {
    this.sales = sales;
    return this;
  }

  /**
   * Detailed ticket sales (&#x3D; number of sold tickets for the current channel/category/price range).
   * minimum: 0
   * @return sales
   */
  @javax.annotation.Nullable
  public Integer getSales() {
    return sales;
  }

  public void setSales(Integer sales) {
    this.sales = sales;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TicketCountsDetailedEntityEventChannelsInnerEventCategoriesInnerEventPriceRangesInner ticketCountsDetailedEntityEventChannelsInnerEventCategoriesInnerEventPriceRangesInner = (TicketCountsDetailedEntityEventChannelsInnerEventCategoriesInnerEventPriceRangesInner) o;
    return Objects.equals(this.currency, ticketCountsDetailedEntityEventChannelsInnerEventCategoriesInnerEventPriceRangesInner.currency) &&
        Objects.equals(this.gross, ticketCountsDetailedEntityEventChannelsInnerEventCategoriesInnerEventPriceRangesInner.gross) &&
        Objects.equals(this.id, ticketCountsDetailedEntityEventChannelsInnerEventCategoriesInnerEventPriceRangesInner.id) &&
        Objects.equals(this.reservations, ticketCountsDetailedEntityEventChannelsInnerEventCategoriesInnerEventPriceRangesInner.reservations) &&
        Objects.equals(this.sales, ticketCountsDetailedEntityEventChannelsInnerEventCategoriesInnerEventPriceRangesInner.sales);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(currency, gross, id, reservations, sales);
  }

  private static <T> int hashCodeNullable(JsonNullable<T> a) {
    if (a == null) {
      return 1;
    }
    return a.isPresent() ? Arrays.deepHashCode(new Object[]{a.get()}) : 31;
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TicketCountsDetailedEntityEventChannelsInnerEventCategoriesInnerEventPriceRangesInner {\n");
    sb.append("    currency: ").append(toIndentedString(currency)).append("\n");
    sb.append("    gross: ").append(toIndentedString(gross)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    reservations: ").append(toIndentedString(reservations)).append("\n");
    sb.append("    sales: ").append(toIndentedString(sales)).append("\n");
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
    openapiFields.add("currency");
    openapiFields.add("gross");
    openapiFields.add("id");
    openapiFields.add("reservations");
    openapiFields.add("sales");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("currency");
    openapiRequiredFields.add("gross");
    openapiRequiredFields.add("id");
    openapiRequiredFields.add("sales");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to TicketCountsDetailedEntityEventChannelsInnerEventCategoriesInnerEventPriceRangesInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!TicketCountsDetailedEntityEventChannelsInnerEventCategoriesInnerEventPriceRangesInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in TicketCountsDetailedEntityEventChannelsInnerEventCategoriesInnerEventPriceRangesInner is not found in the empty JSON string", TicketCountsDetailedEntityEventChannelsInnerEventCategoriesInnerEventPriceRangesInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!TicketCountsDetailedEntityEventChannelsInnerEventCategoriesInnerEventPriceRangesInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TicketCountsDetailedEntityEventChannelsInnerEventCategoriesInnerEventPriceRangesInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : TicketCountsDetailedEntityEventChannelsInnerEventCategoriesInnerEventPriceRangesInner.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("currency").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `currency` to be a primitive type in the JSON string but got `%s`", jsonObj.get("currency").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TicketCountsDetailedEntityEventChannelsInnerEventCategoriesInnerEventPriceRangesInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TicketCountsDetailedEntityEventChannelsInnerEventCategoriesInnerEventPriceRangesInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TicketCountsDetailedEntityEventChannelsInnerEventCategoriesInnerEventPriceRangesInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TicketCountsDetailedEntityEventChannelsInnerEventCategoriesInnerEventPriceRangesInner.class));

       return (TypeAdapter<T>) new TypeAdapter<TicketCountsDetailedEntityEventChannelsInnerEventCategoriesInnerEventPriceRangesInner>() {
           @Override
           public void write(JsonWriter out, TicketCountsDetailedEntityEventChannelsInnerEventCategoriesInnerEventPriceRangesInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TicketCountsDetailedEntityEventChannelsInnerEventCategoriesInnerEventPriceRangesInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of TicketCountsDetailedEntityEventChannelsInnerEventCategoriesInnerEventPriceRangesInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of TicketCountsDetailedEntityEventChannelsInnerEventCategoriesInnerEventPriceRangesInner
   * @throws IOException if the JSON string is invalid with respect to TicketCountsDetailedEntityEventChannelsInnerEventCategoriesInnerEventPriceRangesInner
   */
  public static TicketCountsDetailedEntityEventChannelsInnerEventCategoriesInnerEventPriceRangesInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TicketCountsDetailedEntityEventChannelsInnerEventCategoriesInnerEventPriceRangesInner.class);
  }

  /**
   * Convert an instance of TicketCountsDetailedEntityEventChannelsInnerEventCategoriesInnerEventPriceRangesInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

