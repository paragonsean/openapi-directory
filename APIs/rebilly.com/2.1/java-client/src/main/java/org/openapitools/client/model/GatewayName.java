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
 * The payment gateway name.
 */
@JsonAdapter(GatewayName.Adapter.class)
public enum GatewayName {
  
  A1_GATEWAY("A1Gateway"),
  
  ADYEN("Adyen"),
  
  AIRPAY("Airpay"),
  
  AMEX_VPC("AmexVPC"),
  
  APCO_PAY("ApcoPay"),
  
  ASIA_PAYMENT_GATEWAY("AsiaPaymentGateway"),
  
  ASTRO_PAY_CARD("AstroPayCard"),
  
  AUTHORIZE_NET("AuthorizeNet"),
  
  BAMBORA("Bambora"),
  
  BIT_PAY("BitPay"),
  
  BLUE_SNAP("BlueSnap"),
  
  BRAINTREE_PAYMENTS("BraintreePayments"),
  
  CARDKNOX("Cardknox"),
  
  CASHFLOWS("Cashflows"),
  
  CAS_HLIB("CASHlib"),
  
  CASH_TO_CODE("CashToCode"),
  
  CAURI_PAYMENT("CauriPayment"),
  
  CAYAN("Cayan"),
  
  CC_AVENUE("CCAvenue"),
  
  CHASE("Chase"),
  
  CIRCLE("Circle"),
  
  CITADEL("Citadel"),
  
  CLEARHAUS("Clearhaus"),
  
  COD_VOUCHER("CODVoucher"),
  
  COIN_PAYMENTS("CoinPayments"),
  
  CONEKTA("Conekta"),
  
  COPPR("Coppr"),
  
  CREDORAX("Credorax"),
  
  CRYPTONATOR("Cryptonator"),
  
  CYBER_SOURCE("CyberSource"),
  
  DATA_CASH("DataCash"),
  
  DENGI("Dengi"),
  
  DRAGONPHOENIX("Dragonphoenix"),
  
  DIRECTA24("Directa24"),
  
  D_LOCAL("dLocal"),
  
  EBANX("EBANX"),
  
  ECO_PAYZ("ecoPayz"),
  
  ECORE_PAY("EcorePay"),
  
  ELAVON("Elavon"),
  
  EUTELLER("Euteller"),
  
  E_MERCHANT_PAY("eMerchantPay"),
  
  EMS("EMS"),
  
  EPG("EPG"),
  
  E_PRO("EPro"),
  
  E_ZEE_WALLET("eZeeWallet"),
  
  EZY_EFT("ezyEFT"),
  
  FINRAX("Finrax"),
  
  FLEXEPIN("Flexepin"),
  
  FIN_TEC_SYSTEMS("FinTecSystems"),
  
  FUND_SEND("FundSend"),
  
  FORTE("Forte"),
  
  GET("GET"),
  
  GIGADAT("Gigadat"),
  
  GLOBAL_ONE_PAY("GlobalOnePay"),
  
  GOONEY("Gooney"),
  
  GPAYSAFE("Gpaysafe"),
  
  GREENBOX("Greenbox"),
  
  HI_PAY("HiPay"),
  
  I_CAN_PAY("iCanPay"),
  
  ICEPAY("ICEPAY"),
  
  I_CHEQUE("iCheque"),
  
  I_DEBIT("iDebit"),
  
  ILIXIUM("Ilixium"),
  
  INGENICO("Ingenico"),
  
  INOVAPAY("INOVAPAY"),
  
  INOVIO("Inovio"),
  
  INTUIT("Intuit"),
  
  INSTA_DEBIT("InstaDebit"),
  
  IPAY_OPTIONS("IpayOptions"),
  
  JET_PAY("JetPay"),
  
  JETON("Jeton"),
  
  KHELOCARD("Khelocard"),
  
  KONNEKTIVE("Konnektive"),
  
  LOONIE("loonie"),
  
  LPG("LPG"),
  
  MI_FINITY("MiFinity"),
  
  MONERIS("Moneris"),
  
  MTA_PAY("MtaPay"),
  
  MUCH_BETTER("MuchBetter"),
  
  MY_FATOORAH("MyFatoorah"),
  
  NEOSURF("Neosurf"),
  
  NETBANKING("Netbanking"),
  
  NETELLER("Neteller"),
  
  N_GENIUS("NGenius"),
  
  NINJA_WALLET("NinjaWallet"),
  
  NMI("NMI"),
  
  NUA_PAY("NuaPay"),
  
  OCHA_PAY("OchaPay"),
  
  ONLINEUEBERWEISEN("Onlineueberweisen"),
  
  ON_RAMP("OnRamp"),
  
  PAGSMILE("Pagsmile"),
  
  PANAMERICAN("Panamerican"),
  
  PARAMOUNT_EFT("ParamountEft"),
  
  PARAMOUNT_INTERAC("ParamountInterac"),
  
  PANDA_GATEWAY("PandaGateway"),
  
  PAY4_FUN("Pay4Fun"),
  
  PAY_CASH("PayCash"),
  
  PAY_CLUB("PayClub"),
  
  PAYEEZY("Payeezy"),
  
  PAYFLOW("Payflow"),
  
  PAYMENT_ASIA("PaymentAsia"),
  
  PAYMEN_TECHNOLOGIES("PaymenTechnologies"),
  
  PAYMENTS_OS("PaymentsOS"),
  
  PAYMERO("Paymero"),
  
  PAY_PAL("PayPal"),
  
  PAYR("Payr"),
  
  PAYSAFE("Paysafe"),
  
  PAYSAFECASH("Paysafecash"),
  
  PAY_TABS("PayTabs"),
  
  PAY_U_LATAM("PayULatam"),
  
  PAYVISION("Payvision"),
  
  PIASTRIX("Piastrix"),
  
  PLUGNPAY("Plugnpay"),
  
  POST_FINANCE("PostFinance"),
  
  PROSA("Prosa"),
  
  RAPYD("Rapyd"),
  
  REALEX("Realex"),
  
  REALTIME("Realtime"),
  
  REDSYS("Redsys"),
  
  ROTESSA("Rotessa"),
  
  RPN("RPN"),
  
  SALTAR_PAY("SaltarPay"),
  
  SAGEPAY("Sagepay"),
  
  SEAMLESS_CHEX("SeamlessChex"),
  
  SECURE_TRADING("SecureTrading"),
  
  SECURION_PAY("SecurionPay"),
  
  SKRILL("Skrill"),
  
  SMART_INVOICE("SmartInvoice"),
  
  SMS_VOUCHER("SMSVoucher"),
  
  SOFORT("Sofort"),
  
  SPARK_PAY("SparkPay"),
  
  STATIC_GATEWAY("StaticGateway"),
  
  STRIPE("Stripe"),
  
  TEST_PROCESSOR("TestProcessor"),
  
  TODITO_CASH("ToditoCash"),
  
  TRUST_PAY("TrustPay"),
  
  TRUSTS_PAY("TrustsPay"),
  
  TRUSTLY("Trustly"),
  
  TWINT("TWINT"),
  
  U_PAY_CARD("UPayCard"),
  
  USAE_PAY("USAePay"),
  
  VANTIV_LITLE("VantivLitle"),
  
  VEGAA_H("vegaaH"),
  
  V_CREDITOS("VCreditos"),
  
  WALLET88("Wallet88"),
  
  WALPAY("Walpay"),
  
  WIRECARD("Wirecard"),
  
  WORLDLINE_ATOS_FRANKFURT("WorldlineAtosFrankfurt"),
  
  WORLDPAY("Worldpay"),
  
  X_PAY("XPay"),
  
  ZIMPLER("Zimpler"),
  
  ZOTAPAY("Zotapay");

  private String value;

  GatewayName(String value) {
    this.value = value;
  }

  public String getValue() {
    return value;
  }

  @Override
  public String toString() {
    return String.valueOf(value);
  }

  public static GatewayName fromValue(String value) {
    for (GatewayName b : GatewayName.values()) {
      if (b.value.equals(value)) {
        return b;
      }
    }
    throw new IllegalArgumentException("Unexpected value '" + value + "'");
  }

  public static class Adapter extends TypeAdapter<GatewayName> {
    @Override
    public void write(final JsonWriter jsonWriter, final GatewayName enumeration) throws IOException {
      jsonWriter.value(enumeration.getValue());
    }

    @Override
    public GatewayName read(final JsonReader jsonReader) throws IOException {
      String value = jsonReader.nextString();
      return GatewayName.fromValue(value);
    }
  }

  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
    String value = jsonElement.getAsString();
    GatewayName.fromValue(value);
  }
}

