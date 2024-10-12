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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

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
 * Transaction interface. A transaction is an interaction between a merchant and a customer such as a purchase, a credit, a refund, and so on.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:51.810681-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class SalesDataTransactionInterface {
  public static final String SERIALIZED_NAME_ADDITIONAL_INFORMATION = "additional_information";
  @SerializedName(SERIALIZED_NAME_ADDITIONAL_INFORMATION)
  private List<String> additionalInformation = new ArrayList<>();

  public static final String SERIALIZED_NAME_CHILD_TRANSACTIONS = "child_transactions";
  @SerializedName(SERIALIZED_NAME_CHILD_TRANSACTIONS)
  private List<SalesDataTransactionInterface> childTransactions = new ArrayList<>();

  public static final String SERIALIZED_NAME_CREATED_AT = "created_at";
  @SerializedName(SERIALIZED_NAME_CREATED_AT)
  private String createdAt;

  public static final String SERIALIZED_NAME_EXTENSION_ATTRIBUTES = "extension_attributes";
  @SerializedName(SERIALIZED_NAME_EXTENSION_ATTRIBUTES)
  private Object extensionAttributes;

  public static final String SERIALIZED_NAME_IS_CLOSED = "is_closed";
  @SerializedName(SERIALIZED_NAME_IS_CLOSED)
  private Integer isClosed;

  public static final String SERIALIZED_NAME_ORDER_ID = "order_id";
  @SerializedName(SERIALIZED_NAME_ORDER_ID)
  private Integer orderId;

  public static final String SERIALIZED_NAME_PARENT_ID = "parent_id";
  @SerializedName(SERIALIZED_NAME_PARENT_ID)
  private Integer parentId;

  public static final String SERIALIZED_NAME_PARENT_TXN_ID = "parent_txn_id";
  @SerializedName(SERIALIZED_NAME_PARENT_TXN_ID)
  private String parentTxnId;

  public static final String SERIALIZED_NAME_PAYMENT_ID = "payment_id";
  @SerializedName(SERIALIZED_NAME_PAYMENT_ID)
  private Integer paymentId;

  public static final String SERIALIZED_NAME_TRANSACTION_ID = "transaction_id";
  @SerializedName(SERIALIZED_NAME_TRANSACTION_ID)
  private Integer transactionId;

  public static final String SERIALIZED_NAME_TXN_ID = "txn_id";
  @SerializedName(SERIALIZED_NAME_TXN_ID)
  private String txnId;

  public static final String SERIALIZED_NAME_TXN_TYPE = "txn_type";
  @SerializedName(SERIALIZED_NAME_TXN_TYPE)
  private String txnType;

  public SalesDataTransactionInterface() {
  }

  public SalesDataTransactionInterface additionalInformation(List<String> additionalInformation) {
    this.additionalInformation = additionalInformation;
    return this;
  }

  public SalesDataTransactionInterface addAdditionalInformationItem(String additionalInformationItem) {
    if (this.additionalInformation == null) {
      this.additionalInformation = new ArrayList<>();
    }
    this.additionalInformation.add(additionalInformationItem);
    return this;
  }

  /**
   * Array of additional information. Otherwise, null.
   * @return additionalInformation
   */
  @javax.annotation.Nullable
  public List<String> getAdditionalInformation() {
    return additionalInformation;
  }

  public void setAdditionalInformation(List<String> additionalInformation) {
    this.additionalInformation = additionalInformation;
  }


  public SalesDataTransactionInterface childTransactions(List<SalesDataTransactionInterface> childTransactions) {
    this.childTransactions = childTransactions;
    return this;
  }

  public SalesDataTransactionInterface addChildTransactionsItem(SalesDataTransactionInterface childTransactionsItem) {
    if (this.childTransactions == null) {
      this.childTransactions = new ArrayList<>();
    }
    this.childTransactions.add(childTransactionsItem);
    return this;
  }

  /**
   * Array of child transactions.
   * @return childTransactions
   */
  @javax.annotation.Nonnull
  public List<SalesDataTransactionInterface> getChildTransactions() {
    return childTransactions;
  }

  public void setChildTransactions(List<SalesDataTransactionInterface> childTransactions) {
    this.childTransactions = childTransactions;
  }


  public SalesDataTransactionInterface createdAt(String createdAt) {
    this.createdAt = createdAt;
    return this;
  }

  /**
   * Created-at timestamp.
   * @return createdAt
   */
  @javax.annotation.Nonnull
  public String getCreatedAt() {
    return createdAt;
  }

  public void setCreatedAt(String createdAt) {
    this.createdAt = createdAt;
  }


  public SalesDataTransactionInterface extensionAttributes(Object extensionAttributes) {
    this.extensionAttributes = extensionAttributes;
    return this;
  }

  /**
   * ExtensionInterface class for @see \\Magento\\Sales\\Api\\Data\\TransactionInterface
   * @return extensionAttributes
   */
  @javax.annotation.Nullable
  public Object getExtensionAttributes() {
    return extensionAttributes;
  }

  public void setExtensionAttributes(Object extensionAttributes) {
    this.extensionAttributes = extensionAttributes;
  }


  public SalesDataTransactionInterface isClosed(Integer isClosed) {
    this.isClosed = isClosed;
    return this;
  }

  /**
   * Is-closed flag value.
   * @return isClosed
   */
  @javax.annotation.Nonnull
  public Integer getIsClosed() {
    return isClosed;
  }

  public void setIsClosed(Integer isClosed) {
    this.isClosed = isClosed;
  }


  public SalesDataTransactionInterface orderId(Integer orderId) {
    this.orderId = orderId;
    return this;
  }

  /**
   * Order ID.
   * @return orderId
   */
  @javax.annotation.Nonnull
  public Integer getOrderId() {
    return orderId;
  }

  public void setOrderId(Integer orderId) {
    this.orderId = orderId;
  }


  public SalesDataTransactionInterface parentId(Integer parentId) {
    this.parentId = parentId;
    return this;
  }

  /**
   * The parent ID for the transaction. Otherwise, null.
   * @return parentId
   */
  @javax.annotation.Nullable
  public Integer getParentId() {
    return parentId;
  }

  public void setParentId(Integer parentId) {
    this.parentId = parentId;
  }


  public SalesDataTransactionInterface parentTxnId(String parentTxnId) {
    this.parentTxnId = parentTxnId;
    return this;
  }

  /**
   * Parent transaction business ID.
   * @return parentTxnId
   */
  @javax.annotation.Nonnull
  public String getParentTxnId() {
    return parentTxnId;
  }

  public void setParentTxnId(String parentTxnId) {
    this.parentTxnId = parentTxnId;
  }


  public SalesDataTransactionInterface paymentId(Integer paymentId) {
    this.paymentId = paymentId;
    return this;
  }

  /**
   * Payment ID.
   * @return paymentId
   */
  @javax.annotation.Nonnull
  public Integer getPaymentId() {
    return paymentId;
  }

  public void setPaymentId(Integer paymentId) {
    this.paymentId = paymentId;
  }


  public SalesDataTransactionInterface transactionId(Integer transactionId) {
    this.transactionId = transactionId;
    return this;
  }

  /**
   * Transaction ID.
   * @return transactionId
   */
  @javax.annotation.Nonnull
  public Integer getTransactionId() {
    return transactionId;
  }

  public void setTransactionId(Integer transactionId) {
    this.transactionId = transactionId;
  }


  public SalesDataTransactionInterface txnId(String txnId) {
    this.txnId = txnId;
    return this;
  }

  /**
   * Transaction business ID.
   * @return txnId
   */
  @javax.annotation.Nonnull
  public String getTxnId() {
    return txnId;
  }

  public void setTxnId(String txnId) {
    this.txnId = txnId;
  }


  public SalesDataTransactionInterface txnType(String txnType) {
    this.txnType = txnType;
    return this;
  }

  /**
   * Transaction type.
   * @return txnType
   */
  @javax.annotation.Nonnull
  public String getTxnType() {
    return txnType;
  }

  public void setTxnType(String txnType) {
    this.txnType = txnType;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    SalesDataTransactionInterface salesDataTransactionInterface = (SalesDataTransactionInterface) o;
    return Objects.equals(this.additionalInformation, salesDataTransactionInterface.additionalInformation) &&
        Objects.equals(this.childTransactions, salesDataTransactionInterface.childTransactions) &&
        Objects.equals(this.createdAt, salesDataTransactionInterface.createdAt) &&
        Objects.equals(this.extensionAttributes, salesDataTransactionInterface.extensionAttributes) &&
        Objects.equals(this.isClosed, salesDataTransactionInterface.isClosed) &&
        Objects.equals(this.orderId, salesDataTransactionInterface.orderId) &&
        Objects.equals(this.parentId, salesDataTransactionInterface.parentId) &&
        Objects.equals(this.parentTxnId, salesDataTransactionInterface.parentTxnId) &&
        Objects.equals(this.paymentId, salesDataTransactionInterface.paymentId) &&
        Objects.equals(this.transactionId, salesDataTransactionInterface.transactionId) &&
        Objects.equals(this.txnId, salesDataTransactionInterface.txnId) &&
        Objects.equals(this.txnType, salesDataTransactionInterface.txnType);
  }

  @Override
  public int hashCode() {
    return Objects.hash(additionalInformation, childTransactions, createdAt, extensionAttributes, isClosed, orderId, parentId, parentTxnId, paymentId, transactionId, txnId, txnType);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class SalesDataTransactionInterface {\n");
    sb.append("    additionalInformation: ").append(toIndentedString(additionalInformation)).append("\n");
    sb.append("    childTransactions: ").append(toIndentedString(childTransactions)).append("\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    extensionAttributes: ").append(toIndentedString(extensionAttributes)).append("\n");
    sb.append("    isClosed: ").append(toIndentedString(isClosed)).append("\n");
    sb.append("    orderId: ").append(toIndentedString(orderId)).append("\n");
    sb.append("    parentId: ").append(toIndentedString(parentId)).append("\n");
    sb.append("    parentTxnId: ").append(toIndentedString(parentTxnId)).append("\n");
    sb.append("    paymentId: ").append(toIndentedString(paymentId)).append("\n");
    sb.append("    transactionId: ").append(toIndentedString(transactionId)).append("\n");
    sb.append("    txnId: ").append(toIndentedString(txnId)).append("\n");
    sb.append("    txnType: ").append(toIndentedString(txnType)).append("\n");
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
    openapiFields.add("additional_information");
    openapiFields.add("child_transactions");
    openapiFields.add("created_at");
    openapiFields.add("extension_attributes");
    openapiFields.add("is_closed");
    openapiFields.add("order_id");
    openapiFields.add("parent_id");
    openapiFields.add("parent_txn_id");
    openapiFields.add("payment_id");
    openapiFields.add("transaction_id");
    openapiFields.add("txn_id");
    openapiFields.add("txn_type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("child_transactions");
    openapiRequiredFields.add("created_at");
    openapiRequiredFields.add("is_closed");
    openapiRequiredFields.add("order_id");
    openapiRequiredFields.add("parent_txn_id");
    openapiRequiredFields.add("payment_id");
    openapiRequiredFields.add("transaction_id");
    openapiRequiredFields.add("txn_id");
    openapiRequiredFields.add("txn_type");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to SalesDataTransactionInterface
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!SalesDataTransactionInterface.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in SalesDataTransactionInterface is not found in the empty JSON string", SalesDataTransactionInterface.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!SalesDataTransactionInterface.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `SalesDataTransactionInterface` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : SalesDataTransactionInterface.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the optional json data is an array if present
      if (jsonObj.get("additional_information") != null && !jsonObj.get("additional_information").isJsonNull() && !jsonObj.get("additional_information").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `additional_information` to be an array in the JSON string but got `%s`", jsonObj.get("additional_information").toString()));
      }
      // ensure the json data is an array
      if (!jsonObj.get("child_transactions").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `child_transactions` to be an array in the JSON string but got `%s`", jsonObj.get("child_transactions").toString()));
      }

      JsonArray jsonArraychildTransactions = jsonObj.getAsJsonArray("child_transactions");
      // validate the required field `child_transactions` (array)
      for (int i = 0; i < jsonArraychildTransactions.size(); i++) {
        SalesDataTransactionInterface.validateJsonElement(jsonArraychildTransactions.get(i));
      };
      if (!jsonObj.get("created_at").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `created_at` to be a primitive type in the JSON string but got `%s`", jsonObj.get("created_at").toString()));
      }
      if (!jsonObj.get("parent_txn_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `parent_txn_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("parent_txn_id").toString()));
      }
      if (!jsonObj.get("txn_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `txn_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("txn_id").toString()));
      }
      if (!jsonObj.get("txn_type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `txn_type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("txn_type").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!SalesDataTransactionInterface.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'SalesDataTransactionInterface' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<SalesDataTransactionInterface> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(SalesDataTransactionInterface.class));

       return (TypeAdapter<T>) new TypeAdapter<SalesDataTransactionInterface>() {
           @Override
           public void write(JsonWriter out, SalesDataTransactionInterface value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public SalesDataTransactionInterface read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of SalesDataTransactionInterface given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of SalesDataTransactionInterface
   * @throws IOException if the JSON string is invalid with respect to SalesDataTransactionInterface
   */
  public static SalesDataTransactionInterface fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, SalesDataTransactionInterface.class);
  }

  /**
   * Convert an instance of SalesDataTransactionInterface to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

