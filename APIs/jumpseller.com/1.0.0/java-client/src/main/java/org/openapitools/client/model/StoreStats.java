/*
 * Jumpseller API
 * # Endpoint Structure  All URLs are in the format:   ```text https://api.jumpseller.com/v1/path.json?login=XXXXXX&authtoken=storetoken   ```  The path is prefixed by the API version and the URL takes as parameters the login (your store specific API login) and your authentication token. <br/><br/> ***  # Version  The current version of the API is **v1**.   If we change the API in backward-incompatible ways, we'll increase the version number and maintain stable support for the old urls. <br/><br/> ***  # Authentication  The API uses a token-based authentication with a combination of a login key and an auth token. **Both parameters can be found on the left sidebar of the Account section, accessed from the main menu of your Admin Panel**. The auth token of the user can be reset on the same page.  ![Store Login](/images/support/api/apilogin.png)  The auth token is a **32 characters** string.  If you are developing a Jumpseller App, the authentication should be done using [OAuth-2](/support/oauth-2). Please read the article [Build an App](/support/apps) for more information. <br/><br/> ***  # Curl Examples  To request all the products at your store, you would append the products index path to the base url to create an URL with the format:    ```text https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX ```  In curl, you can invoque that URL with:    ```text curl -X GET \"https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX\" ```  To create a product, you will include the JSON data and specify the MIME Type:    ```text curl -X POST -d '{ \"product\" : {\"name\": \"My new Product!\", \"price\": 100} }' \"https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX\" -H \"Content-Type:application/json\" ```  and to update the product identified with 123:    ```text curl -X PUT -d '{ \"product\" : {\"name\": \"My updated Product!\", \"price\": 99} }' \"https://api.jumpseller.com/v1/products/123.json?login=XXXXXX&authtoken=XXXXX\" -H \"Content-Type:application/json\" ```  or delete it:    ```text curl -X DELETE \"https://api.jumpseller.com/v1/products/123.json?login=XXXXXX&authtoken=XXXXX\" -H \"Content-Type:application/json\" ``` <br/><br/> ***  # PHP Examples  Create a new Product (POST method)  ```php $url = 'https://api.jumpseller.com/v1/products.json?login=XXXXX&authtoken=XXXXX; $ch = curl_init($url); curl_setopt($ch, CURLOPT_RETURNTRANSFER, true); curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));  curl_setopt($ch, CURLOPT_CUSTOMREQUEST, \"POST\"); //post method curl_setopt($ch, CURLOPT_POSTFIELDS, '{ \"product\" : {\"name\": \"My updated Product!\", \"price\": 99} }');  $result = curl_exec($ch); print_r($result); curl_close($ch); ``` <br/><br/> ***  # Plain JSON only. No XML.  * We only support JSON for data serialization. * Our node format has no root element.   * We use snake_case to describe attribute keys (like \"created_at\").   * All empty value are replaced with **null** strings. * All API URLs end in .json to indicate that they accept and return JSON. * POST and PUT methods require you to explicitly state the MIME type of your request's body content as **\"application/json\"**. <br/><br/> ***  # Rate Limit You can perform a maximum of:  + 240 (two hundred forty) requests per minute and + 8 (eight) requests per second   If you exceed this limit, you'll get a 403 Forbidden (Rate Limit Exceeded) response for subsequent requests.    The rate limits apply by IP address and by store. This means that multiple requests on different stores are not counted towards the same rate limit.  This limits are necessary to ensure resources are correctly used. Your application should be aware of this limits and retry any unsuccessful request, check the following Ruby stub:  ```ruby tries = 0; max_tries = 3; begin   HTTParty.send(method, uri) # perform an API call.   sleep 0.5   tries += 1 rescue   unless tries >= max_tries     sleep 1.0 # wait the necessary time before retrying the call again.     retry   end end ```  Finally, you can review the Response Headers of each request:  ```text Jumpseller-PerMinuteRateLimit-Limit: 60   Jumpseller-PerMinuteRateLimit-Remaining: 59 # requests available on the per-second interval   Jumpseller-PerSecondRateLimit-Limit: 2   Jumpseller-PerSecondRateLimit-Remaining: 1 # requests available on the per-second interval ```   to better model your application requests intervals.  In the event of getting your IP banned, the Response Header `Jumpseller-BannedByRateLimit-Reset` informs you the time when will your ban be reseted. <br/><br/> ***  # Pagination  By default we will return 50 objects (products, orders, etc) per page. There is a maximum of 100, using a query string `&limit=100`. If the result set gets paginated it is your responsibility to check the next page for more objects -- you do this by using query strings `&page=2`, `&page=3` and so on.  ```text https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX&page=3&limit=100 ``` <br/><br/> ***  # More * [Jumpseller API wrapper](https://gitlab.com/jumpseller-api/ruby) provides a public Ruby abstraction over our API; * [Apps Page](/apps) showcases external integrations with Jumpseller done by technical experts; * [Imgbb API](https://api.imgbb.com/) provides an easy way to upload and temporaly host for images and files. <br/><br/> *** <br/><br/> 
 *
 * The version of the OpenAPI document: 1.0.0
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
import org.openapitools.client.model.BestSold;
import org.openapitools.client.model.DailyVisits;
import org.openapitools.client.model.PaymentMethodFreq;
import org.openapitools.client.model.Referrer;
import org.openapitools.client.model.ShippingMethodFreq;
import org.openapitools.client.model.StoreStatsConversions;
import org.openapitools.client.model.StoreStatsNewVsReturningCustomers;
import org.openapitools.client.model.StoreStatsOrders;
import org.openapitools.client.model.StoreStatsRegionOrders;
import org.openapitools.client.model.TrafficType;

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
 * StoreStats
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:31:37.537066-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class StoreStats {
  public static final String SERIALIZED_NAME_BEST_SOLD = "best_sold";
  @SerializedName(SERIALIZED_NAME_BEST_SOLD)
  private List<BestSold> bestSold = new ArrayList<>();

  public static final String SERIALIZED_NAME_CONVERSIONS = "conversions";
  @SerializedName(SERIALIZED_NAME_CONVERSIONS)
  private StoreStatsConversions conversions;

  public static final String SERIALIZED_NAME_CURRENCY = "currency";
  @SerializedName(SERIALIZED_NAME_CURRENCY)
  private String currency;

  public static final String SERIALIZED_NAME_DAILY_VISITS = "daily_visits";
  @SerializedName(SERIALIZED_NAME_DAILY_VISITS)
  private List<DailyVisits> dailyVisits = new ArrayList<>();

  public static final String SERIALIZED_NAME_FROM = "from";
  @SerializedName(SERIALIZED_NAME_FROM)
  private String from;

  public static final String SERIALIZED_NAME_NEW_VS_RETURNING_CUSTOMERS = "new_vs_returning_customers";
  @SerializedName(SERIALIZED_NAME_NEW_VS_RETURNING_CUSTOMERS)
  private StoreStatsNewVsReturningCustomers newVsReturningCustomers;

  public static final String SERIALIZED_NAME_NEW_VS_RETURNING_ORDERS = "new_vs_returning_orders";
  @SerializedName(SERIALIZED_NAME_NEW_VS_RETURNING_ORDERS)
  private StoreStatsNewVsReturningCustomers newVsReturningOrders;

  public static final String SERIALIZED_NAME_ORDERS = "orders";
  @SerializedName(SERIALIZED_NAME_ORDERS)
  private StoreStatsOrders orders;

  public static final String SERIALIZED_NAME_PAYMENT_METHODS = "payment_methods";
  @SerializedName(SERIALIZED_NAME_PAYMENT_METHODS)
  private List<PaymentMethodFreq> paymentMethods = new ArrayList<>();

  public static final String SERIALIZED_NAME_REFERRERS = "referrers";
  @SerializedName(SERIALIZED_NAME_REFERRERS)
  private List<Referrer> referrers = new ArrayList<>();

  public static final String SERIALIZED_NAME_REGION_ORDERS = "region_orders";
  @SerializedName(SERIALIZED_NAME_REGION_ORDERS)
  private StoreStatsRegionOrders regionOrders;

  public static final String SERIALIZED_NAME_SEARCH_FREQUENCIES_ALL = "search_frequencies_all";
  @SerializedName(SERIALIZED_NAME_SEARCH_FREQUENCIES_ALL)
  private List<Object> searchFrequenciesAll = new ArrayList<>();

  public static final String SERIALIZED_NAME_SEARCH_FREQUENCIES_WITHOUT_RESULTS = "search_frequencies_without_results";
  @SerializedName(SERIALIZED_NAME_SEARCH_FREQUENCIES_WITHOUT_RESULTS)
  private List<Object> searchFrequenciesWithoutResults = new ArrayList<>();

  public static final String SERIALIZED_NAME_SHIPPING_METHODS = "shipping_methods";
  @SerializedName(SERIALIZED_NAME_SHIPPING_METHODS)
  private List<ShippingMethodFreq> shippingMethods = new ArrayList<>();

  public static final String SERIALIZED_NAME_TO = "to";
  @SerializedName(SERIALIZED_NAME_TO)
  private String to;

  public static final String SERIALIZED_NAME_TRAFFIC_TYPE = "traffic_type";
  @SerializedName(SERIALIZED_NAME_TRAFFIC_TYPE)
  private List<TrafficType> trafficType = new ArrayList<>();

  public static final String SERIALIZED_NAME_VISITS = "visits";
  @SerializedName(SERIALIZED_NAME_VISITS)
  private Integer visits;

  public StoreStats() {
  }

  public StoreStats bestSold(List<BestSold> bestSold) {
    this.bestSold = bestSold;
    return this;
  }

  public StoreStats addBestSoldItem(BestSold bestSoldItem) {
    if (this.bestSold == null) {
      this.bestSold = new ArrayList<>();
    }
    this.bestSold.add(bestSoldItem);
    return this;
  }

  /**
   * Top 10 best sold products.
   * @return bestSold
   */
  @javax.annotation.Nullable
  public List<BestSold> getBestSold() {
    return bestSold;
  }

  public void setBestSold(List<BestSold> bestSold) {
    this.bestSold = bestSold;
  }


  public StoreStats conversions(StoreStatsConversions conversions) {
    this.conversions = conversions;
    return this;
  }

  /**
   * Get conversions
   * @return conversions
   */
  @javax.annotation.Nullable
  public StoreStatsConversions getConversions() {
    return conversions;
  }

  public void setConversions(StoreStatsConversions conversions) {
    this.conversions = conversions;
  }


  public StoreStats currency(String currency) {
    this.currency = currency;
    return this;
  }

  /**
   * Store currency.
   * @return currency
   */
  @javax.annotation.Nullable
  public String getCurrency() {
    return currency;
  }

  public void setCurrency(String currency) {
    this.currency = currency;
  }


  public StoreStats dailyVisits(List<DailyVisits> dailyVisits) {
    this.dailyVisits = dailyVisits;
    return this;
  }

  public StoreStats addDailyVisitsItem(DailyVisits dailyVisitsItem) {
    if (this.dailyVisits == null) {
      this.dailyVisits = new ArrayList<>();
    }
    this.dailyVisits.add(dailyVisitsItem);
    return this;
  }

  /**
   * Visits per day.
   * @return dailyVisits
   */
  @javax.annotation.Nullable
  public List<DailyVisits> getDailyVisits() {
    return dailyVisits;
  }

  public void setDailyVisits(List<DailyVisits> dailyVisits) {
    this.dailyVisits = dailyVisits;
  }


  public StoreStats from(String from) {
    this.from = from;
    return this;
  }

  /**
   * Statistics start date.
   * @return from
   */
  @javax.annotation.Nullable
  public String getFrom() {
    return from;
  }

  public void setFrom(String from) {
    this.from = from;
  }


  public StoreStats newVsReturningCustomers(StoreStatsNewVsReturningCustomers newVsReturningCustomers) {
    this.newVsReturningCustomers = newVsReturningCustomers;
    return this;
  }

  /**
   * Get newVsReturningCustomers
   * @return newVsReturningCustomers
   */
  @javax.annotation.Nullable
  public StoreStatsNewVsReturningCustomers getNewVsReturningCustomers() {
    return newVsReturningCustomers;
  }

  public void setNewVsReturningCustomers(StoreStatsNewVsReturningCustomers newVsReturningCustomers) {
    this.newVsReturningCustomers = newVsReturningCustomers;
  }


  public StoreStats newVsReturningOrders(StoreStatsNewVsReturningCustomers newVsReturningOrders) {
    this.newVsReturningOrders = newVsReturningOrders;
    return this;
  }

  /**
   * Get newVsReturningOrders
   * @return newVsReturningOrders
   */
  @javax.annotation.Nullable
  public StoreStatsNewVsReturningCustomers getNewVsReturningOrders() {
    return newVsReturningOrders;
  }

  public void setNewVsReturningOrders(StoreStatsNewVsReturningCustomers newVsReturningOrders) {
    this.newVsReturningOrders = newVsReturningOrders;
  }


  public StoreStats orders(StoreStatsOrders orders) {
    this.orders = orders;
    return this;
  }

  /**
   * Get orders
   * @return orders
   */
  @javax.annotation.Nullable
  public StoreStatsOrders getOrders() {
    return orders;
  }

  public void setOrders(StoreStatsOrders orders) {
    this.orders = orders;
  }


  public StoreStats paymentMethods(List<PaymentMethodFreq> paymentMethods) {
    this.paymentMethods = paymentMethods;
    return this;
  }

  public StoreStats addPaymentMethodsItem(PaymentMethodFreq paymentMethodsItem) {
    if (this.paymentMethods == null) {
      this.paymentMethods = new ArrayList<>();
    }
    this.paymentMethods.add(paymentMethodsItem);
    return this;
  }

  /**
   * Store payment methods and their frequency.
   * @return paymentMethods
   */
  @javax.annotation.Nullable
  public List<PaymentMethodFreq> getPaymentMethods() {
    return paymentMethods;
  }

  public void setPaymentMethods(List<PaymentMethodFreq> paymentMethods) {
    this.paymentMethods = paymentMethods;
  }


  public StoreStats referrers(List<Referrer> referrers) {
    this.referrers = referrers;
    return this;
  }

  public StoreStats addReferrersItem(Referrer referrersItem) {
    if (this.referrers == null) {
      this.referrers = new ArrayList<>();
    }
    this.referrers.add(referrersItem);
    return this;
  }

  /**
   * Top 10 referrer sources and their frequency.
   * @return referrers
   */
  @javax.annotation.Nullable
  public List<Referrer> getReferrers() {
    return referrers;
  }

  public void setReferrers(List<Referrer> referrers) {
    this.referrers = referrers;
  }


  public StoreStats regionOrders(StoreStatsRegionOrders regionOrders) {
    this.regionOrders = regionOrders;
    return this;
  }

  /**
   * Get regionOrders
   * @return regionOrders
   */
  @javax.annotation.Nullable
  public StoreStatsRegionOrders getRegionOrders() {
    return regionOrders;
  }

  public void setRegionOrders(StoreStatsRegionOrders regionOrders) {
    this.regionOrders = regionOrders;
  }


  public StoreStats searchFrequenciesAll(List<Object> searchFrequenciesAll) {
    this.searchFrequenciesAll = searchFrequenciesAll;
    return this;
  }

  public StoreStats addSearchFrequenciesAllItem(Object searchFrequenciesAllItem) {
    if (this.searchFrequenciesAll == null) {
      this.searchFrequenciesAll = new ArrayList<>();
    }
    this.searchFrequenciesAll.add(searchFrequenciesAllItem);
    return this;
  }

  /**
   * Number of times each search was conducted under the form of an aggregation query.
   * @return searchFrequenciesAll
   */
  @javax.annotation.Nullable
  public List<Object> getSearchFrequenciesAll() {
    return searchFrequenciesAll;
  }

  public void setSearchFrequenciesAll(List<Object> searchFrequenciesAll) {
    this.searchFrequenciesAll = searchFrequenciesAll;
  }


  public StoreStats searchFrequenciesWithoutResults(List<Object> searchFrequenciesWithoutResults) {
    this.searchFrequenciesWithoutResults = searchFrequenciesWithoutResults;
    return this;
  }

  public StoreStats addSearchFrequenciesWithoutResultsItem(Object searchFrequenciesWithoutResultsItem) {
    if (this.searchFrequenciesWithoutResults == null) {
      this.searchFrequenciesWithoutResults = new ArrayList<>();
    }
    this.searchFrequenciesWithoutResults.add(searchFrequenciesWithoutResultsItem);
    return this;
  }

  /**
   * Number of times each search with zero results was conducted under the form of an aggregation query.
   * @return searchFrequenciesWithoutResults
   */
  @javax.annotation.Nullable
  public List<Object> getSearchFrequenciesWithoutResults() {
    return searchFrequenciesWithoutResults;
  }

  public void setSearchFrequenciesWithoutResults(List<Object> searchFrequenciesWithoutResults) {
    this.searchFrequenciesWithoutResults = searchFrequenciesWithoutResults;
  }


  public StoreStats shippingMethods(List<ShippingMethodFreq> shippingMethods) {
    this.shippingMethods = shippingMethods;
    return this;
  }

  public StoreStats addShippingMethodsItem(ShippingMethodFreq shippingMethodsItem) {
    if (this.shippingMethods == null) {
      this.shippingMethods = new ArrayList<>();
    }
    this.shippingMethods.add(shippingMethodsItem);
    return this;
  }

  /**
   * Store shipping methods and their frequency.
   * @return shippingMethods
   */
  @javax.annotation.Nullable
  public List<ShippingMethodFreq> getShippingMethods() {
    return shippingMethods;
  }

  public void setShippingMethods(List<ShippingMethodFreq> shippingMethods) {
    this.shippingMethods = shippingMethods;
  }


  public StoreStats to(String to) {
    this.to = to;
    return this;
  }

  /**
   * Statistics end date.
   * @return to
   */
  @javax.annotation.Nullable
  public String getTo() {
    return to;
  }

  public void setTo(String to) {
    this.to = to;
  }


  public StoreStats trafficType(List<TrafficType> trafficType) {
    this.trafficType = trafficType;
    return this;
  }

  public StoreStats addTrafficTypeItem(TrafficType trafficTypeItem) {
    if (this.trafficType == null) {
      this.trafficType = new ArrayList<>();
    }
    this.trafficType.add(trafficTypeItem);
    return this;
  }

  /**
   * Type of store traffic and its frequency.
   * @return trafficType
   */
  @javax.annotation.Nullable
  public List<TrafficType> getTrafficType() {
    return trafficType;
  }

  public void setTrafficType(List<TrafficType> trafficType) {
    this.trafficType = trafficType;
  }


  public StoreStats visits(Integer visits) {
    this.visits = visits;
    return this;
  }

  /**
   * Total number of visits.
   * @return visits
   */
  @javax.annotation.Nullable
  public Integer getVisits() {
    return visits;
  }

  public void setVisits(Integer visits) {
    this.visits = visits;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    StoreStats storeStats = (StoreStats) o;
    return Objects.equals(this.bestSold, storeStats.bestSold) &&
        Objects.equals(this.conversions, storeStats.conversions) &&
        Objects.equals(this.currency, storeStats.currency) &&
        Objects.equals(this.dailyVisits, storeStats.dailyVisits) &&
        Objects.equals(this.from, storeStats.from) &&
        Objects.equals(this.newVsReturningCustomers, storeStats.newVsReturningCustomers) &&
        Objects.equals(this.newVsReturningOrders, storeStats.newVsReturningOrders) &&
        Objects.equals(this.orders, storeStats.orders) &&
        Objects.equals(this.paymentMethods, storeStats.paymentMethods) &&
        Objects.equals(this.referrers, storeStats.referrers) &&
        Objects.equals(this.regionOrders, storeStats.regionOrders) &&
        Objects.equals(this.searchFrequenciesAll, storeStats.searchFrequenciesAll) &&
        Objects.equals(this.searchFrequenciesWithoutResults, storeStats.searchFrequenciesWithoutResults) &&
        Objects.equals(this.shippingMethods, storeStats.shippingMethods) &&
        Objects.equals(this.to, storeStats.to) &&
        Objects.equals(this.trafficType, storeStats.trafficType) &&
        Objects.equals(this.visits, storeStats.visits);
  }

  @Override
  public int hashCode() {
    return Objects.hash(bestSold, conversions, currency, dailyVisits, from, newVsReturningCustomers, newVsReturningOrders, orders, paymentMethods, referrers, regionOrders, searchFrequenciesAll, searchFrequenciesWithoutResults, shippingMethods, to, trafficType, visits);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class StoreStats {\n");
    sb.append("    bestSold: ").append(toIndentedString(bestSold)).append("\n");
    sb.append("    conversions: ").append(toIndentedString(conversions)).append("\n");
    sb.append("    currency: ").append(toIndentedString(currency)).append("\n");
    sb.append("    dailyVisits: ").append(toIndentedString(dailyVisits)).append("\n");
    sb.append("    from: ").append(toIndentedString(from)).append("\n");
    sb.append("    newVsReturningCustomers: ").append(toIndentedString(newVsReturningCustomers)).append("\n");
    sb.append("    newVsReturningOrders: ").append(toIndentedString(newVsReturningOrders)).append("\n");
    sb.append("    orders: ").append(toIndentedString(orders)).append("\n");
    sb.append("    paymentMethods: ").append(toIndentedString(paymentMethods)).append("\n");
    sb.append("    referrers: ").append(toIndentedString(referrers)).append("\n");
    sb.append("    regionOrders: ").append(toIndentedString(regionOrders)).append("\n");
    sb.append("    searchFrequenciesAll: ").append(toIndentedString(searchFrequenciesAll)).append("\n");
    sb.append("    searchFrequenciesWithoutResults: ").append(toIndentedString(searchFrequenciesWithoutResults)).append("\n");
    sb.append("    shippingMethods: ").append(toIndentedString(shippingMethods)).append("\n");
    sb.append("    to: ").append(toIndentedString(to)).append("\n");
    sb.append("    trafficType: ").append(toIndentedString(trafficType)).append("\n");
    sb.append("    visits: ").append(toIndentedString(visits)).append("\n");
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
    openapiFields.add("best_sold");
    openapiFields.add("conversions");
    openapiFields.add("currency");
    openapiFields.add("daily_visits");
    openapiFields.add("from");
    openapiFields.add("new_vs_returning_customers");
    openapiFields.add("new_vs_returning_orders");
    openapiFields.add("orders");
    openapiFields.add("payment_methods");
    openapiFields.add("referrers");
    openapiFields.add("region_orders");
    openapiFields.add("search_frequencies_all");
    openapiFields.add("search_frequencies_without_results");
    openapiFields.add("shipping_methods");
    openapiFields.add("to");
    openapiFields.add("traffic_type");
    openapiFields.add("visits");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to StoreStats
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!StoreStats.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in StoreStats is not found in the empty JSON string", StoreStats.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!StoreStats.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `StoreStats` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("best_sold") != null && !jsonObj.get("best_sold").isJsonNull()) {
        JsonArray jsonArraybestSold = jsonObj.getAsJsonArray("best_sold");
        if (jsonArraybestSold != null) {
          // ensure the json data is an array
          if (!jsonObj.get("best_sold").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `best_sold` to be an array in the JSON string but got `%s`", jsonObj.get("best_sold").toString()));
          }

          // validate the optional field `best_sold` (array)
          for (int i = 0; i < jsonArraybestSold.size(); i++) {
            BestSold.validateJsonElement(jsonArraybestSold.get(i));
          };
        }
      }
      // validate the optional field `conversions`
      if (jsonObj.get("conversions") != null && !jsonObj.get("conversions").isJsonNull()) {
        StoreStatsConversions.validateJsonElement(jsonObj.get("conversions"));
      }
      if ((jsonObj.get("currency") != null && !jsonObj.get("currency").isJsonNull()) && !jsonObj.get("currency").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `currency` to be a primitive type in the JSON string but got `%s`", jsonObj.get("currency").toString()));
      }
      if (jsonObj.get("daily_visits") != null && !jsonObj.get("daily_visits").isJsonNull()) {
        JsonArray jsonArraydailyVisits = jsonObj.getAsJsonArray("daily_visits");
        if (jsonArraydailyVisits != null) {
          // ensure the json data is an array
          if (!jsonObj.get("daily_visits").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `daily_visits` to be an array in the JSON string but got `%s`", jsonObj.get("daily_visits").toString()));
          }

          // validate the optional field `daily_visits` (array)
          for (int i = 0; i < jsonArraydailyVisits.size(); i++) {
            DailyVisits.validateJsonElement(jsonArraydailyVisits.get(i));
          };
        }
      }
      if ((jsonObj.get("from") != null && !jsonObj.get("from").isJsonNull()) && !jsonObj.get("from").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `from` to be a primitive type in the JSON string but got `%s`", jsonObj.get("from").toString()));
      }
      // validate the optional field `new_vs_returning_customers`
      if (jsonObj.get("new_vs_returning_customers") != null && !jsonObj.get("new_vs_returning_customers").isJsonNull()) {
        StoreStatsNewVsReturningCustomers.validateJsonElement(jsonObj.get("new_vs_returning_customers"));
      }
      // validate the optional field `new_vs_returning_orders`
      if (jsonObj.get("new_vs_returning_orders") != null && !jsonObj.get("new_vs_returning_orders").isJsonNull()) {
        StoreStatsNewVsReturningCustomers.validateJsonElement(jsonObj.get("new_vs_returning_orders"));
      }
      // validate the optional field `orders`
      if (jsonObj.get("orders") != null && !jsonObj.get("orders").isJsonNull()) {
        StoreStatsOrders.validateJsonElement(jsonObj.get("orders"));
      }
      if (jsonObj.get("payment_methods") != null && !jsonObj.get("payment_methods").isJsonNull()) {
        JsonArray jsonArraypaymentMethods = jsonObj.getAsJsonArray("payment_methods");
        if (jsonArraypaymentMethods != null) {
          // ensure the json data is an array
          if (!jsonObj.get("payment_methods").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `payment_methods` to be an array in the JSON string but got `%s`", jsonObj.get("payment_methods").toString()));
          }

          // validate the optional field `payment_methods` (array)
          for (int i = 0; i < jsonArraypaymentMethods.size(); i++) {
            PaymentMethodFreq.validateJsonElement(jsonArraypaymentMethods.get(i));
          };
        }
      }
      if (jsonObj.get("referrers") != null && !jsonObj.get("referrers").isJsonNull()) {
        JsonArray jsonArrayreferrers = jsonObj.getAsJsonArray("referrers");
        if (jsonArrayreferrers != null) {
          // ensure the json data is an array
          if (!jsonObj.get("referrers").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `referrers` to be an array in the JSON string but got `%s`", jsonObj.get("referrers").toString()));
          }

          // validate the optional field `referrers` (array)
          for (int i = 0; i < jsonArrayreferrers.size(); i++) {
            Referrer.validateJsonElement(jsonArrayreferrers.get(i));
          };
        }
      }
      // validate the optional field `region_orders`
      if (jsonObj.get("region_orders") != null && !jsonObj.get("region_orders").isJsonNull()) {
        StoreStatsRegionOrders.validateJsonElement(jsonObj.get("region_orders"));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("search_frequencies_all") != null && !jsonObj.get("search_frequencies_all").isJsonNull() && !jsonObj.get("search_frequencies_all").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `search_frequencies_all` to be an array in the JSON string but got `%s`", jsonObj.get("search_frequencies_all").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("search_frequencies_without_results") != null && !jsonObj.get("search_frequencies_without_results").isJsonNull() && !jsonObj.get("search_frequencies_without_results").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `search_frequencies_without_results` to be an array in the JSON string but got `%s`", jsonObj.get("search_frequencies_without_results").toString()));
      }
      if (jsonObj.get("shipping_methods") != null && !jsonObj.get("shipping_methods").isJsonNull()) {
        JsonArray jsonArrayshippingMethods = jsonObj.getAsJsonArray("shipping_methods");
        if (jsonArrayshippingMethods != null) {
          // ensure the json data is an array
          if (!jsonObj.get("shipping_methods").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `shipping_methods` to be an array in the JSON string but got `%s`", jsonObj.get("shipping_methods").toString()));
          }

          // validate the optional field `shipping_methods` (array)
          for (int i = 0; i < jsonArrayshippingMethods.size(); i++) {
            ShippingMethodFreq.validateJsonElement(jsonArrayshippingMethods.get(i));
          };
        }
      }
      if ((jsonObj.get("to") != null && !jsonObj.get("to").isJsonNull()) && !jsonObj.get("to").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `to` to be a primitive type in the JSON string but got `%s`", jsonObj.get("to").toString()));
      }
      if (jsonObj.get("traffic_type") != null && !jsonObj.get("traffic_type").isJsonNull()) {
        JsonArray jsonArraytrafficType = jsonObj.getAsJsonArray("traffic_type");
        if (jsonArraytrafficType != null) {
          // ensure the json data is an array
          if (!jsonObj.get("traffic_type").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `traffic_type` to be an array in the JSON string but got `%s`", jsonObj.get("traffic_type").toString()));
          }

          // validate the optional field `traffic_type` (array)
          for (int i = 0; i < jsonArraytrafficType.size(); i++) {
            TrafficType.validateJsonElement(jsonArraytrafficType.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!StoreStats.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'StoreStats' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<StoreStats> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(StoreStats.class));

       return (TypeAdapter<T>) new TypeAdapter<StoreStats>() {
           @Override
           public void write(JsonWriter out, StoreStats value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public StoreStats read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of StoreStats given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of StoreStats
   * @throws IOException if the JSON string is invalid with respect to StoreStats
   */
  public static StoreStats fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, StoreStats.class);
  }

  /**
   * Convert an instance of StoreStats to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

