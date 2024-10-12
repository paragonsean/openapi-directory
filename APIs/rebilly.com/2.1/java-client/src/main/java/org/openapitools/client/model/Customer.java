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
import java.time.OffsetDateTime;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.ContactObject;
import org.openapitools.client.model.CustomerAverageValue;
import org.openapitools.client.model.CustomerEmbeddedInner;
import org.openapitools.client.model.CustomerLifetimeRevenue;
import org.openapitools.client.model.CustomerLinksInner;
import org.openapitools.client.model.PaymentInstrument;
import org.openapitools.client.model.Tag;

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
 * Customer
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:20:59.825309-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Customer {
  public static final String SERIALIZED_NAME_EMBEDDED = "_embedded";
  @SerializedName(SERIALIZED_NAME_EMBEDDED)
  private List<CustomerEmbeddedInner> embedded = new ArrayList<>();

  public static final String SERIALIZED_NAME_LINKS = "_links";
  @SerializedName(SERIALIZED_NAME_LINKS)
  private List<CustomerLinksInner> links = new ArrayList<>();

  public static final String SERIALIZED_NAME_AVERAGE_VALUE = "averageValue";
  @SerializedName(SERIALIZED_NAME_AVERAGE_VALUE)
  private CustomerAverageValue averageValue;

  public static final String SERIALIZED_NAME_CREATED_TIME = "createdTime";
  @SerializedName(SERIALIZED_NAME_CREATED_TIME)
  private OffsetDateTime createdTime;

  public static final String SERIALIZED_NAME_CUSTOM_FIELDS = "customFields";
  @SerializedName(SERIALIZED_NAME_CUSTOM_FIELDS)
  private Object customFields = {};

  public static final String SERIALIZED_NAME_DEFAULT_PAYMENT_INSTRUMENT = "defaultPaymentInstrument";
  @SerializedName(SERIALIZED_NAME_DEFAULT_PAYMENT_INSTRUMENT)
  private PaymentInstrument defaultPaymentInstrument;

  public static final String SERIALIZED_NAME_EMAIL = "email";
  @SerializedName(SERIALIZED_NAME_EMAIL)
  private String email;

  public static final String SERIALIZED_NAME_FIRST_NAME = "firstName";
  @SerializedName(SERIALIZED_NAME_FIRST_NAME)
  private String firstName;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_INVOICE_COUNT = "invoiceCount";
  @SerializedName(SERIALIZED_NAME_INVOICE_COUNT)
  private Integer invoiceCount;

  public static final String SERIALIZED_NAME_LAST_NAME = "lastName";
  @SerializedName(SERIALIZED_NAME_LAST_NAME)
  private String lastName;

  public static final String SERIALIZED_NAME_LAST_PAYMENT_TIME = "lastPaymentTime";
  @SerializedName(SERIALIZED_NAME_LAST_PAYMENT_TIME)
  private OffsetDateTime lastPaymentTime;

  public static final String SERIALIZED_NAME_LIFETIME_REVENUE = "lifetimeRevenue";
  @SerializedName(SERIALIZED_NAME_LIFETIME_REVENUE)
  private CustomerLifetimeRevenue lifetimeRevenue;

  public static final String SERIALIZED_NAME_PAYMENT_COUNT = "paymentCount";
  @SerializedName(SERIALIZED_NAME_PAYMENT_COUNT)
  private Integer paymentCount;

  public static final String SERIALIZED_NAME_PAYMENT_TOKEN = "paymentToken";
  @SerializedName(SERIALIZED_NAME_PAYMENT_TOKEN)
  private String paymentToken;

  public static final String SERIALIZED_NAME_PRIMARY_ADDRESS = "primaryAddress";
  @SerializedName(SERIALIZED_NAME_PRIMARY_ADDRESS)
  private ContactObject primaryAddress;

  public static final String SERIALIZED_NAME_REVISION = "revision";
  @SerializedName(SERIALIZED_NAME_REVISION)
  private Integer revision;

  public static final String SERIALIZED_NAME_TAGS = "tags";
  @SerializedName(SERIALIZED_NAME_TAGS)
  private List<Tag> tags = new ArrayList<>();

  public static final String SERIALIZED_NAME_UPDATED_TIME = "updatedTime";
  @SerializedName(SERIALIZED_NAME_UPDATED_TIME)
  private OffsetDateTime updatedTime;

  public static final String SERIALIZED_NAME_WEBSITE_ID = "websiteId";
  @SerializedName(SERIALIZED_NAME_WEBSITE_ID)
  private String websiteId;

  public Customer() {
  }

  public Customer(
     List<CustomerEmbeddedInner> embedded, 
     List<CustomerLinksInner> links, 
     OffsetDateTime createdTime, 
     String email, 
     String firstName, 
     String id, 
     Integer invoiceCount, 
     String lastName, 
     OffsetDateTime lastPaymentTime, 
     Integer paymentCount, 
     Integer revision, 
     List<Tag> tags, 
     OffsetDateTime updatedTime
  ) {
    this();
    this.embedded = embedded;
    this.links = links;
    this.createdTime = createdTime;
    this.email = email;
    this.firstName = firstName;
    this.id = id;
    this.invoiceCount = invoiceCount;
    this.lastName = lastName;
    this.lastPaymentTime = lastPaymentTime;
    this.paymentCount = paymentCount;
    this.revision = revision;
    this.tags = tags;
    this.updatedTime = updatedTime;
  }

  /**
   * Any embedded objects available that are requested by the &#x60;expand&#x60; querystring parameter.
   * @return embedded
   */
  @javax.annotation.Nullable
  public List<CustomerEmbeddedInner> getEmbedded() {
    return embedded;
  }



  /**
   * The links related to resource.
   * @return links
   */
  @javax.annotation.Nullable
  public List<CustomerLinksInner> getLinks() {
    return links;
  }



  public Customer averageValue(CustomerAverageValue averageValue) {
    this.averageValue = averageValue;
    return this;
  }

  /**
   * Get averageValue
   * @return averageValue
   */
  @javax.annotation.Nullable
  public CustomerAverageValue getAverageValue() {
    return averageValue;
  }

  public void setAverageValue(CustomerAverageValue averageValue) {
    this.averageValue = averageValue;
  }


  /**
   * The customer created time.
   * @return createdTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getCreatedTime() {
    return createdTime;
  }



  public Customer customFields(Object customFields) {
    this.customFields = customFields;
    return this;
  }

  /**
   * Custom Fields list as a map &#x60;{\&quot;custom field name\&quot;: \&quot;custom field value\&quot;, ...}&#x60;. The format must follow the saved format (see Custom Fields section for the formats). 
   * @return customFields
   */
  @javax.annotation.Nullable
  public Object getCustomFields() {
    return customFields;
  }

  public void setCustomFields(Object customFields) {
    this.customFields = customFields;
  }


  public Customer defaultPaymentInstrument(PaymentInstrument defaultPaymentInstrument) {
    this.defaultPaymentInstrument = defaultPaymentInstrument;
    return this;
  }

  /**
   * Get defaultPaymentInstrument
   * @return defaultPaymentInstrument
   */
  @javax.annotation.Nullable
  public PaymentInstrument getDefaultPaymentInstrument() {
    return defaultPaymentInstrument;
  }

  public void setDefaultPaymentInstrument(PaymentInstrument defaultPaymentInstrument) {
    this.defaultPaymentInstrument = defaultPaymentInstrument;
  }


  /**
   * The customer&#39;s email.
   * @return email
   */
  @javax.annotation.Nullable
  public String getEmail() {
    return email;
  }



  /**
   * The customer&#39;s first name.
   * @return firstName
   */
  @javax.annotation.Nullable
  public String getFirstName() {
    return firstName;
  }



  /**
   * The customer identifier string.
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }



  /**
   * An auto-incrementing number based on the sequence of invoices. If set to 0, then this record is a Lead, otherwise is a Customer.
   * @return invoiceCount
   */
  @javax.annotation.Nullable
  public Integer getInvoiceCount() {
    return invoiceCount;
  }



  /**
   * The customer&#39;s last name.
   * @return lastName
   */
  @javax.annotation.Nullable
  public String getLastName() {
    return lastName;
  }



  /**
   * The most recent time of an approved payment for the customer.
   * @return lastPaymentTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getLastPaymentTime() {
    return lastPaymentTime;
  }



  public Customer lifetimeRevenue(CustomerLifetimeRevenue lifetimeRevenue) {
    this.lifetimeRevenue = lifetimeRevenue;
    return this;
  }

  /**
   * Get lifetimeRevenue
   * @return lifetimeRevenue
   */
  @javax.annotation.Nullable
  public CustomerLifetimeRevenue getLifetimeRevenue() {
    return lifetimeRevenue;
  }

  public void setLifetimeRevenue(CustomerLifetimeRevenue lifetimeRevenue) {
    this.lifetimeRevenue = lifetimeRevenue;
  }


  /**
   * The number of approved payments for the customer.
   * @return paymentCount
   */
  @javax.annotation.Nullable
  public Integer getPaymentCount() {
    return paymentCount;
  }



  public Customer paymentToken(String paymentToken) {
    this.paymentToken = paymentToken;
    return this;
  }

  /**
   * A write-only payment token; if supplied, it will be converted into a payment instrument and be set as the &#x60;defaultPaymentInstrument&#x60;. The value of this property will override the &#x60;defaultPaymentInstrument&#x60; in the case that both are supplied. The token may only be used once before it is expired. 
   * @return paymentToken
   */
  @javax.annotation.Nullable
  public String getPaymentToken() {
    return paymentToken;
  }

  public void setPaymentToken(String paymentToken) {
    this.paymentToken = paymentToken;
  }


  public Customer primaryAddress(ContactObject primaryAddress) {
    this.primaryAddress = primaryAddress;
    return this;
  }

  /**
   * Get primaryAddress
   * @return primaryAddress
   */
  @javax.annotation.Nullable
  public ContactObject getPrimaryAddress() {
    return primaryAddress;
  }

  public void setPrimaryAddress(ContactObject primaryAddress) {
    this.primaryAddress = primaryAddress;
  }


  /**
   * The number of times the customer data has been modified. The revision is useful when analyzing webhook data to determine if the change takes precedence over the current representation. 
   * @return revision
   */
  @javax.annotation.Nullable
  public Integer getRevision() {
    return revision;
  }



  /**
   * A list of customer&#39;s tags.
   * @return tags
   */
  @javax.annotation.Nullable
  public List<Tag> getTags() {
    return tags;
  }



  /**
   * The customer updated time.
   * @return updatedTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getUpdatedTime() {
    return updatedTime;
  }



  public Customer websiteId(String websiteId) {
    this.websiteId = websiteId;
    return this;
  }

  /**
   * The website&#39;s ID.
   * @return websiteId
   */
  @javax.annotation.Nullable
  public String getWebsiteId() {
    return websiteId;
  }

  public void setWebsiteId(String websiteId) {
    this.websiteId = websiteId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Customer customer = (Customer) o;
    return Objects.equals(this.embedded, customer.embedded) &&
        Objects.equals(this.links, customer.links) &&
        Objects.equals(this.averageValue, customer.averageValue) &&
        Objects.equals(this.createdTime, customer.createdTime) &&
        Objects.equals(this.customFields, customer.customFields) &&
        Objects.equals(this.defaultPaymentInstrument, customer.defaultPaymentInstrument) &&
        Objects.equals(this.email, customer.email) &&
        Objects.equals(this.firstName, customer.firstName) &&
        Objects.equals(this.id, customer.id) &&
        Objects.equals(this.invoiceCount, customer.invoiceCount) &&
        Objects.equals(this.lastName, customer.lastName) &&
        Objects.equals(this.lastPaymentTime, customer.lastPaymentTime) &&
        Objects.equals(this.lifetimeRevenue, customer.lifetimeRevenue) &&
        Objects.equals(this.paymentCount, customer.paymentCount) &&
        Objects.equals(this.paymentToken, customer.paymentToken) &&
        Objects.equals(this.primaryAddress, customer.primaryAddress) &&
        Objects.equals(this.revision, customer.revision) &&
        Objects.equals(this.tags, customer.tags) &&
        Objects.equals(this.updatedTime, customer.updatedTime) &&
        Objects.equals(this.websiteId, customer.websiteId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(embedded, links, averageValue, createdTime, customFields, defaultPaymentInstrument, email, firstName, id, invoiceCount, lastName, lastPaymentTime, lifetimeRevenue, paymentCount, paymentToken, primaryAddress, revision, tags, updatedTime, websiteId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Customer {\n");
    sb.append("    embedded: ").append(toIndentedString(embedded)).append("\n");
    sb.append("    links: ").append(toIndentedString(links)).append("\n");
    sb.append("    averageValue: ").append(toIndentedString(averageValue)).append("\n");
    sb.append("    createdTime: ").append(toIndentedString(createdTime)).append("\n");
    sb.append("    customFields: ").append(toIndentedString(customFields)).append("\n");
    sb.append("    defaultPaymentInstrument: ").append(toIndentedString(defaultPaymentInstrument)).append("\n");
    sb.append("    email: ").append(toIndentedString(email)).append("\n");
    sb.append("    firstName: ").append(toIndentedString(firstName)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    invoiceCount: ").append(toIndentedString(invoiceCount)).append("\n");
    sb.append("    lastName: ").append(toIndentedString(lastName)).append("\n");
    sb.append("    lastPaymentTime: ").append(toIndentedString(lastPaymentTime)).append("\n");
    sb.append("    lifetimeRevenue: ").append(toIndentedString(lifetimeRevenue)).append("\n");
    sb.append("    paymentCount: ").append(toIndentedString(paymentCount)).append("\n");
    sb.append("    paymentToken: ").append(toIndentedString(paymentToken)).append("\n");
    sb.append("    primaryAddress: ").append(toIndentedString(primaryAddress)).append("\n");
    sb.append("    revision: ").append(toIndentedString(revision)).append("\n");
    sb.append("    tags: ").append(toIndentedString(tags)).append("\n");
    sb.append("    updatedTime: ").append(toIndentedString(updatedTime)).append("\n");
    sb.append("    websiteId: ").append(toIndentedString(websiteId)).append("\n");
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
    openapiFields.add("_embedded");
    openapiFields.add("_links");
    openapiFields.add("averageValue");
    openapiFields.add("createdTime");
    openapiFields.add("customFields");
    openapiFields.add("defaultPaymentInstrument");
    openapiFields.add("email");
    openapiFields.add("firstName");
    openapiFields.add("id");
    openapiFields.add("invoiceCount");
    openapiFields.add("lastName");
    openapiFields.add("lastPaymentTime");
    openapiFields.add("lifetimeRevenue");
    openapiFields.add("paymentCount");
    openapiFields.add("paymentToken");
    openapiFields.add("primaryAddress");
    openapiFields.add("revision");
    openapiFields.add("tags");
    openapiFields.add("updatedTime");
    openapiFields.add("websiteId");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Customer
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Customer.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Customer is not found in the empty JSON string", Customer.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Customer.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Customer` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("_embedded") != null && !jsonObj.get("_embedded").isJsonNull()) {
        JsonArray jsonArrayembedded = jsonObj.getAsJsonArray("_embedded");
        if (jsonArrayembedded != null) {
          // ensure the json data is an array
          if (!jsonObj.get("_embedded").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `_embedded` to be an array in the JSON string but got `%s`", jsonObj.get("_embedded").toString()));
          }

          // validate the optional field `_embedded` (array)
          for (int i = 0; i < jsonArrayembedded.size(); i++) {
            CustomerEmbeddedInner.validateJsonElement(jsonArrayembedded.get(i));
          };
        }
      }
      if (jsonObj.get("_links") != null && !jsonObj.get("_links").isJsonNull()) {
        JsonArray jsonArraylinks = jsonObj.getAsJsonArray("_links");
        if (jsonArraylinks != null) {
          // ensure the json data is an array
          if (!jsonObj.get("_links").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `_links` to be an array in the JSON string but got `%s`", jsonObj.get("_links").toString()));
          }

          // validate the optional field `_links` (array)
          for (int i = 0; i < jsonArraylinks.size(); i++) {
            CustomerLinksInner.validateJsonElement(jsonArraylinks.get(i));
          };
        }
      }
      // validate the optional field `averageValue`
      if (jsonObj.get("averageValue") != null && !jsonObj.get("averageValue").isJsonNull()) {
        CustomerAverageValue.validateJsonElement(jsonObj.get("averageValue"));
      }
      // validate the optional field `defaultPaymentInstrument`
      if (jsonObj.get("defaultPaymentInstrument") != null && !jsonObj.get("defaultPaymentInstrument").isJsonNull()) {
        PaymentInstrument.validateJsonElement(jsonObj.get("defaultPaymentInstrument"));
      }
      if ((jsonObj.get("email") != null && !jsonObj.get("email").isJsonNull()) && !jsonObj.get("email").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `email` to be a primitive type in the JSON string but got `%s`", jsonObj.get("email").toString()));
      }
      if ((jsonObj.get("firstName") != null && !jsonObj.get("firstName").isJsonNull()) && !jsonObj.get("firstName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `firstName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("firstName").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("lastName") != null && !jsonObj.get("lastName").isJsonNull()) && !jsonObj.get("lastName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `lastName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("lastName").toString()));
      }
      // validate the optional field `lifetimeRevenue`
      if (jsonObj.get("lifetimeRevenue") != null && !jsonObj.get("lifetimeRevenue").isJsonNull()) {
        CustomerLifetimeRevenue.validateJsonElement(jsonObj.get("lifetimeRevenue"));
      }
      if ((jsonObj.get("paymentToken") != null && !jsonObj.get("paymentToken").isJsonNull()) && !jsonObj.get("paymentToken").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `paymentToken` to be a primitive type in the JSON string but got `%s`", jsonObj.get("paymentToken").toString()));
      }
      // validate the optional field `primaryAddress`
      if (jsonObj.get("primaryAddress") != null && !jsonObj.get("primaryAddress").isJsonNull()) {
        ContactObject.validateJsonElement(jsonObj.get("primaryAddress"));
      }
      if (jsonObj.get("tags") != null && !jsonObj.get("tags").isJsonNull()) {
        JsonArray jsonArraytags = jsonObj.getAsJsonArray("tags");
        if (jsonArraytags != null) {
          // ensure the json data is an array
          if (!jsonObj.get("tags").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `tags` to be an array in the JSON string but got `%s`", jsonObj.get("tags").toString()));
          }

          // validate the optional field `tags` (array)
          for (int i = 0; i < jsonArraytags.size(); i++) {
            Tag.validateJsonElement(jsonArraytags.get(i));
          };
        }
      }
      if ((jsonObj.get("websiteId") != null && !jsonObj.get("websiteId").isJsonNull()) && !jsonObj.get("websiteId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `websiteId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("websiteId").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Customer.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Customer' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Customer> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Customer.class));

       return (TypeAdapter<T>) new TypeAdapter<Customer>() {
           @Override
           public void write(JsonWriter out, Customer value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Customer read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Customer given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Customer
   * @throws IOException if the JSON string is invalid with respect to Customer
   */
  public static Customer fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Customer.class);
  }

  /**
   * Convert an instance of Customer to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

