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
import org.openapitools.client.model.FrameworkAttributeInterface;
import org.openapitools.client.model.QuoteDataAddressInterface;

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
 * Interface ShippingInformationInterface
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:51.810681-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CheckoutDataShippingInformationInterface {
  public static final String SERIALIZED_NAME_BILLING_ADDRESS = "billing_address";
  @SerializedName(SERIALIZED_NAME_BILLING_ADDRESS)
  private QuoteDataAddressInterface billingAddress;

  public static final String SERIALIZED_NAME_CUSTOM_ATTRIBUTES = "custom_attributes";
  @SerializedName(SERIALIZED_NAME_CUSTOM_ATTRIBUTES)
  private List<FrameworkAttributeInterface> customAttributes = new ArrayList<>();

  public static final String SERIALIZED_NAME_EXTENSION_ATTRIBUTES = "extension_attributes";
  @SerializedName(SERIALIZED_NAME_EXTENSION_ATTRIBUTES)
  private Object extensionAttributes;

  public static final String SERIALIZED_NAME_SHIPPING_ADDRESS = "shipping_address";
  @SerializedName(SERIALIZED_NAME_SHIPPING_ADDRESS)
  private QuoteDataAddressInterface shippingAddress;

  public static final String SERIALIZED_NAME_SHIPPING_CARRIER_CODE = "shipping_carrier_code";
  @SerializedName(SERIALIZED_NAME_SHIPPING_CARRIER_CODE)
  private String shippingCarrierCode;

  public static final String SERIALIZED_NAME_SHIPPING_METHOD_CODE = "shipping_method_code";
  @SerializedName(SERIALIZED_NAME_SHIPPING_METHOD_CODE)
  private String shippingMethodCode;

  public CheckoutDataShippingInformationInterface() {
  }

  public CheckoutDataShippingInformationInterface billingAddress(QuoteDataAddressInterface billingAddress) {
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


  public CheckoutDataShippingInformationInterface customAttributes(List<FrameworkAttributeInterface> customAttributes) {
    this.customAttributes = customAttributes;
    return this;
  }

  public CheckoutDataShippingInformationInterface addCustomAttributesItem(FrameworkAttributeInterface customAttributesItem) {
    if (this.customAttributes == null) {
      this.customAttributes = new ArrayList<>();
    }
    this.customAttributes.add(customAttributesItem);
    return this;
  }

  /**
   * Custom attributes values.
   * @return customAttributes
   */
  @javax.annotation.Nullable
  public List<FrameworkAttributeInterface> getCustomAttributes() {
    return customAttributes;
  }

  public void setCustomAttributes(List<FrameworkAttributeInterface> customAttributes) {
    this.customAttributes = customAttributes;
  }


  public CheckoutDataShippingInformationInterface extensionAttributes(Object extensionAttributes) {
    this.extensionAttributes = extensionAttributes;
    return this;
  }

  /**
   * ExtensionInterface class for @see \\Magento\\Checkout\\Api\\Data\\ShippingInformationInterface
   * @return extensionAttributes
   */
  @javax.annotation.Nullable
  public Object getExtensionAttributes() {
    return extensionAttributes;
  }

  public void setExtensionAttributes(Object extensionAttributes) {
    this.extensionAttributes = extensionAttributes;
  }


  public CheckoutDataShippingInformationInterface shippingAddress(QuoteDataAddressInterface shippingAddress) {
    this.shippingAddress = shippingAddress;
    return this;
  }

  /**
   * Get shippingAddress
   * @return shippingAddress
   */
  @javax.annotation.Nonnull
  public QuoteDataAddressInterface getShippingAddress() {
    return shippingAddress;
  }

  public void setShippingAddress(QuoteDataAddressInterface shippingAddress) {
    this.shippingAddress = shippingAddress;
  }


  public CheckoutDataShippingInformationInterface shippingCarrierCode(String shippingCarrierCode) {
    this.shippingCarrierCode = shippingCarrierCode;
    return this;
  }

  /**
   * Carrier code
   * @return shippingCarrierCode
   */
  @javax.annotation.Nonnull
  public String getShippingCarrierCode() {
    return shippingCarrierCode;
  }

  public void setShippingCarrierCode(String shippingCarrierCode) {
    this.shippingCarrierCode = shippingCarrierCode;
  }


  public CheckoutDataShippingInformationInterface shippingMethodCode(String shippingMethodCode) {
    this.shippingMethodCode = shippingMethodCode;
    return this;
  }

  /**
   * Shipping method code
   * @return shippingMethodCode
   */
  @javax.annotation.Nonnull
  public String getShippingMethodCode() {
    return shippingMethodCode;
  }

  public void setShippingMethodCode(String shippingMethodCode) {
    this.shippingMethodCode = shippingMethodCode;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CheckoutDataShippingInformationInterface checkoutDataShippingInformationInterface = (CheckoutDataShippingInformationInterface) o;
    return Objects.equals(this.billingAddress, checkoutDataShippingInformationInterface.billingAddress) &&
        Objects.equals(this.customAttributes, checkoutDataShippingInformationInterface.customAttributes) &&
        Objects.equals(this.extensionAttributes, checkoutDataShippingInformationInterface.extensionAttributes) &&
        Objects.equals(this.shippingAddress, checkoutDataShippingInformationInterface.shippingAddress) &&
        Objects.equals(this.shippingCarrierCode, checkoutDataShippingInformationInterface.shippingCarrierCode) &&
        Objects.equals(this.shippingMethodCode, checkoutDataShippingInformationInterface.shippingMethodCode);
  }

  @Override
  public int hashCode() {
    return Objects.hash(billingAddress, customAttributes, extensionAttributes, shippingAddress, shippingCarrierCode, shippingMethodCode);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CheckoutDataShippingInformationInterface {\n");
    sb.append("    billingAddress: ").append(toIndentedString(billingAddress)).append("\n");
    sb.append("    customAttributes: ").append(toIndentedString(customAttributes)).append("\n");
    sb.append("    extensionAttributes: ").append(toIndentedString(extensionAttributes)).append("\n");
    sb.append("    shippingAddress: ").append(toIndentedString(shippingAddress)).append("\n");
    sb.append("    shippingCarrierCode: ").append(toIndentedString(shippingCarrierCode)).append("\n");
    sb.append("    shippingMethodCode: ").append(toIndentedString(shippingMethodCode)).append("\n");
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
    openapiFields.add("custom_attributes");
    openapiFields.add("extension_attributes");
    openapiFields.add("shipping_address");
    openapiFields.add("shipping_carrier_code");
    openapiFields.add("shipping_method_code");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("shipping_address");
    openapiRequiredFields.add("shipping_carrier_code");
    openapiRequiredFields.add("shipping_method_code");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CheckoutDataShippingInformationInterface
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CheckoutDataShippingInformationInterface.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CheckoutDataShippingInformationInterface is not found in the empty JSON string", CheckoutDataShippingInformationInterface.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CheckoutDataShippingInformationInterface.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CheckoutDataShippingInformationInterface` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : CheckoutDataShippingInformationInterface.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `billing_address`
      if (jsonObj.get("billing_address") != null && !jsonObj.get("billing_address").isJsonNull()) {
        QuoteDataAddressInterface.validateJsonElement(jsonObj.get("billing_address"));
      }
      if (jsonObj.get("custom_attributes") != null && !jsonObj.get("custom_attributes").isJsonNull()) {
        JsonArray jsonArraycustomAttributes = jsonObj.getAsJsonArray("custom_attributes");
        if (jsonArraycustomAttributes != null) {
          // ensure the json data is an array
          if (!jsonObj.get("custom_attributes").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `custom_attributes` to be an array in the JSON string but got `%s`", jsonObj.get("custom_attributes").toString()));
          }

          // validate the optional field `custom_attributes` (array)
          for (int i = 0; i < jsonArraycustomAttributes.size(); i++) {
            FrameworkAttributeInterface.validateJsonElement(jsonArraycustomAttributes.get(i));
          };
        }
      }
      // validate the required field `shipping_address`
      QuoteDataAddressInterface.validateJsonElement(jsonObj.get("shipping_address"));
      if (!jsonObj.get("shipping_carrier_code").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `shipping_carrier_code` to be a primitive type in the JSON string but got `%s`", jsonObj.get("shipping_carrier_code").toString()));
      }
      if (!jsonObj.get("shipping_method_code").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `shipping_method_code` to be a primitive type in the JSON string but got `%s`", jsonObj.get("shipping_method_code").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CheckoutDataShippingInformationInterface.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CheckoutDataShippingInformationInterface' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CheckoutDataShippingInformationInterface> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CheckoutDataShippingInformationInterface.class));

       return (TypeAdapter<T>) new TypeAdapter<CheckoutDataShippingInformationInterface>() {
           @Override
           public void write(JsonWriter out, CheckoutDataShippingInformationInterface value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CheckoutDataShippingInformationInterface read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CheckoutDataShippingInformationInterface given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CheckoutDataShippingInformationInterface
   * @throws IOException if the JSON string is invalid with respect to CheckoutDataShippingInformationInterface
   */
  public static CheckoutDataShippingInformationInterface fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CheckoutDataShippingInformationInterface.class);
  }

  /**
   * Convert an instance of CheckoutDataShippingInformationInterface to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

