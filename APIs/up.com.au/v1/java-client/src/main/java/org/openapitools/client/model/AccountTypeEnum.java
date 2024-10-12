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
import com.google.gson.annotations.SerializedName;

import java.io.IOException;
import com.google.gson.TypeAdapter;
import com.google.gson.JsonElement;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;

/**
 * Specifies the type of bank account. Currently returned values are &#x60;SAVER&#x60; and &#x60;TRANSACTIONAL&#x60;. 
 */
@JsonAdapter(AccountTypeEnum.Adapter.class)
public enum AccountTypeEnum {
  
  SAVER("SAVER"),
  
  TRANSACTIONAL("TRANSACTIONAL");

  private String value;

  AccountTypeEnum(String value) {
    this.value = value;
  }

  public String getValue() {
    return value;
  }

  @Override
  public String toString() {
    return String.valueOf(value);
  }

  public static AccountTypeEnum fromValue(String value) {
    for (AccountTypeEnum b : AccountTypeEnum.values()) {
      if (b.value.equals(value)) {
        return b;
      }
    }
    throw new IllegalArgumentException("Unexpected value '" + value + "'");
  }

  public static class Adapter extends TypeAdapter<AccountTypeEnum> {
    @Override
    public void write(final JsonWriter jsonWriter, final AccountTypeEnum enumeration) throws IOException {
      jsonWriter.value(enumeration.getValue());
    }

    @Override
    public AccountTypeEnum read(final JsonReader jsonReader) throws IOException {
      String value = jsonReader.nextString();
      return AccountTypeEnum.fromValue(value);
    }
  }

  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
    String value = jsonElement.getAsString();
    AccountTypeEnum.fromValue(value);
  }
}

