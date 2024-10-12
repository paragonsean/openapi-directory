/*
 * Avaza API Documentation
 * Welcome to the autogenerated documentation & test tool for Avaza's API. <br/><br/><strong>API Security & Authentication</strong><br/>Authentication options include OAuth2 Implicit and Authorization Code flows, and Personal Access Token. All connections should be encrypted over SSL/TLS <br/><br/>You can set up and manage your api authentication credentials from within your Avaza account. (requires Administrator permissions on your Avaza account).<br/><br/> OAuth2 Authorization endpoint: https://any.avaza.com/oauth2/authorize  <br/>OAuth2 Token endpoint: https://any.avaza.com/oauth2/token<br/>Base URL for subsequent API Requests: https://api.avaza.com/ <br/><br/>Blogpost about authenticating with Avaza's API:  https://www.avaza.com/avaza-api-oauth2-authentication/ <br/>Blogpost on using Avaza's webhooks: https://www.avaza.com/avaza-api-webhook-notifications/<br/>The OAuth flow currently issues Access Tokens that last 1 day, and Refresh tokens that last 180 days<br/>The Api respects the security Roles assigned to the authenticating Avaza user and filters the data return appropriately. <br/><br><strong>Support</strong><br/>For API Support, and to request access please contact Avaza Support Team via our support chat. <br/><br/><strong>User Contributed Libraries:</strong><br/>Graciously contributed by 3rd party users like you. <br/>Note these are not tested or endorsesd by Avaza. We encourage you to review before use, and use at own risk.<br/> <ul><li> - <a target='blank' href='https://packagist.org/packages/debiprasad/oauth2-avaza'>PHP OAuth Client Package for Azava API (by Debiprasad Sahoo)</a></li></ul>
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
 * CreditNoteLineItem
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:11:56.431364-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CreditNoteLineItem {
  public static final String SERIALIZED_NAME_AMOUNT = "Amount";
  @SerializedName(SERIALIZED_NAME_AMOUNT)
  private Double amount;

  public static final String SERIALIZED_NAME_DESCRIPTION = "Description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_DISCOUNT = "Discount";
  @SerializedName(SERIALIZED_NAME_DISCOUNT)
  private Double discount;

  public static final String SERIALIZED_NAME_QUANTITY = "Quantity";
  @SerializedName(SERIALIZED_NAME_QUANTITY)
  private Double quantity;

  public static final String SERIALIZED_NAME_TAX_AMOUNT = "TaxAmount";
  @SerializedName(SERIALIZED_NAME_TAX_AMOUNT)
  private Double taxAmount;

  public static final String SERIALIZED_NAME_TAX_I_D_F_K = "TaxIDFK";
  @SerializedName(SERIALIZED_NAME_TAX_I_D_F_K)
  private Integer taxIDFK;

  public static final String SERIALIZED_NAME_TRANSACTION_LINE_ITEM_I_D = "TransactionLineItemID";
  @SerializedName(SERIALIZED_NAME_TRANSACTION_LINE_ITEM_I_D)
  private Long transactionLineItemID;

  public static final String SERIALIZED_NAME_UNIT_PRICE = "UnitPrice";
  @SerializedName(SERIALIZED_NAME_UNIT_PRICE)
  private Double unitPrice;

  public CreditNoteLineItem() {
  }

  public CreditNoteLineItem amount(Double amount) {
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


  public CreditNoteLineItem description(String description) {
    this.description = description;
    return this;
  }

  /**
   * Get description
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public CreditNoteLineItem discount(Double discount) {
    this.discount = discount;
    return this;
  }

  /**
   * Get discount
   * @return discount
   */
  @javax.annotation.Nullable
  public Double getDiscount() {
    return discount;
  }

  public void setDiscount(Double discount) {
    this.discount = discount;
  }


  public CreditNoteLineItem quantity(Double quantity) {
    this.quantity = quantity;
    return this;
  }

  /**
   * Get quantity
   * @return quantity
   */
  @javax.annotation.Nullable
  public Double getQuantity() {
    return quantity;
  }

  public void setQuantity(Double quantity) {
    this.quantity = quantity;
  }


  public CreditNoteLineItem taxAmount(Double taxAmount) {
    this.taxAmount = taxAmount;
    return this;
  }

  /**
   * Get taxAmount
   * @return taxAmount
   */
  @javax.annotation.Nullable
  public Double getTaxAmount() {
    return taxAmount;
  }

  public void setTaxAmount(Double taxAmount) {
    this.taxAmount = taxAmount;
  }


  public CreditNoteLineItem taxIDFK(Integer taxIDFK) {
    this.taxIDFK = taxIDFK;
    return this;
  }

  /**
   * Get taxIDFK
   * @return taxIDFK
   */
  @javax.annotation.Nullable
  public Integer getTaxIDFK() {
    return taxIDFK;
  }

  public void setTaxIDFK(Integer taxIDFK) {
    this.taxIDFK = taxIDFK;
  }


  public CreditNoteLineItem transactionLineItemID(Long transactionLineItemID) {
    this.transactionLineItemID = transactionLineItemID;
    return this;
  }

  /**
   * Get transactionLineItemID
   * @return transactionLineItemID
   */
  @javax.annotation.Nullable
  public Long getTransactionLineItemID() {
    return transactionLineItemID;
  }

  public void setTransactionLineItemID(Long transactionLineItemID) {
    this.transactionLineItemID = transactionLineItemID;
  }


  public CreditNoteLineItem unitPrice(Double unitPrice) {
    this.unitPrice = unitPrice;
    return this;
  }

  /**
   * Get unitPrice
   * @return unitPrice
   */
  @javax.annotation.Nullable
  public Double getUnitPrice() {
    return unitPrice;
  }

  public void setUnitPrice(Double unitPrice) {
    this.unitPrice = unitPrice;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CreditNoteLineItem creditNoteLineItem = (CreditNoteLineItem) o;
    return Objects.equals(this.amount, creditNoteLineItem.amount) &&
        Objects.equals(this.description, creditNoteLineItem.description) &&
        Objects.equals(this.discount, creditNoteLineItem.discount) &&
        Objects.equals(this.quantity, creditNoteLineItem.quantity) &&
        Objects.equals(this.taxAmount, creditNoteLineItem.taxAmount) &&
        Objects.equals(this.taxIDFK, creditNoteLineItem.taxIDFK) &&
        Objects.equals(this.transactionLineItemID, creditNoteLineItem.transactionLineItemID) &&
        Objects.equals(this.unitPrice, creditNoteLineItem.unitPrice);
  }

  @Override
  public int hashCode() {
    return Objects.hash(amount, description, discount, quantity, taxAmount, taxIDFK, transactionLineItemID, unitPrice);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CreditNoteLineItem {\n");
    sb.append("    amount: ").append(toIndentedString(amount)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    discount: ").append(toIndentedString(discount)).append("\n");
    sb.append("    quantity: ").append(toIndentedString(quantity)).append("\n");
    sb.append("    taxAmount: ").append(toIndentedString(taxAmount)).append("\n");
    sb.append("    taxIDFK: ").append(toIndentedString(taxIDFK)).append("\n");
    sb.append("    transactionLineItemID: ").append(toIndentedString(transactionLineItemID)).append("\n");
    sb.append("    unitPrice: ").append(toIndentedString(unitPrice)).append("\n");
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
    openapiFields.add("Description");
    openapiFields.add("Discount");
    openapiFields.add("Quantity");
    openapiFields.add("TaxAmount");
    openapiFields.add("TaxIDFK");
    openapiFields.add("TransactionLineItemID");
    openapiFields.add("UnitPrice");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CreditNoteLineItem
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CreditNoteLineItem.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CreditNoteLineItem is not found in the empty JSON string", CreditNoteLineItem.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CreditNoteLineItem.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CreditNoteLineItem` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("Description") != null && !jsonObj.get("Description").isJsonNull()) && !jsonObj.get("Description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Description").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CreditNoteLineItem.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CreditNoteLineItem' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CreditNoteLineItem> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CreditNoteLineItem.class));

       return (TypeAdapter<T>) new TypeAdapter<CreditNoteLineItem>() {
           @Override
           public void write(JsonWriter out, CreditNoteLineItem value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CreditNoteLineItem read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CreditNoteLineItem given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CreditNoteLineItem
   * @throws IOException if the JSON string is invalid with respect to CreditNoteLineItem
   */
  public static CreditNoteLineItem fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CreditNoteLineItem.class);
  }

  /**
   * Convert an instance of CreditNoteLineItem to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

