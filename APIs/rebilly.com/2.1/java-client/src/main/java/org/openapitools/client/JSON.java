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


package org.openapitools.client;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonParseException;
import com.google.gson.TypeAdapter;
import com.google.gson.internal.bind.util.ISO8601Utils;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import com.google.gson.JsonElement;
import io.gsonfire.GsonFireBuilder;
import io.gsonfire.TypeSelector;

import okio.ByteString;

import java.io.IOException;
import java.io.StringReader;
import java.lang.reflect.Type;
import java.text.DateFormat;
import java.text.ParseException;
import java.text.ParsePosition;
import java.time.LocalDate;
import java.time.OffsetDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Date;
import java.util.Locale;
import java.util.Map;
import java.util.HashMap;

/*
 * A JSON utility class
 *
 * NOTE: in the future, this class may be converted to static, which may break
 *       backward-compatibility
 */
public class JSON {
    private static Gson gson;
    private static boolean isLenientOnJson = false;
    private static DateTypeAdapter dateTypeAdapter = new DateTypeAdapter();
    private static SqlDateTypeAdapter sqlDateTypeAdapter = new SqlDateTypeAdapter();
    private static OffsetDateTimeTypeAdapter offsetDateTimeTypeAdapter = new OffsetDateTimeTypeAdapter();
    private static LocalDateTypeAdapter localDateTypeAdapter = new LocalDateTypeAdapter();
    private static ByteArrayAdapter byteArrayAdapter = new ByteArrayAdapter();

    @SuppressWarnings("unchecked")
    public static GsonBuilder createGson() {
        GsonFireBuilder fireBuilder = new GsonFireBuilder()
                .registerTypeSelector(org.openapitools.client.model.A1Gateway.class, new TypeSelector<org.openapitools.client.model.A1Gateway>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.A1Gateway> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("A1Gateway", org.openapitools.client.model.A1Gateway.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.A1Gateway3dsServers.class, new TypeSelector<org.openapitools.client.model.A1Gateway3dsServers>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.A1Gateway3dsServers> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Other", org.openapitools.client.model.Other.class);
                        classByDiscriminatorValue.put("Paay3dsServer", org.openapitools.client.model.Paay3dsServer.class);
                        classByDiscriminatorValue.put("A1Gateway3dsServers", org.openapitools.client.model.A1Gateway3dsServers.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "name"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Adyen.class, new TypeSelector<org.openapitools.client.model.Adyen>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Adyen> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Adyen", org.openapitools.client.model.Adyen.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Airpay.class, new TypeSelector<org.openapitools.client.model.Airpay>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Airpay> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Airpay", org.openapitools.client.model.Airpay.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.AmexVPC.class, new TypeSelector<org.openapitools.client.model.AmexVPC>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.AmexVPC> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("AmexVPC", org.openapitools.client.model.AmexVPC.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.AmountAdjustment.class, new TypeSelector<org.openapitools.client.model.AmountAdjustment>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.AmountAdjustment> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("discount", org.openapitools.client.model.Discount.class);
                        classByDiscriminatorValue.put("partial", org.openapitools.client.model.Partial.class);
                        classByDiscriminatorValue.put("AmountAdjustment", org.openapitools.client.model.AmountAdjustment.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "method"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.ApcoPay.class, new TypeSelector<org.openapitools.client.model.ApcoPay>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.ApcoPay> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("ApcoPay", org.openapitools.client.model.ApcoPay.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.ApplePayValidation.class, new TypeSelector<org.openapitools.client.model.ApplePayValidation>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.ApplePayValidation> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("ApplePayValidation", org.openapitools.client.model.ApplePayValidation.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "type"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.AsiaPaymentGateway.class, new TypeSelector<org.openapitools.client.model.AsiaPaymentGateway>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.AsiaPaymentGateway> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("AsiaPaymentGateway", org.openapitools.client.model.AsiaPaymentGateway.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.AstroPayCard.class, new TypeSelector<org.openapitools.client.model.AstroPayCard>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.AstroPayCard> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("AstroPayCard", org.openapitools.client.model.AstroPayCard.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.AuthenticationToken.class, new TypeSelector<org.openapitools.client.model.AuthenticationToken>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.AuthenticationToken> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("password", org.openapitools.client.model.Password.class);
                        classByDiscriminatorValue.put("passwordless", org.openapitools.client.model.Passwordless.class);
                        classByDiscriminatorValue.put("AuthenticationToken", org.openapitools.client.model.AuthenticationToken.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "mode"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.AuthorizeNet.class, new TypeSelector<org.openapitools.client.model.AuthorizeNet>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.AuthorizeNet> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("AuthorizeNet", org.openapitools.client.model.AuthorizeNet.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Auto.class, new TypeSelector<org.openapitools.client.model.Auto>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Auto> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("auto", org.openapitools.client.model.Auto.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "method"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.BBANInstrument.class, new TypeSelector<org.openapitools.client.model.BBANInstrument>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.BBANInstrument> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("BBANInstrument", org.openapitools.client.model.BBANInstrument.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "accountNumberType"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Bambora.class, new TypeSelector<org.openapitools.client.model.Bambora>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Bambora> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Bambora", org.openapitools.client.model.Bambora.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.BankAccountInstrument.class, new TypeSelector<org.openapitools.client.model.BankAccountInstrument>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.BankAccountInstrument> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("BBAN", org.openapitools.client.model.BBANInstrument.class);
                        classByDiscriminatorValue.put("IBAN", org.openapitools.client.model.IBANInstrument.class);
                        classByDiscriminatorValue.put("BankAccountInstrument", org.openapitools.client.model.BankAccountInstrument.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "accountNumberType"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.BitPay.class, new TypeSelector<org.openapitools.client.model.BitPay>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.BitPay> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("BitPay", org.openapitools.client.model.BitPay.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.BlueSnap.class, new TypeSelector<org.openapitools.client.model.BlueSnap>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.BlueSnap> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("BlueSnap", org.openapitools.client.model.BlueSnap.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.BraintreePayments.class, new TypeSelector<org.openapitools.client.model.BraintreePayments>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.BraintreePayments> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("BraintreePayments", org.openapitools.client.model.BraintreePayments.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.CASHlib.class, new TypeSelector<org.openapitools.client.model.CASHlib>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.CASHlib> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("CASHlib", org.openapitools.client.model.CASHlib.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.CCAvenue.class, new TypeSelector<org.openapitools.client.model.CCAvenue>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.CCAvenue> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("CCAvenue", org.openapitools.client.model.CCAvenue.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.CODVoucher.class, new TypeSelector<org.openapitools.client.model.CODVoucher>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.CODVoucher> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("CODVoucher", org.openapitools.client.model.CODVoucher.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.CardinalCommerce3dsServer.class, new TypeSelector<org.openapitools.client.model.CardinalCommerce3dsServer>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.CardinalCommerce3dsServer> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("CardinalCommerce3dsServer", org.openapitools.client.model.CardinalCommerce3dsServer.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "name"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Cardknox.class, new TypeSelector<org.openapitools.client.model.Cardknox>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Cardknox> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Cardknox", org.openapitools.client.model.Cardknox.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.CashToCode.class, new TypeSelector<org.openapitools.client.model.CashToCode>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.CashToCode> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("CashToCode", org.openapitools.client.model.CashToCode.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Cashflows.class, new TypeSelector<org.openapitools.client.model.Cashflows>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Cashflows> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Cashflows", org.openapitools.client.model.Cashflows.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.CauriPayment.class, new TypeSelector<org.openapitools.client.model.CauriPayment>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.CauriPayment> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("CauriPayment", org.openapitools.client.model.CauriPayment.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Cayan.class, new TypeSelector<org.openapitools.client.model.Cayan>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Cayan> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Cayan", org.openapitools.client.model.Cayan.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Chase.class, new TypeSelector<org.openapitools.client.model.Chase>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Chase> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Chase", org.openapitools.client.model.Chase.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Circle.class, new TypeSelector<org.openapitools.client.model.Circle>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Circle> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Circle", org.openapitools.client.model.Circle.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Citadel.class, new TypeSelector<org.openapitools.client.model.Citadel>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Citadel> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Citadel", org.openapitools.client.model.Citadel.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Clearhaus.class, new TypeSelector<org.openapitools.client.model.Clearhaus>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Clearhaus> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Clearhaus", org.openapitools.client.model.Clearhaus.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Clearhaus3dsServer.class, new TypeSelector<org.openapitools.client.model.Clearhaus3dsServer>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Clearhaus3dsServer> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Clearhaus3dsServer", org.openapitools.client.model.Clearhaus3dsServer.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "name"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Clearhaus3dsServers.class, new TypeSelector<org.openapitools.client.model.Clearhaus3dsServers>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Clearhaus3dsServers> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Clearhaus3dsServer", org.openapitools.client.model.Clearhaus3dsServer.class);
                        classByDiscriminatorValue.put("Clearhaus3dsServers", org.openapitools.client.model.Clearhaus3dsServers.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "name"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.CoinPayments.class, new TypeSelector<org.openapitools.client.model.CoinPayments>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.CoinPayments> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("CoinPayments", org.openapitools.client.model.CoinPayments.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.CommonScheduleInstruction.class, new TypeSelector<org.openapitools.client.model.CommonScheduleInstruction>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.CommonScheduleInstruction> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("auto", org.openapitools.client.model.Auto.class);
                        classByDiscriminatorValue.put("date-interval", org.openapitools.client.model.DateInterval.class);
                        classByDiscriminatorValue.put("day-of-month", org.openapitools.client.model.DayOfMonth.class);
                        classByDiscriminatorValue.put("day-of-week", org.openapitools.client.model.DayOfWeek.class);
                        classByDiscriminatorValue.put("immediately", org.openapitools.client.model.Immediately.class);
                        classByDiscriminatorValue.put("intelligent", org.openapitools.client.model.Intelligent.class);
                        classByDiscriminatorValue.put("CommonScheduleInstruction", org.openapitools.client.model.CommonScheduleInstruction.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "method"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Conekta.class, new TypeSelector<org.openapitools.client.model.Conekta>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Conekta> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Conekta", org.openapitools.client.model.Conekta.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Coppr.class, new TypeSelector<org.openapitools.client.model.Coppr>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Coppr> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Coppr", org.openapitools.client.model.Coppr.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.CouponRestriction.class, new TypeSelector<org.openapitools.client.model.CouponRestriction>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.CouponRestriction> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("discounts-per-redemption", org.openapitools.client.model.DiscountsPerRedemption.class);
                        classByDiscriminatorValue.put("minimum-order-amount", org.openapitools.client.model.MinimumOrderAmount.class);
                        classByDiscriminatorValue.put("paid-by-time", org.openapitools.client.model.PaidByTime.class);
                        classByDiscriminatorValue.put("redemptions-per-customer", org.openapitools.client.model.RedemptionsPerCustomer.class);
                        classByDiscriminatorValue.put("restrict-to-invoices", org.openapitools.client.model.RestrictToInvoices.class);
                        classByDiscriminatorValue.put("restrict-to-plans", org.openapitools.client.model.RestrictToPlans.class);
                        classByDiscriminatorValue.put("restrict-to-products", org.openapitools.client.model.RestrictToProducts.class);
                        classByDiscriminatorValue.put("restrict-to-subscriptions", org.openapitools.client.model.RestrictToSubscriptions.class);
                        classByDiscriminatorValue.put("total-redemptions", org.openapitools.client.model.TotalRedemptions.class);
                        classByDiscriminatorValue.put("CouponRestriction", org.openapitools.client.model.CouponRestriction.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "type"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Credorax.class, new TypeSelector<org.openapitools.client.model.Credorax>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Credorax> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Credorax", org.openapitools.client.model.Credorax.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Cryptonator.class, new TypeSelector<org.openapitools.client.model.Cryptonator>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Cryptonator> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Cryptonator", org.openapitools.client.model.Cryptonator.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.CustomEventScheduleInstruction.class, new TypeSelector<org.openapitools.client.model.CustomEventScheduleInstruction>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.CustomEventScheduleInstruction> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("CustomEventScheduleInstruction", org.openapitools.client.model.CustomEventScheduleInstruction.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "method"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.CyberSource.class, new TypeSelector<org.openapitools.client.model.CyberSource>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.CyberSource> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("CyberSource", org.openapitools.client.model.CyberSource.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.DLocal.class, new TypeSelector<org.openapitools.client.model.DLocal>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.DLocal> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("dLocal", org.openapitools.client.model.DLocal.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.DataCash.class, new TypeSelector<org.openapitools.client.model.DataCash>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.DataCash> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("DataCash", org.openapitools.client.model.DataCash.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.DataCash3dsServer.class, new TypeSelector<org.openapitools.client.model.DataCash3dsServer>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.DataCash3dsServer> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("DataCash3dsServer", org.openapitools.client.model.DataCash3dsServer.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "name"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.DataCash3dsServers.class, new TypeSelector<org.openapitools.client.model.DataCash3dsServers>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.DataCash3dsServers> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("DataCash3dsServer", org.openapitools.client.model.DataCash3dsServer.class);
                        classByDiscriminatorValue.put("DataCash3dsServers", org.openapitools.client.model.DataCash3dsServers.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "name"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.DateInterval.class, new TypeSelector<org.openapitools.client.model.DateInterval>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.DateInterval> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("date-interval", org.openapitools.client.model.DateInterval.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "method"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.DayOfMonth.class, new TypeSelector<org.openapitools.client.model.DayOfMonth>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.DayOfMonth> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("day-of-month", org.openapitools.client.model.DayOfMonth.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "method"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.DayOfWeek.class, new TypeSelector<org.openapitools.client.model.DayOfWeek>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.DayOfWeek> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("day-of-week", org.openapitools.client.model.DayOfWeek.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "method"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Dengi.class, new TypeSelector<org.openapitools.client.model.Dengi>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Dengi> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Dengi", org.openapitools.client.model.Dengi.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.DigitalWalletValidation.class, new TypeSelector<org.openapitools.client.model.DigitalWalletValidation>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.DigitalWalletValidation> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Apple Pay", org.openapitools.client.model.ApplePayValidation.class);
                        classByDiscriminatorValue.put("DigitalWalletValidation", org.openapitools.client.model.DigitalWalletValidation.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "type"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Directa24.class, new TypeSelector<org.openapitools.client.model.Directa24>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Directa24> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Directa24", org.openapitools.client.model.Directa24.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Discount.class, new TypeSelector<org.openapitools.client.model.Discount>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Discount> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("discount", org.openapitools.client.model.Discount.class);
                        classByDiscriminatorValue.put("partial", org.openapitools.client.model.Partial.class);
                        classByDiscriminatorValue.put("discount", org.openapitools.client.model.Discount.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "method"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.DiscountsPerRedemption.class, new TypeSelector<org.openapitools.client.model.DiscountsPerRedemption>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.DiscountsPerRedemption> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("discounts-per-redemption", org.openapitools.client.model.DiscountsPerRedemption.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "type"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Dragonphoenix.class, new TypeSelector<org.openapitools.client.model.Dragonphoenix>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Dragonphoenix> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Dragonphoenix", org.openapitools.client.model.Dragonphoenix.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.EBANX.class, new TypeSelector<org.openapitools.client.model.EBANX>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.EBANX> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("EBANX", org.openapitools.client.model.EBANX.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.EMS.class, new TypeSelector<org.openapitools.client.model.EMS>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.EMS> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("EMS", org.openapitools.client.model.EMS.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.EMS3dsServers.class, new TypeSelector<org.openapitools.client.model.EMS3dsServers>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.EMS3dsServers> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("EMS3dsServers", org.openapitools.client.model.EMS3dsServers.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "name"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.EMerchantPay.class, new TypeSelector<org.openapitools.client.model.EMerchantPay>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.EMerchantPay> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("eMerchantPay", org.openapitools.client.model.EMerchantPay.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.EMerchantPay3dsServer.class, new TypeSelector<org.openapitools.client.model.EMerchantPay3dsServer>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.EMerchantPay3dsServer> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("eMerchantPay3dsServer", org.openapitools.client.model.EMerchantPay3dsServer.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "name"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.EMerchantPay3dsServers.class, new TypeSelector<org.openapitools.client.model.EMerchantPay3dsServers>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.EMerchantPay3dsServers> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Other", org.openapitools.client.model.Other.class);
                        classByDiscriminatorValue.put("Paay3dsServer", org.openapitools.client.model.Paay3dsServer.class);
                        classByDiscriminatorValue.put("ThreeDSecureIO3dsServer", org.openapitools.client.model.ThreeDSecureIO3dsServer.class);
                        classByDiscriminatorValue.put("eMerchantPay3dsServer", org.openapitools.client.model.EMerchantPay3dsServer.class);
                        classByDiscriminatorValue.put("eMerchantPay3dsServers", org.openapitools.client.model.EMerchantPay3dsServers.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "name"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.EPG.class, new TypeSelector<org.openapitools.client.model.EPG>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.EPG> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("EPG", org.openapitools.client.model.EPG.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.EPro.class, new TypeSelector<org.openapitools.client.model.EPro>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.EPro> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("EPro", org.openapitools.client.model.EPro.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.EZeeWallet.class, new TypeSelector<org.openapitools.client.model.EZeeWallet>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.EZeeWallet> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("eZeeWallet", org.openapitools.client.model.EZeeWallet.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.EcoPayz.class, new TypeSelector<org.openapitools.client.model.EcoPayz>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.EcoPayz> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("ecoPayz", org.openapitools.client.model.EcoPayz.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.EcorePay.class, new TypeSelector<org.openapitools.client.model.EcorePay>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.EcorePay> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("EcorePay", org.openapitools.client.model.EcorePay.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Elavon.class, new TypeSelector<org.openapitools.client.model.Elavon>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Elavon> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Elavon", org.openapitools.client.model.Elavon.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Euteller.class, new TypeSelector<org.openapitools.client.model.Euteller>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Euteller> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Euteller", org.openapitools.client.model.Euteller.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.EzyEFT.class, new TypeSelector<org.openapitools.client.model.EzyEFT>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.EzyEFT> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("ezyEFT", org.openapitools.client.model.EzyEFT.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.FinTecSystems.class, new TypeSelector<org.openapitools.client.model.FinTecSystems>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.FinTecSystems> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("FinTecSystems", org.openapitools.client.model.FinTecSystems.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Finrax.class, new TypeSelector<org.openapitools.client.model.Finrax>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Finrax> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Finrax", org.openapitools.client.model.Finrax.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Fixed.class, new TypeSelector<org.openapitools.client.model.Fixed>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Fixed> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("fixed", org.openapitools.client.model.Fixed.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "type"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.FixedFee.class, new TypeSelector<org.openapitools.client.model.FixedFee>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.FixedFee> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("fixed-fee", org.openapitools.client.model.FixedFee.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "formula"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.FlatRate.class, new TypeSelector<org.openapitools.client.model.FlatRate>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.FlatRate> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("flat-rate", org.openapitools.client.model.FlatRate.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "formula"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Flexepin.class, new TypeSelector<org.openapitools.client.model.Flexepin>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Flexepin> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Flexepin", org.openapitools.client.model.Flexepin.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Forte.class, new TypeSelector<org.openapitools.client.model.Forte>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Forte> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Forte", org.openapitools.client.model.Forte.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.FundSend.class, new TypeSelector<org.openapitools.client.model.FundSend>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.FundSend> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("FundSend", org.openapitools.client.model.FundSend.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.GET.class, new TypeSelector<org.openapitools.client.model.GET>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.GET> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("GET", org.openapitools.client.model.GET.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.GET3dsServers.class, new TypeSelector<org.openapitools.client.model.GET3dsServers>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.GET3dsServers> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("GET3dsServers", org.openapitools.client.model.GET3dsServers.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "name"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.GatewayAccount.class, new TypeSelector<org.openapitools.client.model.GatewayAccount>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.GatewayAccount> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("A1Gateway", org.openapitools.client.model.A1Gateway.class);
                        classByDiscriminatorValue.put("Adyen", org.openapitools.client.model.Adyen.class);
                        classByDiscriminatorValue.put("Airpay", org.openapitools.client.model.Airpay.class);
                        classByDiscriminatorValue.put("AmexVPC", org.openapitools.client.model.AmexVPC.class);
                        classByDiscriminatorValue.put("ApcoPay", org.openapitools.client.model.ApcoPay.class);
                        classByDiscriminatorValue.put("AsiaPaymentGateway", org.openapitools.client.model.AsiaPaymentGateway.class);
                        classByDiscriminatorValue.put("AstroPayCard", org.openapitools.client.model.AstroPayCard.class);
                        classByDiscriminatorValue.put("AuthorizeNet", org.openapitools.client.model.AuthorizeNet.class);
                        classByDiscriminatorValue.put("Bambora", org.openapitools.client.model.Bambora.class);
                        classByDiscriminatorValue.put("BitPay", org.openapitools.client.model.BitPay.class);
                        classByDiscriminatorValue.put("BlueSnap", org.openapitools.client.model.BlueSnap.class);
                        classByDiscriminatorValue.put("BraintreePayments", org.openapitools.client.model.BraintreePayments.class);
                        classByDiscriminatorValue.put("CASHlib", org.openapitools.client.model.CASHlib.class);
                        classByDiscriminatorValue.put("CCAvenue", org.openapitools.client.model.CCAvenue.class);
                        classByDiscriminatorValue.put("CODVoucher", org.openapitools.client.model.CODVoucher.class);
                        classByDiscriminatorValue.put("Cardknox", org.openapitools.client.model.Cardknox.class);
                        classByDiscriminatorValue.put("CashToCode", org.openapitools.client.model.CashToCode.class);
                        classByDiscriminatorValue.put("Cashflows", org.openapitools.client.model.Cashflows.class);
                        classByDiscriminatorValue.put("CauriPayment", org.openapitools.client.model.CauriPayment.class);
                        classByDiscriminatorValue.put("Cayan", org.openapitools.client.model.Cayan.class);
                        classByDiscriminatorValue.put("Chase", org.openapitools.client.model.Chase.class);
                        classByDiscriminatorValue.put("Circle", org.openapitools.client.model.Circle.class);
                        classByDiscriminatorValue.put("Citadel", org.openapitools.client.model.Citadel.class);
                        classByDiscriminatorValue.put("Clearhaus", org.openapitools.client.model.Clearhaus.class);
                        classByDiscriminatorValue.put("CoinPayments", org.openapitools.client.model.CoinPayments.class);
                        classByDiscriminatorValue.put("Conekta", org.openapitools.client.model.Conekta.class);
                        classByDiscriminatorValue.put("Coppr", org.openapitools.client.model.Coppr.class);
                        classByDiscriminatorValue.put("Credorax", org.openapitools.client.model.Credorax.class);
                        classByDiscriminatorValue.put("Cryptonator", org.openapitools.client.model.Cryptonator.class);
                        classByDiscriminatorValue.put("CyberSource", org.openapitools.client.model.CyberSource.class);
                        classByDiscriminatorValue.put("DataCash", org.openapitools.client.model.DataCash.class);
                        classByDiscriminatorValue.put("Dengi", org.openapitools.client.model.Dengi.class);
                        classByDiscriminatorValue.put("Directa24", org.openapitools.client.model.Directa24.class);
                        classByDiscriminatorValue.put("Dragonphoenix", org.openapitools.client.model.Dragonphoenix.class);
                        classByDiscriminatorValue.put("EBANX", org.openapitools.client.model.EBANX.class);
                        classByDiscriminatorValue.put("EMS", org.openapitools.client.model.EMS.class);
                        classByDiscriminatorValue.put("EPG", org.openapitools.client.model.EPG.class);
                        classByDiscriminatorValue.put("EPro", org.openapitools.client.model.EPro.class);
                        classByDiscriminatorValue.put("EcorePay", org.openapitools.client.model.EcorePay.class);
                        classByDiscriminatorValue.put("Elavon", org.openapitools.client.model.Elavon.class);
                        classByDiscriminatorValue.put("Euteller", org.openapitools.client.model.Euteller.class);
                        classByDiscriminatorValue.put("FinTecSystems", org.openapitools.client.model.FinTecSystems.class);
                        classByDiscriminatorValue.put("Finrax", org.openapitools.client.model.Finrax.class);
                        classByDiscriminatorValue.put("Flexepin", org.openapitools.client.model.Flexepin.class);
                        classByDiscriminatorValue.put("Forte", org.openapitools.client.model.Forte.class);
                        classByDiscriminatorValue.put("FundSend", org.openapitools.client.model.FundSend.class);
                        classByDiscriminatorValue.put("GET", org.openapitools.client.model.GET.class);
                        classByDiscriminatorValue.put("Gigadat", org.openapitools.client.model.Gigadat.class);
                        classByDiscriminatorValue.put("GlobalOne", org.openapitools.client.model.GlobalOne.class);
                        classByDiscriminatorValue.put("Gooney", org.openapitools.client.model.Gooney.class);
                        classByDiscriminatorValue.put("Gpaysafe", org.openapitools.client.model.Gpaysafe.class);
                        classByDiscriminatorValue.put("Greenbox", org.openapitools.client.model.Greenbox.class);
                        classByDiscriminatorValue.put("HiPay", org.openapitools.client.model.HiPay.class);
                        classByDiscriminatorValue.put("ICEPAY", org.openapitools.client.model.ICEPAY.class);
                        classByDiscriminatorValue.put("INOVAPAY", org.openapitools.client.model.INOVAPAY.class);
                        classByDiscriminatorValue.put("Ilixium", org.openapitools.client.model.Ilixium.class);
                        classByDiscriminatorValue.put("Ingenico", org.openapitools.client.model.Ingenico.class);
                        classByDiscriminatorValue.put("Inovio", org.openapitools.client.model.Inovio.class);
                        classByDiscriminatorValue.put("InstaDebit", org.openapitools.client.model.InstaDebit.class);
                        classByDiscriminatorValue.put("Intuit", org.openapitools.client.model.Intuit.class);
                        classByDiscriminatorValue.put("IpayOptions", org.openapitools.client.model.IpayOptions.class);
                        classByDiscriminatorValue.put("JetPay", org.openapitools.client.model.JetPay.class);
                        classByDiscriminatorValue.put("Jeton", org.openapitools.client.model.Jeton.class);
                        classByDiscriminatorValue.put("Khelocard", org.openapitools.client.model.Khelocard.class);
                        classByDiscriminatorValue.put("Konnektive", org.openapitools.client.model.Konnektive.class);
                        classByDiscriminatorValue.put("LPG", org.openapitools.client.model.LPG.class);
                        classByDiscriminatorValue.put("MiFinity", org.openapitools.client.model.MiFinity.class);
                        classByDiscriminatorValue.put("Moneris", org.openapitools.client.model.Moneris.class);
                        classByDiscriminatorValue.put("MtaPay", org.openapitools.client.model.MtaPay.class);
                        classByDiscriminatorValue.put("MuchBetter", org.openapitools.client.model.MuchBetter.class);
                        classByDiscriminatorValue.put("MyFatoorah", org.openapitools.client.model.MyFatoorah.class);
                        classByDiscriminatorValue.put("NGenius", org.openapitools.client.model.NGenius.class);
                        classByDiscriminatorValue.put("NMI", org.openapitools.client.model.NMI.class);
                        classByDiscriminatorValue.put("Neosurf", org.openapitools.client.model.Neosurf.class);
                        classByDiscriminatorValue.put("Netbanking", org.openapitools.client.model.Netbanking.class);
                        classByDiscriminatorValue.put("Neteller", org.openapitools.client.model.Neteller.class);
                        classByDiscriminatorValue.put("NinjaWallet", org.openapitools.client.model.NinjaWallet.class);
                        classByDiscriminatorValue.put("NuaPay", org.openapitools.client.model.NuaPay.class);
                        classByDiscriminatorValue.put("OchaPay", org.openapitools.client.model.OchaPay.class);
                        classByDiscriminatorValue.put("OnRamp", org.openapitools.client.model.OnRamp.class);
                        classByDiscriminatorValue.put("Onlineueberweisen", org.openapitools.client.model.Onlineueberweisen.class);
                        classByDiscriminatorValue.put("Pagsmile", org.openapitools.client.model.Pagsmile.class);
                        classByDiscriminatorValue.put("Panamerican", org.openapitools.client.model.Panamerican.class);
                        classByDiscriminatorValue.put("PandaGateway", org.openapitools.client.model.PandaGateway.class);
                        classByDiscriminatorValue.put("ParamountEft", org.openapitools.client.model.ParamountEft.class);
                        classByDiscriminatorValue.put("ParamountInterac", org.openapitools.client.model.ParamountInterac.class);
                        classByDiscriminatorValue.put("Pay4Fun", org.openapitools.client.model.Pay4Fun.class);
                        classByDiscriminatorValue.put("PayCash", org.openapitools.client.model.PayCash.class);
                        classByDiscriminatorValue.put("PayClub", org.openapitools.client.model.PayClub.class);
                        classByDiscriminatorValue.put("PayPal", org.openapitools.client.model.PayPal.class);
                        classByDiscriminatorValue.put("PayTabs", org.openapitools.client.model.PayTabs.class);
                        classByDiscriminatorValue.put("PayULatam", org.openapitools.client.model.PayULatam.class);
                        classByDiscriminatorValue.put("Payeezy", org.openapitools.client.model.Payeezy.class);
                        classByDiscriminatorValue.put("Payflow", org.openapitools.client.model.Payflow.class);
                        classByDiscriminatorValue.put("PaymenTechnologies", org.openapitools.client.model.PaymenTechnologies.class);
                        classByDiscriminatorValue.put("PaymentAsia", org.openapitools.client.model.PaymentAsia.class);
                        classByDiscriminatorValue.put("PaymentsOS", org.openapitools.client.model.PaymentsOS.class);
                        classByDiscriminatorValue.put("Paymero", org.openapitools.client.model.Paymero.class);
                        classByDiscriminatorValue.put("Payr", org.openapitools.client.model.Payr.class);
                        classByDiscriminatorValue.put("Paysafe", org.openapitools.client.model.Paysafe.class);
                        classByDiscriminatorValue.put("Paysafecash", org.openapitools.client.model.Paysafecash.class);
                        classByDiscriminatorValue.put("Payvision", org.openapitools.client.model.Payvision.class);
                        classByDiscriminatorValue.put("Piastrix", org.openapitools.client.model.Piastrix.class);
                        classByDiscriminatorValue.put("Plugnpay", org.openapitools.client.model.Plugnpay.class);
                        classByDiscriminatorValue.put("PostFinance", org.openapitools.client.model.PostFinance.class);
                        classByDiscriminatorValue.put("Prosa", org.openapitools.client.model.Prosa.class);
                        classByDiscriminatorValue.put("RPN", org.openapitools.client.model.RPN.class);
                        classByDiscriminatorValue.put("Rapyd", org.openapitools.client.model.Rapyd.class);
                        classByDiscriminatorValue.put("Realex", org.openapitools.client.model.Realex.class);
                        classByDiscriminatorValue.put("Realtime", org.openapitools.client.model.Realtime.class);
                        classByDiscriminatorValue.put("Redsys", org.openapitools.client.model.Redsys.class);
                        classByDiscriminatorValue.put("Rotessa", org.openapitools.client.model.Rotessa.class);
                        classByDiscriminatorValue.put("SMSVoucher", org.openapitools.client.model.SMSVoucher.class);
                        classByDiscriminatorValue.put("Sagepay", org.openapitools.client.model.Sagepay.class);
                        classByDiscriminatorValue.put("SaltarPay", org.openapitools.client.model.SaltarPay.class);
                        classByDiscriminatorValue.put("SeamlessChex", org.openapitools.client.model.SeamlessChex.class);
                        classByDiscriminatorValue.put("SecureTrading", org.openapitools.client.model.SecureTrading.class);
                        classByDiscriminatorValue.put("SecurionPay", org.openapitools.client.model.SecurionPay.class);
                        classByDiscriminatorValue.put("Skrill", org.openapitools.client.model.Skrill.class);
                        classByDiscriminatorValue.put("SmartInvoice", org.openapitools.client.model.SmartInvoice.class);
                        classByDiscriminatorValue.put("Sofort", org.openapitools.client.model.Sofort.class);
                        classByDiscriminatorValue.put("SparkPay", org.openapitools.client.model.SparkPay.class);
                        classByDiscriminatorValue.put("StaticGateway", org.openapitools.client.model.StaticGateway.class);
                        classByDiscriminatorValue.put("Stripe", org.openapitools.client.model.Stripe.class);
                        classByDiscriminatorValue.put("TWINT", org.openapitools.client.model.TWINT.class);
                        classByDiscriminatorValue.put("TestProcessor", org.openapitools.client.model.TestProcessor.class);
                        classByDiscriminatorValue.put("ToditoCash", org.openapitools.client.model.ToditoCash.class);
                        classByDiscriminatorValue.put("TrustPay", org.openapitools.client.model.TrustPay.class);
                        classByDiscriminatorValue.put("Trustly", org.openapitools.client.model.Trustly.class);
                        classByDiscriminatorValue.put("TrustsPay", org.openapitools.client.model.TrustsPay.class);
                        classByDiscriminatorValue.put("UPayCard", org.openapitools.client.model.UPayCard.class);
                        classByDiscriminatorValue.put("USAePay", org.openapitools.client.model.USAePay.class);
                        classByDiscriminatorValue.put("VCreditos", org.openapitools.client.model.VCreditos.class);
                        classByDiscriminatorValue.put("VantivLitle", org.openapitools.client.model.VantivLitle.class);
                        classByDiscriminatorValue.put("Wallet88", org.openapitools.client.model.Wallet88.class);
                        classByDiscriminatorValue.put("Walpay", org.openapitools.client.model.Walpay.class);
                        classByDiscriminatorValue.put("Wirecard", org.openapitools.client.model.Wirecard.class);
                        classByDiscriminatorValue.put("WorldlineAtosFrankfurt", org.openapitools.client.model.WorldlineAtosFrankfurt.class);
                        classByDiscriminatorValue.put("Worldpay", org.openapitools.client.model.Worldpay.class);
                        classByDiscriminatorValue.put("XPay", org.openapitools.client.model.XPay.class);
                        classByDiscriminatorValue.put("Zimpler", org.openapitools.client.model.Zimpler.class);
                        classByDiscriminatorValue.put("Zotapay", org.openapitools.client.model.Zotapay.class);
                        classByDiscriminatorValue.put("dLocal", org.openapitools.client.model.DLocal.class);
                        classByDiscriminatorValue.put("eMerchantPay", org.openapitools.client.model.EMerchantPay.class);
                        classByDiscriminatorValue.put("eZeeWallet", org.openapitools.client.model.EZeeWallet.class);
                        classByDiscriminatorValue.put("ecoPayz", org.openapitools.client.model.EcoPayz.class);
                        classByDiscriminatorValue.put("ezyEFT", org.openapitools.client.model.EzyEFT.class);
                        classByDiscriminatorValue.put("iCanPay", org.openapitools.client.model.ICanPay.class);
                        classByDiscriminatorValue.put("iCheque", org.openapitools.client.model.ICheque.class);
                        classByDiscriminatorValue.put("iDebit", org.openapitools.client.model.IDebit.class);
                        classByDiscriminatorValue.put("loonie", org.openapitools.client.model.Loonie.class);
                        classByDiscriminatorValue.put("vegaaH", org.openapitools.client.model.VegaaH.class);
                        classByDiscriminatorValue.put("GatewayAccount", org.openapitools.client.model.GatewayAccount.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Gigadat.class, new TypeSelector<org.openapitools.client.model.Gigadat>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Gigadat> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Gigadat", org.openapitools.client.model.Gigadat.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.GlobalOne.class, new TypeSelector<org.openapitools.client.model.GlobalOne>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.GlobalOne> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("GlobalOne", org.openapitools.client.model.GlobalOne.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Gooney.class, new TypeSelector<org.openapitools.client.model.Gooney>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Gooney> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Gooney", org.openapitools.client.model.Gooney.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Gpaysafe.class, new TypeSelector<org.openapitools.client.model.Gpaysafe>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Gpaysafe> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Gpaysafe", org.openapitools.client.model.Gpaysafe.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Greenbox.class, new TypeSelector<org.openapitools.client.model.Greenbox>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Greenbox> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Greenbox", org.openapitools.client.model.Greenbox.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.HiPay.class, new TypeSelector<org.openapitools.client.model.HiPay>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.HiPay> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("HiPay", org.openapitools.client.model.HiPay.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.IBANInstrument.class, new TypeSelector<org.openapitools.client.model.IBANInstrument>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.IBANInstrument> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("IBANInstrument", org.openapitools.client.model.IBANInstrument.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "accountNumberType"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.ICEPAY.class, new TypeSelector<org.openapitools.client.model.ICEPAY>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.ICEPAY> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("ICEPAY", org.openapitools.client.model.ICEPAY.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.ICanPay.class, new TypeSelector<org.openapitools.client.model.ICanPay>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.ICanPay> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("iCanPay", org.openapitools.client.model.ICanPay.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.ICheque.class, new TypeSelector<org.openapitools.client.model.ICheque>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.ICheque> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("iCheque", org.openapitools.client.model.ICheque.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.IDebit.class, new TypeSelector<org.openapitools.client.model.IDebit>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.IDebit> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("iDebit", org.openapitools.client.model.IDebit.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.INOVAPAY.class, new TypeSelector<org.openapitools.client.model.INOVAPAY>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.INOVAPAY> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("INOVAPAY", org.openapitools.client.model.INOVAPAY.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Ilixium.class, new TypeSelector<org.openapitools.client.model.Ilixium>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Ilixium> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Ilixium", org.openapitools.client.model.Ilixium.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Ilixium3dsServer.class, new TypeSelector<org.openapitools.client.model.Ilixium3dsServer>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Ilixium3dsServer> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Ilixium3dsServer", org.openapitools.client.model.Ilixium3dsServer.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "name"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Ilixium3dsServers.class, new TypeSelector<org.openapitools.client.model.Ilixium3dsServers>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Ilixium3dsServers> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Ilixium3dsServer", org.openapitools.client.model.Ilixium3dsServer.class);
                        classByDiscriminatorValue.put("Ilixium3dsServers", org.openapitools.client.model.Ilixium3dsServers.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "name"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Immediately.class, new TypeSelector<org.openapitools.client.model.Immediately>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Immediately> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("immediately", org.openapitools.client.model.Immediately.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "method"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Ingenico.class, new TypeSelector<org.openapitools.client.model.Ingenico>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Ingenico> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Ingenico", org.openapitools.client.model.Ingenico.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Ingenico3dsServer.class, new TypeSelector<org.openapitools.client.model.Ingenico3dsServer>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Ingenico3dsServer> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Ingenico3dsServer", org.openapitools.client.model.Ingenico3dsServer.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "name"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Ingenico3dsServers.class, new TypeSelector<org.openapitools.client.model.Ingenico3dsServers>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Ingenico3dsServers> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Ingenico3dsServer", org.openapitools.client.model.Ingenico3dsServer.class);
                        classByDiscriminatorValue.put("Ingenico3dsServers", org.openapitools.client.model.Ingenico3dsServers.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "name"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Inovio.class, new TypeSelector<org.openapitools.client.model.Inovio>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Inovio> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Inovio", org.openapitools.client.model.Inovio.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Inovio3dsServer.class, new TypeSelector<org.openapitools.client.model.Inovio3dsServer>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Inovio3dsServer> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Inovio3dsServer", org.openapitools.client.model.Inovio3dsServer.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "name"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Inovio3dsServers.class, new TypeSelector<org.openapitools.client.model.Inovio3dsServers>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Inovio3dsServers> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Inovio3dsServer", org.openapitools.client.model.Inovio3dsServer.class);
                        classByDiscriminatorValue.put("Inovio3dsServers", org.openapitools.client.model.Inovio3dsServers.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "name"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.InstaDebit.class, new TypeSelector<org.openapitools.client.model.InstaDebit>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.InstaDebit> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("InstaDebit", org.openapitools.client.model.InstaDebit.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Intelligent.class, new TypeSelector<org.openapitools.client.model.Intelligent>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Intelligent> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("intelligent", org.openapitools.client.model.Intelligent.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "method"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Intuit.class, new TypeSelector<org.openapitools.client.model.Intuit>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Intuit> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Intuit", org.openapitools.client.model.Intuit.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.InvoiceRetryScheduleInstruction.class, new TypeSelector<org.openapitools.client.model.InvoiceRetryScheduleInstruction>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.InvoiceRetryScheduleInstruction> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("InvoiceRetryScheduleInstruction", org.openapitools.client.model.InvoiceRetryScheduleInstruction.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "method"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.InvoiceShipping.class, new TypeSelector<org.openapitools.client.model.InvoiceShipping>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.InvoiceShipping> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("manual", org.openapitools.client.model.Manual.class);
                        classByDiscriminatorValue.put("rebilly", org.openapitools.client.model.Rebilly.class);
                        classByDiscriminatorValue.put("InvoiceShipping", org.openapitools.client.model.InvoiceShipping.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "calculator"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.InvoiceTax.class, new TypeSelector<org.openapitools.client.model.InvoiceTax>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.InvoiceTax> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("manual", org.openapitools.client.model.Manual2.class);
                        classByDiscriminatorValue.put("rebilly", org.openapitools.client.model.RebillyTaxjar.class);
                        classByDiscriminatorValue.put("InvoiceTax", org.openapitools.client.model.InvoiceTax.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "calculator"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.IpayOptions.class, new TypeSelector<org.openapitools.client.model.IpayOptions>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.IpayOptions> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("IpayOptions", org.openapitools.client.model.IpayOptions.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.JetPay.class, new TypeSelector<org.openapitools.client.model.JetPay>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.JetPay> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("JetPay", org.openapitools.client.model.JetPay.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Jeton.class, new TypeSelector<org.openapitools.client.model.Jeton>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Jeton> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Jeton", org.openapitools.client.model.Jeton.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Khelocard.class, new TypeSelector<org.openapitools.client.model.Khelocard>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Khelocard> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Khelocard", org.openapitools.client.model.Khelocard.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Konnektive.class, new TypeSelector<org.openapitools.client.model.Konnektive>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Konnektive> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Konnektive", org.openapitools.client.model.Konnektive.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.KycDocument2.class, new TypeSelector<org.openapitools.client.model.KycDocument2>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.KycDocument2> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("address-proof", org.openapitools.client.model.ProofOfAddress.class);
                        classByDiscriminatorValue.put("funds-proof", org.openapitools.client.model.ProofOfFunds.class);
                        classByDiscriminatorValue.put("identity-proof", org.openapitools.client.model.ProofOfIdentity.class);
                        classByDiscriminatorValue.put("purchase-proof", org.openapitools.client.model.ProofOfPurchase.class);
                        classByDiscriminatorValue.put("ProofOfAddress", org.openapitools.client.model.ProofOfAddress.class);
                        classByDiscriminatorValue.put("ProofOfFunds", org.openapitools.client.model.ProofOfFunds.class);
                        classByDiscriminatorValue.put("ProofOfIdentity", org.openapitools.client.model.ProofOfIdentity.class);
                        classByDiscriminatorValue.put("ProofOfPurchase", org.openapitools.client.model.ProofOfPurchase.class);
                        classByDiscriminatorValue.put("KycDocument-2", org.openapitools.client.model.KycDocument2.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "documentType"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.LPG.class, new TypeSelector<org.openapitools.client.model.LPG>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.LPG> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("LPG", org.openapitools.client.model.LPG.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Loonie.class, new TypeSelector<org.openapitools.client.model.Loonie>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Loonie> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("loonie", org.openapitools.client.model.Loonie.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Manual.class, new TypeSelector<org.openapitools.client.model.Manual>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Manual> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("manual", org.openapitools.client.model.Manual.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "calculator"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Manual2.class, new TypeSelector<org.openapitools.client.model.Manual2>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Manual2> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("manual-2", org.openapitools.client.model.Manual2.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "calculator"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.MiFinity.class, new TypeSelector<org.openapitools.client.model.MiFinity>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.MiFinity> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("MiFinity", org.openapitools.client.model.MiFinity.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.MinimumOrderAmount.class, new TypeSelector<org.openapitools.client.model.MinimumOrderAmount>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.MinimumOrderAmount> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("minimum-order-amount", org.openapitools.client.model.MinimumOrderAmount.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "type"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.ModelList.class, new TypeSelector<org.openapitools.client.model.ModelList>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.ModelList> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("_list", org.openapitools.client.model.ModelList.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "type"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Moneris.class, new TypeSelector<org.openapitools.client.model.Moneris>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Moneris> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Moneris", org.openapitools.client.model.Moneris.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.MtaPay.class, new TypeSelector<org.openapitools.client.model.MtaPay>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.MtaPay> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("MtaPay", org.openapitools.client.model.MtaPay.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.MuchBetter.class, new TypeSelector<org.openapitools.client.model.MuchBetter>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.MuchBetter> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("MuchBetter", org.openapitools.client.model.MuchBetter.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.MyFatoorah.class, new TypeSelector<org.openapitools.client.model.MyFatoorah>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.MyFatoorah> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("MyFatoorah", org.openapitools.client.model.MyFatoorah.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.NGenius.class, new TypeSelector<org.openapitools.client.model.NGenius>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.NGenius> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("NGenius", org.openapitools.client.model.NGenius.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.NGenius3dsServer.class, new TypeSelector<org.openapitools.client.model.NGenius3dsServer>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.NGenius3dsServer> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("NGenius3dsServer", org.openapitools.client.model.NGenius3dsServer.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "name"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.NGenius3dsServers.class, new TypeSelector<org.openapitools.client.model.NGenius3dsServers>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.NGenius3dsServers> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("NGenius3dsServer", org.openapitools.client.model.NGenius3dsServer.class);
                        classByDiscriminatorValue.put("NGenius3dsServers", org.openapitools.client.model.NGenius3dsServers.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "name"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.NMI.class, new TypeSelector<org.openapitools.client.model.NMI>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.NMI> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("NMI", org.openapitools.client.model.NMI.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.NMI3dsServers.class, new TypeSelector<org.openapitools.client.model.NMI3dsServers>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.NMI3dsServers> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("NMI3dsServers", org.openapitools.client.model.NMI3dsServers.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "name"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Neosurf.class, new TypeSelector<org.openapitools.client.model.Neosurf>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Neosurf> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Neosurf", org.openapitools.client.model.Neosurf.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Netbanking.class, new TypeSelector<org.openapitools.client.model.Netbanking>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Netbanking> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Netbanking", org.openapitools.client.model.Netbanking.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Neteller.class, new TypeSelector<org.openapitools.client.model.Neteller>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Neteller> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Neteller", org.openapitools.client.model.Neteller.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.NinjaWallet.class, new TypeSelector<org.openapitools.client.model.NinjaWallet>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.NinjaWallet> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("NinjaWallet", org.openapitools.client.model.NinjaWallet.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.NuaPay.class, new TypeSelector<org.openapitools.client.model.NuaPay>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.NuaPay> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("NuaPay", org.openapitools.client.model.NuaPay.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.OchaPay.class, new TypeSelector<org.openapitools.client.model.OchaPay>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.OchaPay> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("OchaPay", org.openapitools.client.model.OchaPay.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.OnRamp.class, new TypeSelector<org.openapitools.client.model.OnRamp>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.OnRamp> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("OnRamp", org.openapitools.client.model.OnRamp.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.OneColumn.class, new TypeSelector<org.openapitools.client.model.OneColumn>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.OneColumn> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("one-column", org.openapitools.client.model.OneColumn.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "type"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Onlineueberweisen.class, new TypeSelector<org.openapitools.client.model.Onlineueberweisen>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Onlineueberweisen> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Onlineueberweisen", org.openapitools.client.model.Onlineueberweisen.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Other.class, new TypeSelector<org.openapitools.client.model.Other>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Other> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Other", org.openapitools.client.model.Other.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "name"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Paay3dsServer.class, new TypeSelector<org.openapitools.client.model.Paay3dsServer>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Paay3dsServer> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Paay3dsServer", org.openapitools.client.model.Paay3dsServer.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "name"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Pagsmile.class, new TypeSelector<org.openapitools.client.model.Pagsmile>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Pagsmile> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Pagsmile", org.openapitools.client.model.Pagsmile.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.PaidByTime.class, new TypeSelector<org.openapitools.client.model.PaidByTime>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.PaidByTime> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("paid-by-time", org.openapitools.client.model.PaidByTime.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "type"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Panamerican.class, new TypeSelector<org.openapitools.client.model.Panamerican>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Panamerican> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Panamerican", org.openapitools.client.model.Panamerican.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Panamerican3dsServer.class, new TypeSelector<org.openapitools.client.model.Panamerican3dsServer>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Panamerican3dsServer> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Panamerican3dsServer", org.openapitools.client.model.Panamerican3dsServer.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "name"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Panamerican3dsServers.class, new TypeSelector<org.openapitools.client.model.Panamerican3dsServers>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Panamerican3dsServers> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Panamerican3dsServer", org.openapitools.client.model.Panamerican3dsServer.class);
                        classByDiscriminatorValue.put("Panamerican3dsServers", org.openapitools.client.model.Panamerican3dsServers.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "name"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.PandaGateway.class, new TypeSelector<org.openapitools.client.model.PandaGateway>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.PandaGateway> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("PandaGateway", org.openapitools.client.model.PandaGateway.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.ParamountEft.class, new TypeSelector<org.openapitools.client.model.ParamountEft>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.ParamountEft> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("ParamountEft", org.openapitools.client.model.ParamountEft.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.ParamountInterac.class, new TypeSelector<org.openapitools.client.model.ParamountInterac>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.ParamountInterac> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("ParamountInterac", org.openapitools.client.model.ParamountInterac.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Partial.class, new TypeSelector<org.openapitools.client.model.Partial>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Partial> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("partial", org.openapitools.client.model.Partial.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "method"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Password.class, new TypeSelector<org.openapitools.client.model.Password>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Password> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("password", org.openapitools.client.model.Password.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "mode"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Passwordless.class, new TypeSelector<org.openapitools.client.model.Passwordless>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Passwordless> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("passwordless", org.openapitools.client.model.Passwordless.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "mode"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Pay4Fun.class, new TypeSelector<org.openapitools.client.model.Pay4Fun>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Pay4Fun> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Pay4Fun", org.openapitools.client.model.Pay4Fun.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.PayCash.class, new TypeSelector<org.openapitools.client.model.PayCash>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.PayCash> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("PayCash", org.openapitools.client.model.PayCash.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.PayClub.class, new TypeSelector<org.openapitools.client.model.PayClub>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.PayClub> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("PayClub", org.openapitools.client.model.PayClub.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.PayPal.class, new TypeSelector<org.openapitools.client.model.PayPal>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.PayPal> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("PayPal", org.openapitools.client.model.PayPal.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.PayTabs.class, new TypeSelector<org.openapitools.client.model.PayTabs>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.PayTabs> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("PayTabs", org.openapitools.client.model.PayTabs.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.PayULatam.class, new TypeSelector<org.openapitools.client.model.PayULatam>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.PayULatam> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("PayULatam", org.openapitools.client.model.PayULatam.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Payeezy.class, new TypeSelector<org.openapitools.client.model.Payeezy>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Payeezy> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Payeezy", org.openapitools.client.model.Payeezy.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Payflow.class, new TypeSelector<org.openapitools.client.model.Payflow>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Payflow> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Payflow", org.openapitools.client.model.Payflow.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.PaymenTechnologies.class, new TypeSelector<org.openapitools.client.model.PaymenTechnologies>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.PaymenTechnologies> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("PaymenTechnologies", org.openapitools.client.model.PaymenTechnologies.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.PaymentAsia.class, new TypeSelector<org.openapitools.client.model.PaymentAsia>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.PaymentAsia> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("PaymentAsia", org.openapitools.client.model.PaymentAsia.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.PaymentsOS.class, new TypeSelector<org.openapitools.client.model.PaymentsOS>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.PaymentsOS> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("PaymentsOS", org.openapitools.client.model.PaymentsOS.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Paymero.class, new TypeSelector<org.openapitools.client.model.Paymero>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Paymero> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Paymero", org.openapitools.client.model.Paymero.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Payr.class, new TypeSelector<org.openapitools.client.model.Payr>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Payr> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Payr", org.openapitools.client.model.Payr.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Paysafe.class, new TypeSelector<org.openapitools.client.model.Paysafe>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Paysafe> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Paysafe", org.openapitools.client.model.Paysafe.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Paysafe3dsServer.class, new TypeSelector<org.openapitools.client.model.Paysafe3dsServer>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Paysafe3dsServer> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Paysafe3dsServer", org.openapitools.client.model.Paysafe3dsServer.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "name"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Paysafe3dsServers.class, new TypeSelector<org.openapitools.client.model.Paysafe3dsServers>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Paysafe3dsServers> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Paysafe3dsServer", org.openapitools.client.model.Paysafe3dsServer.class);
                        classByDiscriminatorValue.put("Paysafe3dsServers", org.openapitools.client.model.Paysafe3dsServers.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "name"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Paysafecash.class, new TypeSelector<org.openapitools.client.model.Paysafecash>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Paysafecash> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Paysafecash", org.openapitools.client.model.Paysafecash.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Payvision.class, new TypeSelector<org.openapitools.client.model.Payvision>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Payvision> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Payvision", org.openapitools.client.model.Payvision.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Payvision3dsServer.class, new TypeSelector<org.openapitools.client.model.Payvision3dsServer>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Payvision3dsServer> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Payvision3dsServer", org.openapitools.client.model.Payvision3dsServer.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "name"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Payvision3dsServers.class, new TypeSelector<org.openapitools.client.model.Payvision3dsServers>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Payvision3dsServers> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("CardinalCommerce3dsServer", org.openapitools.client.model.CardinalCommerce3dsServer.class);
                        classByDiscriminatorValue.put("Other", org.openapitools.client.model.Other.class);
                        classByDiscriminatorValue.put("Paay3dsServer", org.openapitools.client.model.Paay3dsServer.class);
                        classByDiscriminatorValue.put("Payvision3dsServer", org.openapitools.client.model.Payvision3dsServer.class);
                        classByDiscriminatorValue.put("ThreeDSecureIO3dsServer", org.openapitools.client.model.ThreeDSecureIO3dsServer.class);
                        classByDiscriminatorValue.put("Payvision3dsServers", org.openapitools.client.model.Payvision3dsServers.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "name"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Percent.class, new TypeSelector<org.openapitools.client.model.Percent>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Percent> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("percent", org.openapitools.client.model.Percent.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "type"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Piastrix.class, new TypeSelector<org.openapitools.client.model.Piastrix>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Piastrix> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Piastrix", org.openapitools.client.model.Piastrix.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Piastrix3dsServer.class, new TypeSelector<org.openapitools.client.model.Piastrix3dsServer>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Piastrix3dsServer> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Piastrix3dsServer", org.openapitools.client.model.Piastrix3dsServer.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "name"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Piastrix3dsServers.class, new TypeSelector<org.openapitools.client.model.Piastrix3dsServers>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Piastrix3dsServers> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Piastrix3dsServer", org.openapitools.client.model.Piastrix3dsServer.class);
                        classByDiscriminatorValue.put("Piastrix3dsServers", org.openapitools.client.model.Piastrix3dsServers.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "name"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.PlanPriceFormula.class, new TypeSelector<org.openapitools.client.model.PlanPriceFormula>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.PlanPriceFormula> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("fixed-fee", org.openapitools.client.model.FixedFee.class);
                        classByDiscriminatorValue.put("flat-rate", org.openapitools.client.model.FlatRate.class);
                        classByDiscriminatorValue.put("stairstep", org.openapitools.client.model.Stairstep.class);
                        classByDiscriminatorValue.put("tiered", org.openapitools.client.model.Tiered.class);
                        classByDiscriminatorValue.put("volume", org.openapitools.client.model.Volume.class);
                        classByDiscriminatorValue.put("PlanPriceFormula", org.openapitools.client.model.PlanPriceFormula.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "formula"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Plugnpay.class, new TypeSelector<org.openapitools.client.model.Plugnpay>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Plugnpay> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Plugnpay", org.openapitools.client.model.Plugnpay.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.PostFinance.class, new TypeSelector<org.openapitools.client.model.PostFinance>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.PostFinance> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("PostFinance", org.openapitools.client.model.PostFinance.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Prosa.class, new TypeSelector<org.openapitools.client.model.Prosa>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Prosa> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Prosa", org.openapitools.client.model.Prosa.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.RPN.class, new TypeSelector<org.openapitools.client.model.RPN>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.RPN> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("RPN", org.openapitools.client.model.RPN.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Rapyd.class, new TypeSelector<org.openapitools.client.model.Rapyd>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Rapyd> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Rapyd", org.openapitools.client.model.Rapyd.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Realex.class, new TypeSelector<org.openapitools.client.model.Realex>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Realex> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Realex", org.openapitools.client.model.Realex.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Realtime.class, new TypeSelector<org.openapitools.client.model.Realtime>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Realtime> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Realtime", org.openapitools.client.model.Realtime.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Rebilly.class, new TypeSelector<org.openapitools.client.model.Rebilly>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Rebilly> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("rebilly", org.openapitools.client.model.Rebilly.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "calculator"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.RebillyTaxjar.class, new TypeSelector<org.openapitools.client.model.RebillyTaxjar>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.RebillyTaxjar> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("rebilly-taxjar", org.openapitools.client.model.RebillyTaxjar.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "calculator"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.RedemptionCancel.class, new TypeSelector<org.openapitools.client.model.RedemptionCancel>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.RedemptionCancel> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("redemption-cancel", org.openapitools.client.model.RedemptionCancel.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "action"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.RedemptionRestriction.class, new TypeSelector<org.openapitools.client.model.RedemptionRestriction>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.RedemptionRestriction> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("RedemptionRestriction", org.openapitools.client.model.RedemptionRestriction.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "type"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.RedemptionsPerCustomer.class, new TypeSelector<org.openapitools.client.model.RedemptionsPerCustomer>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.RedemptionsPerCustomer> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("redemptions-per-customer", org.openapitools.client.model.RedemptionsPerCustomer.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "type"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Redsys.class, new TypeSelector<org.openapitools.client.model.Redsys>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Redsys> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Redsys", org.openapitools.client.model.Redsys.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.ResendEmail.class, new TypeSelector<org.openapitools.client.model.ResendEmail>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.ResendEmail> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("resend-email", org.openapitools.client.model.ResendEmail.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "action"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.RestrictToInvoices.class, new TypeSelector<org.openapitools.client.model.RestrictToInvoices>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.RestrictToInvoices> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("restrict-to-invoices", org.openapitools.client.model.RestrictToInvoices.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "type"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.RestrictToPlans.class, new TypeSelector<org.openapitools.client.model.RestrictToPlans>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.RestrictToPlans> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("restrict-to-plans", org.openapitools.client.model.RestrictToPlans.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "type"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.RestrictToProducts.class, new TypeSelector<org.openapitools.client.model.RestrictToProducts>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.RestrictToProducts> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("restrict-to-products", org.openapitools.client.model.RestrictToProducts.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "type"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.RestrictToSubscriptions.class, new TypeSelector<org.openapitools.client.model.RestrictToSubscriptions>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.RestrictToSubscriptions> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("restrict-to-subscriptions", org.openapitools.client.model.RestrictToSubscriptions.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "type"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Rotessa.class, new TypeSelector<org.openapitools.client.model.Rotessa>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Rotessa> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Rotessa", org.openapitools.client.model.Rotessa.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.RulesetRestore.class, new TypeSelector<org.openapitools.client.model.RulesetRestore>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.RulesetRestore> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("ruleset-restore", org.openapitools.client.model.RulesetRestore.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "action"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.SMSVoucher.class, new TypeSelector<org.openapitools.client.model.SMSVoucher>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.SMSVoucher> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("SMSVoucher", org.openapitools.client.model.SMSVoucher.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Sagepay.class, new TypeSelector<org.openapitools.client.model.Sagepay>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Sagepay> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Sagepay", org.openapitools.client.model.Sagepay.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.SaltarPay.class, new TypeSelector<org.openapitools.client.model.SaltarPay>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.SaltarPay> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("SaltarPay", org.openapitools.client.model.SaltarPay.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.SeamlessChex.class, new TypeSelector<org.openapitools.client.model.SeamlessChex>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.SeamlessChex> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("SeamlessChex", org.openapitools.client.model.SeamlessChex.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.SecureTrading.class, new TypeSelector<org.openapitools.client.model.SecureTrading>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.SecureTrading> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("SecureTrading", org.openapitools.client.model.SecureTrading.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.SecureTrading3dsServer.class, new TypeSelector<org.openapitools.client.model.SecureTrading3dsServer>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.SecureTrading3dsServer> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("SecureTrading3dsServer", org.openapitools.client.model.SecureTrading3dsServer.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "name"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.SecureTrading3dsServers.class, new TypeSelector<org.openapitools.client.model.SecureTrading3dsServers>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.SecureTrading3dsServers> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("SecureTrading3dsServer", org.openapitools.client.model.SecureTrading3dsServer.class);
                        classByDiscriminatorValue.put("SecureTrading3dsServers", org.openapitools.client.model.SecureTrading3dsServers.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "name"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.SecurionPay.class, new TypeSelector<org.openapitools.client.model.SecurionPay>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.SecurionPay> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("SecurionPay", org.openapitools.client.model.SecurionPay.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.SecurionPay3dsServers.class, new TypeSelector<org.openapitools.client.model.SecurionPay3dsServers>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.SecurionPay3dsServers> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("SecurionPay3dsServers", org.openapitools.client.model.SecurionPay3dsServers.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "name"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.ServicePeriodAnchorInstruction.class, new TypeSelector<org.openapitools.client.model.ServicePeriodAnchorInstruction>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.ServicePeriodAnchorInstruction> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("ServicePeriodAnchorInstruction", org.openapitools.client.model.ServicePeriodAnchorInstruction.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "method"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Skrill.class, new TypeSelector<org.openapitools.client.model.Skrill>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Skrill> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Skrill", org.openapitools.client.model.Skrill.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.SmartInvoice.class, new TypeSelector<org.openapitools.client.model.SmartInvoice>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.SmartInvoice> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("SmartInvoice", org.openapitools.client.model.SmartInvoice.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.SmartInvoice3dsServer.class, new TypeSelector<org.openapitools.client.model.SmartInvoice3dsServer>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.SmartInvoice3dsServer> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("SmartInvoice3dsServer", org.openapitools.client.model.SmartInvoice3dsServer.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "name"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.SmartInvoice3dsServers.class, new TypeSelector<org.openapitools.client.model.SmartInvoice3dsServers>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.SmartInvoice3dsServers> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("SmartInvoice3dsServer", org.openapitools.client.model.SmartInvoice3dsServer.class);
                        classByDiscriminatorValue.put("SmartInvoice3dsServers", org.openapitools.client.model.SmartInvoice3dsServers.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "name"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Sofort.class, new TypeSelector<org.openapitools.client.model.Sofort>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Sofort> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Sofort", org.openapitools.client.model.Sofort.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.SparkPay.class, new TypeSelector<org.openapitools.client.model.SparkPay>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.SparkPay> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("SparkPay", org.openapitools.client.model.SparkPay.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Stairstep.class, new TypeSelector<org.openapitools.client.model.Stairstep>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Stairstep> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("stairstep", org.openapitools.client.model.Stairstep.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "formula"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.StaticGateway.class, new TypeSelector<org.openapitools.client.model.StaticGateway>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.StaticGateway> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("StaticGateway", org.openapitools.client.model.StaticGateway.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Stripe.class, new TypeSelector<org.openapitools.client.model.Stripe>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Stripe> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Stripe", org.openapitools.client.model.Stripe.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Stripe3dsServer.class, new TypeSelector<org.openapitools.client.model.Stripe3dsServer>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Stripe3dsServer> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Stripe3dsServer", org.openapitools.client.model.Stripe3dsServer.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "name"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Stripe3dsServers.class, new TypeSelector<org.openapitools.client.model.Stripe3dsServers>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Stripe3dsServers> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Stripe3dsServer", org.openapitools.client.model.Stripe3dsServer.class);
                        classByDiscriminatorValue.put("Stripe3dsServers", org.openapitools.client.model.Stripe3dsServers.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "name"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Subscription.class, new TypeSelector<org.openapitools.client.model.Subscription>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Subscription> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Subscription", org.openapitools.client.model.Subscription.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "orderType"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.TWINT.class, new TypeSelector<org.openapitools.client.model.TWINT>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.TWINT> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("TWINT", org.openapitools.client.model.TWINT.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.TestProcessor.class, new TypeSelector<org.openapitools.client.model.TestProcessor>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.TestProcessor> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("TestProcessor", org.openapitools.client.model.TestProcessor.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.TestProcessor3dsServer.class, new TypeSelector<org.openapitools.client.model.TestProcessor3dsServer>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.TestProcessor3dsServer> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("TestProcessor3dsServer", org.openapitools.client.model.TestProcessor3dsServer.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "name"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.TestProcessor3dsServers.class, new TypeSelector<org.openapitools.client.model.TestProcessor3dsServers>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.TestProcessor3dsServers> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("TestSandbox3dsServer", org.openapitools.client.model.TestProcessor3dsServer.class);
                        classByDiscriminatorValue.put("ThreeDSecureIO3dsServer", org.openapitools.client.model.ThreeDSecureIO3dsServer.class);
                        classByDiscriminatorValue.put("TestProcessor3dsServers", org.openapitools.client.model.TestProcessor3dsServers.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "name"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.ThreeColumns.class, new TypeSelector<org.openapitools.client.model.ThreeColumns>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.ThreeColumns> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("three-columns", org.openapitools.client.model.ThreeColumns.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "type"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.ThreeDSecureIO3dsServer.class, new TypeSelector<org.openapitools.client.model.ThreeDSecureIO3dsServer>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.ThreeDSecureIO3dsServer> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("ThreeDSecureIO3dsServer", org.openapitools.client.model.ThreeDSecureIO3dsServer.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "name"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Tiered.class, new TypeSelector<org.openapitools.client.model.Tiered>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Tiered> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("tiered", org.openapitools.client.model.Tiered.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "formula"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.TimelineAction.class, new TypeSelector<org.openapitools.client.model.TimelineAction>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.TimelineAction> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("redemption-cancel", org.openapitools.client.model.RedemptionCancel.class);
                        classByDiscriminatorValue.put("resend-email", org.openapitools.client.model.ResendEmail.class);
                        classByDiscriminatorValue.put("ruleset-restore", org.openapitools.client.model.RulesetRestore.class);
                        classByDiscriminatorValue.put("TimelineAction", org.openapitools.client.model.TimelineAction.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "action"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.TimelineTable.class, new TypeSelector<org.openapitools.client.model.TimelineTable>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.TimelineTable> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("list", org.openapitools.client.model.ModelList.class);
                        classByDiscriminatorValue.put("one-column", org.openapitools.client.model.OneColumn.class);
                        classByDiscriminatorValue.put("three-columns", org.openapitools.client.model.ThreeColumns.class);
                        classByDiscriminatorValue.put("two-columns", org.openapitools.client.model.TwoColumns.class);
                        classByDiscriminatorValue.put("TimelineTable", org.openapitools.client.model.TimelineTable.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "type"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.ToditoCash.class, new TypeSelector<org.openapitools.client.model.ToditoCash>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.ToditoCash> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("ToditoCash", org.openapitools.client.model.ToditoCash.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.TotalRedemptions.class, new TypeSelector<org.openapitools.client.model.TotalRedemptions>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.TotalRedemptions> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("total-redemptions", org.openapitools.client.model.TotalRedemptions.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "type"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.TrustPay.class, new TypeSelector<org.openapitools.client.model.TrustPay>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.TrustPay> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("TrustPay", org.openapitools.client.model.TrustPay.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Trustly.class, new TypeSelector<org.openapitools.client.model.Trustly>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Trustly> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Trustly", org.openapitools.client.model.Trustly.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.TrustsPay.class, new TypeSelector<org.openapitools.client.model.TrustsPay>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.TrustsPay> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("TrustsPay", org.openapitools.client.model.TrustsPay.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.TwoColumns.class, new TypeSelector<org.openapitools.client.model.TwoColumns>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.TwoColumns> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("two-columns", org.openapitools.client.model.TwoColumns.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "type"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.UPayCard.class, new TypeSelector<org.openapitools.client.model.UPayCard>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.UPayCard> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("UPayCard", org.openapitools.client.model.UPayCard.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.USAePay.class, new TypeSelector<org.openapitools.client.model.USAePay>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.USAePay> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("USAePay", org.openapitools.client.model.USAePay.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.VCreditos.class, new TypeSelector<org.openapitools.client.model.VCreditos>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.VCreditos> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("VCreditos", org.openapitools.client.model.VCreditos.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.VantivLitle.class, new TypeSelector<org.openapitools.client.model.VantivLitle>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.VantivLitle> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("VantivLitle", org.openapitools.client.model.VantivLitle.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.VantivLitle3dsServers.class, new TypeSelector<org.openapitools.client.model.VantivLitle3dsServers>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.VantivLitle3dsServers> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("VantivLitle3dsServers", org.openapitools.client.model.VantivLitle3dsServers.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "name"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.VegaaH.class, new TypeSelector<org.openapitools.client.model.VegaaH>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.VegaaH> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("vegaaH", org.openapitools.client.model.VegaaH.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Volume.class, new TypeSelector<org.openapitools.client.model.Volume>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Volume> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("volume", org.openapitools.client.model.Volume.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "formula"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Wallet88.class, new TypeSelector<org.openapitools.client.model.Wallet88>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Wallet88> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Wallet88", org.openapitools.client.model.Wallet88.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Walpay.class, new TypeSelector<org.openapitools.client.model.Walpay>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Walpay> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Walpay", org.openapitools.client.model.Walpay.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Walpay3dsServers.class, new TypeSelector<org.openapitools.client.model.Walpay3dsServers>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Walpay3dsServers> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Walpay3dsServers", org.openapitools.client.model.Walpay3dsServers.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "name"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Wirecard.class, new TypeSelector<org.openapitools.client.model.Wirecard>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Wirecard> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Wirecard", org.openapitools.client.model.Wirecard.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Wirecard3dsServer.class, new TypeSelector<org.openapitools.client.model.Wirecard3dsServer>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Wirecard3dsServer> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Wirecard3dsServer", org.openapitools.client.model.Wirecard3dsServer.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "name"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Wirecard3dsServers.class, new TypeSelector<org.openapitools.client.model.Wirecard3dsServers>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Wirecard3dsServers> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Wirecard3dsServer", org.openapitools.client.model.Wirecard3dsServer.class);
                        classByDiscriminatorValue.put("Wirecard3dsServers", org.openapitools.client.model.Wirecard3dsServers.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "name"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.WorldlineAtosFrankfurt.class, new TypeSelector<org.openapitools.client.model.WorldlineAtosFrankfurt>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.WorldlineAtosFrankfurt> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("WorldlineAtosFrankfurt", org.openapitools.client.model.WorldlineAtosFrankfurt.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.WorldlineAtosFrankfurt3dsServers.class, new TypeSelector<org.openapitools.client.model.WorldlineAtosFrankfurt3dsServers>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.WorldlineAtosFrankfurt3dsServers> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("ThreeDSecureIO3dsServer", org.openapitools.client.model.ThreeDSecureIO3dsServer.class);
                        classByDiscriminatorValue.put("WorldlineAtosFrankfurt3dsServers", org.openapitools.client.model.WorldlineAtosFrankfurt3dsServers.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "name"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Worldpay.class, new TypeSelector<org.openapitools.client.model.Worldpay>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Worldpay> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Worldpay", org.openapitools.client.model.Worldpay.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Worldpay3dsServers.class, new TypeSelector<org.openapitools.client.model.Worldpay3dsServers>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Worldpay3dsServers> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Worldpay3dsServers", org.openapitools.client.model.Worldpay3dsServers.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "name"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.XPay.class, new TypeSelector<org.openapitools.client.model.XPay>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.XPay> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("XPay", org.openapitools.client.model.XPay.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Zimpler.class, new TypeSelector<org.openapitools.client.model.Zimpler>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Zimpler> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Zimpler", org.openapitools.client.model.Zimpler.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.Zotapay.class, new TypeSelector<org.openapitools.client.model.Zotapay>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.Zotapay> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Zotapay", org.openapitools.client.model.Zotapay.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "gatewayName"));
                    }
          })
        ;
        GsonBuilder builder = fireBuilder.createGsonBuilder();
        return builder;
    }

    private static String getDiscriminatorValue(JsonElement readElement, String discriminatorField) {
        JsonElement element = readElement.getAsJsonObject().get(discriminatorField);
        if (null == element) {
            throw new IllegalArgumentException("missing discriminator field: <" + discriminatorField + ">");
        }
        return element.getAsString();
    }

    /**
     * Returns the Java class that implements the OpenAPI schema for the specified discriminator value.
     *
     * @param classByDiscriminatorValue The map of discriminator values to Java classes.
     * @param discriminatorValue The value of the OpenAPI discriminator in the input data.
     * @return The Java class that implements the OpenAPI schema
     */
    private static Class getClassByDiscriminator(Map classByDiscriminatorValue, String discriminatorValue) {
        Class clazz = (Class) classByDiscriminatorValue.get(discriminatorValue);
        if (null == clazz) {
            throw new IllegalArgumentException("cannot determine model class of name: <" + discriminatorValue + ">");
        }
        return clazz;
    }

    static {
        GsonBuilder gsonBuilder = createGson();
        gsonBuilder.registerTypeAdapter(Date.class, dateTypeAdapter);
        gsonBuilder.registerTypeAdapter(java.sql.Date.class, sqlDateTypeAdapter);
        gsonBuilder.registerTypeAdapter(OffsetDateTime.class, offsetDateTimeTypeAdapter);
        gsonBuilder.registerTypeAdapter(LocalDate.class, localDateTypeAdapter);
        gsonBuilder.registerTypeAdapter(byte[].class, byteArrayAdapter);
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.A1Gateway.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.A1GatewayAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.AML.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.AMLAddressInner.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.AMLAliasesInner.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.AMLPassportInner.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.AchPlaidFeature.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.AclInner.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.AddressMatches.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Adyen.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.AdyenAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.AdyenAllOfSettings.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Airpay.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.AirpayAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.AlternativePaymentInstrument.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.AlternativePaymentInstrument2.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.AlternativePaymentInstrument2EmbeddedInner.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.AlternativePaymentInstrument2LinksInner.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.AlternativePaymentToken.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.AmexVPC.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.AmexVPCAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.AmexVPCAllOfSettings.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ApcoPay.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ApcoPayAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ApcoPayAllOfSettings.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ApiKeyScope.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ApplePayValidation.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ApplePayValidationAllOfValidationRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ApprovalUrlLink.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.AsiaPaymentGateway.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.AsiaPaymentGatewayAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.AstroPayCard.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.AstroPayCardAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.AstroPayCardAllOfSettings.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Attachment.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.AttachmentEmbeddedInner.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.AttachmentLinksInner.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.AttachmentResourceLink.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.AuthTransactionEmbed.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.AuthTransactionLink.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.AuthenticationOptions.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.AuthenticationTokenMetadata.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.AuthorizeNet.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.AuthorizeNetAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Auto.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.BBANInstrument.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.BBANType.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Bambora.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.BamboraAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.BankAccount.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.BankAccountAllOfEmbedded.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.BankAccountAllOfLinks.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.BankAccountCreatePlain.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.BankAccountCreateToken.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.BankAccountEmbed.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.BankAccountToken.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.BankAccountUpdatePlain.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.BitPay.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.BitPayAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.BlankProblem.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Blocklist.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.BlueSnap.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.BlueSnapAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.BraintreePayments.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.BraintreePaymentsAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.BrowserData.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CASHlib.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CASHlibAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CCAvenue.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CCAvenueAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CODVoucher.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CODVoucherAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CardinalCommerce3dsServer.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Cardknox.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CardknoxAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CashInstrument.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CashToCode.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CashToCodeAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CashToCodeAllOfSettings.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Cashflows.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CashflowsAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CauriPayment.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CauriPaymentAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Cayan.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CayanAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Chase.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ChaseAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CheckInstrument.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Circle.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CircleAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Citadel.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CitadelAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Clearhaus.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Clearhaus3dsServer.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ClearhausAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CoinPayments.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CoinPaymentsAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CommonBankAccount.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CommonInvoice.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CommonKycDocument.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CommonKycDocumentLinksInner.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CommonKycRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CommonKycRequestDocumentsInner.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CommonOneTimeOrder.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CommonPayPalAccount.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CommonPaymentCard.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CommonPaymentToken.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CommonPlan.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CommonPlanRecurringInterval.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CommonPlanSetup.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CommonPlanTrial.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CommonProduct.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CommonSubscription.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CommonSubscriptionItemsInner.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CommonSubscriptionOrder.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CommonSubscriptionOrderAllOfLineItemSubtotal.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CommonSubscriptionOrderAllOfRecurringInterval.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CommonSubscriptionOrderAllOfTrial.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CommonTransaction.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CommonTransactionRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CompositeToken.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Conekta.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ConektaAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ContactEmailsInner.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ContactObject.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ContactPhoneNumbersInner.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Coppr.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CopprAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CopprAllOfSettings.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CoreReadyToPay.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Coupon.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CouponExpiration.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CouponRedemption.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Credential.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Credorax.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CredoraxAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Cryptonator.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CryptonatorAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CustomEventScheduleInstruction.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CustomField.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Customer.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CustomerAverageValue.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CustomerEmbed.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CustomerEmbeddedInner.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CustomerJWT.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CustomerLifetimeRevenue.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CustomerLink.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CustomerLinksInner.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CustomerTimeline.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CustomerTimelineCustomEvent.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CyberSource.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CyberSourceAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.DLocal.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.DLocalAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.DLocalAllOfSettings.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.DataCash.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.DataCash3dsServer.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.DataCashAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.DataCashAllOfSettings.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.DateInterval.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.DateIntervalAllOfUnit.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.DayOfMonth.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.DayOfWeek.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.DefaultPaymentInstrumentLink.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Dengi.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.DengiAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.DetailedProblem.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.DigitalWalletToken.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.DigitalWallets.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.DigitalWalletsApplePay.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.DigitalWalletsGooglePay.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Directa24.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Directa24AllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Directa24AllOfSettings.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.DiscountsPerRedemption.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Dispute.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.DisputeEmbeddedInner.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.DisputeLink.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.DisputeLinksInner.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.DocumentedProblem.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Dragonphoenix.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.DragonphoenixAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.DueTimeShiftInstruction.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.DueTimeShiftInstructionUnit.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.DynamicIpnLink.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.EBANX.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.EBANXAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.EMS.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.EMS3dsServers.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.EMSAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.EMSAllOfSettings.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.EMerchantPay.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.EMerchantPay3dsServer.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.EMerchantPayAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.EMerchantPayAllOfSettings.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.EPG.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.EPGAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.EPro.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.EProAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.EZeeWallet.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.EZeeWalletAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.EcoPayz.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.EcoPayzAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.EcoPayzAllOfSettings.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.EcorePay.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.EcorePayAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Elavon.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ElavonAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Error.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Euteller.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.EutellerAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.EzyEFT.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.EzyEFTAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.FileCreateFromInline.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.FileCreateFromUrl.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.FileDownloadLink.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.FileEmbed.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.FileLink.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.FileLinksInner.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.FinTecSystems.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.FinTecSystemsAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.FinTecSystemsAllOfSettings.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Finrax.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.FinraxAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.FinraxAllOfSettings.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Fixed.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.FixedFee.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.FlatRate.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Flexepin.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.FlexepinAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.FlexiblePlan.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Forte.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ForteAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.FundSend.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.FundSendAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GET.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GET3dsServers.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GETAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GatewayAccountEmbed.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GatewayAccountLimit.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GatewayAccountLimitLink.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GatewayAccountLink.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GatewayAccountLinksInner.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Gigadat.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GigadatAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GigadatAllOfSettings.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GlobalOne.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GlobalOneAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Gooney.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GooneyAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Gpaysafe.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GpaysafeAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Greenbox.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GreenboxAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.HiPay.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.HiPayAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.IBANInstrument.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.IBANType.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ICEPAY.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ICEPAYAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ICanPay.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ICanPayAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ICheque.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.IChequeAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.IDebit.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.IDebitAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.INOVAPAY.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.INOVAPAYAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.IdentityMatches.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Ilixium.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Ilixium3dsServer.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.IlixiumAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.IlixiumAllOfSettings.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Immediately.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Ingenico.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Ingenico3dsServer.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.IngenicoAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.InitialInvoiceEmbed.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.InitialInvoiceLink.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Inovio.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Inovio3dsServer.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.InovioAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.InovioAllOfSettings.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.InstaDebit.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.InstaDebitAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.InstrumentReference.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Intelligent.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.IntelligentAllOfUnit.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Intuit.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.IntuitAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.InvalidError.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Invoice.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.InvoiceAllOfEmbedded.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.InvoiceAllOfLinks.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.InvoiceAllOfRetryInstruction.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.InvoiceAllOfRetryInstructionAttempts.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.InvoiceDiscount.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.InvoiceIssue.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.InvoiceItem.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.InvoiceItemEmbeddedInner.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.InvoiceItemLinksInner.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.InvoiceLink.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.InvoiceReissue.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.InvoiceRetryScheduleInstruction.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.InvoiceTaxItem.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.InvoiceTimeShift.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.InvoiceTimeline.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.InvoiceTransaction.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.InvoiceTransactionAllocation.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.InvoiceTransactionAllocationLinksInner.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.InvoicesEmbed.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.InvoicesLink.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.IpayOptions.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.IpayOptionsAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.IpayOptionsAllOfSettings.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.IssueTimeShiftInstruction.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.JetPay.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.JetPayAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Jeton.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.JetonAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.JetonAllOfSettings.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Khelocard.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.KhelocardAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.KhelocardCard.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.KhelocardCardToken.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Konnektive.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.KonnektiveAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.KonnektiveAllOfSettings.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.KycDocument.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.KycDocument2.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.KycDocumentLink.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.KycDocumentRejection.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.KycDocumentsLink.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.KycGathererLink.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.KycRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.KycRequestAllOfLinks.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.LPG.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.LPGAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.LeadSource.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.LeadSourceData.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.LeadSourceEmbed.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.LeadSourceLink.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Link.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Loonie.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.LoonieAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Manual.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Manual2.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Manual2AllOfItems.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.MiFinity.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.MiFinityAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.MinimumOrderAmount.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ModelFile.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ModelList.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Moneris.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.MonerisAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Money.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.MtaPay.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.MtaPayAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.MtaPayAllOfSettings.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.MuchBetter.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.MuchBetterAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.MuchBetterAllOfSettings.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.MyFatoorah.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.MyFatoorahAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.NGenius.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.NGenius3dsServer.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.NGeniusAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.NMI.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.NMI3dsServers.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.NMIAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.NMIAllOfSettings.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Neosurf.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.NeosurfAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Netbanking.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.NetbankingAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Neteller.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.NetellerAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.NetellerAllOfSettings.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.NinjaWallet.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.NinjaWalletAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.NuaPay.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.NuaPayAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.OchaPay.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.OchaPayAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.OnBoardingUrlLink.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.OnRamp.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.OnRampAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.OneColumn.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.OneColumnAllOfData.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.OneTimeOrder.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Onlineueberweisen.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.OnlineueberweisenAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.OnlineueberweisenAllOfSettings.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.OrderTimeline.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Organization.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.OrganizationEmbed.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.OrganizationLink.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.OrganizationQuestionnaire.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Other.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Paay3dsServer.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Pagsmile.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PagsmileAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PaidByTime.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Panamerican.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Panamerican3dsServer.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PanamericanAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PanamericanAllOfSettings.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PandaGateway.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PandaGatewayAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ParamountEft.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ParamountEftAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ParamountInterac.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ParamountInteracAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ParentTransactionEmbed.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ParentTransactionLink.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Partial.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Password.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Passwordless.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PatchKycRequestRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PatchPaymentInstrumentRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PatchTransactionRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Pay4Fun.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Pay4FunAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PayCash.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PayCashAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PayClub.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PayClubAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PayClubAllOfSettings.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PayPal.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PayPalAccount.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PayPalAccountAllOfEmbedded.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PayPalAccountAllOfLinks.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PayPalAllOfSettings.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PayTabs.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PayTabsAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PayULatam.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PayULatamAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Payeezy.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PayeezyAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Payflow.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PayflowAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PaymenTechnologies.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PaymenTechnologiesAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PaymenTechnologiesAllOfSettings.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PaymentAsia.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PaymentAsiaAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PaymentCard.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PaymentCardAllOfEmbedded.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PaymentCardAllOfLinks.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PaymentCardCreatePlain.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PaymentCardCreateToken.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PaymentCardDigitalWalletFeature.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PaymentCardEmbed.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PaymentCardLink.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PaymentCardToken.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PaymentCardUpdatePlain.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PaymentInstruction.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PaymentInstrument.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PaymentInstrument2.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PaymentInstrument3.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PaymentInstrumentCreateToken.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PaymentInstrumentUpdateToken.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PaymentMethods.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PaymentRetry.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PaymentRetryAttemptsInner.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PaymentToken.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PaymentsOS.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PaymentsOSAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Paymero.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PaymeroAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PaymeroAllOfSettings.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PayoutRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Payr.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PayrAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Paysafe.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Paysafe3dsServer.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PaysafeAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Paysafecash.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PaysafecashAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Payvision.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Payvision3dsServer.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PayvisionAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PayvisionAllOfSettings.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Percent.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PermalinkLink.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Piastrix.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Piastrix3dsServer.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PiastrixAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PiastrixAllOfSettings.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PlaidAccountToken.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Plan.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PlanEmbed.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PlanPeriod.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Plugnpay.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PlugnpayAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PostBankAccountRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PostFileRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PostFinance.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PostFinanceAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PostKycDocumentMatchesRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PostPaymentCardRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PostPaymentInstrumentRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PostTagCustomerCollectionRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PriceBasedShippingRate.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Problem.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Product.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ProductEmbed.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ProductLink.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ProofOfAddress.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ProofOfAddressAllOfDocumentMatches.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ProofOfAddressAllOfLinks.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ProofOfFunds.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ProofOfIdentity.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ProofOfIdentityAllOfDocumentMatches.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ProofOfIdentityAllOfLinks.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ProofOfPurchase.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Prosa.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ProsaAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PurchaseBumpOffer.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.QueryUrlLink.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.RPN.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.RPNAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Rapyd.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.RapydAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ReadyToPay.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ReadyToPayAchMethod.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ReadyToPayAchMethodFeature.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ReadyToPayAmount.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ReadyToPayGenericMethod.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ReadyToPayItems.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ReadyToPayItemsItemsInner.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ReadyToPayMethodsInner.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ReadyToPayPaymentCardMethod.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ReadyToPayPaymentCardMethodFeature.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Realex.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.RealexAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Realtime.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.RealtimeAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Rebilly.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.RebillyTaxjar.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.RebillyTaxjarAllOfItems.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.RecalculateInvoiceLink.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.RecentInvoiceEmbed.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.RecentInvoiceLink.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.RedemptionCancel.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.RedemptionRestriction.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.RedemptionsPerCustomer.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Redsys.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.RedsysAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.RefundUrlLink.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ResendEmail.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ResetPasswordToken.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.RestrictToInvoices.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.RestrictToPlans.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.RestrictToProducts.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.RestrictToSubscriptions.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.RetriedTransactionEmbed.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.RetriedTransactionLink.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.RiskMetadata.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Rotessa.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.RotessaAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.RotessaAllOfSettings.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.RulesetRestore.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.SMSVoucher.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.SMSVoucherAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Sagepay.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.SagepayAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.SaltarPay.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.SaltarPayAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.SeamlessChex.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.SeamlessChexAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Search.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.SecureTrading.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.SecureTrading3dsServer.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.SecureTradingAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.SecurionPay.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.SecurionPay3dsServers.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.SecurionPayAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.SelfLink.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ServicePeriodAnchorInstruction.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ShippingZone.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.SignedLinkLink.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Skrill.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.SkrillAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.SmartInvoice.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.SmartInvoice3dsServer.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.SmartInvoiceAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Sofort.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.SofortAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.SparkPay.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.SparkPayAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Stairstep.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.StairstepAllOfBrackets.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.StaticGateway.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.StaticIpnLink.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Stripe.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Stripe3dsServer.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.StripeAllOfSettings.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Subscription.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.SubscriptionCancellation.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.SubscriptionCancellationState.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.SubscriptionChange.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.SubscriptionChangeItemsInner.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.SubscriptionInvoice.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.SubscriptionLink.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.SubscriptionMetadata.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.SubscriptionMetadataEmbeddedInner.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.SubscriptionMetadataLinksInner.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.SubscriptionOrder.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.SubscriptionReactivation.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.TWINT.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.TWINTAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.TWINTAllOfSettings.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Tag.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.TestProcessor.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.TestProcessor3dsServer.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ThreeColumns.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ThreeColumnsAllOfData.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ThreeDSecure.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ThreeDSecureIO3dsServer.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ThreeDSecureResult.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Tiered.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.TimelineExtraData.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.TimelineExtraDataAuthor.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.TimelineExtraDataLinksInner.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ToditoCash.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ToditoCashAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.TotalRedemptions.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Transaction.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.TransactionAllOfBumpOffer.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.TransactionAllOfDcc.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.TransactionAllOfEmbedded.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.TransactionAllOfGateway.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.TransactionAllOfGatewayAvsResponse.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.TransactionAllOfGatewayCvvResponse.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.TransactionAllOfGatewayResponse.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.TransactionAllOfLinks.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.TransactionAllocationsLink.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.TransactionEmbed.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.TransactionLink.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.TransactionQuery.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.TransactionRefund.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.TransactionRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.TransactionTimeline.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.TransactionUpdate.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.TransactionUpdateUrlLink.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.TrustPay.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.TrustPayAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Trustly.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.TrustlyAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.TrustsPay.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.TrustsPayAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.TwoColumns.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.UPayCard.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.UPayCardAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.UPayCardAllOfSettings.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.USAePay.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.USAePayAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.UpcomingInvoiceItem.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.VCreditos.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.VCreditosAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ValidationErrorExtensions.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ValidationErrorExtensionsInvalidFieldsInner.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.VantivLitle.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.VantivLitle3dsServers.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.VantivLitleAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.VaultedInstrument.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.VegaaH.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.VegaaHAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Volume.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Wallet88.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Wallet88AllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Walpay.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Walpay3dsServers.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.WalpayAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.WebsiteEmbed.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.WebsiteLink.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Wirecard.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Wirecard3dsServer.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.WirecardAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.WorldlineAtosFrankfurt.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.WorldlineAtosFrankfurtAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.WorldlineAtosFrankfurtAllOfSettings.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Worldpay.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Worldpay3dsServers.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.WorldpayAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.WorldpayAllOfSettings.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.XPay.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.XPayAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Zimpler.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ZimplerAllOfCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Zotapay.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ZotapayAllOfCredentials.CustomTypeAdapterFactory());
        gson = gsonBuilder.create();
    }

    /**
     * Get Gson.
     *
     * @return Gson
     */
    public static Gson getGson() {
        return gson;
    }

    /**
     * Set Gson.
     *
     * @param gson Gson
     */
    public static void setGson(Gson gson) {
        JSON.gson = gson;
    }

    public static void setLenientOnJson(boolean lenientOnJson) {
        isLenientOnJson = lenientOnJson;
    }

    /**
     * Serialize the given Java object into JSON string.
     *
     * @param obj Object
     * @return String representation of the JSON
     */
    public static String serialize(Object obj) {
        return gson.toJson(obj);
    }

    /**
     * Deserialize the given JSON string to Java object.
     *
     * @param <T>        Type
     * @param body       The JSON string
     * @param returnType The type to deserialize into
     * @return The deserialized Java object
     */
    @SuppressWarnings("unchecked")
    public static <T> T deserialize(String body, Type returnType) {
        try {
            if (isLenientOnJson) {
                JsonReader jsonReader = new JsonReader(new StringReader(body));
                // see https://google-gson.googlecode.com/svn/trunk/gson/docs/javadocs/com/google/gson/stream/JsonReader.html#setLenient(boolean)
                jsonReader.setLenient(true);
                return gson.fromJson(jsonReader, returnType);
            } else {
                return gson.fromJson(body, returnType);
            }
        } catch (JsonParseException e) {
            // Fallback processing when failed to parse JSON form response body:
            // return the response body string directly for the String return type;
            if (returnType.equals(String.class)) {
                return (T) body;
            } else {
                throw (e);
            }
        }
    }

    /**
     * Gson TypeAdapter for Byte Array type
     */
    public static class ByteArrayAdapter extends TypeAdapter<byte[]> {

        @Override
        public void write(JsonWriter out, byte[] value) throws IOException {
            if (value == null) {
                out.nullValue();
            } else {
                out.value(ByteString.of(value).base64());
            }
        }

        @Override
        public byte[] read(JsonReader in) throws IOException {
            switch (in.peek()) {
                case NULL:
                    in.nextNull();
                    return null;
                default:
                    String bytesAsBase64 = in.nextString();
                    ByteString byteString = ByteString.decodeBase64(bytesAsBase64);
                    return byteString.toByteArray();
            }
        }
    }

    /**
     * Gson TypeAdapter for JSR310 OffsetDateTime type
     */
    public static class OffsetDateTimeTypeAdapter extends TypeAdapter<OffsetDateTime> {

        private DateTimeFormatter formatter;

        public OffsetDateTimeTypeAdapter() {
            this(DateTimeFormatter.ISO_OFFSET_DATE_TIME);
        }

        public OffsetDateTimeTypeAdapter(DateTimeFormatter formatter) {
            this.formatter = formatter;
        }

        public void setFormat(DateTimeFormatter dateFormat) {
            this.formatter = dateFormat;
        }

        @Override
        public void write(JsonWriter out, OffsetDateTime date) throws IOException {
            if (date == null) {
                out.nullValue();
            } else {
                out.value(formatter.format(date));
            }
        }

        @Override
        public OffsetDateTime read(JsonReader in) throws IOException {
            switch (in.peek()) {
                case NULL:
                    in.nextNull();
                    return null;
                default:
                    String date = in.nextString();
                    if (date.endsWith("+0000")) {
                        date = date.substring(0, date.length()-5) + "Z";
                    }
                    return OffsetDateTime.parse(date, formatter);
            }
        }
    }

    /**
     * Gson TypeAdapter for JSR310 LocalDate type
     */
    public static class LocalDateTypeAdapter extends TypeAdapter<LocalDate> {

        private DateTimeFormatter formatter;

        public LocalDateTypeAdapter() {
            this(DateTimeFormatter.ISO_LOCAL_DATE);
        }

        public LocalDateTypeAdapter(DateTimeFormatter formatter) {
            this.formatter = formatter;
        }

        public void setFormat(DateTimeFormatter dateFormat) {
            this.formatter = dateFormat;
        }

        @Override
        public void write(JsonWriter out, LocalDate date) throws IOException {
            if (date == null) {
                out.nullValue();
            } else {
                out.value(formatter.format(date));
            }
        }

        @Override
        public LocalDate read(JsonReader in) throws IOException {
            switch (in.peek()) {
                case NULL:
                    in.nextNull();
                    return null;
                default:
                    String date = in.nextString();
                    return LocalDate.parse(date, formatter);
            }
        }
    }

    public static void setOffsetDateTimeFormat(DateTimeFormatter dateFormat) {
        offsetDateTimeTypeAdapter.setFormat(dateFormat);
    }

    public static void setLocalDateFormat(DateTimeFormatter dateFormat) {
        localDateTypeAdapter.setFormat(dateFormat);
    }

    /**
     * Gson TypeAdapter for java.sql.Date type
     * If the dateFormat is null, a simple "yyyy-MM-dd" format will be used
     * (more efficient than SimpleDateFormat).
     */
    public static class SqlDateTypeAdapter extends TypeAdapter<java.sql.Date> {

        private DateFormat dateFormat;

        public SqlDateTypeAdapter() {}

        public SqlDateTypeAdapter(DateFormat dateFormat) {
            this.dateFormat = dateFormat;
        }

        public void setFormat(DateFormat dateFormat) {
            this.dateFormat = dateFormat;
        }

        @Override
        public void write(JsonWriter out, java.sql.Date date) throws IOException {
            if (date == null) {
                out.nullValue();
            } else {
                String value;
                if (dateFormat != null) {
                    value = dateFormat.format(date);
                } else {
                    value = date.toString();
                }
                out.value(value);
            }
        }

        @Override
        public java.sql.Date read(JsonReader in) throws IOException {
            switch (in.peek()) {
                case NULL:
                    in.nextNull();
                    return null;
                default:
                    String date = in.nextString();
                    try {
                        if (dateFormat != null) {
                            return new java.sql.Date(dateFormat.parse(date).getTime());
                        }
                        return new java.sql.Date(ISO8601Utils.parse(date, new ParsePosition(0)).getTime());
                    } catch (ParseException e) {
                        throw new JsonParseException(e);
                    }
            }
        }
    }

    /**
     * Gson TypeAdapter for java.util.Date type
     * If the dateFormat is null, ISO8601Utils will be used.
     */
    public static class DateTypeAdapter extends TypeAdapter<Date> {

        private DateFormat dateFormat;

        public DateTypeAdapter() {}

        public DateTypeAdapter(DateFormat dateFormat) {
            this.dateFormat = dateFormat;
        }

        public void setFormat(DateFormat dateFormat) {
            this.dateFormat = dateFormat;
        }

        @Override
        public void write(JsonWriter out, Date date) throws IOException {
            if (date == null) {
                out.nullValue();
            } else {
                String value;
                if (dateFormat != null) {
                    value = dateFormat.format(date);
                } else {
                    value = ISO8601Utils.format(date, true);
                }
                out.value(value);
            }
        }

        @Override
        public Date read(JsonReader in) throws IOException {
            try {
                switch (in.peek()) {
                    case NULL:
                        in.nextNull();
                        return null;
                    default:
                        String date = in.nextString();
                        try {
                            if (dateFormat != null) {
                                return dateFormat.parse(date);
                            }
                            return ISO8601Utils.parse(date, new ParsePosition(0));
                        } catch (ParseException e) {
                            throw new JsonParseException(e);
                        }
                }
            } catch (IllegalArgumentException e) {
                throw new JsonParseException(e);
            }
        }
    }

    public static void setDateFormat(DateFormat dateFormat) {
        dateTypeAdapter.setFormat(dateFormat);
    }

    public static void setSqlDateFormat(DateFormat dateFormat) {
        sqlDateTypeAdapter.setFormat(dateFormat);
    }
}
