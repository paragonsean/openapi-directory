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
 * ThreeDSecure
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:20:59.825309-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ThreeDSecure {
  public static final String SERIALIZED_NAME_LINKS = "_links";
  @SerializedName(SERIALIZED_NAME_LINKS)
  private List<SelfLink> links = new ArrayList<>();

  public static final String SERIALIZED_NAME_AMOUNT = "amount";
  @SerializedName(SERIALIZED_NAME_AMOUNT)
  private Double amount;

  public static final String SERIALIZED_NAME_CAVV = "cavv";
  @SerializedName(SERIALIZED_NAME_CAVV)
  private String cavv;

  public static final String SERIALIZED_NAME_CREATED_TIME = "createdTime";
  @SerializedName(SERIALIZED_NAME_CREATED_TIME)
  private OffsetDateTime createdTime;

  public static final String SERIALIZED_NAME_CURRENCY = "currency";
  @SerializedName(SERIALIZED_NAME_CURRENCY)
  private String currency;

  public static final String SERIALIZED_NAME_CUSTOMER_ID = "customerId";
  @SerializedName(SERIALIZED_NAME_CUSTOMER_ID)
  private String customerId;

  public static final String SERIALIZED_NAME_ECI = "eci";
  @SerializedName(SERIALIZED_NAME_ECI)
  private Integer eci;

  /**
   * Is the cardholder enrolled in 3DSecure.
   */
  @JsonAdapter(EnrolledEnum.Adapter.class)
  public enum EnrolledEnum {
    Y("Y"),
    
    N("N"),
    
    U("U");

    private String value;

    EnrolledEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static EnrolledEnum fromValue(String value) {
      for (EnrolledEnum b : EnrolledEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<EnrolledEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final EnrolledEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public EnrolledEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return EnrolledEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      EnrolledEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_ENROLLED = "enrolled";
  @SerializedName(SERIALIZED_NAME_ENROLLED)
  private EnrolledEnum enrolled;

  public static final String SERIALIZED_NAME_ENROLLMENT_ECI = "enrollmentEci";
  @SerializedName(SERIALIZED_NAME_ENROLLMENT_ECI)
  private String enrollmentEci;

  public static final String SERIALIZED_NAME_GATEWAY_ACCOUNT_ID = "gatewayAccountId";
  @SerializedName(SERIALIZED_NAME_GATEWAY_ACCOUNT_ID)
  private String gatewayAccountId;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  /**
   * The 3D Secure entry Auth Response Status.
   */
  @JsonAdapter(PayerAuthResponseStatusEnum.Adapter.class)
  public enum PayerAuthResponseStatusEnum {
    Y("Y"),
    
    N("N"),
    
    U("U"),
    
    A("A");

    private String value;

    PayerAuthResponseStatusEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static PayerAuthResponseStatusEnum fromValue(String value) {
      for (PayerAuthResponseStatusEnum b : PayerAuthResponseStatusEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<PayerAuthResponseStatusEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final PayerAuthResponseStatusEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public PayerAuthResponseStatusEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return PayerAuthResponseStatusEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      PayerAuthResponseStatusEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_PAYER_AUTH_RESPONSE_STATUS = "payerAuthResponseStatus";
  @SerializedName(SERIALIZED_NAME_PAYER_AUTH_RESPONSE_STATUS)
  private PayerAuthResponseStatusEnum payerAuthResponseStatus;

  public static final String SERIALIZED_NAME_PAYMENT_CARD_ID = "paymentCardId";
  @SerializedName(SERIALIZED_NAME_PAYMENT_CARD_ID)
  private String paymentCardId;

  /**
   * If signature was verified.
   */
  @JsonAdapter(SignatureVerificationEnum.Adapter.class)
  public enum SignatureVerificationEnum {
    Y("Y"),
    
    N("N");

    private String value;

    SignatureVerificationEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static SignatureVerificationEnum fromValue(String value) {
      for (SignatureVerificationEnum b : SignatureVerificationEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<SignatureVerificationEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final SignatureVerificationEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public SignatureVerificationEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return SignatureVerificationEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      SignatureVerificationEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_SIGNATURE_VERIFICATION = "signatureVerification";
  @SerializedName(SERIALIZED_NAME_SIGNATURE_VERIFICATION)
  private SignatureVerificationEnum signatureVerification;

  public static final String SERIALIZED_NAME_WEBSITE_ID = "websiteId";
  @SerializedName(SERIALIZED_NAME_WEBSITE_ID)
  private String websiteId;

  public static final String SERIALIZED_NAME_XID = "xid";
  @SerializedName(SERIALIZED_NAME_XID)
  private String xid;

  public ThreeDSecure() {
  }

  public ThreeDSecure(
     List<SelfLink> links, 
     OffsetDateTime createdTime, 
     String id
  ) {
    this();
    this.links = links;
    this.createdTime = createdTime;
    this.id = id;
  }

  /**
   * The links related to resource.
   * @return links
   */
  @javax.annotation.Nullable
  public List<SelfLink> getLinks() {
    return links;
  }



  public ThreeDSecure amount(Double amount) {
    this.amount = amount;
    return this;
  }

  /**
   * Transaction amount.
   * @return amount
   */
  @javax.annotation.Nonnull
  public Double getAmount() {
    return amount;
  }

  public void setAmount(Double amount) {
    this.amount = amount;
  }


  public ThreeDSecure cavv(String cavv) {
    this.cavv = cavv;
    return this;
  }

  /**
   * The 3D Secure entry cardholder authentication verification value.
   * @return cavv
   */
  @javax.annotation.Nullable
  public String getCavv() {
    return cavv;
  }

  public void setCavv(String cavv) {
    this.cavv = cavv;
  }


  /**
   * The 3D Secure entry created time.
   * @return createdTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getCreatedTime() {
    return createdTime;
  }



  public ThreeDSecure currency(String currency) {
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


  public ThreeDSecure customerId(String customerId) {
    this.customerId = customerId;
    return this;
  }

  /**
   * Related customer ID.
   * @return customerId
   */
  @javax.annotation.Nonnull
  public String getCustomerId() {
    return customerId;
  }

  public void setCustomerId(String customerId) {
    this.customerId = customerId;
  }


  public ThreeDSecure eci(Integer eci) {
    this.eci = eci;
    return this;
  }

  /**
   * The 3D Secure entry electronic commerce indicator.
   * @return eci
   */
  @javax.annotation.Nullable
  public Integer getEci() {
    return eci;
  }

  public void setEci(Integer eci) {
    this.eci = eci;
  }


  public ThreeDSecure enrolled(EnrolledEnum enrolled) {
    this.enrolled = enrolled;
    return this;
  }

  /**
   * Is the cardholder enrolled in 3DSecure.
   * @return enrolled
   */
  @javax.annotation.Nonnull
  public EnrolledEnum getEnrolled() {
    return enrolled;
  }

  public void setEnrolled(EnrolledEnum enrolled) {
    this.enrolled = enrolled;
  }


  public ThreeDSecure enrollmentEci(String enrollmentEci) {
    this.enrollmentEci = enrollmentEci;
    return this;
  }

  /**
   * The 3D Secure entry enrollment eci.
   * @return enrollmentEci
   */
  @javax.annotation.Nonnull
  public String getEnrollmentEci() {
    return enrollmentEci;
  }

  public void setEnrollmentEci(String enrollmentEci) {
    this.enrollmentEci = enrollmentEci;
  }


  public ThreeDSecure gatewayAccountId(String gatewayAccountId) {
    this.gatewayAccountId = gatewayAccountId;
    return this;
  }

  /**
   * Related gateway account ID.
   * @return gatewayAccountId
   */
  @javax.annotation.Nonnull
  public String getGatewayAccountId() {
    return gatewayAccountId;
  }

  public void setGatewayAccountId(String gatewayAccountId) {
    this.gatewayAccountId = gatewayAccountId;
  }


  /**
   * The 3D Secure entry identifier string.
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }



  public ThreeDSecure payerAuthResponseStatus(PayerAuthResponseStatusEnum payerAuthResponseStatus) {
    this.payerAuthResponseStatus = payerAuthResponseStatus;
    return this;
  }

  /**
   * The 3D Secure entry Auth Response Status.
   * @return payerAuthResponseStatus
   */
  @javax.annotation.Nullable
  public PayerAuthResponseStatusEnum getPayerAuthResponseStatus() {
    return payerAuthResponseStatus;
  }

  public void setPayerAuthResponseStatus(PayerAuthResponseStatusEnum payerAuthResponseStatus) {
    this.payerAuthResponseStatus = payerAuthResponseStatus;
  }


  public ThreeDSecure paymentCardId(String paymentCardId) {
    this.paymentCardId = paymentCardId;
    return this;
  }

  /**
   * Related payment card ID.
   * @return paymentCardId
   */
  @javax.annotation.Nonnull
  public String getPaymentCardId() {
    return paymentCardId;
  }

  public void setPaymentCardId(String paymentCardId) {
    this.paymentCardId = paymentCardId;
  }


  public ThreeDSecure signatureVerification(SignatureVerificationEnum signatureVerification) {
    this.signatureVerification = signatureVerification;
    return this;
  }

  /**
   * If signature was verified.
   * @return signatureVerification
   */
  @javax.annotation.Nullable
  public SignatureVerificationEnum getSignatureVerification() {
    return signatureVerification;
  }

  public void setSignatureVerification(SignatureVerificationEnum signatureVerification) {
    this.signatureVerification = signatureVerification;
  }


  public ThreeDSecure websiteId(String websiteId) {
    this.websiteId = websiteId;
    return this;
  }

  /**
   * Related Website ID.
   * @return websiteId
   */
  @javax.annotation.Nonnull
  public String getWebsiteId() {
    return websiteId;
  }

  public void setWebsiteId(String websiteId) {
    this.websiteId = websiteId;
  }


  public ThreeDSecure xid(String xid) {
    this.xid = xid;
    return this;
  }

  /**
   * The 3D Secure entry transaction Id.
   * @return xid
   */
  @javax.annotation.Nullable
  public String getXid() {
    return xid;
  }

  public void setXid(String xid) {
    this.xid = xid;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ThreeDSecure threeDSecure = (ThreeDSecure) o;
    return Objects.equals(this.links, threeDSecure.links) &&
        Objects.equals(this.amount, threeDSecure.amount) &&
        Objects.equals(this.cavv, threeDSecure.cavv) &&
        Objects.equals(this.createdTime, threeDSecure.createdTime) &&
        Objects.equals(this.currency, threeDSecure.currency) &&
        Objects.equals(this.customerId, threeDSecure.customerId) &&
        Objects.equals(this.eci, threeDSecure.eci) &&
        Objects.equals(this.enrolled, threeDSecure.enrolled) &&
        Objects.equals(this.enrollmentEci, threeDSecure.enrollmentEci) &&
        Objects.equals(this.gatewayAccountId, threeDSecure.gatewayAccountId) &&
        Objects.equals(this.id, threeDSecure.id) &&
        Objects.equals(this.payerAuthResponseStatus, threeDSecure.payerAuthResponseStatus) &&
        Objects.equals(this.paymentCardId, threeDSecure.paymentCardId) &&
        Objects.equals(this.signatureVerification, threeDSecure.signatureVerification) &&
        Objects.equals(this.websiteId, threeDSecure.websiteId) &&
        Objects.equals(this.xid, threeDSecure.xid);
  }

  @Override
  public int hashCode() {
    return Objects.hash(links, amount, cavv, createdTime, currency, customerId, eci, enrolled, enrollmentEci, gatewayAccountId, id, payerAuthResponseStatus, paymentCardId, signatureVerification, websiteId, xid);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ThreeDSecure {\n");
    sb.append("    links: ").append(toIndentedString(links)).append("\n");
    sb.append("    amount: ").append(toIndentedString(amount)).append("\n");
    sb.append("    cavv: ").append(toIndentedString(cavv)).append("\n");
    sb.append("    createdTime: ").append(toIndentedString(createdTime)).append("\n");
    sb.append("    currency: ").append(toIndentedString(currency)).append("\n");
    sb.append("    customerId: ").append(toIndentedString(customerId)).append("\n");
    sb.append("    eci: ").append(toIndentedString(eci)).append("\n");
    sb.append("    enrolled: ").append(toIndentedString(enrolled)).append("\n");
    sb.append("    enrollmentEci: ").append(toIndentedString(enrollmentEci)).append("\n");
    sb.append("    gatewayAccountId: ").append(toIndentedString(gatewayAccountId)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    payerAuthResponseStatus: ").append(toIndentedString(payerAuthResponseStatus)).append("\n");
    sb.append("    paymentCardId: ").append(toIndentedString(paymentCardId)).append("\n");
    sb.append("    signatureVerification: ").append(toIndentedString(signatureVerification)).append("\n");
    sb.append("    websiteId: ").append(toIndentedString(websiteId)).append("\n");
    sb.append("    xid: ").append(toIndentedString(xid)).append("\n");
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
    openapiFields.add("amount");
    openapiFields.add("cavv");
    openapiFields.add("createdTime");
    openapiFields.add("currency");
    openapiFields.add("customerId");
    openapiFields.add("eci");
    openapiFields.add("enrolled");
    openapiFields.add("enrollmentEci");
    openapiFields.add("gatewayAccountId");
    openapiFields.add("id");
    openapiFields.add("payerAuthResponseStatus");
    openapiFields.add("paymentCardId");
    openapiFields.add("signatureVerification");
    openapiFields.add("websiteId");
    openapiFields.add("xid");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("amount");
    openapiRequiredFields.add("currency");
    openapiRequiredFields.add("customerId");
    openapiRequiredFields.add("enrolled");
    openapiRequiredFields.add("enrollmentEci");
    openapiRequiredFields.add("gatewayAccountId");
    openapiRequiredFields.add("paymentCardId");
    openapiRequiredFields.add("websiteId");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ThreeDSecure
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ThreeDSecure.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ThreeDSecure is not found in the empty JSON string", ThreeDSecure.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ThreeDSecure.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ThreeDSecure` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : ThreeDSecure.openapiRequiredFields) {
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
      if ((jsonObj.get("cavv") != null && !jsonObj.get("cavv").isJsonNull()) && !jsonObj.get("cavv").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `cavv` to be a primitive type in the JSON string but got `%s`", jsonObj.get("cavv").toString()));
      }
      if (!jsonObj.get("currency").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `currency` to be a primitive type in the JSON string but got `%s`", jsonObj.get("currency").toString()));
      }
      if (!jsonObj.get("customerId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `customerId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("customerId").toString()));
      }
      if (!jsonObj.get("enrolled").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `enrolled` to be a primitive type in the JSON string but got `%s`", jsonObj.get("enrolled").toString()));
      }
      // validate the required field `enrolled`
      EnrolledEnum.validateJsonElement(jsonObj.get("enrolled"));
      if (!jsonObj.get("enrollmentEci").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `enrollmentEci` to be a primitive type in the JSON string but got `%s`", jsonObj.get("enrollmentEci").toString()));
      }
      if (!jsonObj.get("gatewayAccountId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `gatewayAccountId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("gatewayAccountId").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("payerAuthResponseStatus") != null && !jsonObj.get("payerAuthResponseStatus").isJsonNull()) && !jsonObj.get("payerAuthResponseStatus").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `payerAuthResponseStatus` to be a primitive type in the JSON string but got `%s`", jsonObj.get("payerAuthResponseStatus").toString()));
      }
      // validate the optional field `payerAuthResponseStatus`
      if (jsonObj.get("payerAuthResponseStatus") != null && !jsonObj.get("payerAuthResponseStatus").isJsonNull()) {
        PayerAuthResponseStatusEnum.validateJsonElement(jsonObj.get("payerAuthResponseStatus"));
      }
      if (!jsonObj.get("paymentCardId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `paymentCardId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("paymentCardId").toString()));
      }
      if ((jsonObj.get("signatureVerification") != null && !jsonObj.get("signatureVerification").isJsonNull()) && !jsonObj.get("signatureVerification").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `signatureVerification` to be a primitive type in the JSON string but got `%s`", jsonObj.get("signatureVerification").toString()));
      }
      // validate the optional field `signatureVerification`
      if (jsonObj.get("signatureVerification") != null && !jsonObj.get("signatureVerification").isJsonNull()) {
        SignatureVerificationEnum.validateJsonElement(jsonObj.get("signatureVerification"));
      }
      if (!jsonObj.get("websiteId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `websiteId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("websiteId").toString()));
      }
      if ((jsonObj.get("xid") != null && !jsonObj.get("xid").isJsonNull()) && !jsonObj.get("xid").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `xid` to be a primitive type in the JSON string but got `%s`", jsonObj.get("xid").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ThreeDSecure.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ThreeDSecure' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ThreeDSecure> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ThreeDSecure.class));

       return (TypeAdapter<T>) new TypeAdapter<ThreeDSecure>() {
           @Override
           public void write(JsonWriter out, ThreeDSecure value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ThreeDSecure read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ThreeDSecure given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ThreeDSecure
   * @throws IOException if the JSON string is invalid with respect to ThreeDSecure
   */
  public static ThreeDSecure fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ThreeDSecure.class);
  }

  /**
   * Convert an instance of ThreeDSecure to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

