/*
 * SubscriptionsManagementClient
 * The Admin Subscriptions Management Client.
 *
 * The version of the OpenAPI document: 2015-11-01
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
 * Provisioning state for subscriptions service resources, for example, resource provider registration.
 */
@JsonAdapter(ProvisioningState.Adapter.class)
public enum ProvisioningState {
  
  NOT_SPECIFIED("NotSpecified"),
  
  ACCEPTED("Accepted"),
  
  FAILED("Failed"),
  
  SUCCEEDED("Succeeded");

  private String value;

  ProvisioningState(String value) {
    this.value = value;
  }

  public String getValue() {
    return value;
  }

  @Override
  public String toString() {
    return String.valueOf(value);
  }

  public static ProvisioningState fromValue(String value) {
    for (ProvisioningState b : ProvisioningState.values()) {
      if (b.value.equals(value)) {
        return b;
      }
    }
    throw new IllegalArgumentException("Unexpected value '" + value + "'");
  }

  public static class Adapter extends TypeAdapter<ProvisioningState> {
    @Override
    public void write(final JsonWriter jsonWriter, final ProvisioningState enumeration) throws IOException {
      jsonWriter.value(enumeration.getValue());
    }

    @Override
    public ProvisioningState read(final JsonReader jsonReader) throws IOException {
      String value = jsonReader.nextString();
      return ProvisioningState.fromValue(value);
    }
  }

  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
    String value = jsonElement.getAsString();
    ProvisioningState.fromValue(value);
  }
}

