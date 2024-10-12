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
import org.openapitools.client.model.SelfLink;
import org.openapitools.client.model.TimelineExtraData;

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
 * TransactionTimeline
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:20:59.825309-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class TransactionTimeline {
  public static final String SERIALIZED_NAME_LINKS = "_links";
  @SerializedName(SERIALIZED_NAME_LINKS)
  private List<SelfLink> links = new ArrayList<>();

  public static final String SERIALIZED_NAME_EXTRA_DATA = "extraData";
  @SerializedName(SERIALIZED_NAME_EXTRA_DATA)
  private TimelineExtraData extraData;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_MESSAGE = "message";
  @SerializedName(SERIALIZED_NAME_MESSAGE)
  private String message;

  public static final String SERIALIZED_NAME_OCCURRED_TIME = "occurredTime";
  @SerializedName(SERIALIZED_NAME_OCCURRED_TIME)
  private OffsetDateTime occurredTime;

  /**
   * Shows who or what triggered the Timeline message.
   */
  @JsonAdapter(TriggeredByEnum.Adapter.class)
  public enum TriggeredByEnum {
    REBILLY("rebilly"),
    
    APP("app"),
    
    DIRECT_API("direct-api");

    private String value;

    TriggeredByEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static TriggeredByEnum fromValue(String value) {
      for (TriggeredByEnum b : TriggeredByEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<TriggeredByEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final TriggeredByEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public TriggeredByEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return TriggeredByEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      TriggeredByEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_TRIGGERED_BY = "triggeredBy";
  @SerializedName(SERIALIZED_NAME_TRIGGERED_BY)
  private TriggeredByEnum triggeredBy;

  /**
   * Timeline message type.
   */
  @JsonAdapter(TypeEnum.Adapter.class)
  public enum TypeEnum {
    AMOUNT_ADJUSTED("amount-adjusted"),
    
    BLOCKLIST_MATCHED("blocklist-matched"),
    
    BUMP_OFFER_ACCEPTED("bump-offer-accepted"),
    
    BUMP_OFFER_PRESENTED("bump-offer-presented"),
    
    BUMP_OFFER_REJECTED("bump-offer-rejected"),
    
    CUSTOMER_REDIRECTED_OFFSITE("customer-redirected-offsite"),
    
    CUSTOMER_RETURNED("customer-returned"),
    
    DCC_OFFER_ACCEPTED("dcc-offer-accepted"),
    
    DCC_OFFER_FORCED("dcc-offer-forced"),
    
    DCC_OFFER_PRESENTED("dcc-offer-presented"),
    
    DCC_OFFER_REJECTED("dcc-offer-rejected"),
    
    DISPUTE_CHANGED("dispute-changed"),
    
    DISPUTE_CREATED("dispute-created"),
    
    DISPUTE_FORFEITED("dispute-forfeited"),
    
    DISPUTE_LOST("dispute-lost"),
    
    DISPUTE_RESPONDED("dispute-responded"),
    
    DISPUTE_WON("dispute-won"),
    
    GATEWAY_CONNECTION_FAILED("gateway-connection-failed"),
    
    GATEWAY_CONNECTION_TIMED_OUT("gateway-connection-timed-out"),
    
    GATEWAY_RESPONSE_RECEIVED("gateway-response-received"),
    
    RISK_SCORE_CHANGED("risk-score-changed"),
    
    TIMELINE_COMMENT_CREATED("timeline-comment-created"),
    
    TRANSACTION_ABANDONED("transaction-abandoned"),
    
    TRANSACTION_AMOUNT_DISCREPANCY_FOUND("transaction-amount-discrepancy-found"),
    
    TRANSACTION_APPROVED("transaction-approved"),
    
    TRANSACTION_CANCELED("transaction-canceled"),
    
    TRANSACTION_CAPTURE_DELAYED("transaction-capture-delayed"),
    
    TRANSACTION_CAPTURED("transaction-captured"),
    
    TRANSACTION_DECLINED("transaction-declined"),
    
    TRANSACTION_DISCREPANCY_FOUND("transaction-discrepancy-found"),
    
    TRANSACTION_INITIATED("transaction-initiated"),
    
    TRANSACTION_RECONCILED("transaction-reconciled"),
    
    TRANSACTION_REFUNDED("transaction-refunded"),
    
    TRANSACTION_RETRIED("transaction-retried"),
    
    TRANSACTION_RULES_PROCESSED("transaction-rules-processed"),
    
    TRANSACTION_SCHEDULED_TIME_CHANGED("transaction-scheduled-time-changed"),
    
    TRANSACTION_TIMEOUT_RESOLVED("transaction-timeout-resolved"),
    
    TRANSACTION_VOIDED("transaction-voided"),
    
    TRANSACTION_WAITING_GATEWAY("transaction-waiting-gateway"),
    
    TRANSACTION_QUERIED("transaction-queried"),
    
    TRANSACTION_UPDATED("transaction-updated");

    private String value;

    TypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static TypeEnum fromValue(String value) {
      for (TypeEnum b : TypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<TypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final TypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public TypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return TypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      TypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private TypeEnum type;

  public TransactionTimeline() {
  }

  public TransactionTimeline(
     List<SelfLink> links, 
     String id, 
     OffsetDateTime occurredTime, 
     TriggeredByEnum triggeredBy, 
     TypeEnum type
  ) {
    this();
    this.links = links;
    this.id = id;
    this.occurredTime = occurredTime;
    this.triggeredBy = triggeredBy;
    this.type = type;
  }

  /**
   * The links related to resource.
   * @return links
   */
  @javax.annotation.Nullable
  public List<SelfLink> getLinks() {
    return links;
  }



  public TransactionTimeline extraData(TimelineExtraData extraData) {
    this.extraData = extraData;
    return this;
  }

  /**
   * Get extraData
   * @return extraData
   */
  @javax.annotation.Nullable
  public TimelineExtraData getExtraData() {
    return extraData;
  }

  public void setExtraData(TimelineExtraData extraData) {
    this.extraData = extraData;
  }


  /**
   * The Timeline message identifier string.
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }



  public TransactionTimeline message(String message) {
    this.message = message;
    return this;
  }

  /**
   * The message that describes the message details.
   * @return message
   */
  @javax.annotation.Nullable
  public String getMessage() {
    return message;
  }

  public void setMessage(String message) {
    this.message = message;
  }


  /**
   * Timeline message time.
   * @return occurredTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getOccurredTime() {
    return occurredTime;
  }



  /**
   * Shows who or what triggered the Timeline message.
   * @return triggeredBy
   */
  @javax.annotation.Nullable
  public TriggeredByEnum getTriggeredBy() {
    return triggeredBy;
  }



  /**
   * Timeline message type.
   * @return type
   */
  @javax.annotation.Nullable
  public TypeEnum getType() {
    return type;
  }




  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TransactionTimeline transactionTimeline = (TransactionTimeline) o;
    return Objects.equals(this.links, transactionTimeline.links) &&
        Objects.equals(this.extraData, transactionTimeline.extraData) &&
        Objects.equals(this.id, transactionTimeline.id) &&
        Objects.equals(this.message, transactionTimeline.message) &&
        Objects.equals(this.occurredTime, transactionTimeline.occurredTime) &&
        Objects.equals(this.triggeredBy, transactionTimeline.triggeredBy) &&
        Objects.equals(this.type, transactionTimeline.type);
  }

  @Override
  public int hashCode() {
    return Objects.hash(links, extraData, id, message, occurredTime, triggeredBy, type);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TransactionTimeline {\n");
    sb.append("    links: ").append(toIndentedString(links)).append("\n");
    sb.append("    extraData: ").append(toIndentedString(extraData)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    message: ").append(toIndentedString(message)).append("\n");
    sb.append("    occurredTime: ").append(toIndentedString(occurredTime)).append("\n");
    sb.append("    triggeredBy: ").append(toIndentedString(triggeredBy)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
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
    openapiFields.add("extraData");
    openapiFields.add("id");
    openapiFields.add("message");
    openapiFields.add("occurredTime");
    openapiFields.add("triggeredBy");
    openapiFields.add("type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to TransactionTimeline
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!TransactionTimeline.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in TransactionTimeline is not found in the empty JSON string", TransactionTimeline.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!TransactionTimeline.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TransactionTimeline` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
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
      // validate the optional field `extraData`
      if (jsonObj.get("extraData") != null && !jsonObj.get("extraData").isJsonNull()) {
        TimelineExtraData.validateJsonElement(jsonObj.get("extraData"));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("message") != null && !jsonObj.get("message").isJsonNull()) && !jsonObj.get("message").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `message` to be a primitive type in the JSON string but got `%s`", jsonObj.get("message").toString()));
      }
      if ((jsonObj.get("triggeredBy") != null && !jsonObj.get("triggeredBy").isJsonNull()) && !jsonObj.get("triggeredBy").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `triggeredBy` to be a primitive type in the JSON string but got `%s`", jsonObj.get("triggeredBy").toString()));
      }
      // validate the optional field `triggeredBy`
      if (jsonObj.get("triggeredBy") != null && !jsonObj.get("triggeredBy").isJsonNull()) {
        TriggeredByEnum.validateJsonElement(jsonObj.get("triggeredBy"));
      }
      if ((jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) && !jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
      // validate the optional field `type`
      if (jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) {
        TypeEnum.validateJsonElement(jsonObj.get("type"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TransactionTimeline.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TransactionTimeline' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TransactionTimeline> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TransactionTimeline.class));

       return (TypeAdapter<T>) new TypeAdapter<TransactionTimeline>() {
           @Override
           public void write(JsonWriter out, TransactionTimeline value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TransactionTimeline read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of TransactionTimeline given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of TransactionTimeline
   * @throws IOException if the JSON string is invalid with respect to TransactionTimeline
   */
  public static TransactionTimeline fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TransactionTimeline.class);
  }

  /**
   * Convert an instance of TransactionTimeline to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

