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
import java.util.Arrays;
import org.openapitools.client.model.ContactObject;
import org.openapitools.client.model.RiskMetadata;

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
 * BBAN type object.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:20:59.825309-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class BBANType {
  public static final String SERIALIZED_NAME_ACCOUNT_NUMBER = "accountNumber";
  @SerializedName(SERIALIZED_NAME_ACCOUNT_NUMBER)
  private String accountNumber;

  /**
   * Bank&#39;s Account Number type. A valid value is basic bank account number (BBAN) or international bank account number (IBAN). This is the object for the BBAN.
   */
  @JsonAdapter(AccountNumberTypeEnum.Adapter.class)
  public enum AccountNumberTypeEnum {
    IBAN("IBAN"),
    
    BBAN("BBAN");

    private String value;

    AccountNumberTypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static AccountNumberTypeEnum fromValue(String value) {
      for (AccountNumberTypeEnum b : AccountNumberTypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<AccountNumberTypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final AccountNumberTypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public AccountNumberTypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return AccountNumberTypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      AccountNumberTypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_ACCOUNT_NUMBER_TYPE = "accountNumberType";
  @SerializedName(SERIALIZED_NAME_ACCOUNT_NUMBER_TYPE)
  private AccountNumberTypeEnum accountNumberType = AccountNumberTypeEnum.BBAN;

  /**
   * Bank&#39;s account type.
   */
  @JsonAdapter(AccountTypeEnum.Adapter.class)
  public enum AccountTypeEnum {
    CHECKING("checking"),
    
    SAVINGS("savings"),
    
    OTHER("other");

    private String value;

    AccountTypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static AccountTypeEnum fromValue(String value) {
      for (AccountTypeEnum b : AccountTypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<AccountTypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final AccountTypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public AccountTypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return AccountTypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      AccountTypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_ACCOUNT_TYPE = "accountType";
  @SerializedName(SERIALIZED_NAME_ACCOUNT_TYPE)
  private AccountTypeEnum accountType;

  public static final String SERIALIZED_NAME_BANK_NAME = "bankName";
  @SerializedName(SERIALIZED_NAME_BANK_NAME)
  private String bankName;

  public static final String SERIALIZED_NAME_BIC = "bic";
  @SerializedName(SERIALIZED_NAME_BIC)
  private String bic;

  public static final String SERIALIZED_NAME_BILLING_ADDRESS = "billingAddress";
  @SerializedName(SERIALIZED_NAME_BILLING_ADDRESS)
  private ContactObject billingAddress;

  public static final String SERIALIZED_NAME_CUSTOM_FIELDS = "customFields";
  @SerializedName(SERIALIZED_NAME_CUSTOM_FIELDS)
  private Object customFields = {};

  public static final String SERIALIZED_NAME_CUSTOMER_ID = "customerId";
  @SerializedName(SERIALIZED_NAME_CUSTOMER_ID)
  private String customerId;

  /**
   * The method of payment instrument.
   */
  @JsonAdapter(MethodEnum.Adapter.class)
  public enum MethodEnum {
    ACH("ach");

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

  public static final String SERIALIZED_NAME_RISK_METADATA = "riskMetadata";
  @SerializedName(SERIALIZED_NAME_RISK_METADATA)
  private RiskMetadata riskMetadata;

  public static final String SERIALIZED_NAME_ROUTING_NUMBER = "routingNumber";
  @SerializedName(SERIALIZED_NAME_ROUTING_NUMBER)
  private String routingNumber;

  public BBANType() {
  }

  public BBANType accountNumber(String accountNumber) {
    this.accountNumber = accountNumber;
    return this;
  }

  /**
   * Bank&#39;s account number.
   * @return accountNumber
   */
  @javax.annotation.Nonnull
  public String getAccountNumber() {
    return accountNumber;
  }

  public void setAccountNumber(String accountNumber) {
    this.accountNumber = accountNumber;
  }


  public BBANType accountNumberType(AccountNumberTypeEnum accountNumberType) {
    this.accountNumberType = accountNumberType;
    return this;
  }

  /**
   * Bank&#39;s Account Number type. A valid value is basic bank account number (BBAN) or international bank account number (IBAN). This is the object for the BBAN.
   * @return accountNumberType
   */
  @javax.annotation.Nonnull
  public AccountNumberTypeEnum getAccountNumberType() {
    return accountNumberType;
  }

  public void setAccountNumberType(AccountNumberTypeEnum accountNumberType) {
    this.accountNumberType = accountNumberType;
  }


  public BBANType accountType(AccountTypeEnum accountType) {
    this.accountType = accountType;
    return this;
  }

  /**
   * Bank&#39;s account type.
   * @return accountType
   */
  @javax.annotation.Nonnull
  public AccountTypeEnum getAccountType() {
    return accountType;
  }

  public void setAccountType(AccountTypeEnum accountType) {
    this.accountType = accountType;
  }


  public BBANType bankName(String bankName) {
    this.bankName = bankName;
    return this;
  }

  /**
   * Bank&#39;s name.
   * @return bankName
   */
  @javax.annotation.Nullable
  public String getBankName() {
    return bankName;
  }

  public void setBankName(String bankName) {
    this.bankName = bankName;
  }


  public BBANType bic(String bic) {
    this.bic = bic;
    return this;
  }

  /**
   * Bank Identifier Code.
   * @return bic
   */
  @javax.annotation.Nullable
  public String getBic() {
    return bic;
  }

  public void setBic(String bic) {
    this.bic = bic;
  }


  public BBANType billingAddress(ContactObject billingAddress) {
    this.billingAddress = billingAddress;
    return this;
  }

  /**
   * The billing address.
   * @return billingAddress
   */
  @javax.annotation.Nonnull
  public ContactObject getBillingAddress() {
    return billingAddress;
  }

  public void setBillingAddress(ContactObject billingAddress) {
    this.billingAddress = billingAddress;
  }


  public BBANType customFields(Object customFields) {
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


  public BBANType customerId(String customerId) {
    this.customerId = customerId;
    return this;
  }

  /**
   * Customer&#39;s ID.
   * @return customerId
   */
  @javax.annotation.Nonnull
  public String getCustomerId() {
    return customerId;
  }

  public void setCustomerId(String customerId) {
    this.customerId = customerId;
  }


  public BBANType method(MethodEnum method) {
    this.method = method;
    return this;
  }

  /**
   * The method of payment instrument.
   * @return method
   */
  @javax.annotation.Nonnull
  public MethodEnum getMethod() {
    return method;
  }

  public void setMethod(MethodEnum method) {
    this.method = method;
  }


  public BBANType riskMetadata(RiskMetadata riskMetadata) {
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


  public BBANType routingNumber(String routingNumber) {
    this.routingNumber = routingNumber;
    return this;
  }

  /**
   * Bank&#39;s routing number.
   * @return routingNumber
   */
  @javax.annotation.Nonnull
  public String getRoutingNumber() {
    return routingNumber;
  }

  public void setRoutingNumber(String routingNumber) {
    this.routingNumber = routingNumber;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    BBANType bbANType = (BBANType) o;
    return Objects.equals(this.accountNumber, bbANType.accountNumber) &&
        Objects.equals(this.accountNumberType, bbANType.accountNumberType) &&
        Objects.equals(this.accountType, bbANType.accountType) &&
        Objects.equals(this.bankName, bbANType.bankName) &&
        Objects.equals(this.bic, bbANType.bic) &&
        Objects.equals(this.billingAddress, bbANType.billingAddress) &&
        Objects.equals(this.customFields, bbANType.customFields) &&
        Objects.equals(this.customerId, bbANType.customerId) &&
        Objects.equals(this.method, bbANType.method) &&
        Objects.equals(this.riskMetadata, bbANType.riskMetadata) &&
        Objects.equals(this.routingNumber, bbANType.routingNumber);
  }

  @Override
  public int hashCode() {
    return Objects.hash(accountNumber, accountNumberType, accountType, bankName, bic, billingAddress, customFields, customerId, method, riskMetadata, routingNumber);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class BBANType {\n");
    sb.append("    accountNumber: ").append(toIndentedString(accountNumber)).append("\n");
    sb.append("    accountNumberType: ").append(toIndentedString(accountNumberType)).append("\n");
    sb.append("    accountType: ").append(toIndentedString(accountType)).append("\n");
    sb.append("    bankName: ").append(toIndentedString(bankName)).append("\n");
    sb.append("    bic: ").append(toIndentedString(bic)).append("\n");
    sb.append("    billingAddress: ").append(toIndentedString(billingAddress)).append("\n");
    sb.append("    customFields: ").append(toIndentedString(customFields)).append("\n");
    sb.append("    customerId: ").append(toIndentedString(customerId)).append("\n");
    sb.append("    method: ").append(toIndentedString(method)).append("\n");
    sb.append("    riskMetadata: ").append(toIndentedString(riskMetadata)).append("\n");
    sb.append("    routingNumber: ").append(toIndentedString(routingNumber)).append("\n");
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
    openapiFields.add("accountNumber");
    openapiFields.add("accountNumberType");
    openapiFields.add("accountType");
    openapiFields.add("bankName");
    openapiFields.add("bic");
    openapiFields.add("billingAddress");
    openapiFields.add("customFields");
    openapiFields.add("customerId");
    openapiFields.add("method");
    openapiFields.add("riskMetadata");
    openapiFields.add("routingNumber");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("accountNumber");
    openapiRequiredFields.add("accountNumberType");
    openapiRequiredFields.add("accountType");
    openapiRequiredFields.add("billingAddress");
    openapiRequiredFields.add("customerId");
    openapiRequiredFields.add("method");
    openapiRequiredFields.add("routingNumber");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to BBANType
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!BBANType.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in BBANType is not found in the empty JSON string", BBANType.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!BBANType.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `BBANType` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : BBANType.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("accountNumber").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `accountNumber` to be a primitive type in the JSON string but got `%s`", jsonObj.get("accountNumber").toString()));
      }
      if (!jsonObj.get("accountNumberType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `accountNumberType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("accountNumberType").toString()));
      }
      // validate the required field `accountNumberType`
      AccountNumberTypeEnum.validateJsonElement(jsonObj.get("accountNumberType"));
      if (!jsonObj.get("accountType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `accountType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("accountType").toString()));
      }
      // validate the required field `accountType`
      AccountTypeEnum.validateJsonElement(jsonObj.get("accountType"));
      if ((jsonObj.get("bankName") != null && !jsonObj.get("bankName").isJsonNull()) && !jsonObj.get("bankName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `bankName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("bankName").toString()));
      }
      if ((jsonObj.get("bic") != null && !jsonObj.get("bic").isJsonNull()) && !jsonObj.get("bic").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `bic` to be a primitive type in the JSON string but got `%s`", jsonObj.get("bic").toString()));
      }
      // validate the required field `billingAddress`
      ContactObject.validateJsonElement(jsonObj.get("billingAddress"));
      if (!jsonObj.get("customerId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `customerId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("customerId").toString()));
      }
      if (!jsonObj.get("method").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `method` to be a primitive type in the JSON string but got `%s`", jsonObj.get("method").toString()));
      }
      // validate the required field `method`
      MethodEnum.validateJsonElement(jsonObj.get("method"));
      // validate the optional field `riskMetadata`
      if (jsonObj.get("riskMetadata") != null && !jsonObj.get("riskMetadata").isJsonNull()) {
        RiskMetadata.validateJsonElement(jsonObj.get("riskMetadata"));
      }
      if (!jsonObj.get("routingNumber").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `routingNumber` to be a primitive type in the JSON string but got `%s`", jsonObj.get("routingNumber").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!BBANType.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'BBANType' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<BBANType> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(BBANType.class));

       return (TypeAdapter<T>) new TypeAdapter<BBANType>() {
           @Override
           public void write(JsonWriter out, BBANType value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public BBANType read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of BBANType given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of BBANType
   * @throws IOException if the JSON string is invalid with respect to BBANType
   */
  public static BBANType fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, BBANType.class);
  }

  /**
   * Convert an instance of BBANType to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

