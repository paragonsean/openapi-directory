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
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import org.openapitools.client.model.CommonPlanRecurringInterval;
import org.openapitools.client.model.CommonPlanSetup;
import org.openapitools.client.model.CommonPlanTrial;
import org.openapitools.client.model.InvoiceTimeShift;
import org.openapitools.client.model.PlanPriceFormula;
import org.openapitools.client.model.SelfLink;

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
 * Plan
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:20:59.825309-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Plan {
  public static final String SERIALIZED_NAME_CREATED_TIME = "createdTime";
  @SerializedName(SERIALIZED_NAME_CREATED_TIME)
  private OffsetDateTime createdTime;

  public static final String SERIALIZED_NAME_CURRENCY = "currency";
  @SerializedName(SERIALIZED_NAME_CURRENCY)
  private String currency;

  public static final String SERIALIZED_NAME_CURRENCY_SIGN = "currencySign";
  @SerializedName(SERIALIZED_NAME_CURRENCY_SIGN)
  private String currencySign;

  public static final String SERIALIZED_NAME_CUSTOM_FIELDS = "customFields";
  @SerializedName(SERIALIZED_NAME_CUSTOM_FIELDS)
  private Object customFields = {};

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_IS_TRIAL_ONLY = "isTrialOnly";
  @SerializedName(SERIALIZED_NAME_IS_TRIAL_ONLY)
  private Boolean isTrialOnly;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_PRICING = "pricing";
  @SerializedName(SERIALIZED_NAME_PRICING)
  private PlanPriceFormula pricing;

  public static final String SERIALIZED_NAME_PRODUCT_ID = "productId";
  @SerializedName(SERIALIZED_NAME_PRODUCT_ID)
  private String productId;

  public static final String SERIALIZED_NAME_PRODUCT_OPTIONS = "productOptions";
  @SerializedName(SERIALIZED_NAME_PRODUCT_OPTIONS)
  private Map<String, String> productOptions = new HashMap<>();

  public static final String SERIALIZED_NAME_RECURRING_INTERVAL = "recurringInterval";
  @SerializedName(SERIALIZED_NAME_RECURRING_INTERVAL)
  private CommonPlanRecurringInterval recurringInterval;

  public static final String SERIALIZED_NAME_REVISION = "revision";
  @SerializedName(SERIALIZED_NAME_REVISION)
  private Integer revision;

  public static final String SERIALIZED_NAME_SETUP = "setup";
  @SerializedName(SERIALIZED_NAME_SETUP)
  private CommonPlanSetup setup;

  public static final String SERIALIZED_NAME_TRIAL = "trial";
  @SerializedName(SERIALIZED_NAME_TRIAL)
  private CommonPlanTrial trial;

  public static final String SERIALIZED_NAME_UPDATED_TIME = "updatedTime";
  @SerializedName(SERIALIZED_NAME_UPDATED_TIME)
  private OffsetDateTime updatedTime;

  public static final String SERIALIZED_NAME_LINKS = "_links";
  @SerializedName(SERIALIZED_NAME_LINKS)
  private List<SelfLink> links = new ArrayList<>();

  public static final String SERIALIZED_NAME_INVOICE_TIME_SHIFT = "invoiceTimeShift";
  @SerializedName(SERIALIZED_NAME_INVOICE_TIME_SHIFT)
  private InvoiceTimeShift invoiceTimeShift;

  public Plan() {
  }

  public Plan(
     OffsetDateTime createdTime, 
     String currencySign, 
     String id, 
     Boolean isTrialOnly, 
     Integer revision, 
     OffsetDateTime updatedTime, 
     List<SelfLink> links
  ) {
    this();
    this.createdTime = createdTime;
    this.currencySign = currencySign;
    this.id = id;
    this.isTrialOnly = isTrialOnly;
    this.revision = revision;
    this.updatedTime = updatedTime;
    this.links = links;
  }

  /**
   * Plan created time.
   * @return createdTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getCreatedTime() {
    return createdTime;
  }



  public Plan currency(String currency) {
    this.currency = currency;
    return this;
  }

  /**
   * ISO 4217 alphabetic currency code.
   * @return currency
   */
  @javax.annotation.Nonnull
  public String getCurrency() {
    return currency;
  }

  public void setCurrency(String currency) {
    this.currency = currency;
  }


  /**
   * Currency sign.
   * @return currencySign
   */
  @javax.annotation.Nullable
  public String getCurrencySign() {
    return currencySign;
  }



  public Plan customFields(Object customFields) {
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


  /**
   * The plan ID.
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }



  /**
   * Whether a plan has a trial without recurring instructions.
   * @return isTrialOnly
   */
  @javax.annotation.Nullable
  public Boolean getIsTrialOnly() {
    return isTrialOnly;
  }



  public Plan name(String name) {
    this.name = name;
    return this;
  }

  /**
   * The plan name, displayed on invoices and receipts.
   * @return name
   */
  @javax.annotation.Nonnull
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public Plan pricing(PlanPriceFormula pricing) {
    this.pricing = pricing;
    return this;
  }

  /**
   * Get pricing
   * @return pricing
   */
  @javax.annotation.Nonnull
  public PlanPriceFormula getPricing() {
    return pricing;
  }

  public void setPricing(PlanPriceFormula pricing) {
    this.pricing = pricing;
  }


  public Plan productId(String productId) {
    this.productId = productId;
    return this;
  }

  /**
   * The related product ID.
   * @return productId
   */
  @javax.annotation.Nonnull
  public String getProductId() {
    return productId;
  }

  public void setProductId(String productId) {
    this.productId = productId;
  }


  public Plan productOptions(Map<String, String> productOptions) {
    this.productOptions = productOptions;
    return this;
  }

  public Plan putProductOptionsItem(String key, String productOptionsItem) {
    if (this.productOptions == null) {
      this.productOptions = new HashMap<>();
    }
    this.productOptions.put(key, productOptionsItem);
    return this;
  }

  /**
   * Name-value pairs to specify the product options.
   * @return productOptions
   */
  @javax.annotation.Nullable
  public Map<String, String> getProductOptions() {
    return productOptions;
  }

  public void setProductOptions(Map<String, String> productOptions) {
    this.productOptions = productOptions;
  }


  public Plan recurringInterval(CommonPlanRecurringInterval recurringInterval) {
    this.recurringInterval = recurringInterval;
    return this;
  }

  /**
   * Get recurringInterval
   * @return recurringInterval
   */
  @javax.annotation.Nullable
  public CommonPlanRecurringInterval getRecurringInterval() {
    return recurringInterval;
  }

  public void setRecurringInterval(CommonPlanRecurringInterval recurringInterval) {
    this.recurringInterval = recurringInterval;
  }


  /**
   * Increments when the plan is modified.  Compare to materialized subscription items revision. 
   * @return revision
   */
  @javax.annotation.Nullable
  public Integer getRevision() {
    return revision;
  }



  public Plan setup(CommonPlanSetup setup) {
    this.setup = setup;
    return this;
  }

  /**
   * Get setup
   * @return setup
   */
  @javax.annotation.Nullable
  public CommonPlanSetup getSetup() {
    return setup;
  }

  public void setSetup(CommonPlanSetup setup) {
    this.setup = setup;
  }


  public Plan trial(CommonPlanTrial trial) {
    this.trial = trial;
    return this;
  }

  /**
   * Get trial
   * @return trial
   */
  @javax.annotation.Nullable
  public CommonPlanTrial getTrial() {
    return trial;
  }

  public void setTrial(CommonPlanTrial trial) {
    this.trial = trial;
  }


  /**
   * Plan updated time.
   * @return updatedTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getUpdatedTime() {
    return updatedTime;
  }



  /**
   * The links related to resource.
   * @return links
   */
  @javax.annotation.Nullable
  public List<SelfLink> getLinks() {
    return links;
  }



  public Plan invoiceTimeShift(InvoiceTimeShift invoiceTimeShift) {
    this.invoiceTimeShift = invoiceTimeShift;
    return this;
  }

  /**
   * You can shift issue time and due time of invoices for this plan.
   * @return invoiceTimeShift
   */
  @javax.annotation.Nullable
  public InvoiceTimeShift getInvoiceTimeShift() {
    return invoiceTimeShift;
  }

  public void setInvoiceTimeShift(InvoiceTimeShift invoiceTimeShift) {
    this.invoiceTimeShift = invoiceTimeShift;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Plan plan = (Plan) o;
    return Objects.equals(this.createdTime, plan.createdTime) &&
        Objects.equals(this.currency, plan.currency) &&
        Objects.equals(this.currencySign, plan.currencySign) &&
        Objects.equals(this.customFields, plan.customFields) &&
        Objects.equals(this.id, plan.id) &&
        Objects.equals(this.isTrialOnly, plan.isTrialOnly) &&
        Objects.equals(this.name, plan.name) &&
        Objects.equals(this.pricing, plan.pricing) &&
        Objects.equals(this.productId, plan.productId) &&
        Objects.equals(this.productOptions, plan.productOptions) &&
        Objects.equals(this.recurringInterval, plan.recurringInterval) &&
        Objects.equals(this.revision, plan.revision) &&
        Objects.equals(this.setup, plan.setup) &&
        Objects.equals(this.trial, plan.trial) &&
        Objects.equals(this.updatedTime, plan.updatedTime) &&
        Objects.equals(this.links, plan.links) &&
        Objects.equals(this.invoiceTimeShift, plan.invoiceTimeShift);
  }

  @Override
  public int hashCode() {
    return Objects.hash(createdTime, currency, currencySign, customFields, id, isTrialOnly, name, pricing, productId, productOptions, recurringInterval, revision, setup, trial, updatedTime, links, invoiceTimeShift);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Plan {\n");
    sb.append("    createdTime: ").append(toIndentedString(createdTime)).append("\n");
    sb.append("    currency: ").append(toIndentedString(currency)).append("\n");
    sb.append("    currencySign: ").append(toIndentedString(currencySign)).append("\n");
    sb.append("    customFields: ").append(toIndentedString(customFields)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    isTrialOnly: ").append(toIndentedString(isTrialOnly)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    pricing: ").append(toIndentedString(pricing)).append("\n");
    sb.append("    productId: ").append(toIndentedString(productId)).append("\n");
    sb.append("    productOptions: ").append(toIndentedString(productOptions)).append("\n");
    sb.append("    recurringInterval: ").append(toIndentedString(recurringInterval)).append("\n");
    sb.append("    revision: ").append(toIndentedString(revision)).append("\n");
    sb.append("    setup: ").append(toIndentedString(setup)).append("\n");
    sb.append("    trial: ").append(toIndentedString(trial)).append("\n");
    sb.append("    updatedTime: ").append(toIndentedString(updatedTime)).append("\n");
    sb.append("    links: ").append(toIndentedString(links)).append("\n");
    sb.append("    invoiceTimeShift: ").append(toIndentedString(invoiceTimeShift)).append("\n");
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
    openapiFields.add("createdTime");
    openapiFields.add("currency");
    openapiFields.add("currencySign");
    openapiFields.add("customFields");
    openapiFields.add("id");
    openapiFields.add("isTrialOnly");
    openapiFields.add("name");
    openapiFields.add("pricing");
    openapiFields.add("productId");
    openapiFields.add("productOptions");
    openapiFields.add("recurringInterval");
    openapiFields.add("revision");
    openapiFields.add("setup");
    openapiFields.add("trial");
    openapiFields.add("updatedTime");
    openapiFields.add("_links");
    openapiFields.add("invoiceTimeShift");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("currency");
    openapiRequiredFields.add("name");
    openapiRequiredFields.add("pricing");
    openapiRequiredFields.add("productId");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Plan
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Plan.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Plan is not found in the empty JSON string", Plan.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Plan.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Plan` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : Plan.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("currency").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `currency` to be a primitive type in the JSON string but got `%s`", jsonObj.get("currency").toString()));
      }
      if ((jsonObj.get("currencySign") != null && !jsonObj.get("currencySign").isJsonNull()) && !jsonObj.get("currencySign").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `currencySign` to be a primitive type in the JSON string but got `%s`", jsonObj.get("currencySign").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if (!jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      // validate the required field `pricing`
      PlanPriceFormula.validateJsonElement(jsonObj.get("pricing"));
      if (!jsonObj.get("productId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `productId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("productId").toString()));
      }
      // validate the optional field `recurringInterval`
      if (jsonObj.get("recurringInterval") != null && !jsonObj.get("recurringInterval").isJsonNull()) {
        CommonPlanRecurringInterval.validateJsonElement(jsonObj.get("recurringInterval"));
      }
      // validate the optional field `setup`
      if (jsonObj.get("setup") != null && !jsonObj.get("setup").isJsonNull()) {
        CommonPlanSetup.validateJsonElement(jsonObj.get("setup"));
      }
      // validate the optional field `trial`
      if (jsonObj.get("trial") != null && !jsonObj.get("trial").isJsonNull()) {
        CommonPlanTrial.validateJsonElement(jsonObj.get("trial"));
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
            SelfLink.validateJsonElement(jsonArraylinks.get(i));
          };
        }
      }
      // validate the optional field `invoiceTimeShift`
      if (jsonObj.get("invoiceTimeShift") != null && !jsonObj.get("invoiceTimeShift").isJsonNull()) {
        InvoiceTimeShift.validateJsonElement(jsonObj.get("invoiceTimeShift"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Plan.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Plan' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Plan> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Plan.class));

       return (TypeAdapter<T>) new TypeAdapter<Plan>() {
           @Override
           public void write(JsonWriter out, Plan value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Plan read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Plan given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Plan
   * @throws IOException if the JSON string is invalid with respect to Plan
   */
  public static Plan fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Plan.class);
  }

  /**
   * Convert an instance of Plan to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

