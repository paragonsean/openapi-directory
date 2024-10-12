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
import org.openapitools.client.model.EMS3dsServers;
import org.openapitools.client.model.TestProcessor3dsServers;
import org.openapitools.client.model.ThreeDSecureServerName;
import org.openapitools.client.model.WorldlineAtosFrankfurt3dsServers;

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
 * ThreeDSecureIO3dsServer.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:20:59.825309-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ThreeDSecureIO3dsServer extends WorldlineAtosFrankfurt3dsServers {
  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  protected ThreeDSecureServerName name;

  public static final String SERIALIZED_NAME_MERCHANT_ACQUIRER_BIN_MASTERCARD = "merchantAcquirerBinMastercard";
  @SerializedName(SERIALIZED_NAME_MERCHANT_ACQUIRER_BIN_MASTERCARD)
  private String merchantAcquirerBinMastercard;

  public static final String SERIALIZED_NAME_MERCHANT_ACQUIRER_BIN_VISA = "merchantAcquirerBinVisa";
  @SerializedName(SERIALIZED_NAME_MERCHANT_ACQUIRER_BIN_VISA)
  private String merchantAcquirerBinVisa;

  public static final String SERIALIZED_NAME_MERCHANT_COUNTRY = "merchantCountry";
  @SerializedName(SERIALIZED_NAME_MERCHANT_COUNTRY)
  private String merchantCountry;

  public static final String SERIALIZED_NAME_MERCHANT_ID = "merchantId";
  @SerializedName(SERIALIZED_NAME_MERCHANT_ID)
  private String merchantId;

  public static final String SERIALIZED_NAME_MERCHANT_NAME = "merchantName";
  @SerializedName(SERIALIZED_NAME_MERCHANT_NAME)
  private String merchantName;

  public static final String SERIALIZED_NAME_MERCHANT_URL = "merchantUrl";
  @SerializedName(SERIALIZED_NAME_MERCHANT_URL)
  private String merchantUrl;

  /**
   * 01 - Goods/Service Purchase 03 - Check Acceptance 10 - Account Funding 11 - Quasi-Cash Transaction 28 - Prepaid Activation and Load  Identifies the type of transaction being authenticated. 
   */
  @JsonAdapter(TransactionTypeEnum.Adapter.class)
  public enum TransactionTypeEnum {
    _01("01"),
    
    _03("03"),
    
    _10("10"),
    
    _11("11"),
    
    _28("28");

    private String value;

    TransactionTypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static TransactionTypeEnum fromValue(String value) {
      for (TransactionTypeEnum b : TransactionTypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<TransactionTypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final TransactionTypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public TransactionTypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return TransactionTypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      TransactionTypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_TRANSACTION_TYPE = "transactionType";
  @SerializedName(SERIALIZED_NAME_TRANSACTION_TYPE)
  private TransactionTypeEnum transactionType;

  public static final String SERIALIZED_NAME_V1 = "v1";
  @SerializedName(SERIALIZED_NAME_V1)
  private Boolean v1;

  public static final String SERIALIZED_NAME_V2 = "v2";
  @SerializedName(SERIALIZED_NAME_V2)
  private Boolean v2;

  public ThreeDSecureIO3dsServer() {
    this.name = this.getClass().getSimpleName();
  }

  public ThreeDSecureIO3dsServer name(ThreeDSecureServerName name) {
    this.name = name;
    return this;
  }

  /**
   * Get name
   * @return name
   */
  @javax.annotation.Nonnull
  public ThreeDSecureServerName getName() {
    return name;
  }

  public void setName(ThreeDSecureServerName name) {
    this.name = name;
  }


  public ThreeDSecureIO3dsServer merchantAcquirerBinMastercard(String merchantAcquirerBinMastercard) {
    this.merchantAcquirerBinMastercard = merchantAcquirerBinMastercard;
    return this;
  }

  /**
   * Mastercard Acquirer BIN.
   * @return merchantAcquirerBinMastercard
   */
  @javax.annotation.Nonnull
  public String getMerchantAcquirerBinMastercard() {
    return merchantAcquirerBinMastercard;
  }

  public void setMerchantAcquirerBinMastercard(String merchantAcquirerBinMastercard) {
    this.merchantAcquirerBinMastercard = merchantAcquirerBinMastercard;
  }


  public ThreeDSecureIO3dsServer merchantAcquirerBinVisa(String merchantAcquirerBinVisa) {
    this.merchantAcquirerBinVisa = merchantAcquirerBinVisa;
    return this;
  }

  /**
   * Visa Acquirer BIN.
   * @return merchantAcquirerBinVisa
   */
  @javax.annotation.Nonnull
  public String getMerchantAcquirerBinVisa() {
    return merchantAcquirerBinVisa;
  }

  public void setMerchantAcquirerBinVisa(String merchantAcquirerBinVisa) {
    this.merchantAcquirerBinVisa = merchantAcquirerBinVisa;
  }


  public ThreeDSecureIO3dsServer merchantCountry(String merchantCountry) {
    this.merchantCountry = merchantCountry;
    return this;
  }

  /**
   * Merchant Country ISO Alpha-2 Code.
   * @return merchantCountry
   */
  @javax.annotation.Nonnull
  public String getMerchantCountry() {
    return merchantCountry;
  }

  public void setMerchantCountry(String merchantCountry) {
    this.merchantCountry = merchantCountry;
  }


  public ThreeDSecureIO3dsServer merchantId(String merchantId) {
    this.merchantId = merchantId;
    return this;
  }

  /**
   * Merchant Id.
   * @return merchantId
   */
  @javax.annotation.Nonnull
  public String getMerchantId() {
    return merchantId;
  }

  public void setMerchantId(String merchantId) {
    this.merchantId = merchantId;
  }


  public ThreeDSecureIO3dsServer merchantName(String merchantName) {
    this.merchantName = merchantName;
    return this;
  }

  /**
   * Merchant Name.
   * @return merchantName
   */
  @javax.annotation.Nonnull
  public String getMerchantName() {
    return merchantName;
  }

  public void setMerchantName(String merchantName) {
    this.merchantName = merchantName;
  }


  public ThreeDSecureIO3dsServer merchantUrl(String merchantUrl) {
    this.merchantUrl = merchantUrl;
    return this;
  }

  /**
   * Merchant URL.
   * @return merchantUrl
   */
  @javax.annotation.Nonnull
  public String getMerchantUrl() {
    return merchantUrl;
  }

  public void setMerchantUrl(String merchantUrl) {
    this.merchantUrl = merchantUrl;
  }


  public ThreeDSecureIO3dsServer transactionType(TransactionTypeEnum transactionType) {
    this.transactionType = transactionType;
    return this;
  }

  /**
   * 01 - Goods/Service Purchase 03 - Check Acceptance 10 - Account Funding 11 - Quasi-Cash Transaction 28 - Prepaid Activation and Load  Identifies the type of transaction being authenticated. 
   * @return transactionType
   */
  @javax.annotation.Nullable
  public TransactionTypeEnum getTransactionType() {
    return transactionType;
  }

  public void setTransactionType(TransactionTypeEnum transactionType) {
    this.transactionType = transactionType;
  }


  public ThreeDSecureIO3dsServer v1(Boolean v1) {
    this.v1 = v1;
    return this;
  }

  /**
   * Value determines if requests can use version 1 of 3DS. In case both v1 and v2 are enabled it will prefer v2. If v2 is not supported for the issuer, it will coalesce to v1. 
   * @return v1
   */
  @javax.annotation.Nullable
  public Boolean getV1() {
    return v1;
  }

  public void setV1(Boolean v1) {
    this.v1 = v1;
  }


  public ThreeDSecureIO3dsServer v2(Boolean v2) {
    this.v2 = v2;
    return this;
  }

  /**
   * Value determines if requests will attempt version 2 of 3DS. In case both v1 and v2 are enabled it will prefer v2. If v2 is not supported for the issuer, it will coalesce to v1. 
   * @return v2
   */
  @javax.annotation.Nullable
  public Boolean getV2() {
    return v2;
  }

  public void setV2(Boolean v2) {
    this.v2 = v2;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ThreeDSecureIO3dsServer threeDSecureIO3dsServer = (ThreeDSecureIO3dsServer) o;
    return Objects.equals(this.name, threeDSecureIO3dsServer.name) &&
        Objects.equals(this.merchantAcquirerBinMastercard, threeDSecureIO3dsServer.merchantAcquirerBinMastercard) &&
        Objects.equals(this.merchantAcquirerBinVisa, threeDSecureIO3dsServer.merchantAcquirerBinVisa) &&
        Objects.equals(this.merchantCountry, threeDSecureIO3dsServer.merchantCountry) &&
        Objects.equals(this.merchantId, threeDSecureIO3dsServer.merchantId) &&
        Objects.equals(this.merchantName, threeDSecureIO3dsServer.merchantName) &&
        Objects.equals(this.merchantUrl, threeDSecureIO3dsServer.merchantUrl) &&
        Objects.equals(this.transactionType, threeDSecureIO3dsServer.transactionType) &&
        Objects.equals(this.v1, threeDSecureIO3dsServer.v1) &&
        Objects.equals(this.v2, threeDSecureIO3dsServer.v2) &&
        super.equals(o);
  }

  @Override
  public int hashCode() {
    return Objects.hash(name, merchantAcquirerBinMastercard, merchantAcquirerBinVisa, merchantCountry, merchantId, merchantName, merchantUrl, transactionType, v1, v2, super.hashCode());
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ThreeDSecureIO3dsServer {\n");
    sb.append("    ").append(toIndentedString(super.toString())).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    merchantAcquirerBinMastercard: ").append(toIndentedString(merchantAcquirerBinMastercard)).append("\n");
    sb.append("    merchantAcquirerBinVisa: ").append(toIndentedString(merchantAcquirerBinVisa)).append("\n");
    sb.append("    merchantCountry: ").append(toIndentedString(merchantCountry)).append("\n");
    sb.append("    merchantId: ").append(toIndentedString(merchantId)).append("\n");
    sb.append("    merchantName: ").append(toIndentedString(merchantName)).append("\n");
    sb.append("    merchantUrl: ").append(toIndentedString(merchantUrl)).append("\n");
    sb.append("    transactionType: ").append(toIndentedString(transactionType)).append("\n");
    sb.append("    v1: ").append(toIndentedString(v1)).append("\n");
    sb.append("    v2: ").append(toIndentedString(v2)).append("\n");
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
    openapiFields.add("name");
    openapiFields.add("merchantAcquirerBinMastercard");
    openapiFields.add("merchantAcquirerBinVisa");
    openapiFields.add("merchantCountry");
    openapiFields.add("merchantId");
    openapiFields.add("merchantName");
    openapiFields.add("merchantUrl");
    openapiFields.add("transactionType");
    openapiFields.add("v1");
    openapiFields.add("v2");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("name");
    openapiRequiredFields.add("merchantAcquirerBinMastercard");
    openapiRequiredFields.add("merchantAcquirerBinVisa");
    openapiRequiredFields.add("merchantCountry");
    openapiRequiredFields.add("merchantId");
    openapiRequiredFields.add("merchantName");
    openapiRequiredFields.add("merchantUrl");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ThreeDSecureIO3dsServer
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ThreeDSecureIO3dsServer.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ThreeDSecureIO3dsServer is not found in the empty JSON string", ThreeDSecureIO3dsServer.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ThreeDSecureIO3dsServer.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ThreeDSecureIO3dsServer` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : ThreeDSecureIO3dsServer.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ThreeDSecureIO3dsServer.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ThreeDSecureIO3dsServer' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ThreeDSecureIO3dsServer> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ThreeDSecureIO3dsServer.class));

       return (TypeAdapter<T>) new TypeAdapter<ThreeDSecureIO3dsServer>() {
           @Override
           public void write(JsonWriter out, ThreeDSecureIO3dsServer value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ThreeDSecureIO3dsServer read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ThreeDSecureIO3dsServer given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ThreeDSecureIO3dsServer
   * @throws IOException if the JSON string is invalid with respect to ThreeDSecureIO3dsServer
   */
  public static ThreeDSecureIO3dsServer fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ThreeDSecureIO3dsServer.class);
  }

  /**
   * Convert an instance of ThreeDSecureIO3dsServer to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

