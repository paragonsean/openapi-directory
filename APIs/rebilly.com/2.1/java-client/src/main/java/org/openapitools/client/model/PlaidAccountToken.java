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
import org.openapitools.client.model.LeadSource;
import org.openapitools.client.model.RiskMetadata;
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
 * PlaidAccountToken
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:20:59.825309-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PlaidAccountToken {
  public static final String SERIALIZED_NAME_BILLING_ADDRESS = "billingAddress";
  @SerializedName(SERIALIZED_NAME_BILLING_ADDRESS)
  private ContactObject billingAddress;

  /**
   * The token method.
   */
  @JsonAdapter(MethodEnum.Adapter.class)
  public enum MethodEnum {
    PLAID_ACCOUNT("plaid-account");

    private String value;

    MethodEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static MethodEnum fromValue(String value) {
      for (MethodEnum b : MethodEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<MethodEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final MethodEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public MethodEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return MethodEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      MethodEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_METHOD = "method";
  @SerializedName(SERIALIZED_NAME_METHOD)
  private MethodEnum method;

  public static final String SERIALIZED_NAME_PAYMENT_INSTRUMENT = "paymentInstrument";
  @SerializedName(SERIALIZED_NAME_PAYMENT_INSTRUMENT)
  private Object paymentInstrument;

  public static final String SERIALIZED_NAME_LINKS = "_links";
  @SerializedName(SERIALIZED_NAME_LINKS)
  private List<SelfLink> links = new ArrayList<>();

  public static final String SERIALIZED_NAME_CREATED_TIME = "createdTime";
  @SerializedName(SERIALIZED_NAME_CREATED_TIME)
  private OffsetDateTime createdTime;

  public static final String SERIALIZED_NAME_EXPIRATION_TIME = "expirationTime";
  @SerializedName(SERIALIZED_NAME_EXPIRATION_TIME)
  private OffsetDateTime expirationTime;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_IS_USED = "isUsed";
  @SerializedName(SERIALIZED_NAME_IS_USED)
  private Boolean isUsed = false;

  public static final String SERIALIZED_NAME_LEAD_SOURCE = "leadSource";
  @SerializedName(SERIALIZED_NAME_LEAD_SOURCE)
  private LeadSource leadSource;

  public static final String SERIALIZED_NAME_RISK_METADATA = "riskMetadata";
  @SerializedName(SERIALIZED_NAME_RISK_METADATA)
  private RiskMetadata riskMetadata;

  public static final String SERIALIZED_NAME_UPDATED_TIME = "updatedTime";
  @SerializedName(SERIALIZED_NAME_UPDATED_TIME)
  private OffsetDateTime updatedTime;

  public static final String SERIALIZED_NAME_USAGE_TIME = "usageTime";
  @SerializedName(SERIALIZED_NAME_USAGE_TIME)
  private OffsetDateTime usageTime;

  public PlaidAccountToken() {
  }

  public PlaidAccountToken(
     List<SelfLink> links, 
     OffsetDateTime createdTime, 
     OffsetDateTime expirationTime, 
     String id, 
     Boolean isUsed, 
     OffsetDateTime updatedTime, 
     OffsetDateTime usageTime
  ) {
    this();
    this.links = links;
    this.createdTime = createdTime;
    this.expirationTime = expirationTime;
    this.id = id;
    this.isUsed = isUsed;
    this.updatedTime = updatedTime;
    this.usageTime = usageTime;
  }

  public PlaidAccountToken billingAddress(ContactObject billingAddress) {
    this.billingAddress = billingAddress;
    return this;
  }

  /**
   * The billing address object.
   * @return billingAddress
   */
  @javax.annotation.Nonnull
  public ContactObject getBillingAddress() {
    return billingAddress;
  }

  public void setBillingAddress(ContactObject billingAddress) {
    this.billingAddress = billingAddress;
  }


  public PlaidAccountToken method(MethodEnum method) {
    this.method = method;
    return this;
  }

  /**
   * The token method.
   * @return method
   */
  @javax.annotation.Nonnull
  public MethodEnum getMethod() {
    return method;
  }

  public void setMethod(MethodEnum method) {
    this.method = method;
  }


  public PlaidAccountToken paymentInstrument(Object paymentInstrument) {
    this.paymentInstrument = paymentInstrument;
    return this;
  }

  /**
   * The Plaid payment instrument details.
   * @return paymentInstrument
   */
  @javax.annotation.Nonnull
  public Object getPaymentInstrument() {
    return paymentInstrument;
  }

  public void setPaymentInstrument(Object paymentInstrument) {
    this.paymentInstrument = paymentInstrument;
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
   * Token created time.
   * @return createdTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getCreatedTime() {
    return createdTime;
  }



  /**
   * Token expiration time.
   * @return expirationTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getExpirationTime() {
    return expirationTime;
  }



  /**
   * The token identifier string.
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }



  /**
   * Whether the token was already used.
   * @return isUsed
   */
  @javax.annotation.Nullable
  public Boolean getIsUsed() {
    return isUsed;
  }



  public PlaidAccountToken leadSource(LeadSource leadSource) {
    this.leadSource = leadSource;
    return this;
  }

  /**
   * Get leadSource
   * @return leadSource
   */
  @javax.annotation.Nullable
  public LeadSource getLeadSource() {
    return leadSource;
  }

  public void setLeadSource(LeadSource leadSource) {
    this.leadSource = leadSource;
  }


  public PlaidAccountToken riskMetadata(RiskMetadata riskMetadata) {
    this.riskMetadata = riskMetadata;
    return this;
  }

  /**
   * Get riskMetadata
   * @return riskMetadata
   */
  @javax.annotation.Nullable
  public RiskMetadata getRiskMetadata() {
    return riskMetadata;
  }

  public void setRiskMetadata(RiskMetadata riskMetadata) {
    this.riskMetadata = riskMetadata;
  }


  /**
   * Token updated time.
   * @return updatedTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getUpdatedTime() {
    return updatedTime;
  }



  /**
   * Token usage time.
   * @return usageTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getUsageTime() {
    return usageTime;
  }




  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PlaidAccountToken plaidAccountToken = (PlaidAccountToken) o;
    return Objects.equals(this.billingAddress, plaidAccountToken.billingAddress) &&
        Objects.equals(this.method, plaidAccountToken.method) &&
        Objects.equals(this.paymentInstrument, plaidAccountToken.paymentInstrument) &&
        Objects.equals(this.links, plaidAccountToken.links) &&
        Objects.equals(this.createdTime, plaidAccountToken.createdTime) &&
        Objects.equals(this.expirationTime, plaidAccountToken.expirationTime) &&
        Objects.equals(this.id, plaidAccountToken.id) &&
        Objects.equals(this.isUsed, plaidAccountToken.isUsed) &&
        Objects.equals(this.leadSource, plaidAccountToken.leadSource) &&
        Objects.equals(this.riskMetadata, plaidAccountToken.riskMetadata) &&
        Objects.equals(this.updatedTime, plaidAccountToken.updatedTime) &&
        Objects.equals(this.usageTime, plaidAccountToken.usageTime);
  }

  @Override
  public int hashCode() {
    return Objects.hash(billingAddress, method, paymentInstrument, links, createdTime, expirationTime, id, isUsed, leadSource, riskMetadata, updatedTime, usageTime);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PlaidAccountToken {\n");
    sb.append("    billingAddress: ").append(toIndentedString(billingAddress)).append("\n");
    sb.append("    method: ").append(toIndentedString(method)).append("\n");
    sb.append("    paymentInstrument: ").append(toIndentedString(paymentInstrument)).append("\n");
    sb.append("    links: ").append(toIndentedString(links)).append("\n");
    sb.append("    createdTime: ").append(toIndentedString(createdTime)).append("\n");
    sb.append("    expirationTime: ").append(toIndentedString(expirationTime)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    isUsed: ").append(toIndentedString(isUsed)).append("\n");
    sb.append("    leadSource: ").append(toIndentedString(leadSource)).append("\n");
    sb.append("    riskMetadata: ").append(toIndentedString(riskMetadata)).append("\n");
    sb.append("    updatedTime: ").append(toIndentedString(updatedTime)).append("\n");
    sb.append("    usageTime: ").append(toIndentedString(usageTime)).append("\n");
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
    openapiFields.add("createdTime");
    openapiFields.add("expirationTime");
    openapiFields.add("id");
    openapiFields.add("isUsed");
    openapiFields.add("leadSource");
    openapiFields.add("method");
    openapiFields.add("riskMetadata");
    openapiFields.add("updatedTime");
    openapiFields.add("usageTime");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("billingAddress");
    openapiRequiredFields.add("method");
    openapiRequiredFields.add("paymentInstrument");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PlaidAccountToken
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PlaidAccountToken.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PlaidAccountToken is not found in the empty JSON string", PlaidAccountToken.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PlaidAccountToken.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PlaidAccountToken` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : PlaidAccountToken.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the required field `billingAddress`
      ContactObject.validateJsonElement(jsonObj.get("billingAddress"));
      if (!jsonObj.get("method").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `method` to be a primitive type in the JSON string but got `%s`", jsonObj.get("method").toString()));
      }
      // validate the required field `method`
      MethodEnum.validateJsonElement(jsonObj.get("method"));
      // validate the required field `paymentInstrument`
      Object.validateJsonElement(jsonObj.get("paymentInstrument"));
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
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      // validate the optional field `leadSource`
      if (jsonObj.get("leadSource") != null && !jsonObj.get("leadSource").isJsonNull()) {
        LeadSource.validateJsonElement(jsonObj.get("leadSource"));
      }
      // validate the optional field `riskMetadata`
      if (jsonObj.get("riskMetadata") != null && !jsonObj.get("riskMetadata").isJsonNull()) {
        RiskMetadata.validateJsonElement(jsonObj.get("riskMetadata"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PlaidAccountToken.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PlaidAccountToken' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PlaidAccountToken> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PlaidAccountToken.class));

       return (TypeAdapter<T>) new TypeAdapter<PlaidAccountToken>() {
           @Override
           public void write(JsonWriter out, PlaidAccountToken value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PlaidAccountToken read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PlaidAccountToken given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PlaidAccountToken
   * @throws IOException if the JSON string is invalid with respect to PlaidAccountToken
   */
  public static PlaidAccountToken fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PlaidAccountToken.class);
  }

  /**
   * Convert an instance of PlaidAccountToken to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

