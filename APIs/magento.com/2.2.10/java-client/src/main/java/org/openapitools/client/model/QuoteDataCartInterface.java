/*
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.CustomerDataCustomerInterface;
import org.openapitools.client.model.QuoteDataAddressInterface;
import org.openapitools.client.model.QuoteDataCartExtensionInterface;
import org.openapitools.client.model.QuoteDataCartItemInterface;
import org.openapitools.client.model.QuoteDataCurrencyInterface;

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
 * Interface CartInterface
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:51.810681-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class QuoteDataCartInterface {
  public static final String SERIALIZED_NAME_BILLING_ADDRESS = "billing_address";
  @SerializedName(SERIALIZED_NAME_BILLING_ADDRESS)
  private QuoteDataAddressInterface billingAddress;

  public static final String SERIALIZED_NAME_CONVERTED_AT = "converted_at";
  @SerializedName(SERIALIZED_NAME_CONVERTED_AT)
  private String convertedAt;

  public static final String SERIALIZED_NAME_CREATED_AT = "created_at";
  @SerializedName(SERIALIZED_NAME_CREATED_AT)
  private String createdAt;

  public static final String SERIALIZED_NAME_CURRENCY = "currency";
  @SerializedName(SERIALIZED_NAME_CURRENCY)
  private QuoteDataCurrencyInterface currency;

  public static final String SERIALIZED_NAME_CUSTOMER = "customer";
  @SerializedName(SERIALIZED_NAME_CUSTOMER)
  private CustomerDataCustomerInterface customer;

  public static final String SERIALIZED_NAME_CUSTOMER_IS_GUEST = "customer_is_guest";
  @SerializedName(SERIALIZED_NAME_CUSTOMER_IS_GUEST)
  private Boolean customerIsGuest;

  public static final String SERIALIZED_NAME_CUSTOMER_NOTE = "customer_note";
  @SerializedName(SERIALIZED_NAME_CUSTOMER_NOTE)
  private String customerNote;

  public static final String SERIALIZED_NAME_CUSTOMER_NOTE_NOTIFY = "customer_note_notify";
  @SerializedName(SERIALIZED_NAME_CUSTOMER_NOTE_NOTIFY)
  private Boolean customerNoteNotify;

  public static final String SERIALIZED_NAME_CUSTOMER_TAX_CLASS_ID = "customer_tax_class_id";
  @SerializedName(SERIALIZED_NAME_CUSTOMER_TAX_CLASS_ID)
  private Integer customerTaxClassId;

  public static final String SERIALIZED_NAME_EXTENSION_ATTRIBUTES = "extension_attributes";
  @SerializedName(SERIALIZED_NAME_EXTENSION_ATTRIBUTES)
  private QuoteDataCartExtensionInterface extensionAttributes;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_IS_ACTIVE = "is_active";
  @SerializedName(SERIALIZED_NAME_IS_ACTIVE)
  private Boolean isActive;

  public static final String SERIALIZED_NAME_IS_VIRTUAL = "is_virtual";
  @SerializedName(SERIALIZED_NAME_IS_VIRTUAL)
  private Boolean isVirtual;

  public static final String SERIALIZED_NAME_ITEMS = "items";
  @SerializedName(SERIALIZED_NAME_ITEMS)
  private List<QuoteDataCartItemInterface> items = new ArrayList<>();

  public static final String SERIALIZED_NAME_ITEMS_COUNT = "items_count";
  @SerializedName(SERIALIZED_NAME_ITEMS_COUNT)
  private Integer itemsCount;

  public static final String SERIALIZED_NAME_ITEMS_QTY = "items_qty";
  @SerializedName(SERIALIZED_NAME_ITEMS_QTY)
  private BigDecimal itemsQty;

  public static final String SERIALIZED_NAME_ORIG_ORDER_ID = "orig_order_id";
  @SerializedName(SERIALIZED_NAME_ORIG_ORDER_ID)
  private Integer origOrderId;

  public static final String SERIALIZED_NAME_RESERVED_ORDER_ID = "reserved_order_id";
  @SerializedName(SERIALIZED_NAME_RESERVED_ORDER_ID)
  private String reservedOrderId;

  public static final String SERIALIZED_NAME_STORE_ID = "store_id";
  @SerializedName(SERIALIZED_NAME_STORE_ID)
  private Integer storeId;

  public static final String SERIALIZED_NAME_UPDATED_AT = "updated_at";
  @SerializedName(SERIALIZED_NAME_UPDATED_AT)
  private String updatedAt;

  public QuoteDataCartInterface() {
  }

  public QuoteDataCartInterface billingAddress(QuoteDataAddressInterface billingAddress) {
    this.billingAddress = billingAddress;
    return this;
  }

  /**
   * Get billingAddress
   * @return billingAddress
   */
  @javax.annotation.Nullable
  public QuoteDataAddressInterface getBillingAddress() {
    return billingAddress;
  }

  public void setBillingAddress(QuoteDataAddressInterface billingAddress) {
    this.billingAddress = billingAddress;
  }


  public QuoteDataCartInterface convertedAt(String convertedAt) {
    this.convertedAt = convertedAt;
    return this;
  }

  /**
   * Cart conversion date and time. Otherwise, null.
   * @return convertedAt
   */
  @javax.annotation.Nullable
  public String getConvertedAt() {
    return convertedAt;
  }

  public void setConvertedAt(String convertedAt) {
    this.convertedAt = convertedAt;
  }


  public QuoteDataCartInterface createdAt(String createdAt) {
    this.createdAt = createdAt;
    return this;
  }

  /**
   * Cart creation date and time. Otherwise, null.
   * @return createdAt
   */
  @javax.annotation.Nullable
  public String getCreatedAt() {
    return createdAt;
  }

  public void setCreatedAt(String createdAt) {
    this.createdAt = createdAt;
  }


  public QuoteDataCartInterface currency(QuoteDataCurrencyInterface currency) {
    this.currency = currency;
    return this;
  }

  /**
   * Get currency
   * @return currency
   */
  @javax.annotation.Nullable
  public QuoteDataCurrencyInterface getCurrency() {
    return currency;
  }

  public void setCurrency(QuoteDataCurrencyInterface currency) {
    this.currency = currency;
  }


  public QuoteDataCartInterface customer(CustomerDataCustomerInterface customer) {
    this.customer = customer;
    return this;
  }

  /**
   * Get customer
   * @return customer
   */
  @javax.annotation.Nonnull
  public CustomerDataCustomerInterface getCustomer() {
    return customer;
  }

  public void setCustomer(CustomerDataCustomerInterface customer) {
    this.customer = customer;
  }


  public QuoteDataCartInterface customerIsGuest(Boolean customerIsGuest) {
    this.customerIsGuest = customerIsGuest;
    return this;
  }

  /**
   * For guest customers, false for logged in customers
   * @return customerIsGuest
   */
  @javax.annotation.Nullable
  public Boolean getCustomerIsGuest() {
    return customerIsGuest;
  }

  public void setCustomerIsGuest(Boolean customerIsGuest) {
    this.customerIsGuest = customerIsGuest;
  }


  public QuoteDataCartInterface customerNote(String customerNote) {
    this.customerNote = customerNote;
    return this;
  }

  /**
   * Notice text
   * @return customerNote
   */
  @javax.annotation.Nullable
  public String getCustomerNote() {
    return customerNote;
  }

  public void setCustomerNote(String customerNote) {
    this.customerNote = customerNote;
  }


  public QuoteDataCartInterface customerNoteNotify(Boolean customerNoteNotify) {
    this.customerNoteNotify = customerNoteNotify;
    return this;
  }

  /**
   * Customer notification flag
   * @return customerNoteNotify
   */
  @javax.annotation.Nullable
  public Boolean getCustomerNoteNotify() {
    return customerNoteNotify;
  }

  public void setCustomerNoteNotify(Boolean customerNoteNotify) {
    this.customerNoteNotify = customerNoteNotify;
  }


  public QuoteDataCartInterface customerTaxClassId(Integer customerTaxClassId) {
    this.customerTaxClassId = customerTaxClassId;
    return this;
  }

  /**
   * Customer tax class ID.
   * @return customerTaxClassId
   */
  @javax.annotation.Nullable
  public Integer getCustomerTaxClassId() {
    return customerTaxClassId;
  }

  public void setCustomerTaxClassId(Integer customerTaxClassId) {
    this.customerTaxClassId = customerTaxClassId;
  }


  public QuoteDataCartInterface extensionAttributes(QuoteDataCartExtensionInterface extensionAttributes) {
    this.extensionAttributes = extensionAttributes;
    return this;
  }

  /**
   * Get extensionAttributes
   * @return extensionAttributes
   */
  @javax.annotation.Nullable
  public QuoteDataCartExtensionInterface getExtensionAttributes() {
    return extensionAttributes;
  }

  public void setExtensionAttributes(QuoteDataCartExtensionInterface extensionAttributes) {
    this.extensionAttributes = extensionAttributes;
  }


  public QuoteDataCartInterface id(Integer id) {
    this.id = id;
    return this;
  }

  /**
   * Cart/quote ID.
   * @return id
   */
  @javax.annotation.Nonnull
  public Integer getId() {
    return id;
  }

  public void setId(Integer id) {
    this.id = id;
  }


  public QuoteDataCartInterface isActive(Boolean isActive) {
    this.isActive = isActive;
    return this;
  }

  /**
   * Active status flag value. Otherwise, null.
   * @return isActive
   */
  @javax.annotation.Nullable
  public Boolean getIsActive() {
    return isActive;
  }

  public void setIsActive(Boolean isActive) {
    this.isActive = isActive;
  }


  public QuoteDataCartInterface isVirtual(Boolean isVirtual) {
    this.isVirtual = isVirtual;
    return this;
  }

  /**
   * Virtual flag value. Otherwise, null.
   * @return isVirtual
   */
  @javax.annotation.Nullable
  public Boolean getIsVirtual() {
    return isVirtual;
  }

  public void setIsVirtual(Boolean isVirtual) {
    this.isVirtual = isVirtual;
  }


  public QuoteDataCartInterface items(List<QuoteDataCartItemInterface> items) {
    this.items = items;
    return this;
  }

  public QuoteDataCartInterface addItemsItem(QuoteDataCartItemInterface itemsItem) {
    if (this.items == null) {
      this.items = new ArrayList<>();
    }
    this.items.add(itemsItem);
    return this;
  }

  /**
   * Array of items. Otherwise, null.
   * @return items
   */
  @javax.annotation.Nullable
  public List<QuoteDataCartItemInterface> getItems() {
    return items;
  }

  public void setItems(List<QuoteDataCartItemInterface> items) {
    this.items = items;
  }


  public QuoteDataCartInterface itemsCount(Integer itemsCount) {
    this.itemsCount = itemsCount;
    return this;
  }

  /**
   * Number of different items or products in the cart. Otherwise, null.
   * @return itemsCount
   */
  @javax.annotation.Nullable
  public Integer getItemsCount() {
    return itemsCount;
  }

  public void setItemsCount(Integer itemsCount) {
    this.itemsCount = itemsCount;
  }


  public QuoteDataCartInterface itemsQty(BigDecimal itemsQty) {
    this.itemsQty = itemsQty;
    return this;
  }

  /**
   * Total quantity of all cart items. Otherwise, null.
   * @return itemsQty
   */
  @javax.annotation.Nullable
  public BigDecimal getItemsQty() {
    return itemsQty;
  }

  public void setItemsQty(BigDecimal itemsQty) {
    this.itemsQty = itemsQty;
  }


  public QuoteDataCartInterface origOrderId(Integer origOrderId) {
    this.origOrderId = origOrderId;
    return this;
  }

  /**
   * Original order ID. Otherwise, null.
   * @return origOrderId
   */
  @javax.annotation.Nullable
  public Integer getOrigOrderId() {
    return origOrderId;
  }

  public void setOrigOrderId(Integer origOrderId) {
    this.origOrderId = origOrderId;
  }


  public QuoteDataCartInterface reservedOrderId(String reservedOrderId) {
    this.reservedOrderId = reservedOrderId;
    return this;
  }

  /**
   * Reserved order ID. Otherwise, null.
   * @return reservedOrderId
   */
  @javax.annotation.Nullable
  public String getReservedOrderId() {
    return reservedOrderId;
  }

  public void setReservedOrderId(String reservedOrderId) {
    this.reservedOrderId = reservedOrderId;
  }


  public QuoteDataCartInterface storeId(Integer storeId) {
    this.storeId = storeId;
    return this;
  }

  /**
   * Store identifier
   * @return storeId
   */
  @javax.annotation.Nonnull
  public Integer getStoreId() {
    return storeId;
  }

  public void setStoreId(Integer storeId) {
    this.storeId = storeId;
  }


  public QuoteDataCartInterface updatedAt(String updatedAt) {
    this.updatedAt = updatedAt;
    return this;
  }

  /**
   * Cart last update date and time. Otherwise, null.
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
    QuoteDataCartInterface quoteDataCartInterface = (QuoteDataCartInterface) o;
    return Objects.equals(this.billingAddress, quoteDataCartInterface.billingAddress) &&
        Objects.equals(this.convertedAt, quoteDataCartInterface.convertedAt) &&
        Objects.equals(this.createdAt, quoteDataCartInterface.createdAt) &&
        Objects.equals(this.currency, quoteDataCartInterface.currency) &&
        Objects.equals(this.customer, quoteDataCartInterface.customer) &&
        Objects.equals(this.customerIsGuest, quoteDataCartInterface.customerIsGuest) &&
        Objects.equals(this.customerNote, quoteDataCartInterface.customerNote) &&
        Objects.equals(this.customerNoteNotify, quoteDataCartInterface.customerNoteNotify) &&
        Objects.equals(this.customerTaxClassId, quoteDataCartInterface.customerTaxClassId) &&
        Objects.equals(this.extensionAttributes, quoteDataCartInterface.extensionAttributes) &&
        Objects.equals(this.id, quoteDataCartInterface.id) &&
        Objects.equals(this.isActive, quoteDataCartInterface.isActive) &&
        Objects.equals(this.isVirtual, quoteDataCartInterface.isVirtual) &&
        Objects.equals(this.items, quoteDataCartInterface.items) &&
        Objects.equals(this.itemsCount, quoteDataCartInterface.itemsCount) &&
        Objects.equals(this.itemsQty, quoteDataCartInterface.itemsQty) &&
        Objects.equals(this.origOrderId, quoteDataCartInterface.origOrderId) &&
        Objects.equals(this.reservedOrderId, quoteDataCartInterface.reservedOrderId) &&
        Objects.equals(this.storeId, quoteDataCartInterface.storeId) &&
        Objects.equals(this.updatedAt, quoteDataCartInterface.updatedAt);
  }

  @Override
  public int hashCode() {
    return Objects.hash(billingAddress, convertedAt, createdAt, currency, customer, customerIsGuest, customerNote, customerNoteNotify, customerTaxClassId, extensionAttributes, id, isActive, isVirtual, items, itemsCount, itemsQty, origOrderId, reservedOrderId, storeId, updatedAt);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class QuoteDataCartInterface {\n");
    sb.append("    billingAddress: ").append(toIndentedString(billingAddress)).append("\n");
    sb.append("    convertedAt: ").append(toIndentedString(convertedAt)).append("\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    currency: ").append(toIndentedString(currency)).append("\n");
    sb.append("    customer: ").append(toIndentedString(customer)).append("\n");
    sb.append("    customerIsGuest: ").append(toIndentedString(customerIsGuest)).append("\n");
    sb.append("    customerNote: ").append(toIndentedString(customerNote)).append("\n");
    sb.append("    customerNoteNotify: ").append(toIndentedString(customerNoteNotify)).append("\n");
    sb.append("    customerTaxClassId: ").append(toIndentedString(customerTaxClassId)).append("\n");
    sb.append("    extensionAttributes: ").append(toIndentedString(extensionAttributes)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    isActive: ").append(toIndentedString(isActive)).append("\n");
    sb.append("    isVirtual: ").append(toIndentedString(isVirtual)).append("\n");
    sb.append("    items: ").append(toIndentedString(items)).append("\n");
    sb.append("    itemsCount: ").append(toIndentedString(itemsCount)).append("\n");
    sb.append("    itemsQty: ").append(toIndentedString(itemsQty)).append("\n");
    sb.append("    origOrderId: ").append(toIndentedString(origOrderId)).append("\n");
    sb.append("    reservedOrderId: ").append(toIndentedString(reservedOrderId)).append("\n");
    sb.append("    storeId: ").append(toIndentedString(storeId)).append("\n");
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
    openapiFields.add("billing_address");
    openapiFields.add("converted_at");
    openapiFields.add("created_at");
    openapiFields.add("currency");
    openapiFields.add("customer");
    openapiFields.add("customer_is_guest");
    openapiFields.add("customer_note");
    openapiFields.add("customer_note_notify");
    openapiFields.add("customer_tax_class_id");
    openapiFields.add("extension_attributes");
    openapiFields.add("id");
    openapiFields.add("is_active");
    openapiFields.add("is_virtual");
    openapiFields.add("items");
    openapiFields.add("items_count");
    openapiFields.add("items_qty");
    openapiFields.add("orig_order_id");
    openapiFields.add("reserved_order_id");
    openapiFields.add("store_id");
    openapiFields.add("updated_at");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("customer");
    openapiRequiredFields.add("id");
    openapiRequiredFields.add("store_id");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to QuoteDataCartInterface
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!QuoteDataCartInterface.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in QuoteDataCartInterface is not found in the empty JSON string", QuoteDataCartInterface.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!QuoteDataCartInterface.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `QuoteDataCartInterface` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : QuoteDataCartInterface.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `billing_address`
      if (jsonObj.get("billing_address") != null && !jsonObj.get("billing_address").isJsonNull()) {
        QuoteDataAddressInterface.validateJsonElement(jsonObj.get("billing_address"));
      }
      if ((jsonObj.get("converted_at") != null && !jsonObj.get("converted_at").isJsonNull()) && !jsonObj.get("converted_at").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `converted_at` to be a primitive type in the JSON string but got `%s`", jsonObj.get("converted_at").toString()));
      }
      if ((jsonObj.get("created_at") != null && !jsonObj.get("created_at").isJsonNull()) && !jsonObj.get("created_at").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `created_at` to be a primitive type in the JSON string but got `%s`", jsonObj.get("created_at").toString()));
      }
      // validate the optional field `currency`
      if (jsonObj.get("currency") != null && !jsonObj.get("currency").isJsonNull()) {
        QuoteDataCurrencyInterface.validateJsonElement(jsonObj.get("currency"));
      }
      // validate the required field `customer`
      CustomerDataCustomerInterface.validateJsonElement(jsonObj.get("customer"));
      if ((jsonObj.get("customer_note") != null && !jsonObj.get("customer_note").isJsonNull()) && !jsonObj.get("customer_note").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `customer_note` to be a primitive type in the JSON string but got `%s`", jsonObj.get("customer_note").toString()));
      }
      // validate the optional field `extension_attributes`
      if (jsonObj.get("extension_attributes") != null && !jsonObj.get("extension_attributes").isJsonNull()) {
        QuoteDataCartExtensionInterface.validateJsonElement(jsonObj.get("extension_attributes"));
      }
      if (jsonObj.get("items") != null && !jsonObj.get("items").isJsonNull()) {
        JsonArray jsonArrayitems = jsonObj.getAsJsonArray("items");
        if (jsonArrayitems != null) {
          // ensure the json data is an array
          if (!jsonObj.get("items").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `items` to be an array in the JSON string but got `%s`", jsonObj.get("items").toString()));
          }

          // validate the optional field `items` (array)
          for (int i = 0; i < jsonArrayitems.size(); i++) {
            QuoteDataCartItemInterface.validateJsonElement(jsonArrayitems.get(i));
          };
        }
      }
      if ((jsonObj.get("reserved_order_id") != null && !jsonObj.get("reserved_order_id").isJsonNull()) && !jsonObj.get("reserved_order_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `reserved_order_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("reserved_order_id").toString()));
      }
      if ((jsonObj.get("updated_at") != null && !jsonObj.get("updated_at").isJsonNull()) && !jsonObj.get("updated_at").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `updated_at` to be a primitive type in the JSON string but got `%s`", jsonObj.get("updated_at").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!QuoteDataCartInterface.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'QuoteDataCartInterface' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<QuoteDataCartInterface> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(QuoteDataCartInterface.class));

       return (TypeAdapter<T>) new TypeAdapter<QuoteDataCartInterface>() {
           @Override
           public void write(JsonWriter out, QuoteDataCartInterface value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public QuoteDataCartInterface read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of QuoteDataCartInterface given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of QuoteDataCartInterface
   * @throws IOException if the JSON string is invalid with respect to QuoteDataCartInterface
   */
  public static QuoteDataCartInterface fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, QuoteDataCartInterface.class);
  }

  /**
   * Convert an instance of QuoteDataCartInterface to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

