/*
 * Velo Payments APIs
 * ## Terms and Definitions  Throughout this document and the Velo platform the following terms are used:  * **Payor.** An entity (typically a corporation) which wishes to pay funds to one or more payees via a payout. * **Payee.** The recipient of funds paid out by a payor. * **Payment.** A single transfer of funds from a payor to a payee. * **Payout.** A batch of Payments, typically used by a payor to logically group payments (e.g. by business day). Technically there need be no relationship between the payments in a payout - a single payout can contain payments to multiple payees and/or multiple payments to a single payee. * **Sandbox.** An integration environment provided by Velo Payments which offers a similar API experience to the production environment, but all funding and payment events are simulated, along with many other services such as OFAC sanctions list checking.  ## Overview  The Velo Payments API allows a payor to perform a number of operations. The following is a list of the main capabilities in a natural order of execution:  * Authenticate with the Velo platform * Maintain a collection of payees * Query the payor’s current balance of funds within the platform and perform additional funding * Issue payments to payees * Query the platform for a history of those payments  This document describes the main concepts and APIs required to get up and running with the Velo Payments platform. It is not an exhaustive API reference. For that, please see the separate Velo Payments API Reference.  ## API Considerations  The Velo Payments API is REST based and uses the JSON format for requests and responses.  Most calls are secured using OAuth 2 security and require a valid authentication access token for successful operation. See the Authentication section for details.  Where a dynamic value is required in the examples below, the {token} format is used, suggesting that the caller needs to supply the appropriate value of the token in question (without including the { or } characters).  Where curl examples are given, the –d @filename.json approach is used, indicating that the request body should be placed into a file named filename.json in the current directory. Each of the curl examples in this document should be considered a single line on the command-line, regardless of how they appear in print.  ## Authenticating with the Velo Platform  Once Velo backoffice staff have added your organization as a payor within the Velo platform sandbox, they will create you a payor Id, an API key and an API secret and share these with you in a secure manner.  You will need to use these values to authenticate with the Velo platform in order to gain access to the APIs. The steps to take are explained in the following:  create a string comprising the API key (e.g. 44a9537d-d55d-4b47-8082-14061c2bcdd8) and API secret (e.g. c396b26b-137a-44fd-87f5-34631f8fd529) with a colon between them. E.g. 44a9537d-d55d-4b47-8082-14061c2bcdd8:c396b26b-137a-44fd-87f5-34631f8fd529  base64 encode this string. E.g.: NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==  create an HTTP **Authorization** header with the value set to e.g. Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==  perform the Velo authentication REST call using the HTTP header created above e.g. via curl:  ```   curl -X POST \\   -H \"Content-Type: application/json\" \\   -H \"Authorization: Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==\" \\   'https://api.sandbox.velopayments.com/v1/authenticate?grant_type=client_credentials' ```  If successful, this call will result in a **200** HTTP status code and a response body such as:  ```   {     \"access_token\":\"19f6bafd-93fd-4747-b229-00507bbc991f\",     \"token_type\":\"bearer\",     \"expires_in\":1799,     \"scope\":\"...\"   } ``` ## API access following authentication Following successful authentication, the value of the access_token field in the response (indicated in green above) should then be presented with all subsequent API calls to allow the Velo platform to validate that the caller is authenticated.  This is achieved by setting the HTTP Authorization header with the value set to e.g. Bearer 19f6bafd-93fd-4747-b229-00507bbc991f such as the curl example below:  ```   -H \"Authorization: Bearer 19f6bafd-93fd-4747-b229-00507bbc991f \" ```  If you make other Velo API calls which require authorization but the Authorization header is missing or invalid then you will get a **401** HTTP status response. 
 *
 * The version of the OpenAPI document: 2.35.57
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
import java.util.UUID;

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
 * SourceAccountV3
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:01:55.204956-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class SourceAccountV3 {
  public static final String SERIALIZED_NAME_CURRENCY = "currency";
  @SerializedName(SERIALIZED_NAME_CURRENCY)
  private String currency;

  public static final String SERIALIZED_NAME_SOURCE_ACCOUNT_ID = "sourceAccountId";
  @SerializedName(SERIALIZED_NAME_SOURCE_ACCOUNT_ID)
  private UUID sourceAccountId;

  public static final String SERIALIZED_NAME_SOURCE_ACCOUNT_NAME = "sourceAccountName";
  @SerializedName(SERIALIZED_NAME_SOURCE_ACCOUNT_NAME)
  private String sourceAccountName;

  public static final String SERIALIZED_NAME_TOTAL_PAYOUT_COST = "totalPayoutCost";
  @SerializedName(SERIALIZED_NAME_TOTAL_PAYOUT_COST)
  private Integer totalPayoutCost;

  public SourceAccountV3() {
  }

  public SourceAccountV3 currency(String currency) {
    this.currency = currency;
    return this;
  }

  /**
   * Valid ISO 4217 3 letter currency code. See the &lt;a href&#x3D;\&quot;https://www.iso.org/iso-4217-currency-codes.html\&quot; target&#x3D;\&quot;_blank\&quot; a&gt;ISO specification&lt;/a&gt; for details.
   * @return currency
   */
  @javax.annotation.Nonnull
  public String getCurrency() {
    return currency;
  }

  public void setCurrency(String currency) {
    this.currency = currency;
  }


  public SourceAccountV3 sourceAccountId(UUID sourceAccountId) {
    this.sourceAccountId = sourceAccountId;
    return this;
  }

  /**
   * The id of the payout
   * @return sourceAccountId
   */
  @javax.annotation.Nonnull
  public UUID getSourceAccountId() {
    return sourceAccountId;
  }

  public void setSourceAccountId(UUID sourceAccountId) {
    this.sourceAccountId = sourceAccountId;
  }


  public SourceAccountV3 sourceAccountName(String sourceAccountName) {
    this.sourceAccountName = sourceAccountName;
    return this;
  }

  /**
   * The name of the source account as referencec in the payout
   * @return sourceAccountName
   */
  @javax.annotation.Nonnull
  public String getSourceAccountName() {
    return sourceAccountName;
  }

  public void setSourceAccountName(String sourceAccountName) {
    this.sourceAccountName = sourceAccountName;
  }


  public SourceAccountV3 totalPayoutCost(Integer totalPayoutCost) {
    this.totalPayoutCost = totalPayoutCost;
    return this;
  }

  /**
   * The total amount (in mnor units) that will be debited from the source account for the payout
   * @return totalPayoutCost
   */
  @javax.annotation.Nonnull
  public Integer getTotalPayoutCost() {
    return totalPayoutCost;
  }

  public void setTotalPayoutCost(Integer totalPayoutCost) {
    this.totalPayoutCost = totalPayoutCost;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    SourceAccountV3 sourceAccountV3 = (SourceAccountV3) o;
    return Objects.equals(this.currency, sourceAccountV3.currency) &&
        Objects.equals(this.sourceAccountId, sourceAccountV3.sourceAccountId) &&
        Objects.equals(this.sourceAccountName, sourceAccountV3.sourceAccountName) &&
        Objects.equals(this.totalPayoutCost, sourceAccountV3.totalPayoutCost);
  }

  @Override
  public int hashCode() {
    return Objects.hash(currency, sourceAccountId, sourceAccountName, totalPayoutCost);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class SourceAccountV3 {\n");
    sb.append("    currency: ").append(toIndentedString(currency)).append("\n");
    sb.append("    sourceAccountId: ").append(toIndentedString(sourceAccountId)).append("\n");
    sb.append("    sourceAccountName: ").append(toIndentedString(sourceAccountName)).append("\n");
    sb.append("    totalPayoutCost: ").append(toIndentedString(totalPayoutCost)).append("\n");
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
    openapiFields.add("currency");
    openapiFields.add("sourceAccountId");
    openapiFields.add("sourceAccountName");
    openapiFields.add("totalPayoutCost");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("currency");
    openapiRequiredFields.add("sourceAccountId");
    openapiRequiredFields.add("sourceAccountName");
    openapiRequiredFields.add("totalPayoutCost");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to SourceAccountV3
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!SourceAccountV3.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in SourceAccountV3 is not found in the empty JSON string", SourceAccountV3.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!SourceAccountV3.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `SourceAccountV3` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : SourceAccountV3.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("currency").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `currency` to be a primitive type in the JSON string but got `%s`", jsonObj.get("currency").toString()));
      }
      if (!jsonObj.get("sourceAccountId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `sourceAccountId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("sourceAccountId").toString()));
      }
      if (!jsonObj.get("sourceAccountName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `sourceAccountName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("sourceAccountName").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!SourceAccountV3.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'SourceAccountV3' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<SourceAccountV3> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(SourceAccountV3.class));

       return (TypeAdapter<T>) new TypeAdapter<SourceAccountV3>() {
           @Override
           public void write(JsonWriter out, SourceAccountV3 value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public SourceAccountV3 read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of SourceAccountV3 given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of SourceAccountV3
   * @throws IOException if the JSON string is invalid with respect to SourceAccountV3
   */
  public static SourceAccountV3 fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, SourceAccountV3.class);
  }

  /**
   * Convert an instance of SourceAccountV3 to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

