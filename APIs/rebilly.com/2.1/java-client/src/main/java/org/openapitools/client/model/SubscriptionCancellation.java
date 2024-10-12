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
import java.math.BigDecimal;
import java.time.OffsetDateTime;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.SelfLink;
import org.openapitools.client.model.UpcomingInvoiceItem;

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
 * SubscriptionCancellation
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:20:59.825309-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class SubscriptionCancellation {
  public static final String SERIALIZED_NAME_LINKS = "_links";
  @SerializedName(SERIALIZED_NAME_LINKS)
  private List<SelfLink> links = new ArrayList<>();

  public static final String SERIALIZED_NAME_APPLIED_INVOICE_ID = "appliedInvoiceId";
  @SerializedName(SERIALIZED_NAME_APPLIED_INVOICE_ID)
  private String appliedInvoiceId;

  /**
   * Who did the cancellation.
   */
  @JsonAdapter(CanceledByEnum.Adapter.class)
  public enum CanceledByEnum {
    MERCHANT("merchant"),
    
    CUSTOMER("customer");

    private String value;

    CanceledByEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static CanceledByEnum fromValue(String value) {
      for (CanceledByEnum b : CanceledByEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<CanceledByEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final CanceledByEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public CanceledByEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return CanceledByEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      CanceledByEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_CANCELED_BY = "canceledBy";
  @SerializedName(SERIALIZED_NAME_CANCELED_BY)
  private CanceledByEnum canceledBy = CanceledByEnum.CUSTOMER;

  public static final String SERIALIZED_NAME_CANCELED_TIME = "canceledTime";
  @SerializedName(SERIALIZED_NAME_CANCELED_TIME)
  private OffsetDateTime canceledTime;

  public static final String SERIALIZED_NAME_CHURN_TIME = "churnTime";
  @SerializedName(SERIALIZED_NAME_CHURN_TIME)
  private OffsetDateTime churnTime;

  public static final String SERIALIZED_NAME_CREATED_TIME = "createdTime";
  @SerializedName(SERIALIZED_NAME_CREATED_TIME)
  private OffsetDateTime createdTime;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_LINE_ITEM_SUBTOTAL = "lineItemSubtotal";
  @SerializedName(SERIALIZED_NAME_LINE_ITEM_SUBTOTAL)
  private BigDecimal lineItemSubtotal;

  public static final String SERIALIZED_NAME_LINE_ITEMS = "lineItems";
  @SerializedName(SERIALIZED_NAME_LINE_ITEMS)
  private List<UpcomingInvoiceItem> lineItems;

  public static final String SERIALIZED_NAME_PRORATED = "prorated";
  @SerializedName(SERIALIZED_NAME_PRORATED)
  private Boolean prorated = false;

  public static final String SERIALIZED_NAME_PRORATED_INVOICE_ID = "proratedInvoiceId";
  @SerializedName(SERIALIZED_NAME_PRORATED_INVOICE_ID)
  private String proratedInvoiceId;

  /**
   * Cancellation reason.
   */
  @JsonAdapter(ReasonEnum.Adapter.class)
  public enum ReasonEnum {
    DID_NOT_USE("did-not-use"),
    
    DID_NOT_WANT("did-not-want"),
    
    MISSING_FEATURES("missing-features"),
    
    BUGS_OR_PROBLEMS("bugs-or-problems"),
    
    DO_NOT_REMEMBER("do-not-remember"),
    
    RISK_WARNING("risk-warning"),
    
    CONTRACT_EXPIRED("contract-expired"),
    
    TOO_EXPENSIVE("too-expensive"),
    
    OTHER("other"),
    
    BILLING_FAILURE("billing-failure");

    private String value;

    ReasonEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static ReasonEnum fromValue(String value) {
      for (ReasonEnum b : ReasonEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<ReasonEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final ReasonEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public ReasonEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return ReasonEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      ReasonEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_REASON = "reason";
  @SerializedName(SERIALIZED_NAME_REASON)
  private ReasonEnum reason = ReasonEnum.OTHER;

  /**
   * \&quot;draft\&quot; defines that the cancellation isn&#39;t applied on an invoice and subscription but can be inspected to see the charge. \&quot;confirmed\&quot; will set a subscription to be canceled when the &#x60;churnTime&#x60; is reached. \&quot;completed\&quot; is a read-only status which is set by the system when the churnTime is reached. The cancellation may not be changed or deleted when the status is \&quot;completed\&quot;. 
   */
  @JsonAdapter(StatusEnum.Adapter.class)
  public enum StatusEnum {
    DRAFT("draft"),
    
    CONFIRMED("confirmed"),
    
    COMPLETED("completed"),
    
    REVOKED("revoked");

    private String value;

    StatusEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static StatusEnum fromValue(String value) {
      for (StatusEnum b : StatusEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<StatusEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final StatusEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public StatusEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return StatusEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      StatusEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private StatusEnum status = StatusEnum.CONFIRMED;

  public static final String SERIALIZED_NAME_SUBSCRIPTION_ID = "subscriptionId";
  @SerializedName(SERIALIZED_NAME_SUBSCRIPTION_ID)
  private String subscriptionId;

  public SubscriptionCancellation() {
  }

  public SubscriptionCancellation(
     List<SelfLink> links, 
     String appliedInvoiceId, 
     OffsetDateTime canceledTime, 
     OffsetDateTime createdTime, 
     String id, 
     BigDecimal lineItemSubtotal, 
     String proratedInvoiceId
  ) {
    this();
    this.links = links;
    this.appliedInvoiceId = appliedInvoiceId;
    this.canceledTime = canceledTime;
    this.createdTime = createdTime;
    this.id = id;
    this.lineItemSubtotal = lineItemSubtotal;
    this.proratedInvoiceId = proratedInvoiceId;
  }

  /**
   * The links related to resource.
   * @return links
   */
  @javax.annotation.Nullable
  public List<SelfLink> getLinks() {
    return links;
  }



  /**
   * The identifier of the invoice where the cancellation fees or credits are applied.
   * @return appliedInvoiceId
   */
  @javax.annotation.Nullable
  public String getAppliedInvoiceId() {
    return appliedInvoiceId;
  }



  public SubscriptionCancellation canceledBy(CanceledByEnum canceledBy) {
    this.canceledBy = canceledBy;
    return this;
  }

  /**
   * Who did the cancellation.
   * @return canceledBy
   */
  @javax.annotation.Nullable
  public CanceledByEnum getCanceledBy() {
    return canceledBy;
  }

  public void setCanceledBy(CanceledByEnum canceledBy) {
    this.canceledBy = canceledBy;
  }


  /**
   * The cancellation time (when the status is confirmed which is by default unless specified \&quot;draft\&quot;).
   * @return canceledTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getCanceledTime() {
    return canceledTime;
  }



  public SubscriptionCancellation churnTime(OffsetDateTime churnTime) {
    this.churnTime = churnTime;
    return this;
  }

  /**
   * The time when the subscription will be deactivated.
   * @return churnTime
   */
  @javax.annotation.Nonnull
  public OffsetDateTime getChurnTime() {
    return churnTime;
  }

  public void setChurnTime(OffsetDateTime churnTime) {
    this.churnTime = churnTime;
  }


  /**
   * The time of resource creation (when it is posted).
   * @return createdTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getCreatedTime() {
    return createdTime;
  }



  public SubscriptionCancellation description(String description) {
    this.description = description;
    return this;
  }

  /**
   * Cancel reason description in free form.
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  /**
   * Cancellation identifier.
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }



  /**
   * Subtotal of the line items which will be added after the subscription&#39;s cancellation.
   * @return lineItemSubtotal
   */
  @javax.annotation.Nullable
  public BigDecimal getLineItemSubtotal() {
    return lineItemSubtotal;
  }



  public SubscriptionCancellation lineItems(List<UpcomingInvoiceItem> lineItems) {
    this.lineItems = lineItems;
    return this;
  }

  public SubscriptionCancellation addLineItemsItem(UpcomingInvoiceItem lineItemsItem) {
    if (this.lineItems == null) {
      this.lineItems = new ArrayList<>();
    }
    this.lineItems.add(lineItemsItem);
    return this;
  }

  /**
   * Items to be added to the new invoice. Proration item is generated and added automatically.
   * @return lineItems
   */
  @javax.annotation.Nullable
  public List<UpcomingInvoiceItem> getLineItems() {
    return lineItems;
  }

  public void setLineItems(List<UpcomingInvoiceItem> lineItems) {
    this.lineItems = lineItems;
  }


  public SubscriptionCancellation prorated(Boolean prorated) {
    this.prorated = prorated;
    return this;
  }

  /**
   * Defines if the customer gets a pro-rata credit for the time remaining between &#x60;churnTime&#x60; and subscription&#39;s next renewal time. 
   * @return prorated
   */
  @javax.annotation.Nullable
  public Boolean getProrated() {
    return prorated;
  }

  public void setProrated(Boolean prorated) {
    this.prorated = prorated;
  }


  /**
   * Identifier of the invoice on which the cancellation proration is calculated.
   * @return proratedInvoiceId
   */
  @javax.annotation.Nullable
  public String getProratedInvoiceId() {
    return proratedInvoiceId;
  }



  public SubscriptionCancellation reason(ReasonEnum reason) {
    this.reason = reason;
    return this;
  }

  /**
   * Cancellation reason.
   * @return reason
   */
  @javax.annotation.Nullable
  public ReasonEnum getReason() {
    return reason;
  }

  public void setReason(ReasonEnum reason) {
    this.reason = reason;
  }


  public SubscriptionCancellation status(StatusEnum status) {
    this.status = status;
    return this;
  }

  /**
   * \&quot;draft\&quot; defines that the cancellation isn&#39;t applied on an invoice and subscription but can be inspected to see the charge. \&quot;confirmed\&quot; will set a subscription to be canceled when the &#x60;churnTime&#x60; is reached. \&quot;completed\&quot; is a read-only status which is set by the system when the churnTime is reached. The cancellation may not be changed or deleted when the status is \&quot;completed\&quot;. 
   * @return status
   */
  @javax.annotation.Nullable
  public StatusEnum getStatus() {
    return status;
  }

  public void setStatus(StatusEnum status) {
    this.status = status;
  }


  public SubscriptionCancellation subscriptionId(String subscriptionId) {
    this.subscriptionId = subscriptionId;
    return this;
  }

  /**
   * Identifier of the canceled subscription order.
   * @return subscriptionId
   */
  @javax.annotation.Nonnull
  public String getSubscriptionId() {
    return subscriptionId;
  }

  public void setSubscriptionId(String subscriptionId) {
    this.subscriptionId = subscriptionId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    SubscriptionCancellation subscriptionCancellation = (SubscriptionCancellation) o;
    return Objects.equals(this.links, subscriptionCancellation.links) &&
        Objects.equals(this.appliedInvoiceId, subscriptionCancellation.appliedInvoiceId) &&
        Objects.equals(this.canceledBy, subscriptionCancellation.canceledBy) &&
        Objects.equals(this.canceledTime, subscriptionCancellation.canceledTime) &&
        Objects.equals(this.churnTime, subscriptionCancellation.churnTime) &&
        Objects.equals(this.createdTime, subscriptionCancellation.createdTime) &&
        Objects.equals(this.description, subscriptionCancellation.description) &&
        Objects.equals(this.id, subscriptionCancellation.id) &&
        Objects.equals(this.lineItemSubtotal, subscriptionCancellation.lineItemSubtotal) &&
        Objects.equals(this.lineItems, subscriptionCancellation.lineItems) &&
        Objects.equals(this.prorated, subscriptionCancellation.prorated) &&
        Objects.equals(this.proratedInvoiceId, subscriptionCancellation.proratedInvoiceId) &&
        Objects.equals(this.reason, subscriptionCancellation.reason) &&
        Objects.equals(this.status, subscriptionCancellation.status) &&
        Objects.equals(this.subscriptionId, subscriptionCancellation.subscriptionId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(links, appliedInvoiceId, canceledBy, canceledTime, churnTime, createdTime, description, id, lineItemSubtotal, lineItems, prorated, proratedInvoiceId, reason, status, subscriptionId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class SubscriptionCancellation {\n");
    sb.append("    links: ").append(toIndentedString(links)).append("\n");
    sb.append("    appliedInvoiceId: ").append(toIndentedString(appliedInvoiceId)).append("\n");
    sb.append("    canceledBy: ").append(toIndentedString(canceledBy)).append("\n");
    sb.append("    canceledTime: ").append(toIndentedString(canceledTime)).append("\n");
    sb.append("    churnTime: ").append(toIndentedString(churnTime)).append("\n");
    sb.append("    createdTime: ").append(toIndentedString(createdTime)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    lineItemSubtotal: ").append(toIndentedString(lineItemSubtotal)).append("\n");
    sb.append("    lineItems: ").append(toIndentedString(lineItems)).append("\n");
    sb.append("    prorated: ").append(toIndentedString(prorated)).append("\n");
    sb.append("    proratedInvoiceId: ").append(toIndentedString(proratedInvoiceId)).append("\n");
    sb.append("    reason: ").append(toIndentedString(reason)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    subscriptionId: ").append(toIndentedString(subscriptionId)).append("\n");
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
    openapiFields.add("_links");
    openapiFields.add("appliedInvoiceId");
    openapiFields.add("canceledBy");
    openapiFields.add("canceledTime");
    openapiFields.add("churnTime");
    openapiFields.add("createdTime");
    openapiFields.add("description");
    openapiFields.add("id");
    openapiFields.add("lineItemSubtotal");
    openapiFields.add("lineItems");
    openapiFields.add("prorated");
    openapiFields.add("proratedInvoiceId");
    openapiFields.add("reason");
    openapiFields.add("status");
    openapiFields.add("subscriptionId");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("churnTime");
    openapiRequiredFields.add("subscriptionId");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to SubscriptionCancellation
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!SubscriptionCancellation.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in SubscriptionCancellation is not found in the empty JSON string", SubscriptionCancellation.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!SubscriptionCancellation.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `SubscriptionCancellation` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : SubscriptionCancellation.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
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
      if ((jsonObj.get("appliedInvoiceId") != null && !jsonObj.get("appliedInvoiceId").isJsonNull()) && !jsonObj.get("appliedInvoiceId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `appliedInvoiceId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("appliedInvoiceId").toString()));
      }
      if ((jsonObj.get("canceledBy") != null && !jsonObj.get("canceledBy").isJsonNull()) && !jsonObj.get("canceledBy").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `canceledBy` to be a primitive type in the JSON string but got `%s`", jsonObj.get("canceledBy").toString()));
      }
      // validate the optional field `canceledBy`
      if (jsonObj.get("canceledBy") != null && !jsonObj.get("canceledBy").isJsonNull()) {
        CanceledByEnum.validateJsonElement(jsonObj.get("canceledBy"));
      }
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if (jsonObj.get("lineItems") != null && !jsonObj.get("lineItems").isJsonNull()) {
        JsonArray jsonArraylineItems = jsonObj.getAsJsonArray("lineItems");
        if (jsonArraylineItems != null) {
          // ensure the json data is an array
          if (!jsonObj.get("lineItems").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `lineItems` to be an array in the JSON string but got `%s`", jsonObj.get("lineItems").toString()));
          }

          // validate the optional field `lineItems` (array)
          for (int i = 0; i < jsonArraylineItems.size(); i++) {
            UpcomingInvoiceItem.validateJsonElement(jsonArraylineItems.get(i));
          };
        }
      }
      if ((jsonObj.get("proratedInvoiceId") != null && !jsonObj.get("proratedInvoiceId").isJsonNull()) && !jsonObj.get("proratedInvoiceId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `proratedInvoiceId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("proratedInvoiceId").toString()));
      }
      if ((jsonObj.get("reason") != null && !jsonObj.get("reason").isJsonNull()) && !jsonObj.get("reason").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `reason` to be a primitive type in the JSON string but got `%s`", jsonObj.get("reason").toString()));
      }
      // validate the optional field `reason`
      if (jsonObj.get("reason") != null && !jsonObj.get("reason").isJsonNull()) {
        ReasonEnum.validateJsonElement(jsonObj.get("reason"));
      }
      if ((jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) && !jsonObj.get("status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("status").toString()));
      }
      // validate the optional field `status`
      if (jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) {
        StatusEnum.validateJsonElement(jsonObj.get("status"));
      }
      if (!jsonObj.get("subscriptionId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `subscriptionId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("subscriptionId").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!SubscriptionCancellation.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'SubscriptionCancellation' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<SubscriptionCancellation> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(SubscriptionCancellation.class));

       return (TypeAdapter<T>) new TypeAdapter<SubscriptionCancellation>() {
           @Override
           public void write(JsonWriter out, SubscriptionCancellation value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public SubscriptionCancellation read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of SubscriptionCancellation given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of SubscriptionCancellation
   * @throws IOException if the JSON string is invalid with respect to SubscriptionCancellation
   */
  public static SubscriptionCancellation fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, SubscriptionCancellation.class);
  }

  /**
   * Convert an instance of SubscriptionCancellation to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

