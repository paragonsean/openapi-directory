/*
 * Rebilly REST API
 * # Introduction The Rebilly API is built on HTTP.  Our API is RESTful.  It has predictable resource URLs.  It returns HTTP response codes to indicate errors.  It also accepts and returns JSON in the HTTP body.  You can use your favorite HTTP/REST library for your programming language to use Rebilly's API, or you can use one of our SDKs (currently available in [PHP](https://github.com/Rebilly/rebilly-php) and [Javascript](https://github.com/Rebilly/rebilly-js-sdk)).  We have other APIs that are also available.  Every action from our [app](https://app.rebilly.com) is supported by an API which is documented and available for use so that you may automate any workflows necessary.  This document contains the most commonly integrated resources.  # Authentication  When you sign up for an account, you are given your first secret API key. You can generate additional API keys, and delete API keys (as you may need to rotate your keys in the future). You authenticate to the Rebilly API by providing your secret key in the request header.  Rebilly offers three forms of authentication:  secret key, publishable key, JSON Web Tokens, and public signature key. - [Secret API key](#section/Authentication/SecretApiKey): used for requests made   from the server side. Never share these keys. Keep them guarded and secure. - [Publishable API key](#section/Authentication/PublishableApiKey): used for    requests from the client side. For now can only be used to create    a [Payment Token](#operation/PostToken) and    a [File token](#operation/PostFile). - [JWT](#section/Authentication/JWT): short lifetime tokens that can be assigned a specific expiration time.  Never share your secret keys. Keep them guarded and secure.  &lt;!-- ReDoc-Inject: &lt;security-definitions&gt; --&gt;  # Errors Rebilly follow's the error response format proposed in [RFC 7807](https://tools.ietf.org/html/rfc7807) also known as Problem Details for HTTP APIs.  As with our normal API responses, your client must be prepared to gracefully handle additional members of the response.  ## Forbidden &lt;RedocResponse pointer={\"#/components/responses/Forbidden\"} /&gt;  ## Conflict &lt;RedocResponse pointer={\"#/components/responses/Conflict\"} /&gt;  ## NotFound &lt;RedocResponse pointer={\"#/components/responses/NotFound\"} /&gt;  ## Unauthorized &lt;RedocResponse pointer={\"#/components/responses/Unauthorized\"} /&gt;  ## ValidationError &lt;RedocResponse pointer={\"#/components/responses/ValidationError\"} /&gt;  # SDKs  Rebilly offers a Javascript SDK and a PHP SDK to help interact with the API.  However, no SDK is required to use the API.  Rebilly also offers [FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/),  a client-side iFrame-based solution to help create payment tokens while minimizing PCI DSS compliance burdens and maximizing the customizability. [FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/) is interacting with the [payment tokens creation operation](#operation/PostToken).  ## Javascript SDK  Installation and usage instructions can be found [here](https://docs.rebilly.com/docs/developer-docs/sdks). SDK code examples are included in these docs.  ## PHP SDK For all PHP SDK examples provided in these docs you will need to configure the `$client`. You may do it like this:  ```php $client = new Rebilly\\Client([     'apiKey' =&gt; 'YourApiKeyHere',     'baseUrl' =&gt; 'https://api.rebilly.com', ]); ```  # Using filter with collections Rebilly provides collections filtering. You can use `?filter` param on collections to define which records should be shown in the response.  Here is filter format description:  - Fields and values in filter are separated with `:`: `?filter=firstName:John`.  - Sub-fields are separated with `.`: `?filter=billingAddress.country:US`.  - Multiple filters are separated with `;`: `?filter=firstName:John;lastName:Doe`. They will be joined with `AND` logic. In this example: `firstName:John` AND `lastName:Doe`.  - You can use multiple values using `,` as values separator: `?filter=firstName:John,Bob`. Multiple values specified for a field will be joined with `OR` logic. In this example: `firstName:John` OR `firstName:Bob`.  - To negate the filter use `!`: `?filter=firstName:!John`. Note that you can negate multiple values like this: `?filter=firstName:!John,!Bob`. This filter rule will exclude all Johns and Bobs from the response.  - You can use range filters like this: `?filter=amount:1..10`.  - You can use gte (greater than or equals) filter like this: `?filter=amount:1..`, or lte (less than or equals) than filter like this: `?filter=amount:..10`. This also works for datetime-based fields.  - You can create some [predefined values lists](https://user-api-docs.rebilly.com/#tag/Lists) and use them in filter: `?filter=firstName:@yourListName`. You can also exclude list values: `?filter=firstName:!@yourListName`.  - Datetime-based fields accept values formatted using RFC 3339 like this: `?filter=createdTime:2021-02-14T13:30:00Z`.   # Expand to include embedded objects Rebilly provides the ability to pre-load additional  objects with a request.   You can use `?expand` param on most requests to expand and include embedded objects within the `_embedded` property of the response.  The `_embedded` property contains an array of  objects keyed by the expand parameter value(s).  You may expand multiple objects by passing them as comma-separated to the expand value like so:  ``` ?expand=recentInvoice,customer ```  And in the response, you would see:  ``` \"_embedded\": [     \"recentInvoice\": {...},     \"customer\": {...} ] ``` Expand may be utilitized not only on `GET` requests but also on `PATCH`, `POST`, `PUT` requests too.   # Getting started guide  Rebilly's API has over 300 operations.  That's more than you'll  need to implement your use cases.  If you have a use  case you would like to implement, please consult us for feedback on the best API operations for the task.  Our getting started guide will demonstrate a basic order form use case.  It will allow us to highlight core resources in Rebilly that will be helpful for many other use cases too.  Within 25 minutes, you'll have sent API requests (via our console) to create a subscription order. 
 *
 * The version of the OpenAPI document: 2.1
 * Contact: integrations@rebilly.com
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
import org.openapitools.client.model.Customer;
import org.openapitools.client.model.Invoice;
import org.openapitools.client.model.Subscription;
import org.openapitools.client.model.Transaction;

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
 * Search
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:20:59.825309-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Search {
  public static final String SERIALIZED_NAME_CUSTOMERS = "customers";
  @SerializedName(SERIALIZED_NAME_CUSTOMERS)
  private List<Customer> customers = new ArrayList<>();

  public static final String SERIALIZED_NAME_INVOICES = "invoices";
  @SerializedName(SERIALIZED_NAME_INVOICES)
  private List<Invoice> invoices = new ArrayList<>();

  public static final String SERIALIZED_NAME_ORDERS = "orders";
  @SerializedName(SERIALIZED_NAME_ORDERS)
  private List<Subscription> orders = new ArrayList<>();

  public static final String SERIALIZED_NAME_SEARCHED = "searched";
  @SerializedName(SERIALIZED_NAME_SEARCHED)
  private List<String> searched = new ArrayList<>();

  public static final String SERIALIZED_NAME_TRANSACTIONS = "transactions";
  @SerializedName(SERIALIZED_NAME_TRANSACTIONS)
  private List<Transaction> transactions = new ArrayList<>();

  public Search() {
  }

  public Search(
     List<Customer> customers, 
     List<Invoice> invoices, 
     List<Subscription> orders, 
     List<String> searched, 
     List<Transaction> transactions
  ) {
    this();
    this.customers = customers;
    this.invoices = invoices;
    this.orders = orders;
    this.searched = searched;
    this.transactions = transactions;
  }

  /**
   * List of returned customers.
   * @return customers
   */
  @javax.annotation.Nullable
  public List<Customer> getCustomers() {
    return customers;
  }



  /**
   * List of returned invoices.
   * @return invoices
   */
  @javax.annotation.Nullable
  public List<Invoice> getInvoices() {
    return invoices;
  }



  /**
   * List of returned orders.
   * @return orders
   */
  @javax.annotation.Nullable
  public List<Subscription> getOrders() {
    return orders;
  }



  /**
   * Names of searched resources, even if they returned nothing.
   * @return searched
   */
  @javax.annotation.Nullable
  public List<String> getSearched() {
    return searched;
  }



  /**
   * List of returned transactions.
   * @return transactions
   */
  @javax.annotation.Nullable
  public List<Transaction> getTransactions() {
    return transactions;
  }




  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Search search = (Search) o;
    return Objects.equals(this.customers, search.customers) &&
        Objects.equals(this.invoices, search.invoices) &&
        Objects.equals(this.orders, search.orders) &&
        Objects.equals(this.searched, search.searched) &&
        Objects.equals(this.transactions, search.transactions);
  }

  @Override
  public int hashCode() {
    return Objects.hash(customers, invoices, orders, searched, transactions);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Search {\n");
    sb.append("    customers: ").append(toIndentedString(customers)).append("\n");
    sb.append("    invoices: ").append(toIndentedString(invoices)).append("\n");
    sb.append("    orders: ").append(toIndentedString(orders)).append("\n");
    sb.append("    searched: ").append(toIndentedString(searched)).append("\n");
    sb.append("    transactions: ").append(toIndentedString(transactions)).append("\n");
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
    openapiFields.add("customers");
    openapiFields.add("invoices");
    openapiFields.add("orders");
    openapiFields.add("searched");
    openapiFields.add("transactions");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Search
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Search.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Search is not found in the empty JSON string", Search.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Search.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Search` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("customers") != null && !jsonObj.get("customers").isJsonNull()) {
        JsonArray jsonArraycustomers = jsonObj.getAsJsonArray("customers");
        if (jsonArraycustomers != null) {
          // ensure the json data is an array
          if (!jsonObj.get("customers").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `customers` to be an array in the JSON string but got `%s`", jsonObj.get("customers").toString()));
          }

          // validate the optional field `customers` (array)
          for (int i = 0; i < jsonArraycustomers.size(); i++) {
            Customer.validateJsonElement(jsonArraycustomers.get(i));
          };
        }
      }
      if (jsonObj.get("invoices") != null && !jsonObj.get("invoices").isJsonNull()) {
        JsonArray jsonArrayinvoices = jsonObj.getAsJsonArray("invoices");
        if (jsonArrayinvoices != null) {
          // ensure the json data is an array
          if (!jsonObj.get("invoices").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `invoices` to be an array in the JSON string but got `%s`", jsonObj.get("invoices").toString()));
          }

          // validate the optional field `invoices` (array)
          for (int i = 0; i < jsonArrayinvoices.size(); i++) {
            Invoice.validateJsonElement(jsonArrayinvoices.get(i));
          };
        }
      }
      if (jsonObj.get("orders") != null && !jsonObj.get("orders").isJsonNull()) {
        JsonArray jsonArrayorders = jsonObj.getAsJsonArray("orders");
        if (jsonArrayorders != null) {
          // ensure the json data is an array
          if (!jsonObj.get("orders").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `orders` to be an array in the JSON string but got `%s`", jsonObj.get("orders").toString()));
          }

          // validate the optional field `orders` (array)
          for (int i = 0; i < jsonArrayorders.size(); i++) {
            Subscription.validateJsonElement(jsonArrayorders.get(i));
          };
        }
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("searched") != null && !jsonObj.get("searched").isJsonNull() && !jsonObj.get("searched").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `searched` to be an array in the JSON string but got `%s`", jsonObj.get("searched").toString()));
      }
      if (jsonObj.get("transactions") != null && !jsonObj.get("transactions").isJsonNull()) {
        JsonArray jsonArraytransactions = jsonObj.getAsJsonArray("transactions");
        if (jsonArraytransactions != null) {
          // ensure the json data is an array
          if (!jsonObj.get("transactions").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `transactions` to be an array in the JSON string but got `%s`", jsonObj.get("transactions").toString()));
          }

          // validate the optional field `transactions` (array)
          for (int i = 0; i < jsonArraytransactions.size(); i++) {
            Transaction.validateJsonElement(jsonArraytransactions.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Search.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Search' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Search> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Search.class));

       return (TypeAdapter<T>) new TypeAdapter<Search>() {
           @Override
           public void write(JsonWriter out, Search value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Search read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Search given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Search
   * @throws IOException if the JSON string is invalid with respect to Search
   */
  public static Search fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Search.class);
  }

  /**
   * Convert an instance of Search to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

