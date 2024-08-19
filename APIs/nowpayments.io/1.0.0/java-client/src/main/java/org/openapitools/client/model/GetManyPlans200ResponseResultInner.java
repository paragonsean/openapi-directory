/*
 * NOWPayments API
 * NOWPayments is a non-custodial cryptocurrency payment processing platform. Accept payments in a wide range of cryptos and get them instantly converted into a coin of your choice and sent to your wallet. Keeping it simple – no excess.  # Sandbox  Before production usage, you can test our API using the Sandbox. Details can be found [here](https://documenter.getpostman.com/view/7907941/T1LSCRHC)  # Authentication  To use the NOWPayments API you should do the following:  *   Sign up at [nowpayments.io](https://nowpayments.io) *   Specify your outcome wallet *   Generate an API key       # Standard e-commerce flow for NOWPayments API:  1.  API - Check API availability with the [\"GET API status\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#9998079f-dcc8-4e07-9ac7-3d52f0fd733a) method. If required, check the list of available payment currencies with the [\"GET available currencies\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#1c268f89-4fe7-471e-81b4-5a3153577b73) method. 2.  UI - Ask a customer to select item/items for purchase to determine the total sum; 3.  UI - Ask a customer to select payment currency 4.  API - Get the minimum payment amount for the selected currency pair (payment currency to your Outcome Wallet currency) with the [\"GET Minimum payment amount\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#41b02221-2d58-4fcf-9529-59d3763d6434) method; 5.  API - Get the estimate of the total amount in crypto with [\"GET Estimated price\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#7025cacf-7040-4c7b-a83f-f9ff0a22a822) and check that it is larger than the minimum payment amount from step 4; 6.  API - Call the [\"POST Create payment\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#5e37f3ad-0fa1-4292-af51-5c7f95730486) method to create a payment and get the deposit address (in our example, the generated BTC wallet address is returned from this method); 7.  UI - Ask a customer to send the payment to the generated deposit address (in our example, user has to send BTC coins); 8.  UI - A customer sends coins, NOWPayments processes and exchanges them (if required), and settles the payment to your Outcome Wallet (in our example, to your ETH address); 9.  API - You can get the payment status either via our IPN callbacks or manually, using [\"GET Payment Status\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#0b77a8e3-2344-4760-a0bd-247da067db6d) and display it to a customer so that they know when their payment has been processed. 10.  API - you call the list of payments made to your account via the [\"GET List of payments\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#c8399c0e-d798-4f01-83ae-ddaa6905c2da) method. Additionally, you can see all of this information in your [Account](https://account.nowpayments.io/payments) on NOWPayments website.       ## Alternative flow  1.  API - Check API availability with the [\"GET API status\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#9998079f-dcc8-4e07-9ac7-3d52f0fd733a) method. If required, check the list of available payment currencies with the [\"GET available currencies\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#1c268f89-4fe7-471e-81b4-5a3153577b73) method. 2.  UI - Ask a customer to select item/items for purchase to determine the total sum; 3.  UI - Ask a customer to select payment currency 4.  API - Get the minimum payment amount for the selected currency pair (payment currency to your Outcome Wallet currency) with the [\"GET Minimum payment amount\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#41b02221-2d58-4fcf-9529-59d3763d6434) method; 5.  API - Get the estimate of the total amount in crypto with [\"GET Estimated price\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#7025cacf-7040-4c7b-a83f-f9ff0a22a822) and check that it is larger than the minimum payment amount from step 4; 6.  API - Call the [\"POST Create Invoice](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#3e3ce25e-f43f-4636-bbd9-11560e46048b) method to create an invoice. Set \"success_url\" - parameter so that the user will be redirected to your website after successful payment. 7.  UI - display the invoice url or redirect the user to the generated link. 8.  NOWPayments - the customer completes the payment and is redirected back to your website (only if \"success_url\" parameter is configured correctly!). 9.  API - You can get the payment status either via our IPN callbacks or manually, using [\"GET Payment Status\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#0b77a8e3-2344-4760-a0bd-247da067db6d) and display it to a customer so that they know when their payment has been processed. 10.  API - you call the list of payments made to your account via the [\"GET List of payments\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#c8399c0e-d798-4f01-83ae-ddaa6905c2da) method. Additionally, you can see all of this information in your [Account](https://account.nowpayments.io/invoices) on NOWPayments website.       # API Documentation  ## Instant Payments Notifications  IPN (Instant payment notifications, or callbacks) are used to notify you when transaction status is changed.   To use them, you should complete the following steps:  1.  Generate and save the IPN Secret key in Store Settings tab at the Dashboard. 2.  Insert your URL address where you want to get callbacks in create_payment request. The parameter name is ipn_callback_url. You will receive payment updates (statuses) to this URL address. 3.  You will receive all the parameters at the URL address you specified in (2) by POST request.       The POST request will contain the *x-nowpayments-sig* parameter in the header.       The body of the request is similiar to a [get payment status](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#0b77a8e3-2344-4760-a0bd-247da067db6d) response body.       Example:       {\"payment_id\":5077125051,\"payment_status\":\"waiting\",\"pay_address\":\"0xd1cDE08A07cD25adEbEd35c3867a59228C09B606\",\"price_amount\":170,\"price_currency\":\"usd\",\"pay_amount\":155.38559757,\"actually_paid\":0,\"pay_currency\":\"mana\",\"order_id\":\"2\",\"order_description\":\"Apple Macbook Pro 2019 x 1\",\"purchase_id\":\"6084744717\",\"created_at\":\"2021-04-12T14:22:54.942Z\",\"updated_at\":\"2021-04-12T14:23:06.244Z\",\"outcome_amount\":1131.7812095,\"outcome_currency\":\"trx\"} 4.  Sort all the parameters from the POST request in alphabetical order. 5.  Convert them to string using       [JSON.stringify](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify) (params, Object.keys(params).sort()) or the same function. 6.  Sign a string with an IPN-secret key with HMAC and sha-512 key 7.  Compare the signed string from the previous step with the x-nowpayments-sig , which is stored in the header of the callback request.       If these strings are similar it is a success.       Otherwise, contact us on [support@nowpayments.io](mailto:support@nowpayments.io) to solve the problem.       Example of creating a signed string at Node.JS  ``` const hmac = crypto.createHmac('sha512', notificationsKey); hmac.update(JSON.stringify(params, Object.keys(params).sort())); const signature = hmac.digest('hex');  ```  Example of comparing signed strings in PHP  ``` function check_ipn_request_is_valid()     {         $error_msg = \"Unknown error\";         $auth_ok = false;         $request_data = null;         if (isset($_SERVER['HTTP_X_NOWPAYMENTS_SIG']) && !empty($_SERVER['HTTP_X_NOWPAYMENTS_SIG'])) {             $recived_hmac = $_SERVER['HTTP_X_NOWPAYMENTS_SIG'];             $request_json = file_get_contents('php://input');             $request_data = json_decode($request_json, true);             ksort($request_data);             $sorted_request_json = json_encode($request_data, JSON_UNESCAPED_SLASHES);             if ($request_json !== false && !empty($request_json)) {                 $hmac = hash_hmac(\"sha512\", $sorted_request_json, trim($this->ipn_secret));                 if ($hmac == $recived_hmac) {                     $auth_ok = true;                 } else {                     $error_msg = 'HMAC signature does not match';                 }             } else {                 $error_msg = 'Error reading POST data';             }         } else {             $error_msg = 'No HMAC signature sent.';         }     }  ```  ## Recurrent payment notifications  If an error is detected, the payment is flagged and will receive additional recurrent notifications (number of recurrent notifications can be changed in your Store Settings-> Instant Payment Notifications).  If an error is received again during processing of the payment, recurrent notifications will be initiated again.  Example: \"Timeout\" is set to 1 minute and \"Number of recurrent notifications\" is set to 3.  Once an error is detected, you will receive 3 notifications at 1 minute intervals.  ## Several payments for one order  If you want to create several payments for one Order you should do the following:  *   Create a payment for the full order amount. *   Save \"purchase_id\" which will be in \"create_payment\" response *   Create next payment or payments with this \"purchase_id\" in \"create_payment\" request. *   **Only works for partially_paid payments**       It may be useful if you want to give your customers opportunity to pay a full order with several payments, for example, one part in BTC and one part in ETH. Also, if your customer accidentally paid you only part of a full amount, you can automatically ask them to make another payment.  ## Packages  Please find our out-of-the box packages for easy integration below:  [JavaScript package](https://www.npmjs.com/package/@nowpaymentsio/nowpayments-api-js)  \\[PHP package\\]   ([https://packagist.org/packages/nowpayments/nowpayments-api-php](https://packagist.org/packages/nowpayments/nowpayments-api-php))  More coming soon!  ## Payments
 *
 * The version of the OpenAPI document: 1.0.0
 * 
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
import java.math.BigDecimal;
import java.util.Arrays;
import org.openapitools.jackson.nullable.JsonNullable;

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
 * GetManyPlans200ResponseResultInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:30:50.751981-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetManyPlans200ResponseResultInner {
  public static final String SERIALIZED_NAME_AMOUNT = "amount";
  @SerializedName(SERIALIZED_NAME_AMOUNT)
  private BigDecimal amount;

  public static final String SERIALIZED_NAME_CANCEL_URL = "cancel_url";
  @SerializedName(SERIALIZED_NAME_CANCEL_URL)
  private Object cancelUrl = null;

  public static final String SERIALIZED_NAME_CREATED_AT = "created_at";
  @SerializedName(SERIALIZED_NAME_CREATED_AT)
  private String createdAt;

  public static final String SERIALIZED_NAME_CURRENCY = "currency";
  @SerializedName(SERIALIZED_NAME_CURRENCY)
  private String currency;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_INTERVAL_DAY = "interval_day";
  @SerializedName(SERIALIZED_NAME_INTERVAL_DAY)
  private String intervalDay;

  public static final String SERIALIZED_NAME_IPN_CALLBACK_URL = "ipn_callback_url";
  @SerializedName(SERIALIZED_NAME_IPN_CALLBACK_URL)
  private Object ipnCallbackUrl = null;

  public static final String SERIALIZED_NAME_PARTIALLY_PAID_URL = "partially_paid_url";
  @SerializedName(SERIALIZED_NAME_PARTIALLY_PAID_URL)
  private Object partiallyPaidUrl = null;

  public static final String SERIALIZED_NAME_SUCCESS_URL = "success_url";
  @SerializedName(SERIALIZED_NAME_SUCCESS_URL)
  private Object successUrl = null;

  public static final String SERIALIZED_NAME_TITLE = "title";
  @SerializedName(SERIALIZED_NAME_TITLE)
  private String title;

  public static final String SERIALIZED_NAME_UPDATED_AT = "updated_at";
  @SerializedName(SERIALIZED_NAME_UPDATED_AT)
  private String updatedAt;

  public GetManyPlans200ResponseResultInner() {
  }

  public GetManyPlans200ResponseResultInner amount(BigDecimal amount) {
    this.amount = amount;
    return this;
  }

  /**
   * Get amount
   * @return amount
   */
  @javax.annotation.Nullable
  public BigDecimal getAmount() {
    return amount;
  }

  public void setAmount(BigDecimal amount) {
    this.amount = amount;
  }


  public GetManyPlans200ResponseResultInner cancelUrl(Object cancelUrl) {
    this.cancelUrl = cancelUrl;
    return this;
  }

  /**
   * Get cancelUrl
   * @return cancelUrl
   */
  @javax.annotation.Nullable
  public Object getCancelUrl() {
    return cancelUrl;
  }

  public void setCancelUrl(Object cancelUrl) {
    this.cancelUrl = cancelUrl;
  }


  public GetManyPlans200ResponseResultInner createdAt(String createdAt) {
    this.createdAt = createdAt;
    return this;
  }

  /**
   * Get createdAt
   * @return createdAt
   */
  @javax.annotation.Nullable
  public String getCreatedAt() {
    return createdAt;
  }

  public void setCreatedAt(String createdAt) {
    this.createdAt = createdAt;
  }


  public GetManyPlans200ResponseResultInner currency(String currency) {
    this.currency = currency;
    return this;
  }

  /**
   * Get currency
   * @return currency
   */
  @javax.annotation.Nullable
  public String getCurrency() {
    return currency;
  }

  public void setCurrency(String currency) {
    this.currency = currency;
  }


  public GetManyPlans200ResponseResultInner id(String id) {
    this.id = id;
    return this;
  }

  /**
   * Get id
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }


  public GetManyPlans200ResponseResultInner intervalDay(String intervalDay) {
    this.intervalDay = intervalDay;
    return this;
  }

  /**
   * Get intervalDay
   * @return intervalDay
   */
  @javax.annotation.Nullable
  public String getIntervalDay() {
    return intervalDay;
  }

  public void setIntervalDay(String intervalDay) {
    this.intervalDay = intervalDay;
  }


  public GetManyPlans200ResponseResultInner ipnCallbackUrl(Object ipnCallbackUrl) {
    this.ipnCallbackUrl = ipnCallbackUrl;
    return this;
  }

  /**
   * Get ipnCallbackUrl
   * @return ipnCallbackUrl
   */
  @javax.annotation.Nullable
  public Object getIpnCallbackUrl() {
    return ipnCallbackUrl;
  }

  public void setIpnCallbackUrl(Object ipnCallbackUrl) {
    this.ipnCallbackUrl = ipnCallbackUrl;
  }


  public GetManyPlans200ResponseResultInner partiallyPaidUrl(Object partiallyPaidUrl) {
    this.partiallyPaidUrl = partiallyPaidUrl;
    return this;
  }

  /**
   * Get partiallyPaidUrl
   * @return partiallyPaidUrl
   */
  @javax.annotation.Nullable
  public Object getPartiallyPaidUrl() {
    return partiallyPaidUrl;
  }

  public void setPartiallyPaidUrl(Object partiallyPaidUrl) {
    this.partiallyPaidUrl = partiallyPaidUrl;
  }


  public GetManyPlans200ResponseResultInner successUrl(Object successUrl) {
    this.successUrl = successUrl;
    return this;
  }

  /**
   * Get successUrl
   * @return successUrl
   */
  @javax.annotation.Nullable
  public Object getSuccessUrl() {
    return successUrl;
  }

  public void setSuccessUrl(Object successUrl) {
    this.successUrl = successUrl;
  }


  public GetManyPlans200ResponseResultInner title(String title) {
    this.title = title;
    return this;
  }

  /**
   * Get title
   * @return title
   */
  @javax.annotation.Nullable
  public String getTitle() {
    return title;
  }

  public void setTitle(String title) {
    this.title = title;
  }


  public GetManyPlans200ResponseResultInner updatedAt(String updatedAt) {
    this.updatedAt = updatedAt;
    return this;
  }

  /**
   * Get updatedAt
   * @return updatedAt
   */
  @javax.annotation.Nullable
  public String getUpdatedAt() {
    return updatedAt;
  }

  public void setUpdatedAt(String updatedAt) {
    this.updatedAt = updatedAt;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetManyPlans200ResponseResultInner getManyPlans200ResponseResultInner = (GetManyPlans200ResponseResultInner) o;
    return Objects.equals(this.amount, getManyPlans200ResponseResultInner.amount) &&
        Objects.equals(this.cancelUrl, getManyPlans200ResponseResultInner.cancelUrl) &&
        Objects.equals(this.createdAt, getManyPlans200ResponseResultInner.createdAt) &&
        Objects.equals(this.currency, getManyPlans200ResponseResultInner.currency) &&
        Objects.equals(this.id, getManyPlans200ResponseResultInner.id) &&
        Objects.equals(this.intervalDay, getManyPlans200ResponseResultInner.intervalDay) &&
        Objects.equals(this.ipnCallbackUrl, getManyPlans200ResponseResultInner.ipnCallbackUrl) &&
        Objects.equals(this.partiallyPaidUrl, getManyPlans200ResponseResultInner.partiallyPaidUrl) &&
        Objects.equals(this.successUrl, getManyPlans200ResponseResultInner.successUrl) &&
        Objects.equals(this.title, getManyPlans200ResponseResultInner.title) &&
        Objects.equals(this.updatedAt, getManyPlans200ResponseResultInner.updatedAt);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(amount, cancelUrl, createdAt, currency, id, intervalDay, ipnCallbackUrl, partiallyPaidUrl, successUrl, title, updatedAt);
  }

  private static <T> int hashCodeNullable(JsonNullable<T> a) {
    if (a == null) {
      return 1;
    }
    return a.isPresent() ? Arrays.deepHashCode(new Object[]{a.get()}) : 31;
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetManyPlans200ResponseResultInner {\n");
    sb.append("    amount: ").append(toIndentedString(amount)).append("\n");
    sb.append("    cancelUrl: ").append(toIndentedString(cancelUrl)).append("\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    currency: ").append(toIndentedString(currency)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    intervalDay: ").append(toIndentedString(intervalDay)).append("\n");
    sb.append("    ipnCallbackUrl: ").append(toIndentedString(ipnCallbackUrl)).append("\n");
    sb.append("    partiallyPaidUrl: ").append(toIndentedString(partiallyPaidUrl)).append("\n");
    sb.append("    successUrl: ").append(toIndentedString(successUrl)).append("\n");
    sb.append("    title: ").append(toIndentedString(title)).append("\n");
    sb.append("    updatedAt: ").append(toIndentedString(updatedAt)).append("\n");
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
    openapiFields.add("amount");
    openapiFields.add("cancel_url");
    openapiFields.add("created_at");
    openapiFields.add("currency");
    openapiFields.add("id");
    openapiFields.add("interval_day");
    openapiFields.add("ipn_callback_url");
    openapiFields.add("partially_paid_url");
    openapiFields.add("success_url");
    openapiFields.add("title");
    openapiFields.add("updated_at");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetManyPlans200ResponseResultInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetManyPlans200ResponseResultInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetManyPlans200ResponseResultInner is not found in the empty JSON string", GetManyPlans200ResponseResultInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetManyPlans200ResponseResultInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetManyPlans200ResponseResultInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("created_at") != null && !jsonObj.get("created_at").isJsonNull()) && !jsonObj.get("created_at").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `created_at` to be a primitive type in the JSON string but got `%s`", jsonObj.get("created_at").toString()));
      }
      if ((jsonObj.get("currency") != null && !jsonObj.get("currency").isJsonNull()) && !jsonObj.get("currency").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `currency` to be a primitive type in the JSON string but got `%s`", jsonObj.get("currency").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("interval_day") != null && !jsonObj.get("interval_day").isJsonNull()) && !jsonObj.get("interval_day").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `interval_day` to be a primitive type in the JSON string but got `%s`", jsonObj.get("interval_day").toString()));
      }
      if ((jsonObj.get("title") != null && !jsonObj.get("title").isJsonNull()) && !jsonObj.get("title").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `title` to be a primitive type in the JSON string but got `%s`", jsonObj.get("title").toString()));
      }
      if ((jsonObj.get("updated_at") != null && !jsonObj.get("updated_at").isJsonNull()) && !jsonObj.get("updated_at").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `updated_at` to be a primitive type in the JSON string but got `%s`", jsonObj.get("updated_at").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetManyPlans200ResponseResultInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetManyPlans200ResponseResultInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetManyPlans200ResponseResultInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetManyPlans200ResponseResultInner.class));

       return (TypeAdapter<T>) new TypeAdapter<GetManyPlans200ResponseResultInner>() {
           @Override
           public void write(JsonWriter out, GetManyPlans200ResponseResultInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetManyPlans200ResponseResultInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetManyPlans200ResponseResultInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetManyPlans200ResponseResultInner
   * @throws IOException if the JSON string is invalid with respect to GetManyPlans200ResponseResultInner
   */
  public static GetManyPlans200ResponseResultInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetManyPlans200ResponseResultInner.class);
  }

  /**
   * Convert an instance of GetManyPlans200ResponseResultInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

