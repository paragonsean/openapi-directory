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
 * DataCashAllOfCredentials
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:20:59.825309-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class DataCashAllOfCredentials {
  public static final String SERIALIZED_NAME_CLIENT = "client";
  @SerializedName(SERIALIZED_NAME_CLIENT)
  private String client;

  public static final String SERIALIZED_NAME_MASTER_CARD_PAYOUTS_CLIENT = "masterCardPayoutsClient";
  @SerializedName(SERIALIZED_NAME_MASTER_CARD_PAYOUTS_CLIENT)
  private String masterCardPayoutsClient;

  public static final String SERIALIZED_NAME_MASTER_CARD_PAYOUTS_PASSWORD = "masterCardPayoutsPassword";
  @SerializedName(SERIALIZED_NAME_MASTER_CARD_PAYOUTS_PASSWORD)
  private String masterCardPayoutsPassword;

  public static final String SERIALIZED_NAME_PASSWORD = "password";
  @SerializedName(SERIALIZED_NAME_PASSWORD)
  private String password;

  public static final String SERIALIZED_NAME_REPORT_GROUP = "reportGroup";
  @SerializedName(SERIALIZED_NAME_REPORT_GROUP)
  private String reportGroup;

  public static final String SERIALIZED_NAME_REPORT_PASSWORD = "reportPassword";
  @SerializedName(SERIALIZED_NAME_REPORT_PASSWORD)
  private String reportPassword;

  public static final String SERIALIZED_NAME_REPORT_USER = "reportUser";
  @SerializedName(SERIALIZED_NAME_REPORT_USER)
  private String reportUser;

  public static final String SERIALIZED_NAME_VISA_PAYOUTS_CLIENT = "visaPayoutsClient";
  @SerializedName(SERIALIZED_NAME_VISA_PAYOUTS_CLIENT)
  private String visaPayoutsClient;

  public static final String SERIALIZED_NAME_VISA_PAYOUTS_PASSWORD = "visaPayoutsPassword";
  @SerializedName(SERIALIZED_NAME_VISA_PAYOUTS_PASSWORD)
  private String visaPayoutsPassword;

  public DataCashAllOfCredentials() {
  }

  public DataCashAllOfCredentials client(String client) {
    this.client = client;
    return this;
  }

  /**
   * DataCash Gateway client.
   * @return client
   */
  @javax.annotation.Nonnull
  public String getClient() {
    return client;
  }

  public void setClient(String client) {
    this.client = client;
  }


  public DataCashAllOfCredentials masterCardPayoutsClient(String masterCardPayoutsClient) {
    this.masterCardPayoutsClient = masterCardPayoutsClient;
    return this;
  }

  /**
   * DataCash Gateway client for MasterCard payouts (OCT).
   * @return masterCardPayoutsClient
   */
  @javax.annotation.Nullable
  public String getMasterCardPayoutsClient() {
    return masterCardPayoutsClient;
  }

  public void setMasterCardPayoutsClient(String masterCardPayoutsClient) {
    this.masterCardPayoutsClient = masterCardPayoutsClient;
  }


  public DataCashAllOfCredentials masterCardPayoutsPassword(String masterCardPayoutsPassword) {
    this.masterCardPayoutsPassword = masterCardPayoutsPassword;
    return this;
  }

  /**
   * DataCash Gateway password for MasterCard payouts (OCT).
   * @return masterCardPayoutsPassword
   */
  @javax.annotation.Nullable
  public String getMasterCardPayoutsPassword() {
    return masterCardPayoutsPassword;
  }

  public void setMasterCardPayoutsPassword(String masterCardPayoutsPassword) {
    this.masterCardPayoutsPassword = masterCardPayoutsPassword;
  }


  public DataCashAllOfCredentials password(String password) {
    this.password = password;
    return this;
  }

  /**
   * DataCash Gateway password.
   * @return password
   */
  @javax.annotation.Nonnull
  public String getPassword() {
    return password;
  }

  public void setPassword(String password) {
    this.password = password;
  }


  public DataCashAllOfCredentials reportGroup(String reportGroup) {
    this.reportGroup = reportGroup;
    return this;
  }

  /**
   * DataCash report group.
   * @return reportGroup
   */
  @javax.annotation.Nullable
  public String getReportGroup() {
    return reportGroup;
  }

  public void setReportGroup(String reportGroup) {
    this.reportGroup = reportGroup;
  }


  public DataCashAllOfCredentials reportPassword(String reportPassword) {
    this.reportPassword = reportPassword;
    return this;
  }

  /**
   * DataCash report password.
   * @return reportPassword
   */
  @javax.annotation.Nullable
  public String getReportPassword() {
    return reportPassword;
  }

  public void setReportPassword(String reportPassword) {
    this.reportPassword = reportPassword;
  }


  public DataCashAllOfCredentials reportUser(String reportUser) {
    this.reportUser = reportUser;
    return this;
  }

  /**
   * DataCash report user.
   * @return reportUser
   */
  @javax.annotation.Nullable
  public String getReportUser() {
    return reportUser;
  }

  public void setReportUser(String reportUser) {
    this.reportUser = reportUser;
  }


  public DataCashAllOfCredentials visaPayoutsClient(String visaPayoutsClient) {
    this.visaPayoutsClient = visaPayoutsClient;
    return this;
  }

  /**
   * DataCash Gateway client for Visa payouts (OCT).
   * @return visaPayoutsClient
   */
  @javax.annotation.Nullable
  public String getVisaPayoutsClient() {
    return visaPayoutsClient;
  }

  public void setVisaPayoutsClient(String visaPayoutsClient) {
    this.visaPayoutsClient = visaPayoutsClient;
  }


  public DataCashAllOfCredentials visaPayoutsPassword(String visaPayoutsPassword) {
    this.visaPayoutsPassword = visaPayoutsPassword;
    return this;
  }

  /**
   * DataCash Gateway password for Visa payouts (OCT).
   * @return visaPayoutsPassword
   */
  @javax.annotation.Nullable
  public String getVisaPayoutsPassword() {
    return visaPayoutsPassword;
  }

  public void setVisaPayoutsPassword(String visaPayoutsPassword) {
    this.visaPayoutsPassword = visaPayoutsPassword;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    DataCashAllOfCredentials dataCashAllOfCredentials = (DataCashAllOfCredentials) o;
    return Objects.equals(this.client, dataCashAllOfCredentials.client) &&
        Objects.equals(this.masterCardPayoutsClient, dataCashAllOfCredentials.masterCardPayoutsClient) &&
        Objects.equals(this.masterCardPayoutsPassword, dataCashAllOfCredentials.masterCardPayoutsPassword) &&
        Objects.equals(this.password, dataCashAllOfCredentials.password) &&
        Objects.equals(this.reportGroup, dataCashAllOfCredentials.reportGroup) &&
        Objects.equals(this.reportPassword, dataCashAllOfCredentials.reportPassword) &&
        Objects.equals(this.reportUser, dataCashAllOfCredentials.reportUser) &&
        Objects.equals(this.visaPayoutsClient, dataCashAllOfCredentials.visaPayoutsClient) &&
        Objects.equals(this.visaPayoutsPassword, dataCashAllOfCredentials.visaPayoutsPassword);
  }

  @Override
  public int hashCode() {
    return Objects.hash(client, masterCardPayoutsClient, masterCardPayoutsPassword, password, reportGroup, reportPassword, reportUser, visaPayoutsClient, visaPayoutsPassword);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class DataCashAllOfCredentials {\n");
    sb.append("    client: ").append(toIndentedString(client)).append("\n");
    sb.append("    masterCardPayoutsClient: ").append(toIndentedString(masterCardPayoutsClient)).append("\n");
    sb.append("    masterCardPayoutsPassword: ").append("*").append("\n");
    sb.append("    password: ").append("*").append("\n");
    sb.append("    reportGroup: ").append(toIndentedString(reportGroup)).append("\n");
    sb.append("    reportPassword: ").append("*").append("\n");
    sb.append("    reportUser: ").append(toIndentedString(reportUser)).append("\n");
    sb.append("    visaPayoutsClient: ").append(toIndentedString(visaPayoutsClient)).append("\n");
    sb.append("    visaPayoutsPassword: ").append("*").append("\n");
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
    openapiFields.add("client");
    openapiFields.add("masterCardPayoutsClient");
    openapiFields.add("masterCardPayoutsPassword");
    openapiFields.add("password");
    openapiFields.add("reportGroup");
    openapiFields.add("reportPassword");
    openapiFields.add("reportUser");
    openapiFields.add("visaPayoutsClient");
    openapiFields.add("visaPayoutsPassword");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("client");
    openapiRequiredFields.add("password");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to DataCashAllOfCredentials
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!DataCashAllOfCredentials.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in DataCashAllOfCredentials is not found in the empty JSON string", DataCashAllOfCredentials.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!DataCashAllOfCredentials.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `DataCashAllOfCredentials` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : DataCashAllOfCredentials.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("client").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `client` to be a primitive type in the JSON string but got `%s`", jsonObj.get("client").toString()));
      }
      if ((jsonObj.get("masterCardPayoutsClient") != null && !jsonObj.get("masterCardPayoutsClient").isJsonNull()) && !jsonObj.get("masterCardPayoutsClient").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `masterCardPayoutsClient` to be a primitive type in the JSON string but got `%s`", jsonObj.get("masterCardPayoutsClient").toString()));
      }
      if ((jsonObj.get("masterCardPayoutsPassword") != null && !jsonObj.get("masterCardPayoutsPassword").isJsonNull()) && !jsonObj.get("masterCardPayoutsPassword").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `masterCardPayoutsPassword` to be a primitive type in the JSON string but got `%s`", jsonObj.get("masterCardPayoutsPassword").toString()));
      }
      if (!jsonObj.get("password").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `password` to be a primitive type in the JSON string but got `%s`", jsonObj.get("password").toString()));
      }
      if ((jsonObj.get("reportGroup") != null && !jsonObj.get("reportGroup").isJsonNull()) && !jsonObj.get("reportGroup").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `reportGroup` to be a primitive type in the JSON string but got `%s`", jsonObj.get("reportGroup").toString()));
      }
      if ((jsonObj.get("reportPassword") != null && !jsonObj.get("reportPassword").isJsonNull()) && !jsonObj.get("reportPassword").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `reportPassword` to be a primitive type in the JSON string but got `%s`", jsonObj.get("reportPassword").toString()));
      }
      if ((jsonObj.get("reportUser") != null && !jsonObj.get("reportUser").isJsonNull()) && !jsonObj.get("reportUser").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `reportUser` to be a primitive type in the JSON string but got `%s`", jsonObj.get("reportUser").toString()));
      }
      if ((jsonObj.get("visaPayoutsClient") != null && !jsonObj.get("visaPayoutsClient").isJsonNull()) && !jsonObj.get("visaPayoutsClient").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `visaPayoutsClient` to be a primitive type in the JSON string but got `%s`", jsonObj.get("visaPayoutsClient").toString()));
      }
      if ((jsonObj.get("visaPayoutsPassword") != null && !jsonObj.get("visaPayoutsPassword").isJsonNull()) && !jsonObj.get("visaPayoutsPassword").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `visaPayoutsPassword` to be a primitive type in the JSON string but got `%s`", jsonObj.get("visaPayoutsPassword").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!DataCashAllOfCredentials.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'DataCashAllOfCredentials' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<DataCashAllOfCredentials> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(DataCashAllOfCredentials.class));

       return (TypeAdapter<T>) new TypeAdapter<DataCashAllOfCredentials>() {
           @Override
           public void write(JsonWriter out, DataCashAllOfCredentials value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public DataCashAllOfCredentials read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of DataCashAllOfCredentials given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of DataCashAllOfCredentials
   * @throws IOException if the JSON string is invalid with respect to DataCashAllOfCredentials
   */
  public static DataCashAllOfCredentials fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, DataCashAllOfCredentials.class);
  }

  /**
   * Convert an instance of DataCashAllOfCredentials to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

