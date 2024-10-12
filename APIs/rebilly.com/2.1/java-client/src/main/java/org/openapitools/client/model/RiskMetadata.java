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
import java.util.HashMap;
import java.util.Map;
import org.openapitools.client.model.BrowserData;

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
 * Risk metadata used for 3DS and risk scoring.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:20:59.825309-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class RiskMetadata {
  public static final String SERIALIZED_NAME_ACCURACY_RADIUS = "accuracyRadius";
  @SerializedName(SERIALIZED_NAME_ACCURACY_RADIUS)
  private Integer accuracyRadius;

  public static final String SERIALIZED_NAME_BROWSER_DATA = "browserData";
  @SerializedName(SERIALIZED_NAME_BROWSER_DATA)
  private BrowserData browserData;

  public static final String SERIALIZED_NAME_CITY = "city";
  @SerializedName(SERIALIZED_NAME_CITY)
  private String city;

  public static final String SERIALIZED_NAME_COUNTRY = "country";
  @SerializedName(SERIALIZED_NAME_COUNTRY)
  private String country;

  public static final String SERIALIZED_NAME_DEVICE_VELOCITY = "deviceVelocity";
  @SerializedName(SERIALIZED_NAME_DEVICE_VELOCITY)
  private Integer deviceVelocity;

  public static final String SERIALIZED_NAME_DISTANCE = "distance";
  @SerializedName(SERIALIZED_NAME_DISTANCE)
  private Integer distance;

  public static final String SERIALIZED_NAME_FINGERPRINT = "fingerprint";
  @SerializedName(SERIALIZED_NAME_FINGERPRINT)
  private String fingerprint;

  public static final String SERIALIZED_NAME_HAS_MISMATCHED_BANK_COUNTRY = "hasMismatchedBankCountry";
  @SerializedName(SERIALIZED_NAME_HAS_MISMATCHED_BANK_COUNTRY)
  private Boolean hasMismatchedBankCountry;

  public static final String SERIALIZED_NAME_HAS_MISMATCHED_BILLING_ADDRESS_COUNTRY = "hasMismatchedBillingAddressCountry";
  @SerializedName(SERIALIZED_NAME_HAS_MISMATCHED_BILLING_ADDRESS_COUNTRY)
  private Boolean hasMismatchedBillingAddressCountry;

  public static final String SERIALIZED_NAME_HAS_MISMATCHED_HOLDER_NAME = "hasMismatchedHolderName";
  @SerializedName(SERIALIZED_NAME_HAS_MISMATCHED_HOLDER_NAME)
  private Boolean hasMismatchedHolderName;

  public static final String SERIALIZED_NAME_HAS_MISMATCHED_TIME_ZONE = "hasMismatchedTimeZone";
  @SerializedName(SERIALIZED_NAME_HAS_MISMATCHED_TIME_ZONE)
  private Boolean hasMismatchedTimeZone;

  public static final String SERIALIZED_NAME_HTTP_HEADERS = "httpHeaders";
  @SerializedName(SERIALIZED_NAME_HTTP_HEADERS)
  private Map<String, String> httpHeaders = new HashMap<>();

  public static final String SERIALIZED_NAME_IP_ADDRESS = "ipAddress";
  @SerializedName(SERIALIZED_NAME_IP_ADDRESS)
  private String ipAddress;

  public static final String SERIALIZED_NAME_IS_HOSTING = "isHosting";
  @SerializedName(SERIALIZED_NAME_IS_HOSTING)
  private Boolean isHosting;

  public static final String SERIALIZED_NAME_IS_PROXY = "isProxy";
  @SerializedName(SERIALIZED_NAME_IS_PROXY)
  private Boolean isProxy;

  public static final String SERIALIZED_NAME_IS_TOR = "isTor";
  @SerializedName(SERIALIZED_NAME_IS_TOR)
  private Boolean isTor;

  public static final String SERIALIZED_NAME_IS_VPN = "isVpn";
  @SerializedName(SERIALIZED_NAME_IS_VPN)
  private Boolean isVpn;

  public static final String SERIALIZED_NAME_ISP = "isp";
  @SerializedName(SERIALIZED_NAME_ISP)
  private String isp;

  public static final String SERIALIZED_NAME_LATITUDE = "latitude";
  @SerializedName(SERIALIZED_NAME_LATITUDE)
  private Double latitude;

  public static final String SERIALIZED_NAME_LONGITUDE = "longitude";
  @SerializedName(SERIALIZED_NAME_LONGITUDE)
  private Double longitude;

  public static final String SERIALIZED_NAME_PAYMENT_INSTRUMENT_VELOCITY = "paymentInstrumentVelocity";
  @SerializedName(SERIALIZED_NAME_PAYMENT_INSTRUMENT_VELOCITY)
  private Integer paymentInstrumentVelocity;

  public static final String SERIALIZED_NAME_POSTAL_CODE = "postalCode";
  @SerializedName(SERIALIZED_NAME_POSTAL_CODE)
  private String postalCode;

  public static final String SERIALIZED_NAME_REGION = "region";
  @SerializedName(SERIALIZED_NAME_REGION)
  private String region;

  public static final String SERIALIZED_NAME_SCORE = "score";
  @SerializedName(SERIALIZED_NAME_SCORE)
  private Integer score;

  public static final String SERIALIZED_NAME_TIME_ZONE = "timeZone";
  @SerializedName(SERIALIZED_NAME_TIME_ZONE)
  private String timeZone;

  public static final String SERIALIZED_NAME_VPN_SERVICE_NAME = "vpnServiceName";
  @SerializedName(SERIALIZED_NAME_VPN_SERVICE_NAME)
  private String vpnServiceName;

  public RiskMetadata() {
  }

  public RiskMetadata(
     Integer accuracyRadius, 
     String city, 
     String country, 
     Integer deviceVelocity, 
     Integer distance, 
     Boolean hasMismatchedBankCountry, 
     Boolean hasMismatchedBillingAddressCountry, 
     Boolean hasMismatchedHolderName, 
     Boolean hasMismatchedTimeZone, 
     Boolean isHosting, 
     Boolean isProxy, 
     Boolean isTor, 
     Boolean isVpn, 
     String isp, 
     Double latitude, 
     Double longitude, 
     Integer paymentInstrumentVelocity, 
     String postalCode, 
     String region, 
     Integer score, 
     String timeZone, 
     String vpnServiceName
  ) {
    this();
    this.accuracyRadius = accuracyRadius;
    this.city = city;
    this.country = country;
    this.deviceVelocity = deviceVelocity;
    this.distance = distance;
    this.hasMismatchedBankCountry = hasMismatchedBankCountry;
    this.hasMismatchedBillingAddressCountry = hasMismatchedBillingAddressCountry;
    this.hasMismatchedHolderName = hasMismatchedHolderName;
    this.hasMismatchedTimeZone = hasMismatchedTimeZone;
    this.isHosting = isHosting;
    this.isProxy = isProxy;
    this.isTor = isTor;
    this.isVpn = isVpn;
    this.isp = isp;
    this.latitude = latitude;
    this.longitude = longitude;
    this.paymentInstrumentVelocity = paymentInstrumentVelocity;
    this.postalCode = postalCode;
    this.region = region;
    this.score = score;
    this.timeZone = timeZone;
    this.vpnServiceName = vpnServiceName;
  }

  /**
   * Accuracy radius for specified ipAddress (kilometers).
   * @return accuracyRadius
   */
  @javax.annotation.Nullable
  public Integer getAccuracyRadius() {
    return accuracyRadius;
  }



  public RiskMetadata browserData(BrowserData browserData) {
    this.browserData = browserData;
    return this;
  }

  /**
   * Get browserData
   * @return browserData
   */
  @javax.annotation.Nullable
  public BrowserData getBrowserData() {
    return browserData;
  }

  public void setBrowserData(BrowserData browserData) {
    this.browserData = browserData;
  }


  /**
   * City for specified ipAddress.
   * @return city
   */
  @javax.annotation.Nullable
  public String getCity() {
    return city;
  }



  /**
   * Country ISO Alpha-2 code for specified ipAddress.
   * @return country
   */
  @javax.annotation.Nullable
  public String getCountry() {
    return country;
  }



  /**
   * Number of transactions for this device (based on fingerprint) in the last 24 hours.
   * @return deviceVelocity
   */
  @javax.annotation.Nullable
  public Integer getDeviceVelocity() {
    return deviceVelocity;
  }



  /**
   * Distance between IP Address and Billing Address geolocation (kilometers).
   * @return distance
   */
  @javax.annotation.Nullable
  public Integer getDistance() {
    return distance;
  }



  public RiskMetadata fingerprint(String fingerprint) {
    this.fingerprint = fingerprint;
    return this;
  }

  /**
   * The fingerprint.
   * @return fingerprint
   */
  @javax.annotation.Nullable
  public String getFingerprint() {
    return fingerprint;
  }

  public void setFingerprint(String fingerprint) {
    this.fingerprint = fingerprint;
  }


  /**
   * True if the bank country and geo-IP address are not the same.
   * @return hasMismatchedBankCountry
   */
  @javax.annotation.Nullable
  public Boolean getHasMismatchedBankCountry() {
    return hasMismatchedBankCountry;
  }



  /**
   * True if the billing address country and geo-IP address are not the same.
   * @return hasMismatchedBillingAddressCountry
   */
  @javax.annotation.Nullable
  public Boolean getHasMismatchedBillingAddressCountry() {
    return hasMismatchedBillingAddressCountry;
  }



  /**
   * True if the customer&#39;s name from billing address and from customer&#39;s primary address are not the same.
   * @return hasMismatchedHolderName
   */
  @javax.annotation.Nullable
  public Boolean getHasMismatchedHolderName() {
    return hasMismatchedHolderName;
  }



  /**
   * True if the browser time zone and IP address associated time zone are not the same.
   * @return hasMismatchedTimeZone
   */
  @javax.annotation.Nullable
  public Boolean getHasMismatchedTimeZone() {
    return hasMismatchedTimeZone;
  }



  public RiskMetadata httpHeaders(Map<String, String> httpHeaders) {
    this.httpHeaders = httpHeaders;
    return this;
  }

  public RiskMetadata putHttpHeadersItem(String key, String httpHeadersItem) {
    if (this.httpHeaders == null) {
      this.httpHeaders = new HashMap<>();
    }
    this.httpHeaders.put(key, httpHeadersItem);
    return this;
  }

  /**
   * The HTTP headers.
   * @return httpHeaders
   */
  @javax.annotation.Nullable
  public Map<String, String> getHttpHeaders() {
    return httpHeaders;
  }

  public void setHttpHeaders(Map<String, String> httpHeaders) {
    this.httpHeaders = httpHeaders;
  }


  public RiskMetadata ipAddress(String ipAddress) {
    this.ipAddress = ipAddress;
    return this;
  }

  /**
   * The customer&#39;s IP.
   * @return ipAddress
   */
  @javax.annotation.Nullable
  public String getIpAddress() {
    return ipAddress;
  }

  public void setIpAddress(String ipAddress) {
    this.ipAddress = ipAddress;
  }


  /**
   * True if customer&#39;s ip address is related to hosting.
   * @return isHosting
   */
  @javax.annotation.Nullable
  public Boolean getIsHosting() {
    return isHosting;
  }



  /**
   * True if customer&#39;s ip address is related to proxy.
   * @return isProxy
   */
  @javax.annotation.Nullable
  public Boolean getIsProxy() {
    return isProxy;
  }



  /**
   * True if customer&#39;s ip address is related to TOR.
   * @return isTor
   */
  @javax.annotation.Nullable
  public Boolean getIsTor() {
    return isTor;
  }



  /**
   * True if customer&#39;s ip address is related to VPN.
   * @return isVpn
   */
  @javax.annotation.Nullable
  public Boolean getIsVpn() {
    return isVpn;
  }



  /**
   * Internet Service Provider name, if available.
   * @return isp
   */
  @javax.annotation.Nullable
  public String getIsp() {
    return isp;
  }



  /**
   * Latitude for specified ipAddress.
   * @return latitude
   */
  @javax.annotation.Nullable
  public Double getLatitude() {
    return latitude;
  }



  /**
   * Longitude for specified ipAddress.
   * @return longitude
   */
  @javax.annotation.Nullable
  public Double getLongitude() {
    return longitude;
  }



  /**
   * Number of transactions for this payment instrument (based on fingerprint) in the last 24 hours.
   * @return paymentInstrumentVelocity
   */
  @javax.annotation.Nullable
  public Integer getPaymentInstrumentVelocity() {
    return paymentInstrumentVelocity;
  }



  /**
   * Postal code for specified ipAddress.
   * @return postalCode
   */
  @javax.annotation.Nullable
  public String getPostalCode() {
    return postalCode;
  }



  /**
   * Region for specified ipAddress.
   * @return region
   */
  @javax.annotation.Nullable
  public String getRegion() {
    return region;
  }



  /**
   * Risk score computed per all the factors.
   * @return score
   */
  @javax.annotation.Nullable
  public Integer getScore() {
    return score;
  }



  /**
   * Time zone for specified ipAddress.
   * @return timeZone
   */
  @javax.annotation.Nullable
  public String getTimeZone() {
    return timeZone;
  }



  /**
   * VPN service name, if available.
   * @return vpnServiceName
   */
  @javax.annotation.Nullable
  public String getVpnServiceName() {
    return vpnServiceName;
  }




  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    RiskMetadata riskMetadata = (RiskMetadata) o;
    return Objects.equals(this.accuracyRadius, riskMetadata.accuracyRadius) &&
        Objects.equals(this.browserData, riskMetadata.browserData) &&
        Objects.equals(this.city, riskMetadata.city) &&
        Objects.equals(this.country, riskMetadata.country) &&
        Objects.equals(this.deviceVelocity, riskMetadata.deviceVelocity) &&
        Objects.equals(this.distance, riskMetadata.distance) &&
        Objects.equals(this.fingerprint, riskMetadata.fingerprint) &&
        Objects.equals(this.hasMismatchedBankCountry, riskMetadata.hasMismatchedBankCountry) &&
        Objects.equals(this.hasMismatchedBillingAddressCountry, riskMetadata.hasMismatchedBillingAddressCountry) &&
        Objects.equals(this.hasMismatchedHolderName, riskMetadata.hasMismatchedHolderName) &&
        Objects.equals(this.hasMismatchedTimeZone, riskMetadata.hasMismatchedTimeZone) &&
        Objects.equals(this.httpHeaders, riskMetadata.httpHeaders) &&
        Objects.equals(this.ipAddress, riskMetadata.ipAddress) &&
        Objects.equals(this.isHosting, riskMetadata.isHosting) &&
        Objects.equals(this.isProxy, riskMetadata.isProxy) &&
        Objects.equals(this.isTor, riskMetadata.isTor) &&
        Objects.equals(this.isVpn, riskMetadata.isVpn) &&
        Objects.equals(this.isp, riskMetadata.isp) &&
        Objects.equals(this.latitude, riskMetadata.latitude) &&
        Objects.equals(this.longitude, riskMetadata.longitude) &&
        Objects.equals(this.paymentInstrumentVelocity, riskMetadata.paymentInstrumentVelocity) &&
        Objects.equals(this.postalCode, riskMetadata.postalCode) &&
        Objects.equals(this.region, riskMetadata.region) &&
        Objects.equals(this.score, riskMetadata.score) &&
        Objects.equals(this.timeZone, riskMetadata.timeZone) &&
        Objects.equals(this.vpnServiceName, riskMetadata.vpnServiceName);
  }

  @Override
  public int hashCode() {
    return Objects.hash(accuracyRadius, browserData, city, country, deviceVelocity, distance, fingerprint, hasMismatchedBankCountry, hasMismatchedBillingAddressCountry, hasMismatchedHolderName, hasMismatchedTimeZone, httpHeaders, ipAddress, isHosting, isProxy, isTor, isVpn, isp, latitude, longitude, paymentInstrumentVelocity, postalCode, region, score, timeZone, vpnServiceName);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class RiskMetadata {\n");
    sb.append("    accuracyRadius: ").append(toIndentedString(accuracyRadius)).append("\n");
    sb.append("    browserData: ").append(toIndentedString(browserData)).append("\n");
    sb.append("    city: ").append(toIndentedString(city)).append("\n");
    sb.append("    country: ").append(toIndentedString(country)).append("\n");
    sb.append("    deviceVelocity: ").append(toIndentedString(deviceVelocity)).append("\n");
    sb.append("    distance: ").append(toIndentedString(distance)).append("\n");
    sb.append("    fingerprint: ").append(toIndentedString(fingerprint)).append("\n");
    sb.append("    hasMismatchedBankCountry: ").append(toIndentedString(hasMismatchedBankCountry)).append("\n");
    sb.append("    hasMismatchedBillingAddressCountry: ").append(toIndentedString(hasMismatchedBillingAddressCountry)).append("\n");
    sb.append("    hasMismatchedHolderName: ").append(toIndentedString(hasMismatchedHolderName)).append("\n");
    sb.append("    hasMismatchedTimeZone: ").append(toIndentedString(hasMismatchedTimeZone)).append("\n");
    sb.append("    httpHeaders: ").append(toIndentedString(httpHeaders)).append("\n");
    sb.append("    ipAddress: ").append(toIndentedString(ipAddress)).append("\n");
    sb.append("    isHosting: ").append(toIndentedString(isHosting)).append("\n");
    sb.append("    isProxy: ").append(toIndentedString(isProxy)).append("\n");
    sb.append("    isTor: ").append(toIndentedString(isTor)).append("\n");
    sb.append("    isVpn: ").append(toIndentedString(isVpn)).append("\n");
    sb.append("    isp: ").append(toIndentedString(isp)).append("\n");
    sb.append("    latitude: ").append(toIndentedString(latitude)).append("\n");
    sb.append("    longitude: ").append(toIndentedString(longitude)).append("\n");
    sb.append("    paymentInstrumentVelocity: ").append(toIndentedString(paymentInstrumentVelocity)).append("\n");
    sb.append("    postalCode: ").append(toIndentedString(postalCode)).append("\n");
    sb.append("    region: ").append(toIndentedString(region)).append("\n");
    sb.append("    score: ").append(toIndentedString(score)).append("\n");
    sb.append("    timeZone: ").append(toIndentedString(timeZone)).append("\n");
    sb.append("    vpnServiceName: ").append(toIndentedString(vpnServiceName)).append("\n");
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
    openapiFields.add("accuracyRadius");
    openapiFields.add("browserData");
    openapiFields.add("city");
    openapiFields.add("country");
    openapiFields.add("deviceVelocity");
    openapiFields.add("distance");
    openapiFields.add("fingerprint");
    openapiFields.add("hasMismatchedBankCountry");
    openapiFields.add("hasMismatchedBillingAddressCountry");
    openapiFields.add("hasMismatchedHolderName");
    openapiFields.add("hasMismatchedTimeZone");
    openapiFields.add("httpHeaders");
    openapiFields.add("ipAddress");
    openapiFields.add("isHosting");
    openapiFields.add("isProxy");
    openapiFields.add("isTor");
    openapiFields.add("isVpn");
    openapiFields.add("isp");
    openapiFields.add("latitude");
    openapiFields.add("longitude");
    openapiFields.add("paymentInstrumentVelocity");
    openapiFields.add("postalCode");
    openapiFields.add("region");
    openapiFields.add("score");
    openapiFields.add("timeZone");
    openapiFields.add("vpnServiceName");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to RiskMetadata
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!RiskMetadata.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in RiskMetadata is not found in the empty JSON string", RiskMetadata.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!RiskMetadata.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `RiskMetadata` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `browserData`
      if (jsonObj.get("browserData") != null && !jsonObj.get("browserData").isJsonNull()) {
        BrowserData.validateJsonElement(jsonObj.get("browserData"));
      }
      if ((jsonObj.get("city") != null && !jsonObj.get("city").isJsonNull()) && !jsonObj.get("city").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `city` to be a primitive type in the JSON string but got `%s`", jsonObj.get("city").toString()));
      }
      if ((jsonObj.get("country") != null && !jsonObj.get("country").isJsonNull()) && !jsonObj.get("country").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `country` to be a primitive type in the JSON string but got `%s`", jsonObj.get("country").toString()));
      }
      if ((jsonObj.get("fingerprint") != null && !jsonObj.get("fingerprint").isJsonNull()) && !jsonObj.get("fingerprint").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `fingerprint` to be a primitive type in the JSON string but got `%s`", jsonObj.get("fingerprint").toString()));
      }
      if ((jsonObj.get("ipAddress") != null && !jsonObj.get("ipAddress").isJsonNull()) && !jsonObj.get("ipAddress").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ipAddress` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ipAddress").toString()));
      }
      if ((jsonObj.get("isp") != null && !jsonObj.get("isp").isJsonNull()) && !jsonObj.get("isp").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `isp` to be a primitive type in the JSON string but got `%s`", jsonObj.get("isp").toString()));
      }
      if ((jsonObj.get("postalCode") != null && !jsonObj.get("postalCode").isJsonNull()) && !jsonObj.get("postalCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `postalCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("postalCode").toString()));
      }
      if ((jsonObj.get("region") != null && !jsonObj.get("region").isJsonNull()) && !jsonObj.get("region").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `region` to be a primitive type in the JSON string but got `%s`", jsonObj.get("region").toString()));
      }
      if ((jsonObj.get("timeZone") != null && !jsonObj.get("timeZone").isJsonNull()) && !jsonObj.get("timeZone").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `timeZone` to be a primitive type in the JSON string but got `%s`", jsonObj.get("timeZone").toString()));
      }
      if ((jsonObj.get("vpnServiceName") != null && !jsonObj.get("vpnServiceName").isJsonNull()) && !jsonObj.get("vpnServiceName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `vpnServiceName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("vpnServiceName").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!RiskMetadata.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'RiskMetadata' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<RiskMetadata> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(RiskMetadata.class));

       return (TypeAdapter<T>) new TypeAdapter<RiskMetadata>() {
           @Override
           public void write(JsonWriter out, RiskMetadata value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public RiskMetadata read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of RiskMetadata given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of RiskMetadata
   * @throws IOException if the JSON string is invalid with respect to RiskMetadata
   */
  public static RiskMetadata fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, RiskMetadata.class);
  }

  /**
   * Convert an instance of RiskMetadata to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

