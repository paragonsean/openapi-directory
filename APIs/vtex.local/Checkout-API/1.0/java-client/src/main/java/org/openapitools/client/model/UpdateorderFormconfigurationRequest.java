/*
 * Checkout API
 * >ℹ️ Check the new [Checkout onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/checkout-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about the Checkout and is organized by focusing on the developer's journey.    The Checkout API allows you to obtain and configure information about the shopping cart and its attachments, personalization of custom fields, orderForm structure, fulfillment data, order management, and identification of the sellers delivery region.    >ℹ️ Data modification operations (`POST`, `PATCH`, `PUT` or `DELETE` endpoints) shall not be performed in parallel in the Checkout APIs. They need to be enqueued by the client/requester. Otherwise, old values ​​can be overwritten incorrectly or competition errors may occur.    >⚠️ All endpoints that consult or edit the orderForm can change the authentication depending on the customer context. If you are handling information from a customer with a complete profile on the store, authentication will be required. You can only access or modify the customer data for these profiles with an authenticated request.    ## Shopping cart    Allows merchants to simulate, configure and customize shopping cart information.    - [POST - Cart Simulation](https://developers.vtex.com/vtex-rest-api/reference/cartsimulation)  - [GET - Get current or create a new cart](https://developers.vtex.com/vtex-rest-api/reference/createanewcart)  - [GET - Get cart information by ID](https://developers.vtex.com/vtex-rest-api/reference/getcartinformationbyid)  - [POST - Remove all items](https://developers.vtex.com/vtex-rest-api/reference/removeallitems)  - [GET - Remove all personal data](https://developers.vtex.com/vtex-rest-api/reference/removeallpersonaldata)  - [POST - Update cart items](https://developers.vtex.com/vtex-rest-api/reference/itemsupdate)  - [POST - Add cart items](https://developers.vtex.com/vtex-rest-api/reference/items)  - [PUT - Change price](https://developers.vtex.com/vtex-rest-api/reference/pricechange)  - [PATCH - Ignore profile data](https://developers.vtex.com/vtex-rest-api/reference/ignoreprofiledata)  - [GET - Cart installments](https://developers.vtex.com/vtex-rest-api/reference/getcartinstallments)  - [POST - Add coupons to the cart](https://developers.vtex.com/vtex-rest-api/reference/addcoupons)      ## Cart attachments    Allows merchants to obtain client profiles and add information to a given shopping cart.    - [GET - Get client profile by email](https://developers.vtex.com/vtex-rest-api/reference/getclientprofilebyemail)  - [POST - Add client profile](https://developers.vtex.com/vtex-rest-api/reference/addclientprofile)  - [POST - Add shipping address and select delivery option](https://developers.vtex.com/vtex-rest-api/reference/addshippingaddress)  - [POST - Add client preferences](https://developers.vtex.com/vtex-rest-api/reference/addclientpreferences)  - [POST - Add marketing data](https://developers.vtex.com/vtex-rest-api/reference/addmarketingdata)  - [POST - Add payment data](https://developers.vtex.com/vtex-rest-api/reference/addpaymentdata)  - [POST - Add merchant context data](https://developers.vtex.com/vtex-rest-api/reference/addmerchantcontextdata)      ## Custom data    Allows merchants to manage custom fields that were created by an app in their account.    - [PUT - Set multiple custom field values](https://developers.vtex.com/vtex-rest-api/reference/setmultiplecustomfieldvalues)  - [PUT - Set single custom field value](https://developers.vtex.com/vtex-rest-api/reference/setsinglecustomfieldvalue)  - [DELETE - Remove single custom field value](https://developers.vtex.com/vtex-rest-api/reference/removesinglecustomfieldvalue)      ## Configuration    Allows merchants to configure orderForm in the account and seller exchange on a given order.    - [GET - Get orderForm configuration](https://developers.vtex.com/vtex-rest-api/reference/getorderformconfiguration)  - [POST - Update orderForm configuration](https://developers.vtex.com/vtex-rest-api/reference/updateorderformconfiguration)  - [GET - Get window to change seller](https://developers.vtex.com/vtex-rest-api/reference/getwindowtochangeseller)  - [POST - Update window to change seller](https://developers.vtex.com/vtex-rest-api/reference/updatewindowtochangeseller)  - [POST - Clear orderForm messages](https://developers.vtex.com/vtex-rest-api/reference/clearorderformmessages)      ## Fulfillment    Allows merchants to obtain pickup points and address information.    - [GET - List pickup points by location](https://developers.vtex.com/vtex-rest-api/reference/listpickupppointsbylocation)  - [GET - Get address by postal code](https://developers.vtex.com/vtex-rest-api/reference/getaddressbypostalcode)      ## Order placement    Allows merchants to place and process orders by creating a new cart or using an existing cart.    - [POST - Place order from an existing cart](https://developers.vtex.com/vtex-rest-api/reference/placeorderfromexistingorderform)  - [PUT - Place order](https://developers.vtex.com/vtex-rest-api/reference/placeorder)  - [POST - Process order](https://developers.vtex.com/vtex-rest-api/reference/processorder)      ## Region    Allows merchants to obtain a list of sellers serving a specific delivery region.    - [GET - Get sellers by region or address](https://developers.vtex.com/vtex-rest-api/reference/getsellersbyregion)
 *
 * The version of the OpenAPI document: 1.0
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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.PaymentConfiguration;
import org.openapitools.client.model.UpdateorderFormconfigurationRequestAppsInner;
import org.openapitools.client.model.UpdateorderFormconfigurationRequestTaxConfiguration;

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
 * UpdateorderFormconfigurationRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:55:50.715443-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class UpdateorderFormconfigurationRequest {
  public static final String SERIALIZED_NAME_ALLOW_MANUAL_PRICE = "allowManualPrice";
  @SerializedName(SERIALIZED_NAME_ALLOW_MANUAL_PRICE)
  private Boolean allowManualPrice;

  public static final String SERIALIZED_NAME_ALLOW_MULTIPLE_DELIVERIES = "allowMultipleDeliveries";
  @SerializedName(SERIALIZED_NAME_ALLOW_MULTIPLE_DELIVERIES)
  private Boolean allowMultipleDeliveries;

  public static final String SERIALIZED_NAME_APPS = "apps";
  @SerializedName(SERIALIZED_NAME_APPS)
  private List<UpdateorderFormconfigurationRequestAppsInner> apps;

  public static final String SERIALIZED_NAME_DECIMAL_DIGITS_PRECISION = "decimalDigitsPrecision";
  @SerializedName(SERIALIZED_NAME_DECIMAL_DIGITS_PRECISION)
  private Integer decimalDigitsPrecision;

  public static final String SERIALIZED_NAME_MASK_FIRST_PURCHASE_DATA = "maskFirstPurchaseData";
  @SerializedName(SERIALIZED_NAME_MASK_FIRST_PURCHASE_DATA)
  private Boolean maskFirstPurchaseData;

  public static final String SERIALIZED_NAME_MAX_NUMBER_OF_WHITE_LABEL_SELLERS = "maxNumberOfWhiteLabelSellers";
  @SerializedName(SERIALIZED_NAME_MAX_NUMBER_OF_WHITE_LABEL_SELLERS)
  private Integer maxNumberOfWhiteLabelSellers;

  public static final String SERIALIZED_NAME_MINIMUM_QUANTITY_ACCUMULATED_FOR_ITEMS = "minimumQuantityAccumulatedForItems";
  @SerializedName(SERIALIZED_NAME_MINIMUM_QUANTITY_ACCUMULATED_FOR_ITEMS)
  private Integer minimumQuantityAccumulatedForItems;

  public static final String SERIALIZED_NAME_MINIMUM_VALUE_ACCUMULATED = "minimumValueAccumulated";
  @SerializedName(SERIALIZED_NAME_MINIMUM_VALUE_ACCUMULATED)
  private Integer minimumValueAccumulated;

  public static final String SERIALIZED_NAME_PAYMENT_CONFIGURATION = "paymentConfiguration";
  @SerializedName(SERIALIZED_NAME_PAYMENT_CONFIGURATION)
  private PaymentConfiguration paymentConfiguration;

  public static final String SERIALIZED_NAME_PAYMENT_SYSTEM_TO_CHECK_FIRST_INSTALLMENT = "paymentSystemToCheckFirstInstallment";
  @SerializedName(SERIALIZED_NAME_PAYMENT_SYSTEM_TO_CHECK_FIRST_INSTALLMENT)
  private String paymentSystemToCheckFirstInstallment;

  public static final String SERIALIZED_NAME_RECAPTCHA_VALIDATION = "recaptchaValidation";
  @SerializedName(SERIALIZED_NAME_RECAPTCHA_VALIDATION)
  private String recaptchaValidation = "vtexCriteria";

  public static final String SERIALIZED_NAME_TAX_CONFIGURATION = "taxConfiguration";
  @SerializedName(SERIALIZED_NAME_TAX_CONFIGURATION)
  private UpdateorderFormconfigurationRequestTaxConfiguration taxConfiguration;

  public UpdateorderFormconfigurationRequest() {
  }

  public UpdateorderFormconfigurationRequest allowManualPrice(Boolean allowManualPrice) {
    this.allowManualPrice = allowManualPrice;
    return this;
  }

  /**
   * Allows the editing of SKU prices right in the cart.
   * @return allowManualPrice
   */
  @javax.annotation.Nullable
  public Boolean getAllowManualPrice() {
    return allowManualPrice;
  }

  public void setAllowManualPrice(Boolean allowManualPrice) {
    this.allowManualPrice = allowManualPrice;
  }


  public UpdateorderFormconfigurationRequest allowMultipleDeliveries(Boolean allowMultipleDeliveries) {
    this.allowMultipleDeliveries = allowMultipleDeliveries;
    return this;
  }

  /**
   * On the same purchase, allows the selection of items from multiple delivery channels.
   * @return allowMultipleDeliveries
   */
  @javax.annotation.Nullable
  public Boolean getAllowMultipleDeliveries() {
    return allowMultipleDeliveries;
  }

  public void setAllowMultipleDeliveries(Boolean allowMultipleDeliveries) {
    this.allowMultipleDeliveries = allowMultipleDeliveries;
  }


  public UpdateorderFormconfigurationRequest apps(List<UpdateorderFormconfigurationRequestAppsInner> apps) {
    this.apps = apps;
    return this;
  }

  public UpdateorderFormconfigurationRequest addAppsItem(UpdateorderFormconfigurationRequestAppsInner appsItem) {
    if (this.apps == null) {
      this.apps = new ArrayList<>();
    }
    this.apps.add(appsItem);
    return this;
  }

  /**
   * Array of objects containing Apps configuration information.
   * @return apps
   */
  @javax.annotation.Nullable
  public List<UpdateorderFormconfigurationRequestAppsInner> getApps() {
    return apps;
  }

  public void setApps(List<UpdateorderFormconfigurationRequestAppsInner> apps) {
    this.apps = apps;
  }


  public UpdateorderFormconfigurationRequest decimalDigitsPrecision(Integer decimalDigitsPrecision) {
    this.decimalDigitsPrecision = decimalDigitsPrecision;
    return this;
  }

  /**
   * Number of price digits.
   * @return decimalDigitsPrecision
   */
  @javax.annotation.Nonnull
  public Integer getDecimalDigitsPrecision() {
    return decimalDigitsPrecision;
  }

  public void setDecimalDigitsPrecision(Integer decimalDigitsPrecision) {
    this.decimalDigitsPrecision = decimalDigitsPrecision;
  }


  public UpdateorderFormconfigurationRequest maskFirstPurchaseData(Boolean maskFirstPurchaseData) {
    this.maskFirstPurchaseData = maskFirstPurchaseData;
    return this;
  }

  /**
   * Allows, on a first purchase, masking client&#39;s data. It could be useful when a shared cart is used and the client doesn&#39;t want to share its data.
   * @return maskFirstPurchaseData
   */
  @javax.annotation.Nullable
  public Boolean getMaskFirstPurchaseData() {
    return maskFirstPurchaseData;
  }

  public void setMaskFirstPurchaseData(Boolean maskFirstPurchaseData) {
    this.maskFirstPurchaseData = maskFirstPurchaseData;
  }


  public UpdateorderFormconfigurationRequest maxNumberOfWhiteLabelSellers(Integer maxNumberOfWhiteLabelSellers) {
    this.maxNumberOfWhiteLabelSellers = maxNumberOfWhiteLabelSellers;
    return this;
  }

  /**
   * Allows the input of a limit of white label sellers involved on the cart.
   * @return maxNumberOfWhiteLabelSellers
   */
  @javax.annotation.Nullable
  public Integer getMaxNumberOfWhiteLabelSellers() {
    return maxNumberOfWhiteLabelSellers;
  }

  public void setMaxNumberOfWhiteLabelSellers(Integer maxNumberOfWhiteLabelSellers) {
    this.maxNumberOfWhiteLabelSellers = maxNumberOfWhiteLabelSellers;
  }


  public UpdateorderFormconfigurationRequest minimumQuantityAccumulatedForItems(Integer minimumQuantityAccumulatedForItems) {
    this.minimumQuantityAccumulatedForItems = minimumQuantityAccumulatedForItems;
    return this;
  }

  /**
   * Minimum SKU quantity by cart.
   * @return minimumQuantityAccumulatedForItems
   */
  @javax.annotation.Nonnull
  public Integer getMinimumQuantityAccumulatedForItems() {
    return minimumQuantityAccumulatedForItems;
  }

  public void setMinimumQuantityAccumulatedForItems(Integer minimumQuantityAccumulatedForItems) {
    this.minimumQuantityAccumulatedForItems = minimumQuantityAccumulatedForItems;
  }


  public UpdateorderFormconfigurationRequest minimumValueAccumulated(Integer minimumValueAccumulated) {
    this.minimumValueAccumulated = minimumValueAccumulated;
    return this;
  }

  /**
   * Minimum cart value.
   * @return minimumValueAccumulated
   */
  @javax.annotation.Nullable
  public Integer getMinimumValueAccumulated() {
    return minimumValueAccumulated;
  }

  public void setMinimumValueAccumulated(Integer minimumValueAccumulated) {
    this.minimumValueAccumulated = minimumValueAccumulated;
  }


  public UpdateorderFormconfigurationRequest paymentConfiguration(PaymentConfiguration paymentConfiguration) {
    this.paymentConfiguration = paymentConfiguration;
    return this;
  }

  /**
   * Get paymentConfiguration
   * @return paymentConfiguration
   */
  @javax.annotation.Nonnull
  public PaymentConfiguration getPaymentConfiguration() {
    return paymentConfiguration;
  }

  public void setPaymentConfiguration(PaymentConfiguration paymentConfiguration) {
    this.paymentConfiguration = paymentConfiguration;
  }


  public UpdateorderFormconfigurationRequest paymentSystemToCheckFirstInstallment(String paymentSystemToCheckFirstInstallment) {
    this.paymentSystemToCheckFirstInstallment = paymentSystemToCheckFirstInstallment;
    return this;
  }

  /**
   * If you want to apply a first installment discount to a particular payment system, set this field to that payment system&#39;s ID. Learn more: [Configuring a discount for orders prepaid in full](https://help.vtex.com/en/tutorial/configurar-desconto-de-preco-a-vista--7Lfcj9Wb5dpYfA2gKkACIt).
   * @return paymentSystemToCheckFirstInstallment
   */
  @javax.annotation.Nullable
  public String getPaymentSystemToCheckFirstInstallment() {
    return paymentSystemToCheckFirstInstallment;
  }

  public void setPaymentSystemToCheckFirstInstallment(String paymentSystemToCheckFirstInstallment) {
    this.paymentSystemToCheckFirstInstallment = paymentSystemToCheckFirstInstallment;
  }


  public UpdateorderFormconfigurationRequest recaptchaValidation(String recaptchaValidation) {
    this.recaptchaValidation = recaptchaValidation;
    return this;
  }

  /**
   * Configures reCAPTCHA validation for the account, defining in which situations the shopper will be prompted to validate a purchase with reCAPTCHA. Learn more about [reCAPTCHA validation for VTEX stores](https://help.vtex.com/tutorial/recaptcha-no-checkout--18Te3oDd7f4qcjKu9jhNzP)    Possible values are:  - &#x60;\&quot;never\&quot;&#x60;: no purchases are validated with reCAPTCHA.  - &#x60;\&quot;always\&quot;&#x60;: every purchase is validated with reCAPTCHA.  - &#x60;\&quot;vtexCriteria\&quot;&#x60;: only some purchases are validated with reCAPTCHA in order to minimize friction and improve shopping experience. VTEX’s algorithm determines which sessions are trustworthy and which should be validated with reCAPTCHA. This is the recommended option.
   * @return recaptchaValidation
   */
  @javax.annotation.Nullable
  public String getRecaptchaValidation() {
    return recaptchaValidation;
  }

  public void setRecaptchaValidation(String recaptchaValidation) {
    this.recaptchaValidation = recaptchaValidation;
  }


  public UpdateorderFormconfigurationRequest taxConfiguration(UpdateorderFormconfigurationRequestTaxConfiguration taxConfiguration) {
    this.taxConfiguration = taxConfiguration;
    return this;
  }

  /**
   * Get taxConfiguration
   * @return taxConfiguration
   */
  @javax.annotation.Nullable
  public UpdateorderFormconfigurationRequestTaxConfiguration getTaxConfiguration() {
    return taxConfiguration;
  }

  public void setTaxConfiguration(UpdateorderFormconfigurationRequestTaxConfiguration taxConfiguration) {
    this.taxConfiguration = taxConfiguration;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    UpdateorderFormconfigurationRequest updateorderFormconfigurationRequest = (UpdateorderFormconfigurationRequest) o;
    return Objects.equals(this.allowManualPrice, updateorderFormconfigurationRequest.allowManualPrice) &&
        Objects.equals(this.allowMultipleDeliveries, updateorderFormconfigurationRequest.allowMultipleDeliveries) &&
        Objects.equals(this.apps, updateorderFormconfigurationRequest.apps) &&
        Objects.equals(this.decimalDigitsPrecision, updateorderFormconfigurationRequest.decimalDigitsPrecision) &&
        Objects.equals(this.maskFirstPurchaseData, updateorderFormconfigurationRequest.maskFirstPurchaseData) &&
        Objects.equals(this.maxNumberOfWhiteLabelSellers, updateorderFormconfigurationRequest.maxNumberOfWhiteLabelSellers) &&
        Objects.equals(this.minimumQuantityAccumulatedForItems, updateorderFormconfigurationRequest.minimumQuantityAccumulatedForItems) &&
        Objects.equals(this.minimumValueAccumulated, updateorderFormconfigurationRequest.minimumValueAccumulated) &&
        Objects.equals(this.paymentConfiguration, updateorderFormconfigurationRequest.paymentConfiguration) &&
        Objects.equals(this.paymentSystemToCheckFirstInstallment, updateorderFormconfigurationRequest.paymentSystemToCheckFirstInstallment) &&
        Objects.equals(this.recaptchaValidation, updateorderFormconfigurationRequest.recaptchaValidation) &&
        Objects.equals(this.taxConfiguration, updateorderFormconfigurationRequest.taxConfiguration);
  }

  @Override
  public int hashCode() {
    return Objects.hash(allowManualPrice, allowMultipleDeliveries, apps, decimalDigitsPrecision, maskFirstPurchaseData, maxNumberOfWhiteLabelSellers, minimumQuantityAccumulatedForItems, minimumValueAccumulated, paymentConfiguration, paymentSystemToCheckFirstInstallment, recaptchaValidation, taxConfiguration);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class UpdateorderFormconfigurationRequest {\n");
    sb.append("    allowManualPrice: ").append(toIndentedString(allowManualPrice)).append("\n");
    sb.append("    allowMultipleDeliveries: ").append(toIndentedString(allowMultipleDeliveries)).append("\n");
    sb.append("    apps: ").append(toIndentedString(apps)).append("\n");
    sb.append("    decimalDigitsPrecision: ").append(toIndentedString(decimalDigitsPrecision)).append("\n");
    sb.append("    maskFirstPurchaseData: ").append(toIndentedString(maskFirstPurchaseData)).append("\n");
    sb.append("    maxNumberOfWhiteLabelSellers: ").append(toIndentedString(maxNumberOfWhiteLabelSellers)).append("\n");
    sb.append("    minimumQuantityAccumulatedForItems: ").append(toIndentedString(minimumQuantityAccumulatedForItems)).append("\n");
    sb.append("    minimumValueAccumulated: ").append(toIndentedString(minimumValueAccumulated)).append("\n");
    sb.append("    paymentConfiguration: ").append(toIndentedString(paymentConfiguration)).append("\n");
    sb.append("    paymentSystemToCheckFirstInstallment: ").append(toIndentedString(paymentSystemToCheckFirstInstallment)).append("\n");
    sb.append("    recaptchaValidation: ").append(toIndentedString(recaptchaValidation)).append("\n");
    sb.append("    taxConfiguration: ").append(toIndentedString(taxConfiguration)).append("\n");
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
    openapiFields.add("allowManualPrice");
    openapiFields.add("allowMultipleDeliveries");
    openapiFields.add("apps");
    openapiFields.add("decimalDigitsPrecision");
    openapiFields.add("maskFirstPurchaseData");
    openapiFields.add("maxNumberOfWhiteLabelSellers");
    openapiFields.add("minimumQuantityAccumulatedForItems");
    openapiFields.add("minimumValueAccumulated");
    openapiFields.add("paymentConfiguration");
    openapiFields.add("paymentSystemToCheckFirstInstallment");
    openapiFields.add("recaptchaValidation");
    openapiFields.add("taxConfiguration");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("allowManualPrice");
    openapiRequiredFields.add("allowMultipleDeliveries");
    openapiRequiredFields.add("apps");
    openapiRequiredFields.add("decimalDigitsPrecision");
    openapiRequiredFields.add("minimumQuantityAccumulatedForItems");
    openapiRequiredFields.add("minimumValueAccumulated");
    openapiRequiredFields.add("paymentConfiguration");
    openapiRequiredFields.add("taxConfiguration");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to UpdateorderFormconfigurationRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!UpdateorderFormconfigurationRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in UpdateorderFormconfigurationRequest is not found in the empty JSON string", UpdateorderFormconfigurationRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!UpdateorderFormconfigurationRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `UpdateorderFormconfigurationRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : UpdateorderFormconfigurationRequest.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the json data is an array
      if (!jsonObj.get("apps").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `apps` to be an array in the JSON string but got `%s`", jsonObj.get("apps").toString()));
      }

      JsonArray jsonArrayapps = jsonObj.getAsJsonArray("apps");
      // validate the required field `apps` (array)
      for (int i = 0; i < jsonArrayapps.size(); i++) {
        UpdateorderFormconfigurationRequestAppsInner.validateJsonElement(jsonArrayapps.get(i));
      };
      // validate the required field `paymentConfiguration`
      PaymentConfiguration.validateJsonElement(jsonObj.get("paymentConfiguration"));
      if ((jsonObj.get("paymentSystemToCheckFirstInstallment") != null && !jsonObj.get("paymentSystemToCheckFirstInstallment").isJsonNull()) && !jsonObj.get("paymentSystemToCheckFirstInstallment").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `paymentSystemToCheckFirstInstallment` to be a primitive type in the JSON string but got `%s`", jsonObj.get("paymentSystemToCheckFirstInstallment").toString()));
      }
      if ((jsonObj.get("recaptchaValidation") != null && !jsonObj.get("recaptchaValidation").isJsonNull()) && !jsonObj.get("recaptchaValidation").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `recaptchaValidation` to be a primitive type in the JSON string but got `%s`", jsonObj.get("recaptchaValidation").toString()));
      }
      // validate the required field `taxConfiguration`
      UpdateorderFormconfigurationRequestTaxConfiguration.validateJsonElement(jsonObj.get("taxConfiguration"));
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!UpdateorderFormconfigurationRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'UpdateorderFormconfigurationRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<UpdateorderFormconfigurationRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(UpdateorderFormconfigurationRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<UpdateorderFormconfigurationRequest>() {
           @Override
           public void write(JsonWriter out, UpdateorderFormconfigurationRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public UpdateorderFormconfigurationRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of UpdateorderFormconfigurationRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of UpdateorderFormconfigurationRequest
   * @throws IOException if the JSON string is invalid with respect to UpdateorderFormconfigurationRequest
   */
  public static UpdateorderFormconfigurationRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, UpdateorderFormconfigurationRequest.class);
  }

  /**
   * Convert an instance of UpdateorderFormconfigurationRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

