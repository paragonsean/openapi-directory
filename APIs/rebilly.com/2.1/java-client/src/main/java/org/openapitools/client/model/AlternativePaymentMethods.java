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
import com.google.gson.annotations.SerializedName;

import java.io.IOException;
import com.google.gson.TypeAdapter;
import com.google.gson.JsonElement;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;

/**
 * Gets or Sets AlternativePaymentMethods
 */
@JsonAdapter(AlternativePaymentMethods.Adapter.class)
public enum AlternativePaymentMethods {
  
  CASH("cash"),
  
  CHECK("check"),
  
  PAYPAL("paypal"),
  
  ADV_CASH("AdvCash"),
  
  ALFA_CLICK("Alfa-click"),
  
  ALIPAY("Alipay"),
  
  ASTRO_PAY_CARD("AstroPay Card"),
  
  ASTRO_PAY_GO("AstroPay-GO"),
  
  BANK_TRANSFER("bank-transfer"),
  
  BANK_TRANSFER_2("bank-transfer-2"),
  
  BANK_TRANSFER_3("bank-transfer-3"),
  
  BANK_TRANSFER_4("bank-transfer-4"),
  
  BANK_TRANSFER_5("bank-transfer-5"),
  
  BANK_TRANSFER_6("bank-transfer-6"),
  
  BANK_TRANSFER_7("bank-transfer-7"),
  
  BANK_TRANSFER_8("bank-transfer-8"),
  
  BANK_TRANSFER_9("bank-transfer-9"),
  
  BEELINE("Beeline"),
  
  BELFIUS_DIRECT_NET("Belfius-direct-net"),
  
  BITCOIN("bitcoin"),
  
  BOLETO("Boleto"),
  
  CASH_DEPOSIT("cash-deposit"),
  
  CAS_HLIB("CASHlib"),
  
  CASH_TO_CODE("CashToCode"),
  
  CHINA_UNION_PAY("China UnionPay"),
  
  COD_VOUCHER("CODVoucher"),
  
  CONEKTA_OXXO("Conekta-oxxo"),
  
  CUPON_DE_PAGOS("Cupon-de-pagos"),
  
  CRYPTOCURRENCY("cryptocurrency"),
  
  DOMESTIC_CARDS("domestic-cards"),
  
  ECHECK("echeck"),
  
  ECO_PAYZ("ecoPayz"),
  
  ECO_VOUCHER("ecoVoucher"),
  
  EPS("EPS"),
  
  E_PAY_BG("ePay.bg"),
  
  E_ZEE_WALLET("eZeeWallet"),
  
  FLEXEPIN("Flexepin"),
  
  GIROPAY("Giropay"),
  
  GPAYSAFE("Gpaysafe"),
  
  GOOGLE_PAY("Google Pay"),
  
  I_DEBIT("iDebit"),
  
  I_DEAL("iDEAL"),
  
  ING_HOMEPAY("ING-homepay"),
  
  INOVAPAY_PIN("INOVAPAY-pin"),
  
  INOVAPAY_WALLET("INOVAPAY-wallet"),
  
  INSTA_DEBIT("InstaDebit"),
  
  INSTANT_BANK_TRANSFER("instant-bank-transfer"),
  
  INTERAC("Interac"),
  
  INTERAC_ONLINE("Interac-online"),
  
  INTERAC_E_TRANSFER("Interac-eTransfer"),
  
  INVOICE("invoice"),
  
  I_WALLET("iWallet"),
  
  JETON("Jeton"),
  
  JPAY("jpay"),
  
  KHELOCARD("Khelocard"),
  
  KLARNA("Klarna"),
  
  LOONIE("loonie"),
  
  MEGAFON("Megafon"),
  
  MI_FINITY_E_WALLET("MiFinity-eWallet"),
  
  MISCELLANEOUS("miscellaneous"),
  
  BANCONTACT("Bancontact"),
  
  MTS("MTS"),
  
  MUCH_BETTER("MuchBetter"),
  
  NEOSURF("Neosurf"),
  
  NETBANKING("Netbanking"),
  
  NETELLER("Neteller"),
  
  NORDEA_SOLO("Nordea-Solo"),
  
  OCHA_PAY("OchaPay"),
  
  ONLINE_BANK_TRANSFER("online-bank-transfer"),
  
  ONLINEUEBERWEISEN("Onlineueberweisen"),
  
  ORIENTAL_WALLET("oriental-wallet"),
  
  OXXO("OXXO"),
  
  PAGSMILE_DEPOSIT_EXPRESS("Pagsmile-deposit-express"),
  
  PAGSMILE_LOTTERY("Pagsmile-lottery"),
  
  PAY_CASH("PayCash"),
  
  PAYEER("Payeer"),
  
  PAYMENT_ASIA_CRYPTO("PaymentAsia-crypto"),
  
  PAYMERO("Paymero"),
  
  PERFECT_MONEY("Perfect-money"),
  
  PIASTRIX("Piastrix"),
  
  PLAID_ACCOUNT("plaid-account"),
  
  PAY_TABS("PayTabs"),
  
  PAYSAFECARD("Paysafecard"),
  
  PAYSAFECASH("Paysafecash"),
  
  PAY4_FUN("Pay4Fun"),
  
  PIN_PAY("PinPay"),
  
  PHONE("phone"),
  
  PHONE_PE("PhonePe"),
  
  POLI("POLi"),
  
  POST_FINANCE_CARD("PostFinance-card"),
  
  POST_FINANCE_E_FINANCE("PostFinance-e-finance"),
  
  PRZELEWY24("Przelewy24"),
  
  QIWI("QIWI"),
  
  QQ_PAY("QQPay"),
  
  RESURS("Resurs"),
  
  SEPA("SEPA"),
  
  SKRILL("Skrill"),
  
  SKRILL_RAPID_TRANSFER("Skrill Rapid Transfer"),
  
  SMS_VOUCHER("SMSVoucher"),
  
  SOFORT("Sofort"),
  
  SPARK_PAY("SparkPay"),
  
  SWIFT_DBT("swift-dbt"),
  
  TELE2("Tele2"),
  
  TERMINALY_RF("Terminaly-RF"),
  
  TODITO_CASH_CARD("ToditoCash-card"),
  
  TRUSTLY("Trustly"),
  
  U_PAY_CARD("UPayCard"),
  
  UPI("UPI"),
  
  V_CREDITOS("VCreditos"),
  
  VENUS_POINT("VenusPoint"),
  
  VOUCHER("voucher"),
  
  VOUCHER_2("voucher-2"),
  
  VOUCHER_3("voucher-3"),
  
  VOUCHER_4("voucher-4"),
  
  WEBMONEY("Webmoney"),
  
  WEBPAY("Webpay"),
  
  WEBPAY_2("Webpay-2"),
  
  WEBPAY_CARD("Webpay Card"),
  
  WE_CHAT_PAY("WeChat Pay"),
  
  X_PAY_P2_P("XPay-P2P"),
  
  X_PAY_QR("XPay-QR"),
  
  YANDEX_MONEY("Yandex-money"),
  
  ZOTAPAY("Zotapay"),
  
  ZIMPLER("Zimpler");

  private String value;

  AlternativePaymentMethods(String value) {
    this.value = value;
  }

  public String getValue() {
    return value;
  }

  @Override
  public String toString() {
    return String.valueOf(value);
  }

  public static AlternativePaymentMethods fromValue(String value) {
    for (AlternativePaymentMethods b : AlternativePaymentMethods.values()) {
      if (b.value.equals(value)) {
        return b;
      }
    }
    throw new IllegalArgumentException("Unexpected value '" + value + "'");
  }

  public static class Adapter extends TypeAdapter<AlternativePaymentMethods> {
    @Override
    public void write(final JsonWriter jsonWriter, final AlternativePaymentMethods enumeration) throws IOException {
      jsonWriter.value(enumeration.getValue());
    }

    @Override
    public AlternativePaymentMethods read(final JsonReader jsonReader) throws IOException {
      String value = jsonReader.nextString();
      return AlternativePaymentMethods.fromValue(value);
    }
  }

  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
    String value = jsonElement.getAsString();
    AlternativePaymentMethods.fromValue(value);
  }
}

