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
 * EventsCapacitiesEntityEventCategoriesInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:12:11.901875-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class EventsCapacitiesEntityEventCategoriesInner {
  public static final String SERIALIZED_NAME_COMPS = "comps";
  @SerializedName(SERIALIZED_NAME_COMPS)
  private Integer comps;

  public static final String SERIALIZED_NAME_HOLDS = "holds";
  @SerializedName(SERIALIZED_NAME_HOLDS)
  private Integer holds;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_KILLS = "kills";
  @SerializedName(SERIALIZED_NAME_KILLS)
  private Integer kills;

  public static final String SERIALIZED_NAME_SELLABLE_CAPACITY = "sellable_capacity";
  @SerializedName(SERIALIZED_NAME_SELLABLE_CAPACITY)
  private Integer sellableCapacity;

  public static final String SERIALIZED_NAME_TOTAL_CAPACITY = "total_capacity";
  @SerializedName(SERIALIZED_NAME_TOTAL_CAPACITY)
  private Integer totalCapacity;

  public EventsCapacitiesEntityEventCategoriesInner() {
  }

  public EventsCapacitiesEntityEventCategoriesInner comps(Integer comps) {
    this.comps = comps;
    return this;
  }

  /**
   * Number of comps in the category.
   * @return comps
   */
  @javax.annotation.Nullable
  public Integer getComps() {
    return comps;
  }

  public void setComps(Integer comps) {
    this.comps = comps;
  }


  public EventsCapacitiesEntityEventCategoriesInner holds(Integer holds) {
    this.holds = holds;
    return this;
  }

  /**
   * Number of *holds* in the category. &lt;span class&#x3D;\&quot;definition\&quot;&gt;Holds&lt;/span&gt; are seats/places that are not in sale at the date of the capacity, but will eventually be later.
   * @return holds
   */
  @javax.annotation.Nullable
  public Integer getHolds() {
    return holds;
  }

  public void setHolds(Integer holds) {
    this.holds = holds;
  }


  public EventsCapacitiesEntityEventCategoriesInner id(Integer id) {
    this.id = id;
    return this;
  }

  /**
   * Unique ID of the event category.
   * @return id
   */
  @javax.annotation.Nonnull
  public Integer getId() {
    return id;
  }

  public void setId(Integer id) {
    this.id = id;
  }


  public EventsCapacitiesEntityEventCategoriesInner kills(Integer kills) {
    this.kills = kills;
    return this;
  }

  /**
   * Number of *kills* in the category. &lt;span class&#x3D;\&quot;definition\&quot;&gt;Kills&lt;/span&gt; are seats/places that will not be sold for technical reasons.
   * @return kills
   */
  @javax.annotation.Nullable
  public Integer getKills() {
    return kills;
  }

  public void setKills(Integer kills) {
    this.kills = kills;
  }


  public EventsCapacitiesEntityEventCategoriesInner sellableCapacity(Integer sellableCapacity) {
    this.sellableCapacity = sellableCapacity;
    return this;
  }

  /**
   * Number of sellable seats/places in the category. This is calculated by the formula: &#x60;total_capacity - kills - comps - holds&#x60;.
   * @return sellableCapacity
   */
  @javax.annotation.Nonnull
  public Integer getSellableCapacity() {
    return sellableCapacity;
  }

  public void setSellableCapacity(Integer sellableCapacity) {
    this.sellableCapacity = sellableCapacity;
  }


  public EventsCapacitiesEntityEventCategoriesInner totalCapacity(Integer totalCapacity) {
    this.totalCapacity = totalCapacity;
    return this;
  }

  /**
   * Total number of seats/places in the category.
   * @return totalCapacity
   */
  @javax.annotation.Nonnull
  public Integer getTotalCapacity() {
    return totalCapacity;
  }

  public void setTotalCapacity(Integer totalCapacity) {
    this.totalCapacity = totalCapacity;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    EventsCapacitiesEntityEventCategoriesInner eventsCapacitiesEntityEventCategoriesInner = (EventsCapacitiesEntityEventCategoriesInner) o;
    return Objects.equals(this.comps, eventsCapacitiesEntityEventCategoriesInner.comps) &&
        Objects.equals(this.holds, eventsCapacitiesEntityEventCategoriesInner.holds) &&
        Objects.equals(this.id, eventsCapacitiesEntityEventCategoriesInner.id) &&
        Objects.equals(this.kills, eventsCapacitiesEntityEventCategoriesInner.kills) &&
        Objects.equals(this.sellableCapacity, eventsCapacitiesEntityEventCategoriesInner.sellableCapacity) &&
        Objects.equals(this.totalCapacity, eventsCapacitiesEntityEventCategoriesInner.totalCapacity);
  }

  @Override
  public int hashCode() {
    return Objects.hash(comps, holds, id, kills, sellableCapacity, totalCapacity);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class EventsCapacitiesEntityEventCategoriesInner {\n");
    sb.append("    comps: ").append(toIndentedString(comps)).append("\n");
    sb.append("    holds: ").append(toIndentedString(holds)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    kills: ").append(toIndentedString(kills)).append("\n");
    sb.append("    sellableCapacity: ").append(toIndentedString(sellableCapacity)).append("\n");
    sb.append("    totalCapacity: ").append(toIndentedString(totalCapacity)).append("\n");
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
    openapiFields.add("comps");
    openapiFields.add("holds");
    openapiFields.add("id");
    openapiFields.add("kills");
    openapiFields.add("sellable_capacity");
    openapiFields.add("total_capacity");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("comps");
    openapiRequiredFields.add("holds");
    openapiRequiredFields.add("id");
    openapiRequiredFields.add("kills");
    openapiRequiredFields.add("sellable_capacity");
    openapiRequiredFields.add("total_capacity");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to EventsCapacitiesEntityEventCategoriesInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!EventsCapacitiesEntityEventCategoriesInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in EventsCapacitiesEntityEventCategoriesInner is not found in the empty JSON string", EventsCapacitiesEntityEventCategoriesInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!EventsCapacitiesEntityEventCategoriesInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `EventsCapacitiesEntityEventCategoriesInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : EventsCapacitiesEntityEventCategoriesInner.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!EventsCapacitiesEntityEventCategoriesInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'EventsCapacitiesEntityEventCategoriesInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<EventsCapacitiesEntityEventCategoriesInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(EventsCapacitiesEntityEventCategoriesInner.class));

       return (TypeAdapter<T>) new TypeAdapter<EventsCapacitiesEntityEventCategoriesInner>() {
           @Override
           public void write(JsonWriter out, EventsCapacitiesEntityEventCategoriesInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public EventsCapacitiesEntityEventCategoriesInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of EventsCapacitiesEntityEventCategoriesInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of EventsCapacitiesEntityEventCategoriesInner
   * @throws IOException if the JSON string is invalid with respect to EventsCapacitiesEntityEventCategoriesInner
   */
  public static EventsCapacitiesEntityEventCategoriesInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, EventsCapacitiesEntityEventCategoriesInner.class);
  }

  /**
   * Convert an instance of EventsCapacitiesEntityEventCategoriesInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

