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
 * Coupon mass delete results interface.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:51.810681-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class SalesRuleDataCouponMassDeleteResultInterface {
  public static final String SERIALIZED_NAME_FAILED_ITEMS = "failed_items";
  @SerializedName(SERIALIZED_NAME_FAILED_ITEMS)
  private List<String> failedItems = new ArrayList<>();

  public static final String SERIALIZED_NAME_MISSING_ITEMS = "missing_items";
  @SerializedName(SERIALIZED_NAME_MISSING_ITEMS)
  private List<String> missingItems = new ArrayList<>();

  public SalesRuleDataCouponMassDeleteResultInterface() {
  }

  public SalesRuleDataCouponMassDeleteResultInterface failedItems(List<String> failedItems) {
    this.failedItems = failedItems;
    return this;
  }

  public SalesRuleDataCouponMassDeleteResultInterface addFailedItemsItem(String failedItemsItem) {
    if (this.failedItems == null) {
      this.failedItems = new ArrayList<>();
    }
    this.failedItems.add(failedItemsItem);
    return this;
  }

  /**
   * List of failed items.
   * @return failedItems
   */
  @javax.annotation.Nonnull
  public List<String> getFailedItems() {
    return failedItems;
  }

  public void setFailedItems(List<String> failedItems) {
    this.failedItems = failedItems;
  }


  public SalesRuleDataCouponMassDeleteResultInterface missingItems(List<String> missingItems) {
    this.missingItems = missingItems;
    return this;
  }

  public SalesRuleDataCouponMassDeleteResultInterface addMissingItemsItem(String missingItemsItem) {
    if (this.missingItems == null) {
      this.missingItems = new ArrayList<>();
    }
    this.missingItems.add(missingItemsItem);
    return this;
  }

  /**
   * List of missing items.
   * @return missingItems
   */
  @javax.annotation.Nonnull
  public List<String> getMissingItems() {
    return missingItems;
  }

  public void setMissingItems(List<String> missingItems) {
    this.missingItems = missingItems;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    SalesRuleDataCouponMassDeleteResultInterface salesRuleDataCouponMassDeleteResultInterface = (SalesRuleDataCouponMassDeleteResultInterface) o;
    return Objects.equals(this.failedItems, salesRuleDataCouponMassDeleteResultInterface.failedItems) &&
        Objects.equals(this.missingItems, salesRuleDataCouponMassDeleteResultInterface.missingItems);
  }

  @Override
  public int hashCode() {
    return Objects.hash(failedItems, missingItems);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class SalesRuleDataCouponMassDeleteResultInterface {\n");
    sb.append("    failedItems: ").append(toIndentedString(failedItems)).append("\n");
    sb.append("    missingItems: ").append(toIndentedString(missingItems)).append("\n");
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
    openapiFields.add("failed_items");
    openapiFields.add("missing_items");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("failed_items");
    openapiRequiredFields.add("missing_items");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to SalesRuleDataCouponMassDeleteResultInterface
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!SalesRuleDataCouponMassDeleteResultInterface.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in SalesRuleDataCouponMassDeleteResultInterface is not found in the empty JSON string", SalesRuleDataCouponMassDeleteResultInterface.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!SalesRuleDataCouponMassDeleteResultInterface.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `SalesRuleDataCouponMassDeleteResultInterface` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : SalesRuleDataCouponMassDeleteResultInterface.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the required json array is present
      if (jsonObj.get("failed_items") == null) {
        throw new IllegalArgumentException("Expected the field `linkedContent` to be an array in the JSON string but got `null`");
      } else if (!jsonObj.get("failed_items").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `failed_items` to be an array in the JSON string but got `%s`", jsonObj.get("failed_items").toString()));
      }
      // ensure the required json array is present
      if (jsonObj.get("missing_items") == null) {
        throw new IllegalArgumentException("Expected the field `linkedContent` to be an array in the JSON string but got `null`");
      } else if (!jsonObj.get("missing_items").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `missing_items` to be an array in the JSON string but got `%s`", jsonObj.get("missing_items").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!SalesRuleDataCouponMassDeleteResultInterface.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'SalesRuleDataCouponMassDeleteResultInterface' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<SalesRuleDataCouponMassDeleteResultInterface> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(SalesRuleDataCouponMassDeleteResultInterface.class));

       return (TypeAdapter<T>) new TypeAdapter<SalesRuleDataCouponMassDeleteResultInterface>() {
           @Override
           public void write(JsonWriter out, SalesRuleDataCouponMassDeleteResultInterface value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public SalesRuleDataCouponMassDeleteResultInterface read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of SalesRuleDataCouponMassDeleteResultInterface given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of SalesRuleDataCouponMassDeleteResultInterface
   * @throws IOException if the JSON string is invalid with respect to SalesRuleDataCouponMassDeleteResultInterface
   */
  public static SalesRuleDataCouponMassDeleteResultInterface fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, SalesRuleDataCouponMassDeleteResultInterface.class);
  }

  /**
   * Convert an instance of SalesRuleDataCouponMassDeleteResultInterface to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

