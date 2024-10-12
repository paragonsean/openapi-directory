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
import org.openapitools.client.model.NegotiableQuoteDataNegotiableQuoteInterface;
import org.openapitools.client.model.QuoteDataShippingAssignmentInterface;

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
 * ExtensionInterface class for @see \\Magento\\Quote\\Api\\Data\\CartInterface
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:51.810681-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class QuoteDataCartExtensionInterface {
  public static final String SERIALIZED_NAME_AMAZON_ORDER_REFERENCE_ID = "amazon_order_reference_id";
  @SerializedName(SERIALIZED_NAME_AMAZON_ORDER_REFERENCE_ID)
  private String amazonOrderReferenceId;

  public static final String SERIALIZED_NAME_NEGOTIABLE_QUOTE = "negotiable_quote";
  @SerializedName(SERIALIZED_NAME_NEGOTIABLE_QUOTE)
  private NegotiableQuoteDataNegotiableQuoteInterface negotiableQuote;

  public static final String SERIALIZED_NAME_SHIPPING_ASSIGNMENTS = "shipping_assignments";
  @SerializedName(SERIALIZED_NAME_SHIPPING_ASSIGNMENTS)
  private List<QuoteDataShippingAssignmentInterface> shippingAssignments = new ArrayList<>();

  public QuoteDataCartExtensionInterface() {
  }

  public QuoteDataCartExtensionInterface amazonOrderReferenceId(String amazonOrderReferenceId) {
    this.amazonOrderReferenceId = amazonOrderReferenceId;
    return this;
  }

  /**
   * Get amazonOrderReferenceId
   * @return amazonOrderReferenceId
   */
  @javax.annotation.Nullable
  public String getAmazonOrderReferenceId() {
    return amazonOrderReferenceId;
  }

  public void setAmazonOrderReferenceId(String amazonOrderReferenceId) {
    this.amazonOrderReferenceId = amazonOrderReferenceId;
  }


  public QuoteDataCartExtensionInterface negotiableQuote(NegotiableQuoteDataNegotiableQuoteInterface negotiableQuote) {
    this.negotiableQuote = negotiableQuote;
    return this;
  }

  /**
   * Get negotiableQuote
   * @return negotiableQuote
   */
  @javax.annotation.Nullable
  public NegotiableQuoteDataNegotiableQuoteInterface getNegotiableQuote() {
    return negotiableQuote;
  }

  public void setNegotiableQuote(NegotiableQuoteDataNegotiableQuoteInterface negotiableQuote) {
    this.negotiableQuote = negotiableQuote;
  }


  public QuoteDataCartExtensionInterface shippingAssignments(List<QuoteDataShippingAssignmentInterface> shippingAssignments) {
    this.shippingAssignments = shippingAssignments;
    return this;
  }

  public QuoteDataCartExtensionInterface addShippingAssignmentsItem(QuoteDataShippingAssignmentInterface shippingAssignmentsItem) {
    if (this.shippingAssignments == null) {
      this.shippingAssignments = new ArrayList<>();
    }
    this.shippingAssignments.add(shippingAssignmentsItem);
    return this;
  }

  /**
   * Get shippingAssignments
   * @return shippingAssignments
   */
  @javax.annotation.Nullable
  public List<QuoteDataShippingAssignmentInterface> getShippingAssignments() {
    return shippingAssignments;
  }

  public void setShippingAssignments(List<QuoteDataShippingAssignmentInterface> shippingAssignments) {
    this.shippingAssignments = shippingAssignments;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    QuoteDataCartExtensionInterface quoteDataCartExtensionInterface = (QuoteDataCartExtensionInterface) o;
    return Objects.equals(this.amazonOrderReferenceId, quoteDataCartExtensionInterface.amazonOrderReferenceId) &&
        Objects.equals(this.negotiableQuote, quoteDataCartExtensionInterface.negotiableQuote) &&
        Objects.equals(this.shippingAssignments, quoteDataCartExtensionInterface.shippingAssignments);
  }

  @Override
  public int hashCode() {
    return Objects.hash(amazonOrderReferenceId, negotiableQuote, shippingAssignments);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class QuoteDataCartExtensionInterface {\n");
    sb.append("    amazonOrderReferenceId: ").append(toIndentedString(amazonOrderReferenceId)).append("\n");
    sb.append("    negotiableQuote: ").append(toIndentedString(negotiableQuote)).append("\n");
    sb.append("    shippingAssignments: ").append(toIndentedString(shippingAssignments)).append("\n");
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
    openapiFields.add("amazon_order_reference_id");
    openapiFields.add("negotiable_quote");
    openapiFields.add("shipping_assignments");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to QuoteDataCartExtensionInterface
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!QuoteDataCartExtensionInterface.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in QuoteDataCartExtensionInterface is not found in the empty JSON string", QuoteDataCartExtensionInterface.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!QuoteDataCartExtensionInterface.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `QuoteDataCartExtensionInterface` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("amazon_order_reference_id") != null && !jsonObj.get("amazon_order_reference_id").isJsonNull()) && !jsonObj.get("amazon_order_reference_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `amazon_order_reference_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("amazon_order_reference_id").toString()));
      }
      // validate the optional field `negotiable_quote`
      if (jsonObj.get("negotiable_quote") != null && !jsonObj.get("negotiable_quote").isJsonNull()) {
        NegotiableQuoteDataNegotiableQuoteInterface.validateJsonElement(jsonObj.get("negotiable_quote"));
      }
      if (jsonObj.get("shipping_assignments") != null && !jsonObj.get("shipping_assignments").isJsonNull()) {
        JsonArray jsonArrayshippingAssignments = jsonObj.getAsJsonArray("shipping_assignments");
        if (jsonArrayshippingAssignments != null) {
          // ensure the json data is an array
          if (!jsonObj.get("shipping_assignments").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `shipping_assignments` to be an array in the JSON string but got `%s`", jsonObj.get("shipping_assignments").toString()));
          }

          // validate the optional field `shipping_assignments` (array)
          for (int i = 0; i < jsonArrayshippingAssignments.size(); i++) {
            QuoteDataShippingAssignmentInterface.validateJsonElement(jsonArrayshippingAssignments.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!QuoteDataCartExtensionInterface.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'QuoteDataCartExtensionInterface' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<QuoteDataCartExtensionInterface> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(QuoteDataCartExtensionInterface.class));

       return (TypeAdapter<T>) new TypeAdapter<QuoteDataCartExtensionInterface>() {
           @Override
           public void write(JsonWriter out, QuoteDataCartExtensionInterface value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public QuoteDataCartExtensionInterface read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of QuoteDataCartExtensionInterface given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of QuoteDataCartExtensionInterface
   * @throws IOException if the JSON string is invalid with respect to QuoteDataCartExtensionInterface
   */
  public static QuoteDataCartExtensionInterface fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, QuoteDataCartExtensionInterface.class);
  }

  /**
   * Convert an instance of QuoteDataCartExtensionInterface to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

