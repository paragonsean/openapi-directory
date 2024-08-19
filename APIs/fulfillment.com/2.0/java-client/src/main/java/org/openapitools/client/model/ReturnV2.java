/*
 * Fulfillment.com APIv2
 * Welcome to our current iteration of our REST API. While we encourage you to upgrade to v2.0 we will continue support for our [SOAP API](https://github.com/fulfillment/soap-integration).  # Versioning  The Fulfillment.com (FDC) REST API is version controlled and backwards compatible. We have many future APIs scheduled for publication within our v2.0 spec so please be prepared for us to add data nodes in our responses, however, we will not remove knowledge from previously published APIs.  #### A Current Response  ```javascript {   id: 123 } ```  #### A Potential Future Response  ```javascript {   id: 123,   reason: \"More Knowledge\" } ```  # Getting Started  We use OAuth v2.0 to authenticate clients, you can choose [implicit](https://oauth.net/2/grant-types/implicit/) or [password](https://oauth.net/2/grant-types/password/) grant type. To obtain an OAuth `client_id` and `client_secret` contact your account executive.  **Tip**: Generate an additional login and use those credentials for your integration so that changes are accredited to that \"user\".  You are now ready to make requests to our other APIs by filling your `Authorization` header with `Bearer {access_token}`.  ## Perpetuating Access  Perpetuating access to FDC without storing your password locally can be achieved using the `refresh_token` returned by [POST /oauth/access_token](#operation/generateToken).  A simple concept to achieve this is outlined below.  1. Your application/script will ask you for your `username` and `password`, your `client_id` and `client_secret` will be accessible via a DB or ENV. 2. [Request an access_token](#operation/generateToken)   + Your function should be capable of formatting your request for both a `grant_type` of \\\"password\\\" (step 1) and \\\"refresh_token\\\" (step 4). 3. Store the `access_token` and `refresh_token` so future requests can skip step 1 4. When the `access_token` expires request anew using your `refresh_token`, replace both tokens in local storage.  + If this fails you will have to revert to step 1.  Alternatively if you choose for your application/script to have access to your `username` and `password` you can skip step 4.  In all scenarios we recommend storing all credentials outside your codebase.  ## Date Time Definitions  We will report all date-time stamps using the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) standard. When using listing API's where fromDate and toDate are available note that both dates are inclusive while requiring the fromDate to be before or at the toDate.  ### The Fulfillment Process  Many steps are required to fulfill your order we report back to you three fundamental milestones inside the orders model.  * `recordedOn` When we received your order. This will never change.  * `dispatchDate` When the current iteration of your order was scheduled for fulfillment. This may change however it is an indicator that the physical process of fulfillment has begun and a tracking number has been **assigned** to your order. The tracking number **MAY CHANGE**. You will not be able to cancel an order once it has been dispatched. If you need to recall an order that has been dispatched please contact your account executive.  * `departDate` When we recorded your order passing our final inspection and placed with the carrier. At this point it is **safe to inform the consignee** of the tracking number as it will not change.  ## Evaluating Error Responses  We currently return two different error models, with and without context. All errors will include a `message` node while errors with `context` will include additional information designed to save you time when encountering highly probable errors. For example, when you send us a request to create a duplicate order, we will reject your request and the context will include the FDC order `id` so that you may record it for your records.  ### Without Context  New order with missing required fields.  | Header | Response | | ------ | -------- | | Status | `400 Bad Request` |  ```javascript {       \"message\": \"Invalid request body\" } ```  ### With Context  New order with duplicate `merchantOrderId`.  | Header | Response | | ------ | -------- | | Status | `409 Conflict` |  ```javascript {   \"message\": \"Duplicate Order\",   \"context\": {     \"id\": 123   } } ```  ## Status Codes  Codes are a concatenation of State, Stage, and Detail.  `^([0-9]{2})([0-9]{2})([0-9]{2})$`  | Code | State              | Stage    | Detail         | | ---- | ------------------ | -------- | -------------- | | 010101 | Processing Order | Recieved | Customer Order | | 010102 | Processing Order | Recieved | Recieved | | 010201 | Processing Order | Approved | | | 010301 | Processing Order | Hold | Merchant Stock | | 010302 | Processing Order | Hold | Merchant Funds | | 010303 | Processing Order | Hold | For Merchant | | 010304 | Processing Order | Hold | Oversized Shipment | | 010305 | Processing Order | Hold | Invalid Parent Order | | 010306 | Processing Order | Hold | Invalid Address | | 010307 | Processing Order | Hold | By Admin | | 010401 | Processing Order | Address Problem | Incomplete Address | | 010402 | Processing Order | Address Problem | Invalid Locality | | 010403 | Processing Order | Address Problem | Invalid Region | | 010404 | Processing Order | Address Problem | Address Not Found | | 010405 | Processing Order | Address Problem | Many Addresses Found | | 010406 | Processing Order | Address Problem | Invalid Postal Code | | 010407 | Processing Order | Address Problem | Country Not Mapped | | 010408 | Processing Order | Address Problem | Invalid Recipient Name | | 010409 | Processing Order | Address Problem | Bad UK Address | | 010410 | Processing Order | Address Problem | Invalid Address Line 1 or 2 | | 010501 | Processing Order | Sku Problem | Invalid SKU | | 010501 | Processing Order | Sku Problem | Child Order has Invalid SKUs | | 010601 | Processing Order | Facility Problem | Facility Not Mapped | | 010701 | Processing Order | Ship Method Problem | Unmapped Ship Method | | 010702 | Processing Order | Ship Method Problem | Unmapped Ship Cost | | 010703 | Processing Order | Ship Method Problem | Missing Ship Method | | 010704 | Processing Order | Ship Method Problem | Invalid Ship Method | | 010705 | Processing Order | Ship Method Problem | Order Weight Outside of Ship Method Weight | | 010801 | Processing Order | Inventory Problem | Insufficient Inventory In Facility | | 010802 | Processing Order | Inventory Problem | Issue Encountered During Inventory Adjustment | | 010901 | Processing Order | Released To WMS | Released | | 020101 | Fulfillment In Progress | Postage Problem | Address Issue | | 020102 | Fulfillment In Progress | Postage Problem | Postage OK, OMS Issue Occurred | | 020103 | Fulfillment In Progress | Postage Problem | Postage Void Failed | | 020201 | Fulfillment In Progress | Postage Acquired | | | 020301 | Fulfillment In Progress | Postage Voided | Postage Void Failed Gracefully | | 020301 | Fulfillment In Progress | Hold | Departure Hold Requested | | 020401 | Fulfillment In Progress | 4PL Processing | | | 020501 | Fulfillment In Progress | 4PL Problem | Order is Proccessable, Postage Issue Occurred | | 020601 | Fulfillment In Progress | Label Printed | | | 020701 | Fulfillment In Progress | Shipment Cubed | | | 020801 | Fulfillment In Progress | Picking Inventory | | | 020901 | Fulfillment In Progress | Label Print Verified | | | 021001 | Fulfillment In Progress | Passed Final Inspection | | | 030101 | Shipped | Fulfilled By 4PL | | | 030102 | Shipped | Fulfilled By 4PL | Successfully Fulfilled, OMS Encountered Issue During Processing | | 030201 | Shipped | Fulfilled By FDC | | | 040101 | Returned | Returned | | | 050101 | Cancelled | Cancelled | | | 060101 | Test | Test | Test | 
 *
 * The version of the OpenAPI document: 2.0
 * Contact: dev@fulfillment.com
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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.ReturnV2Order;
import org.openapitools.client.model.ReturnV2Reason;
import org.openapitools.client.model.RmaItemV2;
import org.openapitools.client.model.UserV2;
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
 * ReturnV2
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:32:09.361421-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ReturnV2 {
  public static final String SERIALIZED_NAME_COMMENTS = "comments";
  @SerializedName(SERIALIZED_NAME_COMMENTS)
  private String comments;

  public static final String SERIALIZED_NAME_CREATED_AT = "createdAt";
  @SerializedName(SERIALIZED_NAME_CREATED_AT)
  private OffsetDateTime createdAt;

  public static final String SERIALIZED_NAME_CREATED_BY = "createdBy";
  @SerializedName(SERIALIZED_NAME_CREATED_BY)
  private Object createdBy = null;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_ORDER = "order";
  @SerializedName(SERIALIZED_NAME_ORDER)
  private ReturnV2Order order;

  public static final String SERIALIZED_NAME_REASON = "reason";
  @SerializedName(SERIALIZED_NAME_REASON)
  private ReturnV2Reason reason;

  public static final String SERIALIZED_NAME_RETURNED_BY = "returnedBy";
  @SerializedName(SERIALIZED_NAME_RETURNED_BY)
  private String returnedBy;

  public static final String SERIALIZED_NAME_RMA_ITEMS = "rmaItems";
  @SerializedName(SERIALIZED_NAME_RMA_ITEMS)
  private List<RmaItemV2> rmaItems = new ArrayList<>();

  public static final String SERIALIZED_NAME_RMA_NUMBER = "rmaNumber";
  @SerializedName(SERIALIZED_NAME_RMA_NUMBER)
  private String rmaNumber;

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private ReturnV2Reason status;

  public static final String SERIALIZED_NAME_UPDATED_AT = "updatedAt";
  @SerializedName(SERIALIZED_NAME_UPDATED_AT)
  private OffsetDateTime updatedAt;

  public static final String SERIALIZED_NAME_UPDATED_BY = "updatedBy";
  @SerializedName(SERIALIZED_NAME_UPDATED_BY)
  private UserV2 updatedBy;

  public ReturnV2() {
  }

  public ReturnV2 comments(String comments) {
    this.comments = comments;
    return this;
  }

  /**
   * Get comments
   * @return comments
   */
  @javax.annotation.Nullable
  public String getComments() {
    return comments;
  }

  public void setComments(String comments) {
    this.comments = comments;
  }


  public ReturnV2 createdAt(OffsetDateTime createdAt) {
    this.createdAt = createdAt;
    return this;
  }

  /**
   * Get createdAt
   * @return createdAt
   */
  @javax.annotation.Nonnull
  public OffsetDateTime getCreatedAt() {
    return createdAt;
  }

  public void setCreatedAt(OffsetDateTime createdAt) {
    this.createdAt = createdAt;
  }


  public ReturnV2 createdBy(Object createdBy) {
    this.createdBy = createdBy;
    return this;
  }

  /**
   * Get createdBy
   * @return createdBy
   */
  @javax.annotation.Nonnull
  public Object getCreatedBy() {
    return createdBy;
  }

  public void setCreatedBy(Object createdBy) {
    this.createdBy = createdBy;
  }


  public ReturnV2 id(Integer id) {
    this.id = id;
    return this;
  }

  /**
   * Get id
   * @return id
   */
  @javax.annotation.Nonnull
  public Integer getId() {
    return id;
  }

  public void setId(Integer id) {
    this.id = id;
  }


  public ReturnV2 order(ReturnV2Order order) {
    this.order = order;
    return this;
  }

  /**
   * Get order
   * @return order
   */
  @javax.annotation.Nullable
  public ReturnV2Order getOrder() {
    return order;
  }

  public void setOrder(ReturnV2Order order) {
    this.order = order;
  }


  public ReturnV2 reason(ReturnV2Reason reason) {
    this.reason = reason;
    return this;
  }

  /**
   * Get reason
   * @return reason
   */
  @javax.annotation.Nonnull
  public ReturnV2Reason getReason() {
    return reason;
  }

  public void setReason(ReturnV2Reason reason) {
    this.reason = reason;
  }


  public ReturnV2 returnedBy(String returnedBy) {
    this.returnedBy = returnedBy;
    return this;
  }

  /**
   * Get returnedBy
   * @return returnedBy
   */
  @javax.annotation.Nullable
  public String getReturnedBy() {
    return returnedBy;
  }

  public void setReturnedBy(String returnedBy) {
    this.returnedBy = returnedBy;
  }


  public ReturnV2 rmaItems(List<RmaItemV2> rmaItems) {
    this.rmaItems = rmaItems;
    return this;
  }

  public ReturnV2 addRmaItemsItem(RmaItemV2 rmaItemsItem) {
    if (this.rmaItems == null) {
      this.rmaItems = new ArrayList<>();
    }
    this.rmaItems.add(rmaItemsItem);
    return this;
  }

  /**
   * Get rmaItems
   * @return rmaItems
   */
  @javax.annotation.Nullable
  public List<RmaItemV2> getRmaItems() {
    return rmaItems;
  }

  public void setRmaItems(List<RmaItemV2> rmaItems) {
    this.rmaItems = rmaItems;
  }


  public ReturnV2 rmaNumber(String rmaNumber) {
    this.rmaNumber = rmaNumber;
    return this;
  }

  /**
   * Get rmaNumber
   * @return rmaNumber
   */
  @javax.annotation.Nullable
  public String getRmaNumber() {
    return rmaNumber;
  }

  public void setRmaNumber(String rmaNumber) {
    this.rmaNumber = rmaNumber;
  }


  public ReturnV2 status(ReturnV2Reason status) {
    this.status = status;
    return this;
  }

  /**
   * Get status
   * @return status
   */
  @javax.annotation.Nonnull
  public ReturnV2Reason getStatus() {
    return status;
  }

  public void setStatus(ReturnV2Reason status) {
    this.status = status;
  }


  public ReturnV2 updatedAt(OffsetDateTime updatedAt) {
    this.updatedAt = updatedAt;
    return this;
  }

  /**
   * Get updatedAt
   * @return updatedAt
   */
  @javax.annotation.Nonnull
  public OffsetDateTime getUpdatedAt() {
    return updatedAt;
  }

  public void setUpdatedAt(OffsetDateTime updatedAt) {
    this.updatedAt = updatedAt;
  }


  public ReturnV2 updatedBy(UserV2 updatedBy) {
    this.updatedBy = updatedBy;
    return this;
  }

  /**
   * Get updatedBy
   * @return updatedBy
   */
  @javax.annotation.Nonnull
  public UserV2 getUpdatedBy() {
    return updatedBy;
  }

  public void setUpdatedBy(UserV2 updatedBy) {
    this.updatedBy = updatedBy;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ReturnV2 returnV2 = (ReturnV2) o;
    return Objects.equals(this.comments, returnV2.comments) &&
        Objects.equals(this.createdAt, returnV2.createdAt) &&
        Objects.equals(this.createdBy, returnV2.createdBy) &&
        Objects.equals(this.id, returnV2.id) &&
        Objects.equals(this.order, returnV2.order) &&
        Objects.equals(this.reason, returnV2.reason) &&
        Objects.equals(this.returnedBy, returnV2.returnedBy) &&
        Objects.equals(this.rmaItems, returnV2.rmaItems) &&
        Objects.equals(this.rmaNumber, returnV2.rmaNumber) &&
        Objects.equals(this.status, returnV2.status) &&
        Objects.equals(this.updatedAt, returnV2.updatedAt) &&
        Objects.equals(this.updatedBy, returnV2.updatedBy);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(comments, createdAt, createdBy, id, order, reason, returnedBy, rmaItems, rmaNumber, status, updatedAt, updatedBy);
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
    sb.append("class ReturnV2 {\n");
    sb.append("    comments: ").append(toIndentedString(comments)).append("\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    createdBy: ").append(toIndentedString(createdBy)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    order: ").append(toIndentedString(order)).append("\n");
    sb.append("    reason: ").append(toIndentedString(reason)).append("\n");
    sb.append("    returnedBy: ").append(toIndentedString(returnedBy)).append("\n");
    sb.append("    rmaItems: ").append(toIndentedString(rmaItems)).append("\n");
    sb.append("    rmaNumber: ").append(toIndentedString(rmaNumber)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    updatedAt: ").append(toIndentedString(updatedAt)).append("\n");
    sb.append("    updatedBy: ").append(toIndentedString(updatedBy)).append("\n");
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
    openapiFields.add("comments");
    openapiFields.add("createdAt");
    openapiFields.add("createdBy");
    openapiFields.add("id");
    openapiFields.add("order");
    openapiFields.add("reason");
    openapiFields.add("returnedBy");
    openapiFields.add("rmaItems");
    openapiFields.add("rmaNumber");
    openapiFields.add("status");
    openapiFields.add("updatedAt");
    openapiFields.add("updatedBy");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("createdAt");
    openapiRequiredFields.add("createdBy");
    openapiRequiredFields.add("id");
    openapiRequiredFields.add("reason");
    openapiRequiredFields.add("status");
    openapiRequiredFields.add("updatedAt");
    openapiRequiredFields.add("updatedBy");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ReturnV2
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ReturnV2.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ReturnV2 is not found in the empty JSON string", ReturnV2.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ReturnV2.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ReturnV2` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : ReturnV2.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("comments") != null && !jsonObj.get("comments").isJsonNull()) && !jsonObj.get("comments").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `comments` to be a primitive type in the JSON string but got `%s`", jsonObj.get("comments").toString()));
      }
      // validate the optional field `order`
      if (jsonObj.get("order") != null && !jsonObj.get("order").isJsonNull()) {
        ReturnV2Order.validateJsonElement(jsonObj.get("order"));
      }
      // validate the required field `reason`
      ReturnV2Reason.validateJsonElement(jsonObj.get("reason"));
      if ((jsonObj.get("returnedBy") != null && !jsonObj.get("returnedBy").isJsonNull()) && !jsonObj.get("returnedBy").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `returnedBy` to be a primitive type in the JSON string but got `%s`", jsonObj.get("returnedBy").toString()));
      }
      if (jsonObj.get("rmaItems") != null && !jsonObj.get("rmaItems").isJsonNull()) {
        JsonArray jsonArrayrmaItems = jsonObj.getAsJsonArray("rmaItems");
        if (jsonArrayrmaItems != null) {
          // ensure the json data is an array
          if (!jsonObj.get("rmaItems").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `rmaItems` to be an array in the JSON string but got `%s`", jsonObj.get("rmaItems").toString()));
          }

          // validate the optional field `rmaItems` (array)
          for (int i = 0; i < jsonArrayrmaItems.size(); i++) {
            RmaItemV2.validateJsonElement(jsonArrayrmaItems.get(i));
          };
        }
      }
      if ((jsonObj.get("rmaNumber") != null && !jsonObj.get("rmaNumber").isJsonNull()) && !jsonObj.get("rmaNumber").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `rmaNumber` to be a primitive type in the JSON string but got `%s`", jsonObj.get("rmaNumber").toString()));
      }
      // validate the required field `status`
      ReturnV2Reason.validateJsonElement(jsonObj.get("status"));
      // validate the required field `updatedBy`
      UserV2.validateJsonElement(jsonObj.get("updatedBy"));
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ReturnV2.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ReturnV2' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ReturnV2> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ReturnV2.class));

       return (TypeAdapter<T>) new TypeAdapter<ReturnV2>() {
           @Override
           public void write(JsonWriter out, ReturnV2 value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ReturnV2 read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ReturnV2 given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ReturnV2
   * @throws IOException if the JSON string is invalid with respect to ReturnV2
   */
  public static ReturnV2 fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ReturnV2.class);
  }

  /**
   * Convert an instance of ReturnV2 to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

