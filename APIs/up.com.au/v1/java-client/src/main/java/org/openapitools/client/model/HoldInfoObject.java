/*
 * Up API
 * The Up API gives you programmatic access to your balances and transaction data. You can request past transactions or set up webhooks to receive real-time events when new transactions hit your account. It’s new, it’s exciting and it’s just the beginning. 
 *
 * The version of the OpenAPI document: v1
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
import org.openapitools.client.model.MoneyObject;

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
 * Provides information about the amount at which a transaction was in the &#x60;HELD&#x60; status. 
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:04:05.017128-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class HoldInfoObject {
  public static final String SERIALIZED_NAME_AMOUNT = "amount";
  @SerializedName(SERIALIZED_NAME_AMOUNT)
  private MoneyObject amount;

  public static final String SERIALIZED_NAME_FOREIGN_AMOUNT = "foreignAmount";
  @SerializedName(SERIALIZED_NAME_FOREIGN_AMOUNT)
  private MoneyObject foreignAmount;

  public HoldInfoObject() {
  }

  public HoldInfoObject amount(MoneyObject amount) {
    this.amount = amount;
    return this;
  }

  /**
   * The amount of this transaction while in the &#x60;HELD&#x60; status, in Australian dollars. 
   * @return amount
   */
  @javax.annotation.Nonnull
  public MoneyObject getAmount() {
    return amount;
  }

  public void setAmount(MoneyObject amount) {
    this.amount = amount;
  }


  public HoldInfoObject foreignAmount(MoneyObject foreignAmount) {
    this.foreignAmount = foreignAmount;
    return this;
  }

  /**
   * The foreign currency amount of this transaction while in the &#x60;HELD&#x60; status. This field will be &#x60;null&#x60; for domestic transactions. The amount was converted to the AUD amount reflected in the &#x60;amount&#x60; field. 
   * @return foreignAmount
   */
  @javax.annotation.Nullable
  public MoneyObject getForeignAmount() {
    return foreignAmount;
  }

  public void setForeignAmount(MoneyObject foreignAmount) {
    this.foreignAmount = foreignAmount;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    HoldInfoObject holdInfoObject = (HoldInfoObject) o;
    return Objects.equals(this.amount, holdInfoObject.amount) &&
        Objects.equals(this.foreignAmount, holdInfoObject.foreignAmount);
  }

  @Override
  public int hashCode() {
    return Objects.hash(amount, foreignAmount);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class HoldInfoObject {\n");
    sb.append("    amount: ").append(toIndentedString(amount)).append("\n");
    sb.append("    foreignAmount: ").append(toIndentedString(foreignAmount)).append("\n");
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
    openapiFields.add("amount");
    openapiFields.add("foreignAmount");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("amount");
    openapiRequiredFields.add("foreignAmount");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to HoldInfoObject
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!HoldInfoObject.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in HoldInfoObject is not found in the empty JSON string", HoldInfoObject.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!HoldInfoObject.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `HoldInfoObject` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : HoldInfoObject.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the required field `amount`
      MoneyObject.validateJsonElement(jsonObj.get("amount"));
      // validate the required field `foreignAmount`
      MoneyObject.validateJsonElement(jsonObj.get("foreignAmount"));
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!HoldInfoObject.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'HoldInfoObject' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<HoldInfoObject> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(HoldInfoObject.class));

       return (TypeAdapter<T>) new TypeAdapter<HoldInfoObject>() {
           @Override
           public void write(JsonWriter out, HoldInfoObject value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public HoldInfoObject read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of HoldInfoObject given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of HoldInfoObject
   * @throws IOException if the JSON string is invalid with respect to HoldInfoObject
   */
  public static HoldInfoObject fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, HoldInfoObject.class);
  }

  /**
   * Convert an instance of HoldInfoObject to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

