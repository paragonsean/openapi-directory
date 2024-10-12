/*
 * Keycloak Admin REST API
 * This is a REST API reference for the Keycloak Admin
 *
 * The version of the OpenAPI document: 1
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
 * AddressClaimSet
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:16.227825-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AddressClaimSet {
  public static final String SERIALIZED_NAME_COUNTRY = "country";
  @SerializedName(SERIALIZED_NAME_COUNTRY)
  private String country;

  public static final String SERIALIZED_NAME_FORMATTED = "formatted";
  @SerializedName(SERIALIZED_NAME_FORMATTED)
  private String formatted;

  public static final String SERIALIZED_NAME_LOCALITY = "locality";
  @SerializedName(SERIALIZED_NAME_LOCALITY)
  private String locality;

  public static final String SERIALIZED_NAME_POSTAL_CODE = "postal_code";
  @SerializedName(SERIALIZED_NAME_POSTAL_CODE)
  private String postalCode;

  public static final String SERIALIZED_NAME_REGION = "region";
  @SerializedName(SERIALIZED_NAME_REGION)
  private String region;

  public static final String SERIALIZED_NAME_STREET_ADDRESS = "street_address";
  @SerializedName(SERIALIZED_NAME_STREET_ADDRESS)
  private String streetAddress;

  public AddressClaimSet() {
  }

  public AddressClaimSet country(String country) {
    this.country = country;
    return this;
  }

  /**
   * Get country
   * @return country
   */
  @javax.annotation.Nullable
  public String getCountry() {
    return country;
  }

  public void setCountry(String country) {
    this.country = country;
  }


  public AddressClaimSet formatted(String formatted) {
    this.formatted = formatted;
    return this;
  }

  /**
   * Get formatted
   * @return formatted
   */
  @javax.annotation.Nullable
  public String getFormatted() {
    return formatted;
  }

  public void setFormatted(String formatted) {
    this.formatted = formatted;
  }


  public AddressClaimSet locality(String locality) {
    this.locality = locality;
    return this;
  }

  /**
   * Get locality
   * @return locality
   */
  @javax.annotation.Nullable
  public String getLocality() {
    return locality;
  }

  public void setLocality(String locality) {
    this.locality = locality;
  }


  public AddressClaimSet postalCode(String postalCode) {
    this.postalCode = postalCode;
    return this;
  }

  /**
   * Get postalCode
   * @return postalCode
   */
  @javax.annotation.Nullable
  public String getPostalCode() {
    return postalCode;
  }

  public void setPostalCode(String postalCode) {
    this.postalCode = postalCode;
  }


  public AddressClaimSet region(String region) {
    this.region = region;
    return this;
  }

  /**
   * Get region
   * @return region
   */
  @javax.annotation.Nullable
  public String getRegion() {
    return region;
  }

  public void setRegion(String region) {
    this.region = region;
  }


  public AddressClaimSet streetAddress(String streetAddress) {
    this.streetAddress = streetAddress;
    return this;
  }

  /**
   * Get streetAddress
   * @return streetAddress
   */
  @javax.annotation.Nullable
  public String getStreetAddress() {
    return streetAddress;
  }

  public void setStreetAddress(String streetAddress) {
    this.streetAddress = streetAddress;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AddressClaimSet addressClaimSet = (AddressClaimSet) o;
    return Objects.equals(this.country, addressClaimSet.country) &&
        Objects.equals(this.formatted, addressClaimSet.formatted) &&
        Objects.equals(this.locality, addressClaimSet.locality) &&
        Objects.equals(this.postalCode, addressClaimSet.postalCode) &&
        Objects.equals(this.region, addressClaimSet.region) &&
        Objects.equals(this.streetAddress, addressClaimSet.streetAddress);
  }

  @Override
  public int hashCode() {
    return Objects.hash(country, formatted, locality, postalCode, region, streetAddress);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AddressClaimSet {\n");
    sb.append("    country: ").append(toIndentedString(country)).append("\n");
    sb.append("    formatted: ").append(toIndentedString(formatted)).append("\n");
    sb.append("    locality: ").append(toIndentedString(locality)).append("\n");
    sb.append("    postalCode: ").append(toIndentedString(postalCode)).append("\n");
    sb.append("    region: ").append(toIndentedString(region)).append("\n");
    sb.append("    streetAddress: ").append(toIndentedString(streetAddress)).append("\n");
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
    openapiFields.add("country");
    openapiFields.add("formatted");
    openapiFields.add("locality");
    openapiFields.add("postal_code");
    openapiFields.add("region");
    openapiFields.add("street_address");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AddressClaimSet
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AddressClaimSet.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AddressClaimSet is not found in the empty JSON string", AddressClaimSet.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AddressClaimSet.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AddressClaimSet` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("country") != null && !jsonObj.get("country").isJsonNull()) && !jsonObj.get("country").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `country` to be a primitive type in the JSON string but got `%s`", jsonObj.get("country").toString()));
      }
      if ((jsonObj.get("formatted") != null && !jsonObj.get("formatted").isJsonNull()) && !jsonObj.get("formatted").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `formatted` to be a primitive type in the JSON string but got `%s`", jsonObj.get("formatted").toString()));
      }
      if ((jsonObj.get("locality") != null && !jsonObj.get("locality").isJsonNull()) && !jsonObj.get("locality").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `locality` to be a primitive type in the JSON string but got `%s`", jsonObj.get("locality").toString()));
      }
      if ((jsonObj.get("postal_code") != null && !jsonObj.get("postal_code").isJsonNull()) && !jsonObj.get("postal_code").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `postal_code` to be a primitive type in the JSON string but got `%s`", jsonObj.get("postal_code").toString()));
      }
      if ((jsonObj.get("region") != null && !jsonObj.get("region").isJsonNull()) && !jsonObj.get("region").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `region` to be a primitive type in the JSON string but got `%s`", jsonObj.get("region").toString()));
      }
      if ((jsonObj.get("street_address") != null && !jsonObj.get("street_address").isJsonNull()) && !jsonObj.get("street_address").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `street_address` to be a primitive type in the JSON string but got `%s`", jsonObj.get("street_address").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AddressClaimSet.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AddressClaimSet' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AddressClaimSet> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AddressClaimSet.class));

       return (TypeAdapter<T>) new TypeAdapter<AddressClaimSet>() {
           @Override
           public void write(JsonWriter out, AddressClaimSet value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AddressClaimSet read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AddressClaimSet given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AddressClaimSet
   * @throws IOException if the JSON string is invalid with respect to AddressClaimSet
   */
  public static AddressClaimSet fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AddressClaimSet.class);
  }

  /**
   * Convert an instance of AddressClaimSet to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

