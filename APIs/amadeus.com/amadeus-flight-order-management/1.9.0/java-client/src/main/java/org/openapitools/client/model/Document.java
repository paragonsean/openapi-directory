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
import java.time.LocalDate;
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
 * the information that are found on an ID document
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:02:54.608298-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Document {
  public static final String SERIALIZED_NAME_BIRTH_PLACE = "birthPlace";
  @SerializedName(SERIALIZED_NAME_BIRTH_PLACE)
  private String birthPlace;

  public static final String SERIALIZED_NAME_EXPIRY_DATE = "expiryDate";
  @SerializedName(SERIALIZED_NAME_EXPIRY_DATE)
  private LocalDate expiryDate;

  public static final String SERIALIZED_NAME_ISSUANCE_COUNTRY = "issuanceCountry";
  @SerializedName(SERIALIZED_NAME_ISSUANCE_COUNTRY)
  private String issuanceCountry;

  public static final String SERIALIZED_NAME_ISSUANCE_DATE = "issuanceDate";
  @SerializedName(SERIALIZED_NAME_ISSUANCE_DATE)
  private LocalDate issuanceDate;

  public static final String SERIALIZED_NAME_ISSUANCE_LOCATION = "issuanceLocation";
  @SerializedName(SERIALIZED_NAME_ISSUANCE_LOCATION)
  private String issuanceLocation;

  public static final String SERIALIZED_NAME_NATIONALITY = "nationality";
  @SerializedName(SERIALIZED_NAME_NATIONALITY)
  private String nationality;

  public static final String SERIALIZED_NAME_NUMBER = "number";
  @SerializedName(SERIALIZED_NAME_NUMBER)
  private String number;

  public Document() {
  }

  public Document birthPlace(String birthPlace) {
    this.birthPlace = birthPlace;
    return this;
  }

  /**
   * Birth place as indicated on the document
   * @return birthPlace
   */
  @javax.annotation.Nullable
  public String getBirthPlace() {
    return birthPlace;
  }

  public void setBirthPlace(String birthPlace) {
    this.birthPlace = birthPlace;
  }


  public Document expiryDate(LocalDate expiryDate) {
    this.expiryDate = expiryDate;
    return this;
  }

  /**
   * Date after which the document is not valid anymore.
   * @return expiryDate
   */
  @javax.annotation.Nullable
  public LocalDate getExpiryDate() {
    return expiryDate;
  }

  public void setExpiryDate(LocalDate expiryDate) {
    this.expiryDate = expiryDate;
  }


  public Document issuanceCountry(String issuanceCountry) {
    this.issuanceCountry = issuanceCountry;
    return this;
  }

  /**
   * [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the country that issued the document
   * @return issuanceCountry
   */
  @javax.annotation.Nullable
  public String getIssuanceCountry() {
    return issuanceCountry;
  }

  public void setIssuanceCountry(String issuanceCountry) {
    this.issuanceCountry = issuanceCountry;
  }


  public Document issuanceDate(LocalDate issuanceDate) {
    this.issuanceDate = issuanceDate;
    return this;
  }

  /**
   * Date at which the document has been issued.
   * @return issuanceDate
   */
  @javax.annotation.Nullable
  public LocalDate getIssuanceDate() {
    return issuanceDate;
  }

  public void setIssuanceDate(LocalDate issuanceDate) {
    this.issuanceDate = issuanceDate;
  }


  public Document issuanceLocation(String issuanceLocation) {
    this.issuanceLocation = issuanceLocation;
    return this;
  }

  /**
   * A more precise information concerning the place where the document has been issued, when available. It may be a country, a state, a city or any other type of location. e.g. New-York
   * @return issuanceLocation
   */
  @javax.annotation.Nullable
  public String getIssuanceLocation() {
    return issuanceLocation;
  }

  public void setIssuanceLocation(String issuanceLocation) {
    this.issuanceLocation = issuanceLocation;
  }


  public Document nationality(String nationality) {
    this.nationality = nationality;
    return this;
  }

  /**
   * [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the nationality appearing on the document
   * @return nationality
   */
  @javax.annotation.Nullable
  public String getNationality() {
    return nationality;
  }

  public void setNationality(String nationality) {
    this.nationality = nationality;
  }


  public Document number(String number) {
    this.number = number;
    return this;
  }

  /**
   * The document number (shown on the document) . E.g. QFU514563221J
   * @return number
   */
  @javax.annotation.Nullable
  public String getNumber() {
    return number;
  }

  public void setNumber(String number) {
    this.number = number;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Document document = (Document) o;
    return Objects.equals(this.birthPlace, document.birthPlace) &&
        Objects.equals(this.expiryDate, document.expiryDate) &&
        Objects.equals(this.issuanceCountry, document.issuanceCountry) &&
        Objects.equals(this.issuanceDate, document.issuanceDate) &&
        Objects.equals(this.issuanceLocation, document.issuanceLocation) &&
        Objects.equals(this.nationality, document.nationality) &&
        Objects.equals(this.number, document.number);
  }

  @Override
  public int hashCode() {
    return Objects.hash(birthPlace, expiryDate, issuanceCountry, issuanceDate, issuanceLocation, nationality, number);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Document {\n");
    sb.append("    birthPlace: ").append(toIndentedString(birthPlace)).append("\n");
    sb.append("    expiryDate: ").append(toIndentedString(expiryDate)).append("\n");
    sb.append("    issuanceCountry: ").append(toIndentedString(issuanceCountry)).append("\n");
    sb.append("    issuanceDate: ").append(toIndentedString(issuanceDate)).append("\n");
    sb.append("    issuanceLocation: ").append(toIndentedString(issuanceLocation)).append("\n");
    sb.append("    nationality: ").append(toIndentedString(nationality)).append("\n");
    sb.append("    number: ").append(toIndentedString(number)).append("\n");
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
    openapiFields.add("birthPlace");
    openapiFields.add("expiryDate");
    openapiFields.add("issuanceCountry");
    openapiFields.add("issuanceDate");
    openapiFields.add("issuanceLocation");
    openapiFields.add("nationality");
    openapiFields.add("number");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Document
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Document.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Document is not found in the empty JSON string", Document.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Document.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Document` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("birthPlace") != null && !jsonObj.get("birthPlace").isJsonNull()) && !jsonObj.get("birthPlace").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `birthPlace` to be a primitive type in the JSON string but got `%s`", jsonObj.get("birthPlace").toString()));
      }
      if ((jsonObj.get("issuanceCountry") != null && !jsonObj.get("issuanceCountry").isJsonNull()) && !jsonObj.get("issuanceCountry").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `issuanceCountry` to be a primitive type in the JSON string but got `%s`", jsonObj.get("issuanceCountry").toString()));
      }
      if ((jsonObj.get("issuanceLocation") != null && !jsonObj.get("issuanceLocation").isJsonNull()) && !jsonObj.get("issuanceLocation").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `issuanceLocation` to be a primitive type in the JSON string but got `%s`", jsonObj.get("issuanceLocation").toString()));
      }
      if ((jsonObj.get("nationality") != null && !jsonObj.get("nationality").isJsonNull()) && !jsonObj.get("nationality").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `nationality` to be a primitive type in the JSON string but got `%s`", jsonObj.get("nationality").toString()));
      }
      if ((jsonObj.get("number") != null && !jsonObj.get("number").isJsonNull()) && !jsonObj.get("number").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `number` to be a primitive type in the JSON string but got `%s`", jsonObj.get("number").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Document.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Document' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Document> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Document.class));

       return (TypeAdapter<T>) new TypeAdapter<Document>() {
           @Override
           public void write(JsonWriter out, Document value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Document read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Document given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Document
   * @throws IOException if the JSON string is invalid with respect to Document
   */
  public static Document fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Document.class);
  }

  /**
   * Convert an instance of Document to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

