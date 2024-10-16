/*
 * CallFire API Documentation
 * CallFire
 *
 * The version of the OpenAPI document: V2
 * Contact: support@callfire.com
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
import org.openapitools.client.model.Region;

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
 * ~
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:59:09.684594-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Number {
  public static final String SERIALIZED_NAME_NATIONAL_FORMAT = "nationalFormat";
  @SerializedName(SERIALIZED_NAME_NATIONAL_FORMAT)
  private String nationalFormat;

  public static final String SERIALIZED_NAME_NUMBER = "number";
  @SerializedName(SERIALIZED_NAME_NUMBER)
  private String number;

  public static final String SERIALIZED_NAME_REGION = "region";
  @SerializedName(SERIALIZED_NAME_REGION)
  private Region region;

  public static final String SERIALIZED_NAME_SEND_EMAIL_ON_CREATE = "sendEmailOnCreate";
  @SerializedName(SERIALIZED_NAME_SEND_EMAIL_ON_CREATE)
  private Boolean sendEmailOnCreate;

  public static final String SERIALIZED_NAME_TOLL_FREE = "tollFree";
  @SerializedName(SERIALIZED_NAME_TOLL_FREE)
  private Boolean tollFree;

  public Number() {
  }

  public Number nationalFormat(String nationalFormat) {
    this.nationalFormat = nationalFormat;
    return this;
  }

  /**
   * ~
   * @return nationalFormat
   */
  @javax.annotation.Nullable
  public String getNationalFormat() {
    return nationalFormat;
  }

  public void setNationalFormat(String nationalFormat) {
    this.nationalFormat = nationalFormat;
  }


  public Number number(String number) {
    this.number = number;
    return this;
  }

  /**
   * ~
   * @return number
   */
  @javax.annotation.Nullable
  public String getNumber() {
    return number;
  }

  public void setNumber(String number) {
    this.number = number;
  }


  public Number region(Region region) {
    this.region = region;
    return this;
  }

  /**
   * Get region
   * @return region
   */
  @javax.annotation.Nullable
  public Region getRegion() {
    return region;
  }

  public void setRegion(Region region) {
    this.region = region;
  }


  public Number sendEmailOnCreate(Boolean sendEmailOnCreate) {
    this.sendEmailOnCreate = sendEmailOnCreate;
    return this;
  }

  /**
   * ~
   * @return sendEmailOnCreate
   */
  @javax.annotation.Nullable
  public Boolean getSendEmailOnCreate() {
    return sendEmailOnCreate;
  }

  public void setSendEmailOnCreate(Boolean sendEmailOnCreate) {
    this.sendEmailOnCreate = sendEmailOnCreate;
  }


  public Number tollFree(Boolean tollFree) {
    this.tollFree = tollFree;
    return this;
  }

  /**
   * ~
   * @return tollFree
   */
  @javax.annotation.Nullable
  public Boolean getTollFree() {
    return tollFree;
  }

  public void setTollFree(Boolean tollFree) {
    this.tollFree = tollFree;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Number number = (Number) o;
    return Objects.equals(this.nationalFormat, number.nationalFormat) &&
        Objects.equals(this.number, number.number) &&
        Objects.equals(this.region, number.region) &&
        Objects.equals(this.sendEmailOnCreate, number.sendEmailOnCreate) &&
        Objects.equals(this.tollFree, number.tollFree);
  }

  @Override
  public int hashCode() {
    return Objects.hash(nationalFormat, number, region, sendEmailOnCreate, tollFree);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Number {\n");
    sb.append("    nationalFormat: ").append(toIndentedString(nationalFormat)).append("\n");
    sb.append("    number: ").append(toIndentedString(number)).append("\n");
    sb.append("    region: ").append(toIndentedString(region)).append("\n");
    sb.append("    sendEmailOnCreate: ").append(toIndentedString(sendEmailOnCreate)).append("\n");
    sb.append("    tollFree: ").append(toIndentedString(tollFree)).append("\n");
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
    openapiFields.add("nationalFormat");
    openapiFields.add("number");
    openapiFields.add("region");
    openapiFields.add("sendEmailOnCreate");
    openapiFields.add("tollFree");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Number
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Number.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Number is not found in the empty JSON string", Number.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Number.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Number` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("nationalFormat") != null && !jsonObj.get("nationalFormat").isJsonNull()) && !jsonObj.get("nationalFormat").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `nationalFormat` to be a primitive type in the JSON string but got `%s`", jsonObj.get("nationalFormat").toString()));
      }
      if ((jsonObj.get("number") != null && !jsonObj.get("number").isJsonNull()) && !jsonObj.get("number").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `number` to be a primitive type in the JSON string but got `%s`", jsonObj.get("number").toString()));
      }
      // validate the optional field `region`
      if (jsonObj.get("region") != null && !jsonObj.get("region").isJsonNull()) {
        Region.validateJsonElement(jsonObj.get("region"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Number.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Number' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Number> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Number.class));

       return (TypeAdapter<T>) new TypeAdapter<Number>() {
           @Override
           public void write(JsonWriter out, Number value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Number read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Number given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Number
   * @throws IOException if the JSON string is invalid with respect to Number
   */
  public static Number fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Number.class);
  }

  /**
   * Convert an instance of Number to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

