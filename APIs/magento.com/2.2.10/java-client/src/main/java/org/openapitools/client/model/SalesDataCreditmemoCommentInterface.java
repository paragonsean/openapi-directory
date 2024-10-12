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
 * Credit memo comment interface. After a customer places and pays for an order and an invoice has been issued, the merchant can create a credit memo to refund all or part of the amount paid for any returned or undelivered items. The memo restores funds to the customer account so that the customer can make future purchases. A credit memo usually includes comments that detail why the credit memo amount was credited to the customer.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:51.810681-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class SalesDataCreditmemoCommentInterface {
  public static final String SERIALIZED_NAME_COMMENT = "comment";
  @SerializedName(SERIALIZED_NAME_COMMENT)
  private String comment;

  public static final String SERIALIZED_NAME_CREATED_AT = "created_at";
  @SerializedName(SERIALIZED_NAME_CREATED_AT)
  private String createdAt;

  public static final String SERIALIZED_NAME_ENTITY_ID = "entity_id";
  @SerializedName(SERIALIZED_NAME_ENTITY_ID)
  private Integer entityId;

  public static final String SERIALIZED_NAME_EXTENSION_ATTRIBUTES = "extension_attributes";
  @SerializedName(SERIALIZED_NAME_EXTENSION_ATTRIBUTES)
  private Object extensionAttributes;

  public static final String SERIALIZED_NAME_IS_CUSTOMER_NOTIFIED = "is_customer_notified";
  @SerializedName(SERIALIZED_NAME_IS_CUSTOMER_NOTIFIED)
  private Integer isCustomerNotified;

  public static final String SERIALIZED_NAME_IS_VISIBLE_ON_FRONT = "is_visible_on_front";
  @SerializedName(SERIALIZED_NAME_IS_VISIBLE_ON_FRONT)
  private Integer isVisibleOnFront;

  public static final String SERIALIZED_NAME_PARENT_ID = "parent_id";
  @SerializedName(SERIALIZED_NAME_PARENT_ID)
  private Integer parentId;

  public SalesDataCreditmemoCommentInterface() {
  }

  public SalesDataCreditmemoCommentInterface comment(String comment) {
    this.comment = comment;
    return this;
  }

  /**
   * Comment.
   * @return comment
   */
  @javax.annotation.Nonnull
  public String getComment() {
    return comment;
  }

  public void setComment(String comment) {
    this.comment = comment;
  }


  public SalesDataCreditmemoCommentInterface createdAt(String createdAt) {
    this.createdAt = createdAt;
    return this;
  }

  /**
   * Created-at timestamp.
   * @return createdAt
   */
  @javax.annotation.Nullable
  public String getCreatedAt() {
    return createdAt;
  }

  public void setCreatedAt(String createdAt) {
    this.createdAt = createdAt;
  }


  public SalesDataCreditmemoCommentInterface entityId(Integer entityId) {
    this.entityId = entityId;
    return this;
  }

  /**
   * Credit memo ID.
   * @return entityId
   */
  @javax.annotation.Nullable
  public Integer getEntityId() {
    return entityId;
  }

  public void setEntityId(Integer entityId) {
    this.entityId = entityId;
  }


  public SalesDataCreditmemoCommentInterface extensionAttributes(Object extensionAttributes) {
    this.extensionAttributes = extensionAttributes;
    return this;
  }

  /**
   * ExtensionInterface class for @see \\Magento\\Sales\\Api\\Data\\CreditmemoCommentInterface
   * @return extensionAttributes
   */
  @javax.annotation.Nullable
  public Object getExtensionAttributes() {
    return extensionAttributes;
  }

  public void setExtensionAttributes(Object extensionAttributes) {
    this.extensionAttributes = extensionAttributes;
  }


  public SalesDataCreditmemoCommentInterface isCustomerNotified(Integer isCustomerNotified) {
    this.isCustomerNotified = isCustomerNotified;
    return this;
  }

  /**
   * Is-customer-notified flag value.
   * @return isCustomerNotified
   */
  @javax.annotation.Nonnull
  public Integer getIsCustomerNotified() {
    return isCustomerNotified;
  }

  public void setIsCustomerNotified(Integer isCustomerNotified) {
    this.isCustomerNotified = isCustomerNotified;
  }


  public SalesDataCreditmemoCommentInterface isVisibleOnFront(Integer isVisibleOnFront) {
    this.isVisibleOnFront = isVisibleOnFront;
    return this;
  }

  /**
   * Is-visible-on-storefront flag value.
   * @return isVisibleOnFront
   */
  @javax.annotation.Nonnull
  public Integer getIsVisibleOnFront() {
    return isVisibleOnFront;
  }

  public void setIsVisibleOnFront(Integer isVisibleOnFront) {
    this.isVisibleOnFront = isVisibleOnFront;
  }


  public SalesDataCreditmemoCommentInterface parentId(Integer parentId) {
    this.parentId = parentId;
    return this;
  }

  /**
   * Parent ID.
   * @return parentId
   */
  @javax.annotation.Nonnull
  public Integer getParentId() {
    return parentId;
  }

  public void setParentId(Integer parentId) {
    this.parentId = parentId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    SalesDataCreditmemoCommentInterface salesDataCreditmemoCommentInterface = (SalesDataCreditmemoCommentInterface) o;
    return Objects.equals(this.comment, salesDataCreditmemoCommentInterface.comment) &&
        Objects.equals(this.createdAt, salesDataCreditmemoCommentInterface.createdAt) &&
        Objects.equals(this.entityId, salesDataCreditmemoCommentInterface.entityId) &&
        Objects.equals(this.extensionAttributes, salesDataCreditmemoCommentInterface.extensionAttributes) &&
        Objects.equals(this.isCustomerNotified, salesDataCreditmemoCommentInterface.isCustomerNotified) &&
        Objects.equals(this.isVisibleOnFront, salesDataCreditmemoCommentInterface.isVisibleOnFront) &&
        Objects.equals(this.parentId, salesDataCreditmemoCommentInterface.parentId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(comment, createdAt, entityId, extensionAttributes, isCustomerNotified, isVisibleOnFront, parentId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class SalesDataCreditmemoCommentInterface {\n");
    sb.append("    comment: ").append(toIndentedString(comment)).append("\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    entityId: ").append(toIndentedString(entityId)).append("\n");
    sb.append("    extensionAttributes: ").append(toIndentedString(extensionAttributes)).append("\n");
    sb.append("    isCustomerNotified: ").append(toIndentedString(isCustomerNotified)).append("\n");
    sb.append("    isVisibleOnFront: ").append(toIndentedString(isVisibleOnFront)).append("\n");
    sb.append("    parentId: ").append(toIndentedString(parentId)).append("\n");
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
    openapiFields.add("comment");
    openapiFields.add("created_at");
    openapiFields.add("entity_id");
    openapiFields.add("extension_attributes");
    openapiFields.add("is_customer_notified");
    openapiFields.add("is_visible_on_front");
    openapiFields.add("parent_id");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("comment");
    openapiRequiredFields.add("is_customer_notified");
    openapiRequiredFields.add("is_visible_on_front");
    openapiRequiredFields.add("parent_id");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to SalesDataCreditmemoCommentInterface
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!SalesDataCreditmemoCommentInterface.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in SalesDataCreditmemoCommentInterface is not found in the empty JSON string", SalesDataCreditmemoCommentInterface.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!SalesDataCreditmemoCommentInterface.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `SalesDataCreditmemoCommentInterface` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : SalesDataCreditmemoCommentInterface.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("comment").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `comment` to be a primitive type in the JSON string but got `%s`", jsonObj.get("comment").toString()));
      }
      if ((jsonObj.get("created_at") != null && !jsonObj.get("created_at").isJsonNull()) && !jsonObj.get("created_at").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `created_at` to be a primitive type in the JSON string but got `%s`", jsonObj.get("created_at").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!SalesDataCreditmemoCommentInterface.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'SalesDataCreditmemoCommentInterface' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<SalesDataCreditmemoCommentInterface> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(SalesDataCreditmemoCommentInterface.class));

       return (TypeAdapter<T>) new TypeAdapter<SalesDataCreditmemoCommentInterface>() {
           @Override
           public void write(JsonWriter out, SalesDataCreditmemoCommentInterface value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public SalesDataCreditmemoCommentInterface read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of SalesDataCreditmemoCommentInterface given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of SalesDataCreditmemoCommentInterface
   * @throws IOException if the JSON string is invalid with respect to SalesDataCreditmemoCommentInterface
   */
  public static SalesDataCreditmemoCommentInterface fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, SalesDataCreditmemoCommentInterface.class);
  }

  /**
   * Convert an instance of SalesDataCreditmemoCommentInterface to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

