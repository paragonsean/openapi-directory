/*
 * Flight Order Management
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.9.0
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
import org.openapitools.client.model.BaggageAllowance;
import org.openapitools.client.model.ServiceName;

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
 * AdditionalServicesRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:02:54.608298-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AdditionalServicesRequest {
  public static final String SERIALIZED_NAME_CHARGEABLE_CHECKED_BAGS = "chargeableCheckedBags";
  @SerializedName(SERIALIZED_NAME_CHARGEABLE_CHECKED_BAGS)
  private BaggageAllowance chargeableCheckedBags;

  public static final String SERIALIZED_NAME_CHARGEABLE_SEAT_NUMBER = "chargeableSeatNumber";
  @SerializedName(SERIALIZED_NAME_CHARGEABLE_SEAT_NUMBER)
  private String chargeableSeatNumber;

  public static final String SERIALIZED_NAME_OTHER_SERVICES = "otherServices";
  @SerializedName(SERIALIZED_NAME_OTHER_SERVICES)
  private List<ServiceName> otherServices = new ArrayList<>();

  public AdditionalServicesRequest() {
  }

  public AdditionalServicesRequest chargeableCheckedBags(BaggageAllowance chargeableCheckedBags) {
    this.chargeableCheckedBags = chargeableCheckedBags;
    return this;
  }

  /**
   * Get chargeableCheckedBags
   * @return chargeableCheckedBags
   */
  @javax.annotation.Nullable
  public BaggageAllowance getChargeableCheckedBags() {
    return chargeableCheckedBags;
  }

  public void setChargeableCheckedBags(BaggageAllowance chargeableCheckedBags) {
    this.chargeableCheckedBags = chargeableCheckedBags;
  }


  public AdditionalServicesRequest chargeableSeatNumber(String chargeableSeatNumber) {
    this.chargeableSeatNumber = chargeableSeatNumber;
    return this;
  }

  /**
   * seat number
   * @return chargeableSeatNumber
   */
  @javax.annotation.Nullable
  public String getChargeableSeatNumber() {
    return chargeableSeatNumber;
  }

  public void setChargeableSeatNumber(String chargeableSeatNumber) {
    this.chargeableSeatNumber = chargeableSeatNumber;
  }


  public AdditionalServicesRequest otherServices(List<ServiceName> otherServices) {
    this.otherServices = otherServices;
    return this;
  }

  public AdditionalServicesRequest addOtherServicesItem(ServiceName otherServicesItem) {
    if (this.otherServices == null) {
      this.otherServices = new ArrayList<>();
    }
    this.otherServices.add(otherServicesItem);
    return this;
  }

  /**
   * Other services to add
   * @return otherServices
   */
  @javax.annotation.Nullable
  public List<ServiceName> getOtherServices() {
    return otherServices;
  }

  public void setOtherServices(List<ServiceName> otherServices) {
    this.otherServices = otherServices;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AdditionalServicesRequest additionalServicesRequest = (AdditionalServicesRequest) o;
    return Objects.equals(this.chargeableCheckedBags, additionalServicesRequest.chargeableCheckedBags) &&
        Objects.equals(this.chargeableSeatNumber, additionalServicesRequest.chargeableSeatNumber) &&
        Objects.equals(this.otherServices, additionalServicesRequest.otherServices);
  }

  @Override
  public int hashCode() {
    return Objects.hash(chargeableCheckedBags, chargeableSeatNumber, otherServices);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AdditionalServicesRequest {\n");
    sb.append("    chargeableCheckedBags: ").append(toIndentedString(chargeableCheckedBags)).append("\n");
    sb.append("    chargeableSeatNumber: ").append(toIndentedString(chargeableSeatNumber)).append("\n");
    sb.append("    otherServices: ").append(toIndentedString(otherServices)).append("\n");
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
    openapiFields.add("chargeableCheckedBags");
    openapiFields.add("chargeableSeatNumber");
    openapiFields.add("otherServices");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AdditionalServicesRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AdditionalServicesRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AdditionalServicesRequest is not found in the empty JSON string", AdditionalServicesRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AdditionalServicesRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AdditionalServicesRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `chargeableCheckedBags`
      if (jsonObj.get("chargeableCheckedBags") != null && !jsonObj.get("chargeableCheckedBags").isJsonNull()) {
        BaggageAllowance.validateJsonElement(jsonObj.get("chargeableCheckedBags"));
      }
      if ((jsonObj.get("chargeableSeatNumber") != null && !jsonObj.get("chargeableSeatNumber").isJsonNull()) && !jsonObj.get("chargeableSeatNumber").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `chargeableSeatNumber` to be a primitive type in the JSON string but got `%s`", jsonObj.get("chargeableSeatNumber").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("otherServices") != null && !jsonObj.get("otherServices").isJsonNull() && !jsonObj.get("otherServices").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `otherServices` to be an array in the JSON string but got `%s`", jsonObj.get("otherServices").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AdditionalServicesRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AdditionalServicesRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AdditionalServicesRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AdditionalServicesRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<AdditionalServicesRequest>() {
           @Override
           public void write(JsonWriter out, AdditionalServicesRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AdditionalServicesRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AdditionalServicesRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AdditionalServicesRequest
   * @throws IOException if the JSON string is invalid with respect to AdditionalServicesRequest
   */
  public static AdditionalServicesRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AdditionalServicesRequest.class);
  }

  /**
   * Convert an instance of AdditionalServicesRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

