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
 * GetListOfPayments200ResponseDataInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:30:50.751981-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetListOfPayments200ResponseDataInner {
  public static final String SERIALIZED_NAME_ACTUALLY_PAID = "actually_paid";
  @SerializedName(SERIALIZED_NAME_ACTUALLY_PAID)
  private BigDecimal actuallyPaid;

  public static final String SERIALIZED_NAME_ORDER_DESCRIPTION = "order_description";
  @SerializedName(SERIALIZED_NAME_ORDER_DESCRIPTION)
  private String orderDescription;

  public static final String SERIALIZED_NAME_ORDER_ID = "order_id";
  @SerializedName(SERIALIZED_NAME_ORDER_ID)
  private String orderId;

  public static final String SERIALIZED_NAME_OUTCOME_AMOUNT = "outcome_amount";
  @SerializedName(SERIALIZED_NAME_OUTCOME_AMOUNT)
  private BigDecimal outcomeAmount;

  public static final String SERIALIZED_NAME_OUTCOME_CURRENCY = "outcome_currency";
  @SerializedName(SERIALIZED_NAME_OUTCOME_CURRENCY)
  private String outcomeCurrency;

  public static final String SERIALIZED_NAME_PAY_ADDRESS = "pay_address";
  @SerializedName(SERIALIZED_NAME_PAY_ADDRESS)
  private String payAddress;

  public static final String SERIALIZED_NAME_PAY_AMOUNT = "pay_amount";
  @SerializedName(SERIALIZED_NAME_PAY_AMOUNT)
  private BigDecimal payAmount;

  public static final String SERIALIZED_NAME_PAY_CURRENCY = "pay_currency";
  @SerializedName(SERIALIZED_NAME_PAY_CURRENCY)
  private String payCurrency;

  public static final String SERIALIZED_NAME_PAYMENT_ID = "payment_id";
  @SerializedName(SERIALIZED_NAME_PAYMENT_ID)
  private BigDecimal paymentId;

  public static final String SERIALIZED_NAME_PAYMENT_STATUS = "payment_status";
  @SerializedName(SERIALIZED_NAME_PAYMENT_STATUS)
  private String paymentStatus;

  public static final String SERIALIZED_NAME_PRICE_AMOUNT = "price_amount";
  @SerializedName(SERIALIZED_NAME_PRICE_AMOUNT)
  private BigDecimal priceAmount;

  public static final String SERIALIZED_NAME_PRICE_CURRENCY = "price_currency";
  @SerializedName(SERIALIZED_NAME_PRICE_CURRENCY)
  private String priceCurrency;

  public static final String SERIALIZED_NAME_PURCHASE_ID = "purchase_id";
  @SerializedName(SERIALIZED_NAME_PURCHASE_ID)
  private String purchaseId;

  public GetListOfPayments200ResponseDataInner() {
  }

  public GetListOfPayments200ResponseDataInner actuallyPaid(BigDecimal actuallyPaid) {
    this.actuallyPaid = actuallyPaid;
    return this;
  }

  /**
   * Get actuallyPaid
   * @return actuallyPaid
   */
  @javax.annotation.Nullable
  public BigDecimal getActuallyPaid() {
    return actuallyPaid;
  }

  public void setActuallyPaid(BigDecimal actuallyPaid) {
    this.actuallyPaid = actuallyPaid;
  }


  public GetListOfPayments200ResponseDataInner orderDescription(String orderDescription) {
    this.orderDescription = orderDescription;
    return this;
  }

  /**
   * Get orderDescription
   * @return orderDescription
   */
  @javax.annotation.Nullable
  public String getOrderDescription() {
    return orderDescription;
  }

  public void setOrderDescription(String orderDescription) {
    this.orderDescription = orderDescription;
  }


  public GetListOfPayments200ResponseDataInner orderId(String orderId) {
    this.orderId = orderId;
    return this;
  }

  /**
   * Get orderId
   * @return orderId
   */
  @javax.annotation.Nullable
  public String getOrderId() {
    return orderId;
  }

  public void setOrderId(String orderId) {
    this.orderId = orderId;
  }


  public GetListOfPayments200ResponseDataInner outcomeAmount(BigDecimal outcomeAmount) {
    this.outcomeAmount = outcomeAmount;
    return this;
  }

  /**
   * Get outcomeAmount
   * @return outcomeAmount
   */
  @javax.annotation.Nullable
  public BigDecimal getOutcomeAmount() {
    return outcomeAmount;
  }

  public void setOutcomeAmount(BigDecimal outcomeAmount) {
    this.outcomeAmount = outcomeAmount;
  }


  public GetListOfPayments200ResponseDataInner outcomeCurrency(String outcomeCurrency) {
    this.outcomeCurrency = outcomeCurrency;
    return this;
  }

  /**
   * Get outcomeCurrency
   * @return outcomeCurrency
   */
  @javax.annotation.Nullable
  public String getOutcomeCurrency() {
    return outcomeCurrency;
  }

  public void setOutcomeCurrency(String outcomeCurrency) {
    this.outcomeCurrency = outcomeCurrency;
  }


  public GetListOfPayments200ResponseDataInner payAddress(String payAddress) {
    this.payAddress = payAddress;
    return this;
  }

  /**
   * Get payAddress
   * @return payAddress
   */
  @javax.annotation.Nullable
  public String getPayAddress() {
    return payAddress;
  }

  public void setPayAddress(String payAddress) {
    this.payAddress = payAddress;
  }


  public GetListOfPayments200ResponseDataInner payAmount(BigDecimal payAmount) {
    this.payAmount = payAmount;
    return this;
  }

  /**
   * Get payAmount
   * @return payAmount
   */
  @javax.annotation.Nullable
  public BigDecimal getPayAmount() {
    return payAmount;
  }

  public void setPayAmount(BigDecimal payAmount) {
    this.payAmount = payAmount;
  }


  public GetListOfPayments200ResponseDataInner payCurrency(String payCurrency) {
    this.payCurrency = payCurrency;
    return this;
  }

  /**
   * Get payCurrency
   * @return payCurrency
   */
  @javax.annotation.Nullable
  public String getPayCurrency() {
    return payCurrency;
  }

  public void setPayCurrency(String payCurrency) {
    this.payCurrency = payCurrency;
  }


  public GetListOfPayments200ResponseDataInner paymentId(BigDecimal paymentId) {
    this.paymentId = paymentId;
    return this;
  }

  /**
   * Get paymentId
   * @return paymentId
   */
  @javax.annotation.Nullable
  public BigDecimal getPaymentId() {
    return paymentId;
  }

  public void setPaymentId(BigDecimal paymentId) {
    this.paymentId = paymentId;
  }


  public GetListOfPayments200ResponseDataInner paymentStatus(String paymentStatus) {
    this.paymentStatus = paymentStatus;
    return this;
  }

  /**
   * Get paymentStatus
   * @return paymentStatus
   */
  @javax.annotation.Nullable
  public String getPaymentStatus() {
    return paymentStatus;
  }

  public void setPaymentStatus(String paymentStatus) {
    this.paymentStatus = paymentStatus;
  }


  public GetListOfPayments200ResponseDataInner priceAmount(BigDecimal priceAmount) {
    this.priceAmount = priceAmount;
    return this;
  }

  /**
   * Get priceAmount
   * @return priceAmount
   */
  @javax.annotation.Nullable
  public BigDecimal getPriceAmount() {
    return priceAmount;
  }

  public void setPriceAmount(BigDecimal priceAmount) {
    this.priceAmount = priceAmount;
  }


  public GetListOfPayments200ResponseDataInner priceCurrency(String priceCurrency) {
    this.priceCurrency = priceCurrency;
    return this;
  }

  /**
   * Get priceCurrency
   * @return priceCurrency
   */
  @javax.annotation.Nullable
  public String getPriceCurrency() {
    return priceCurrency;
  }

  public void setPriceCurrency(String priceCurrency) {
    this.priceCurrency = priceCurrency;
  }


  public GetListOfPayments200ResponseDataInner purchaseId(String purchaseId) {
    this.purchaseId = purchaseId;
    return this;
  }

  /**
   * Get purchaseId
   * @return purchaseId
   */
  @javax.annotation.Nullable
  public String getPurchaseId() {
    return purchaseId;
  }

  public void setPurchaseId(String purchaseId) {
    this.purchaseId = purchaseId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetListOfPayments200ResponseDataInner getListOfPayments200ResponseDataInner = (GetListOfPayments200ResponseDataInner) o;
    return Objects.equals(this.actuallyPaid, getListOfPayments200ResponseDataInner.actuallyPaid) &&
        Objects.equals(this.orderDescription, getListOfPayments200ResponseDataInner.orderDescription) &&
        Objects.equals(this.orderId, getListOfPayments200ResponseDataInner.orderId) &&
        Objects.equals(this.outcomeAmount, getListOfPayments200ResponseDataInner.outcomeAmount) &&
        Objects.equals(this.outcomeCurrency, getListOfPayments200ResponseDataInner.outcomeCurrency) &&
        Objects.equals(this.payAddress, getListOfPayments200ResponseDataInner.payAddress) &&
        Objects.equals(this.payAmount, getListOfPayments200ResponseDataInner.payAmount) &&
        Objects.equals(this.payCurrency, getListOfPayments200ResponseDataInner.payCurrency) &&
        Objects.equals(this.paymentId, getListOfPayments200ResponseDataInner.paymentId) &&
        Objects.equals(this.paymentStatus, getListOfPayments200ResponseDataInner.paymentStatus) &&
        Objects.equals(this.priceAmount, getListOfPayments200ResponseDataInner.priceAmount) &&
        Objects.equals(this.priceCurrency, getListOfPayments200ResponseDataInner.priceCurrency) &&
        Objects.equals(this.purchaseId, getListOfPayments200ResponseDataInner.purchaseId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(actuallyPaid, orderDescription, orderId, outcomeAmount, outcomeCurrency, payAddress, payAmount, payCurrency, paymentId, paymentStatus, priceAmount, priceCurrency, purchaseId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetListOfPayments200ResponseDataInner {\n");
    sb.append("    actuallyPaid: ").append(toIndentedString(actuallyPaid)).append("\n");
    sb.append("    orderDescription: ").append(toIndentedString(orderDescription)).append("\n");
    sb.append("    orderId: ").append(toIndentedString(orderId)).append("\n");
    sb.append("    outcomeAmount: ").append(toIndentedString(outcomeAmount)).append("\n");
    sb.append("    outcomeCurrency: ").append(toIndentedString(outcomeCurrency)).append("\n");
    sb.append("    payAddress: ").append(toIndentedString(payAddress)).append("\n");
    sb.append("    payAmount: ").append(toIndentedString(payAmount)).append("\n");
    sb.append("    payCurrency: ").append(toIndentedString(payCurrency)).append("\n");
    sb.append("    paymentId: ").append(toIndentedString(paymentId)).append("\n");
    sb.append("    paymentStatus: ").append(toIndentedString(paymentStatus)).append("\n");
    sb.append("    priceAmount: ").append(toIndentedString(priceAmount)).append("\n");
    sb.append("    priceCurrency: ").append(toIndentedString(priceCurrency)).append("\n");
    sb.append("    purchaseId: ").append(toIndentedString(purchaseId)).append("\n");
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
    openapiFields.add("actually_paid");
    openapiFields.add("order_description");
    openapiFields.add("order_id");
    openapiFields.add("outcome_amount");
    openapiFields.add("outcome_currency");
    openapiFields.add("pay_address");
    openapiFields.add("pay_amount");
    openapiFields.add("pay_currency");
    openapiFields.add("payment_id");
    openapiFields.add("payment_status");
    openapiFields.add("price_amount");
    openapiFields.add("price_currency");
    openapiFields.add("purchase_id");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetListOfPayments200ResponseDataInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetListOfPayments200ResponseDataInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetListOfPayments200ResponseDataInner is not found in the empty JSON string", GetListOfPayments200ResponseDataInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetListOfPayments200ResponseDataInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetListOfPayments200ResponseDataInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("order_description") != null && !jsonObj.get("order_description").isJsonNull()) && !jsonObj.get("order_description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `order_description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("order_description").toString()));
      }
      if ((jsonObj.get("order_id") != null && !jsonObj.get("order_id").isJsonNull()) && !jsonObj.get("order_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `order_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("order_id").toString()));
      }
      if ((jsonObj.get("outcome_currency") != null && !jsonObj.get("outcome_currency").isJsonNull()) && !jsonObj.get("outcome_currency").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `outcome_currency` to be a primitive type in the JSON string but got `%s`", jsonObj.get("outcome_currency").toString()));
      }
      if ((jsonObj.get("pay_address") != null && !jsonObj.get("pay_address").isJsonNull()) && !jsonObj.get("pay_address").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `pay_address` to be a primitive type in the JSON string but got `%s`", jsonObj.get("pay_address").toString()));
      }
      if ((jsonObj.get("pay_currency") != null && !jsonObj.get("pay_currency").isJsonNull()) && !jsonObj.get("pay_currency").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `pay_currency` to be a primitive type in the JSON string but got `%s`", jsonObj.get("pay_currency").toString()));
      }
      if ((jsonObj.get("payment_status") != null && !jsonObj.get("payment_status").isJsonNull()) && !jsonObj.get("payment_status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `payment_status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("payment_status").toString()));
      }
      if ((jsonObj.get("price_currency") != null && !jsonObj.get("price_currency").isJsonNull()) && !jsonObj.get("price_currency").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `price_currency` to be a primitive type in the JSON string but got `%s`", jsonObj.get("price_currency").toString()));
      }
      if ((jsonObj.get("purchase_id") != null && !jsonObj.get("purchase_id").isJsonNull()) && !jsonObj.get("purchase_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `purchase_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("purchase_id").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetListOfPayments200ResponseDataInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetListOfPayments200ResponseDataInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetListOfPayments200ResponseDataInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetListOfPayments200ResponseDataInner.class));

       return (TypeAdapter<T>) new TypeAdapter<GetListOfPayments200ResponseDataInner>() {
           @Override
           public void write(JsonWriter out, GetListOfPayments200ResponseDataInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetListOfPayments200ResponseDataInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetListOfPayments200ResponseDataInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetListOfPayments200ResponseDataInner
   * @throws IOException if the JSON string is invalid with respect to GetListOfPayments200ResponseDataInner
   */
  public static GetListOfPayments200ResponseDataInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetListOfPayments200ResponseDataInner.class);
  }

  /**
   * Convert an instance of GetListOfPayments200ResponseDataInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

