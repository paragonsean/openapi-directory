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
 * EstimateLineItemDetails
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:11:56.431364-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class EstimateLineItemDetails {
  public static final String SERIALIZED_NAME_AMOUNT = "Amount";
  @SerializedName(SERIALIZED_NAME_AMOUNT)
  private Double amount;

  public static final String SERIALIZED_NAME_DESCRIPTION = "Description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_DISCOUNT = "Discount";
  @SerializedName(SERIALIZED_NAME_DISCOUNT)
  private Double discount;

  public static final String SERIALIZED_NAME_ESTIMATE_LINE_ITEM_I_D = "EstimateLineItemID";
  @SerializedName(SERIALIZED_NAME_ESTIMATE_LINE_ITEM_I_D)
  private Long estimateLineItemID;

  public static final String SERIALIZED_NAME_INVENTORY_ITEM_I_D_F_K = "InventoryItemIDFK";
  @SerializedName(SERIALIZED_NAME_INVENTORY_ITEM_I_D_F_K)
  private Long inventoryItemIDFK;

  public static final String SERIALIZED_NAME_INVENTORY_ITEM_NAME = "InventoryItemName";
  @SerializedName(SERIALIZED_NAME_INVENTORY_ITEM_NAME)
  private String inventoryItemName;

  public static final String SERIALIZED_NAME_INVENTORY_ITEM_S_K_U = "InventoryItemSKU";
  @SerializedName(SERIALIZED_NAME_INVENTORY_ITEM_S_K_U)
  private String inventoryItemSKU;

  public static final String SERIALIZED_NAME_QUANTITY = "Quantity";
  @SerializedName(SERIALIZED_NAME_QUANTITY)
  private Double quantity;

  public static final String SERIALIZED_NAME_TAX_AMOUNT = "TaxAmount";
  @SerializedName(SERIALIZED_NAME_TAX_AMOUNT)
  private Double taxAmount;

  public static final String SERIALIZED_NAME_TAX_CODE = "TaxCode";
  @SerializedName(SERIALIZED_NAME_TAX_CODE)
  private String taxCode;

  public static final String SERIALIZED_NAME_TAX_I_D_F_K = "TaxIDFK";
  @SerializedName(SERIALIZED_NAME_TAX_I_D_F_K)
  private Integer taxIDFK;

  public static final String SERIALIZED_NAME_TAX_NAME = "TaxName";
  @SerializedName(SERIALIZED_NAME_TAX_NAME)
  private String taxName;

  public static final String SERIALIZED_NAME_UNIT_PRICE = "UnitPrice";
  @SerializedName(SERIALIZED_NAME_UNIT_PRICE)
  private Double unitPrice;

  public EstimateLineItemDetails() {
  }

  public EstimateLineItemDetails amount(Double amount) {
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


  public EstimateLineItemDetails description(String description) {
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


  public EstimateLineItemDetails discount(Double discount) {
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


  public EstimateLineItemDetails estimateLineItemID(Long estimateLineItemID) {
    this.estimateLineItemID = estimateLineItemID;
    return this;
  }

  /**
   * Get estimateLineItemID
   * @return estimateLineItemID
   */
  @javax.annotation.Nullable
  public Long getEstimateLineItemID() {
    return estimateLineItemID;
  }

  public void setEstimateLineItemID(Long estimateLineItemID) {
    this.estimateLineItemID = estimateLineItemID;
  }


  public EstimateLineItemDetails inventoryItemIDFK(Long inventoryItemIDFK) {
    this.inventoryItemIDFK = inventoryItemIDFK;
    return this;
  }

  /**
   * Get inventoryItemIDFK
   * @return inventoryItemIDFK
   */
  @javax.annotation.Nullable
  public Long getInventoryItemIDFK() {
    return inventoryItemIDFK;
  }

  public void setInventoryItemIDFK(Long inventoryItemIDFK) {
    this.inventoryItemIDFK = inventoryItemIDFK;
  }


  public EstimateLineItemDetails inventoryItemName(String inventoryItemName) {
    this.inventoryItemName = inventoryItemName;
    return this;
  }

  /**
   * Get inventoryItemName
   * @return inventoryItemName
   */
  @javax.annotation.Nullable
  public String getInventoryItemName() {
    return inventoryItemName;
  }

  public void setInventoryItemName(String inventoryItemName) {
    this.inventoryItemName = inventoryItemName;
  }


  public EstimateLineItemDetails inventoryItemSKU(String inventoryItemSKU) {
    this.inventoryItemSKU = inventoryItemSKU;
    return this;
  }

  /**
   * Get inventoryItemSKU
   * @return inventoryItemSKU
   */
  @javax.annotation.Nullable
  public String getInventoryItemSKU() {
    return inventoryItemSKU;
  }

  public void setInventoryItemSKU(String inventoryItemSKU) {
    this.inventoryItemSKU = inventoryItemSKU;
  }


  public EstimateLineItemDetails quantity(Double quantity) {
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


  public EstimateLineItemDetails taxAmount(Double taxAmount) {
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


  public EstimateLineItemDetails taxCode(String taxCode) {
    this.taxCode = taxCode;
    return this;
  }

  /**
   * Get taxCode
   * @return taxCode
   */
  @javax.annotation.Nullable
  public String getTaxCode() {
    return taxCode;
  }

  public void setTaxCode(String taxCode) {
    this.taxCode = taxCode;
  }


  public EstimateLineItemDetails taxIDFK(Integer taxIDFK) {
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


  public EstimateLineItemDetails taxName(String taxName) {
    this.taxName = taxName;
    return this;
  }

  /**
   * Get taxName
   * @return taxName
   */
  @javax.annotation.Nullable
  public String getTaxName() {
    return taxName;
  }

  public void setTaxName(String taxName) {
    this.taxName = taxName;
  }


  public EstimateLineItemDetails unitPrice(Double unitPrice) {
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
    EstimateLineItemDetails estimateLineItemDetails = (EstimateLineItemDetails) o;
    return Objects.equals(this.amount, estimateLineItemDetails.amount) &&
        Objects.equals(this.description, estimateLineItemDetails.description) &&
        Objects.equals(this.discount, estimateLineItemDetails.discount) &&
        Objects.equals(this.estimateLineItemID, estimateLineItemDetails.estimateLineItemID) &&
        Objects.equals(this.inventoryItemIDFK, estimateLineItemDetails.inventoryItemIDFK) &&
        Objects.equals(this.inventoryItemName, estimateLineItemDetails.inventoryItemName) &&
        Objects.equals(this.inventoryItemSKU, estimateLineItemDetails.inventoryItemSKU) &&
        Objects.equals(this.quantity, estimateLineItemDetails.quantity) &&
        Objects.equals(this.taxAmount, estimateLineItemDetails.taxAmount) &&
        Objects.equals(this.taxCode, estimateLineItemDetails.taxCode) &&
        Objects.equals(this.taxIDFK, estimateLineItemDetails.taxIDFK) &&
        Objects.equals(this.taxName, estimateLineItemDetails.taxName) &&
        Objects.equals(this.unitPrice, estimateLineItemDetails.unitPrice);
  }

  @Override
  public int hashCode() {
    return Objects.hash(amount, description, discount, estimateLineItemID, inventoryItemIDFK, inventoryItemName, inventoryItemSKU, quantity, taxAmount, taxCode, taxIDFK, taxName, unitPrice);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class EstimateLineItemDetails {\n");
    sb.append("    amount: ").append(toIndentedString(amount)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    discount: ").append(toIndentedString(discount)).append("\n");
    sb.append("    estimateLineItemID: ").append(toIndentedString(estimateLineItemID)).append("\n");
    sb.append("    inventoryItemIDFK: ").append(toIndentedString(inventoryItemIDFK)).append("\n");
    sb.append("    inventoryItemName: ").append(toIndentedString(inventoryItemName)).append("\n");
    sb.append("    inventoryItemSKU: ").append(toIndentedString(inventoryItemSKU)).append("\n");
    sb.append("    quantity: ").append(toIndentedString(quantity)).append("\n");
    sb.append("    taxAmount: ").append(toIndentedString(taxAmount)).append("\n");
    sb.append("    taxCode: ").append(toIndentedString(taxCode)).append("\n");
    sb.append("    taxIDFK: ").append(toIndentedString(taxIDFK)).append("\n");
    sb.append("    taxName: ").append(toIndentedString(taxName)).append("\n");
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
    openapiFields.add("EstimateLineItemID");
    openapiFields.add("InventoryItemIDFK");
    openapiFields.add("InventoryItemName");
    openapiFields.add("InventoryItemSKU");
    openapiFields.add("Quantity");
    openapiFields.add("TaxAmount");
    openapiFields.add("TaxCode");
    openapiFields.add("TaxIDFK");
    openapiFields.add("TaxName");
    openapiFields.add("UnitPrice");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to EstimateLineItemDetails
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!EstimateLineItemDetails.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in EstimateLineItemDetails is not found in the empty JSON string", EstimateLineItemDetails.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!EstimateLineItemDetails.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `EstimateLineItemDetails` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("Description") != null && !jsonObj.get("Description").isJsonNull()) && !jsonObj.get("Description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Description").toString()));
      }
      if ((jsonObj.get("InventoryItemName") != null && !jsonObj.get("InventoryItemName").isJsonNull()) && !jsonObj.get("InventoryItemName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `InventoryItemName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("InventoryItemName").toString()));
      }
      if ((jsonObj.get("InventoryItemSKU") != null && !jsonObj.get("InventoryItemSKU").isJsonNull()) && !jsonObj.get("InventoryItemSKU").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `InventoryItemSKU` to be a primitive type in the JSON string but got `%s`", jsonObj.get("InventoryItemSKU").toString()));
      }
      if ((jsonObj.get("TaxCode") != null && !jsonObj.get("TaxCode").isJsonNull()) && !jsonObj.get("TaxCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `TaxCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("TaxCode").toString()));
      }
      if ((jsonObj.get("TaxName") != null && !jsonObj.get("TaxName").isJsonNull()) && !jsonObj.get("TaxName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `TaxName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("TaxName").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!EstimateLineItemDetails.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'EstimateLineItemDetails' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<EstimateLineItemDetails> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(EstimateLineItemDetails.class));

       return (TypeAdapter<T>) new TypeAdapter<EstimateLineItemDetails>() {
           @Override
           public void write(JsonWriter out, EstimateLineItemDetails value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public EstimateLineItemDetails read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of EstimateLineItemDetails given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of EstimateLineItemDetails
   * @throws IOException if the JSON string is invalid with respect to EstimateLineItemDetails
   */
  public static EstimateLineItemDetails fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, EstimateLineItemDetails.class);
  }

  /**
   * Convert an instance of EstimateLineItemDetails to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

