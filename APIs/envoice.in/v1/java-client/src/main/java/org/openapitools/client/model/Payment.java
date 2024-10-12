/*
 * API v1.0.0
 * [![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/80638214aa04722c9203)  <span style='margin-left: 0.5em;'>or</span>  <a href='https://documenter.getpostman.com/view/3559821/TVeqcn2L' class='openapi-button' _ngcontent-c6>View Postman docs</a>    # Quickstart    Visit [github](https://github.com/EmitKnowledge/Envoice) to view the quickstart tutorial.    <div class='postman-tutorial'>    # Tutorial for running the API in postman    Click on \"\"Run in Postman\"\" button  <br /><br />  ![postman - tutorial - 1](/Assets/images/api/postman-tutorial/postman-tutorial-1.png)     ---     A new page will open.  Click the \"\"Postman for windows\"\" to run postman as a desktop app.  Make sure you have already [installed](https://www.getpostman.com/docs/postman/launching_postman/installation_and_updates) Postman.  <br /><br />  ![postman - tutorial - 2](/Assets/images/api/postman-tutorial/postman-tutorial-2.png)     ---     In chrome an alert might show up to set a default app for opening postman links. Click on \"\"Open Postman\"\".  <br /><br />  ![postman - tutorial - 3](/Assets/images/api/postman-tutorial/postman-tutorial-3.png)     ---     The OpenAPI specification will be imported in Postman as a new collection named \"\"Envoice api\"\"  <br /><br />  ![postman - tutorial - 4](/Assets/images/api/postman-tutorial/postman-tutorial-4.png)     ---     When testing be sure to check and modify the environment variables to suit your api key and secret. The domain is set to envoice's endpoint so you don't really need to change that.    <sub>\\*Eye button in top right corner </sub>  <br /><br />   ![postman - tutorial - 5](/Assets/images/api/postman-tutorial/postman-tutorial-5.png)  <br /><br />   ![postman - tutorial - 6](/Assets/images/api/postman-tutorial/postman-tutorial-6.png)     ---     You don't need to change the values of the header parameters, because they will be replaced automatically when you send a request with real values from the environment configured in the previous step.  <br /><br />  ![postman - tutorial - 7](/Assets/images/api/postman-tutorial/postman-tutorial-7.png)     ---     Modify the example data to suit your needs and send a request.  <br /><br />  ![postman - tutorial - 8](/Assets/images/api/postman-tutorial/postman-tutorial-8.png)  </div>    # Webhooks    Webhooks allow you to build or set up Envoice Apps which subscribe to invoice activities.   When one of those events is triggered, we'll send a HTTP POST payload to the webhook's configured URL.   Webhooks can be used to update an external invoice data storage.    In order to use webhooks visit [this link](/account/settings#api-tab) and add upto 10 webhook urls that will return status `200` in order to signal that the webhook is working.  All nonworking webhooks will be ignored after a certain period of time and several retry attempts.  If after several attempts the webhook starts to work, we will send you all activities, both past and present, in chronological order.    The payload of the webhook is in format:  ```  {      Signature: \"\"sha256 string\"\",      Timestamp: \"\"YYYY-MM-DDTHH:mm:ss.FFFFFFFZ\"\",      Activity: {          Message: \"string\",          Link: \"share url\",          Type: int,                  InvoiceNumber: \"string\",          InvoiceId: int,                  OrderNumber: \"string\",          OrderId: int,          Id: int,          CreatedOn: \"YYYY-MM-DDTHH:mm:ss.FFFFFFFZ\"      }  }  ```            
 *
 * The version of the OpenAPI document: v1
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
import java.time.OffsetDateTime;
import java.util.Arrays;
import org.openapitools.client.model.Invoice;

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
 * Payment
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:01:00.947845-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Payment {
  public static final String SERIALIZED_NAME_AMOUNT = "Amount";
  @SerializedName(SERIALIZED_NAME_AMOUNT)
  private Double amount;

  public static final String SERIALIZED_NAME_ID = "Id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_INVOICE = "Invoice";
  @SerializedName(SERIALIZED_NAME_INVOICE)
  private Invoice invoice;

  public static final String SERIALIZED_NAME_INVOICE_ID = "InvoiceId";
  @SerializedName(SERIALIZED_NAME_INVOICE_ID)
  private Integer invoiceId;

  public static final String SERIALIZED_NAME_IS_AUTOMATIC = "IsAutomatic";
  @SerializedName(SERIALIZED_NAME_IS_AUTOMATIC)
  private Boolean isAutomatic;

  public static final String SERIALIZED_NAME_NOTE = "Note";
  @SerializedName(SERIALIZED_NAME_NOTE)
  private String note;

  public static final String SERIALIZED_NAME_PAID_ON = "PaidOn";
  @SerializedName(SERIALIZED_NAME_PAID_ON)
  private OffsetDateTime paidOn;

  public static final String SERIALIZED_NAME_REFERENCE_ID = "ReferenceId";
  @SerializedName(SERIALIZED_NAME_REFERENCE_ID)
  private String referenceId;

  /**
   * Gets or Sets type
   */
  @JsonAdapter(TypeEnum.Adapter.class)
  public enum TypeEnum {
    OTHER("Other"),
    
    PAYPAL("Paypal"),
    
    STRIPE("Stripe"),
    
    PAYONEER("Payoneer"),
    
    BANK("Bank"),
    
    CASH("Cash"),
    
    CHEQUE("Cheque"),
    
    ACH("Ach"),
    
    SEPA("Sepa"),
    
    SQUARE("Square"),
    
    KLIK_AND_PAY("KlikAndPay"),
    
    RAZORPAY("Razorpay"),
    
    WEPAY("Wepay"),
    
    HALKBANK("Halkbank"),
    
    TWO_CHECKOUT("TwoCheckout"),
    
    PAYMENT_WALL("PaymentWall"),
    
    BAMBORA_EU("BamboraEU"),
    
    BAMBORA_NA("BamboraNA"),
    
    NLB("Nlb"),
    
    AUTHORIZE_NET("AuthorizeNet"),
    
    BRAINTREE("Braintree");

    private String value;

    TypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static TypeEnum fromValue(String value) {
      for (TypeEnum b : TypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<TypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final TypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public TypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return TypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      TypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_TYPE = "Type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private TypeEnum type;

  public Payment() {
  }

  public Payment amount(Double amount) {
    this.amount = amount;
    return this;
  }

  /**
   * Get amount
   * @return amount
   */
  @javax.annotation.Nullable
  public Double getAmount() {
    return amount;
  }

  public void setAmount(Double amount) {
    this.amount = amount;
  }


  public Payment id(Integer id) {
    this.id = id;
    return this;
  }

  /**
   * Get id
   * @return id
   */
  @javax.annotation.Nullable
  public Integer getId() {
    return id;
  }

  public void setId(Integer id) {
    this.id = id;
  }


  public Payment invoice(Invoice invoice) {
    this.invoice = invoice;
    return this;
  }

  /**
   * Get invoice
   * @return invoice
   */
  @javax.annotation.Nullable
  public Invoice getInvoice() {
    return invoice;
  }

  public void setInvoice(Invoice invoice) {
    this.invoice = invoice;
  }


  public Payment invoiceId(Integer invoiceId) {
    this.invoiceId = invoiceId;
    return this;
  }

  /**
   * Get invoiceId
   * @return invoiceId
   */
  @javax.annotation.Nullable
  public Integer getInvoiceId() {
    return invoiceId;
  }

  public void setInvoiceId(Integer invoiceId) {
    this.invoiceId = invoiceId;
  }


  public Payment isAutomatic(Boolean isAutomatic) {
    this.isAutomatic = isAutomatic;
    return this;
  }

  /**
   * Get isAutomatic
   * @return isAutomatic
   */
  @javax.annotation.Nullable
  public Boolean getIsAutomatic() {
    return isAutomatic;
  }

  public void setIsAutomatic(Boolean isAutomatic) {
    this.isAutomatic = isAutomatic;
  }


  public Payment note(String note) {
    this.note = note;
    return this;
  }

  /**
   * Get note
   * @return note
   */
  @javax.annotation.Nullable
  public String getNote() {
    return note;
  }

  public void setNote(String note) {
    this.note = note;
  }


  public Payment paidOn(OffsetDateTime paidOn) {
    this.paidOn = paidOn;
    return this;
  }

  /**
   * Get paidOn
   * @return paidOn
   */
  @javax.annotation.Nullable
  public OffsetDateTime getPaidOn() {
    return paidOn;
  }

  public void setPaidOn(OffsetDateTime paidOn) {
    this.paidOn = paidOn;
  }


  public Payment referenceId(String referenceId) {
    this.referenceId = referenceId;
    return this;
  }

  /**
   * Get referenceId
   * @return referenceId
   */
  @javax.annotation.Nullable
  public String getReferenceId() {
    return referenceId;
  }

  public void setReferenceId(String referenceId) {
    this.referenceId = referenceId;
  }


  public Payment type(TypeEnum type) {
    this.type = type;
    return this;
  }

  /**
   * Get type
   * @return type
   */
  @javax.annotation.Nullable
  public TypeEnum getType() {
    return type;
  }

  public void setType(TypeEnum type) {
    this.type = type;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Payment payment = (Payment) o;
    return Objects.equals(this.amount, payment.amount) &&
        Objects.equals(this.id, payment.id) &&
        Objects.equals(this.invoice, payment.invoice) &&
        Objects.equals(this.invoiceId, payment.invoiceId) &&
        Objects.equals(this.isAutomatic, payment.isAutomatic) &&
        Objects.equals(this.note, payment.note) &&
        Objects.equals(this.paidOn, payment.paidOn) &&
        Objects.equals(this.referenceId, payment.referenceId) &&
        Objects.equals(this.type, payment.type);
  }

  @Override
  public int hashCode() {
    return Objects.hash(amount, id, invoice, invoiceId, isAutomatic, note, paidOn, referenceId, type);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Payment {\n");
    sb.append("    amount: ").append(toIndentedString(amount)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    invoice: ").append(toIndentedString(invoice)).append("\n");
    sb.append("    invoiceId: ").append(toIndentedString(invoiceId)).append("\n");
    sb.append("    isAutomatic: ").append(toIndentedString(isAutomatic)).append("\n");
    sb.append("    note: ").append(toIndentedString(note)).append("\n");
    sb.append("    paidOn: ").append(toIndentedString(paidOn)).append("\n");
    sb.append("    referenceId: ").append(toIndentedString(referenceId)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
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
    openapiFields.add("Amount");
    openapiFields.add("Id");
    openapiFields.add("Invoice");
    openapiFields.add("InvoiceId");
    openapiFields.add("IsAutomatic");
    openapiFields.add("Note");
    openapiFields.add("PaidOn");
    openapiFields.add("ReferenceId");
    openapiFields.add("Type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Payment
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Payment.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Payment is not found in the empty JSON string", Payment.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Payment.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Payment` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `Invoice`
      if (jsonObj.get("Invoice") != null && !jsonObj.get("Invoice").isJsonNull()) {
        Invoice.validateJsonElement(jsonObj.get("Invoice"));
      }
      if ((jsonObj.get("Note") != null && !jsonObj.get("Note").isJsonNull()) && !jsonObj.get("Note").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Note` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Note").toString()));
      }
      if ((jsonObj.get("ReferenceId") != null && !jsonObj.get("ReferenceId").isJsonNull()) && !jsonObj.get("ReferenceId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ReferenceId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ReferenceId").toString()));
      }
      if ((jsonObj.get("Type") != null && !jsonObj.get("Type").isJsonNull()) && !jsonObj.get("Type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Type").toString()));
      }
      // validate the optional field `Type`
      if (jsonObj.get("Type") != null && !jsonObj.get("Type").isJsonNull()) {
        TypeEnum.validateJsonElement(jsonObj.get("Type"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Payment.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Payment' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Payment> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Payment.class));

       return (TypeAdapter<T>) new TypeAdapter<Payment>() {
           @Override
           public void write(JsonWriter out, Payment value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Payment read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Payment given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Payment
   * @throws IOException if the JSON string is invalid with respect to Payment
   */
  public static Payment fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Payment.class);
  }

  /**
   * Convert an instance of Payment to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

