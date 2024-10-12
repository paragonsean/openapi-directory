/*
 * Rebilly REST API
 * # Introduction The Rebilly API is built on HTTP.  Our API is RESTful.  It has predictable resource URLs.  It returns HTTP response codes to indicate errors.  It also accepts and returns JSON in the HTTP body.  You can use your favorite HTTP/REST library for your programming language to use Rebilly's API, or you can use one of our SDKs (currently available in [PHP](https://github.com/Rebilly/rebilly-php) and [Javascript](https://github.com/Rebilly/rebilly-js-sdk)).  We have other APIs that are also available.  Every action from our [app](https://app.rebilly.com) is supported by an API which is documented and available for use so that you may automate any workflows necessary.  This document contains the most commonly integrated resources.  # Authentication  When you sign up for an account, you are given your first secret API key. You can generate additional API keys, and delete API keys (as you may need to rotate your keys in the future). You authenticate to the Rebilly API by providing your secret key in the request header.  Rebilly offers three forms of authentication:  secret key, publishable key, JSON Web Tokens, and public signature key. - [Secret API key](#section/Authentication/SecretApiKey): used for requests made   from the server side. Never share these keys. Keep them guarded and secure. - [Publishable API key](#section/Authentication/PublishableApiKey): used for    requests from the client side. For now can only be used to create    a [Payment Token](#operation/PostToken) and    a [File token](#operation/PostFile). - [JWT](#section/Authentication/JWT): short lifetime tokens that can be assigned a specific expiration time.  Never share your secret keys. Keep them guarded and secure.  &lt;!-- ReDoc-Inject: &lt;security-definitions&gt; --&gt;  # Errors Rebilly follow's the error response format proposed in [RFC 7807](https://tools.ietf.org/html/rfc7807) also known as Problem Details for HTTP APIs.  As with our normal API responses, your client must be prepared to gracefully handle additional members of the response.  ## Forbidden &lt;RedocResponse pointer={\"#/components/responses/Forbidden\"} /&gt;  ## Conflict &lt;RedocResponse pointer={\"#/components/responses/Conflict\"} /&gt;  ## NotFound &lt;RedocResponse pointer={\"#/components/responses/NotFound\"} /&gt;  ## Unauthorized &lt;RedocResponse pointer={\"#/components/responses/Unauthorized\"} /&gt;  ## ValidationError &lt;RedocResponse pointer={\"#/components/responses/ValidationError\"} /&gt;  # SDKs  Rebilly offers a Javascript SDK and a PHP SDK to help interact with the API.  However, no SDK is required to use the API.  Rebilly also offers [FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/),  a client-side iFrame-based solution to help create payment tokens while minimizing PCI DSS compliance burdens and maximizing the customizability. [FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/) is interacting with the [payment tokens creation operation](#operation/PostToken).  ## Javascript SDK  Installation and usage instructions can be found [here](https://docs.rebilly.com/docs/developer-docs/sdks). SDK code examples are included in these docs.  ## PHP SDK For all PHP SDK examples provided in these docs you will need to configure the `$client`. You may do it like this:  ```php $client = new Rebilly\\Client([     'apiKey' =&gt; 'YourApiKeyHere',     'baseUrl' =&gt; 'https://api.rebilly.com', ]); ```  # Using filter with collections Rebilly provides collections filtering. You can use `?filter` param on collections to define which records should be shown in the response.  Here is filter format description:  - Fields and values in filter are separated with `:`: `?filter=firstName:John`.  - Sub-fields are separated with `.`: `?filter=billingAddress.country:US`.  - Multiple filters are separated with `;`: `?filter=firstName:John;lastName:Doe`. They will be joined with `AND` logic. In this example: `firstName:John` AND `lastName:Doe`.  - You can use multiple values using `,` as values separator: `?filter=firstName:John,Bob`. Multiple values specified for a field will be joined with `OR` logic. In this example: `firstName:John` OR `firstName:Bob`.  - To negate the filter use `!`: `?filter=firstName:!John`. Note that you can negate multiple values like this: `?filter=firstName:!John,!Bob`. This filter rule will exclude all Johns and Bobs from the response.  - You can use range filters like this: `?filter=amount:1..10`.  - You can use gte (greater than or equals) filter like this: `?filter=amount:1..`, or lte (less than or equals) than filter like this: `?filter=amount:..10`. This also works for datetime-based fields.  - You can create some [predefined values lists](https://user-api-docs.rebilly.com/#tag/Lists) and use them in filter: `?filter=firstName:@yourListName`. You can also exclude list values: `?filter=firstName:!@yourListName`.  - Datetime-based fields accept values formatted using RFC 3339 like this: `?filter=createdTime:2021-02-14T13:30:00Z`.   # Expand to include embedded objects Rebilly provides the ability to pre-load additional  objects with a request.   You can use `?expand` param on most requests to expand and include embedded objects within the `_embedded` property of the response.  The `_embedded` property contains an array of  objects keyed by the expand parameter value(s).  You may expand multiple objects by passing them as comma-separated to the expand value like so:  ``` ?expand=recentInvoice,customer ```  And in the response, you would see:  ``` \"_embedded\": [     \"recentInvoice\": {...},     \"customer\": {...} ] ``` Expand may be utilitized not only on `GET` requests but also on `PATCH`, `POST`, `PUT` requests too.   # Getting started guide  Rebilly's API has over 300 operations.  That's more than you'll  need to implement your use cases.  If you have a use  case you would like to implement, please consult us for feedback on the best API operations for the task.  Our getting started guide will demonstrate a basic order form use case.  It will allow us to highlight core resources in Rebilly that will be helpful for many other use cases too.  Within 25 minutes, you'll have sent API requests (via our console) to create a subscription order. 
 *
 * The version of the OpenAPI document: 2.1
 * Contact: integrations@rebilly.com
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
import java.time.OffsetDateTime;
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
 * Line item.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:20:59.825309-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class UpcomingInvoiceItem {
  public static final String SERIALIZED_NAME_CREATED_TIME = "createdTime";
  @SerializedName(SERIALIZED_NAME_CREATED_TIME)
  private OffsetDateTime createdTime;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_PERIOD_END_TIME = "periodEndTime";
  @SerializedName(SERIALIZED_NAME_PERIOD_END_TIME)
  private OffsetDateTime periodEndTime;

  public static final String SERIALIZED_NAME_PERIOD_START_TIME = "periodStartTime";
  @SerializedName(SERIALIZED_NAME_PERIOD_START_TIME)
  private OffsetDateTime periodStartTime;

  public static final String SERIALIZED_NAME_QUANTITY = "quantity";
  @SerializedName(SERIALIZED_NAME_QUANTITY)
  private Integer quantity;

  /**
   * Type of line item.
   */
  @JsonAdapter(TypeEnum.Adapter.class)
  public enum TypeEnum {
    DEBIT("debit"),
    
    CREDIT("credit");

    private String value;

    TypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static TypeEnum fromValue(String value) {
      for (TypeEnum b : TypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<TypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final TypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public TypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return TypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      TypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private TypeEnum type;

  public static final String SERIALIZED_NAME_UNIT_PRICE_AMOUNT = "unitPriceAmount";
  @SerializedName(SERIALIZED_NAME_UNIT_PRICE_AMOUNT)
  private Double unitPriceAmount;

  public static final String SERIALIZED_NAME_UNIT_PRICE_CURRENCY = "unitPriceCurrency";
  @SerializedName(SERIALIZED_NAME_UNIT_PRICE_CURRENCY)
  private String unitPriceCurrency;

  public UpcomingInvoiceItem() {
  }

  public UpcomingInvoiceItem(
     OffsetDateTime createdTime
  ) {
    this();
    this.createdTime = createdTime;
  }

  /**
   * Date-time when the item was added to the subscription.
   * @return createdTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getCreatedTime() {
    return createdTime;
  }



  public UpcomingInvoiceItem description(String description) {
    this.description = description;
    return this;
  }

  /**
   * Description of line item.
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public UpcomingInvoiceItem periodEndTime(OffsetDateTime periodEndTime) {
    this.periodEndTime = periodEndTime;
    return this;
  }

  /**
   * Date-time when the period ends for this item.
   * @return periodEndTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getPeriodEndTime() {
    return periodEndTime;
  }

  public void setPeriodEndTime(OffsetDateTime periodEndTime) {
    this.periodEndTime = periodEndTime;
  }


  public UpcomingInvoiceItem periodStartTime(OffsetDateTime periodStartTime) {
    this.periodStartTime = periodStartTime;
    return this;
  }

  /**
   * Date-time when the period begins for this item.
   * @return periodStartTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getPeriodStartTime() {
    return periodStartTime;
  }

  public void setPeriodStartTime(OffsetDateTime periodStartTime) {
    this.periodStartTime = periodStartTime;
  }


  public UpcomingInvoiceItem quantity(Integer quantity) {
    this.quantity = quantity;
    return this;
  }

  /**
   * Quantity of line item.
   * @return quantity
   */
  @javax.annotation.Nonnull
  public Integer getQuantity() {
    return quantity;
  }

  public void setQuantity(Integer quantity) {
    this.quantity = quantity;
  }


  public UpcomingInvoiceItem type(TypeEnum type) {
    this.type = type;
    return this;
  }

  /**
   * Type of line item.
   * @return type
   */
  @javax.annotation.Nonnull
  public TypeEnum getType() {
    return type;
  }

  public void setType(TypeEnum type) {
    this.type = type;
  }


  public UpcomingInvoiceItem unitPriceAmount(Double unitPriceAmount) {
    this.unitPriceAmount = unitPriceAmount;
    return this;
  }

  /**
   * Unit price of the line item.
   * @return unitPriceAmount
   */
  @javax.annotation.Nonnull
  public Double getUnitPriceAmount() {
    return unitPriceAmount;
  }

  public void setUnitPriceAmount(Double unitPriceAmount) {
    this.unitPriceAmount = unitPriceAmount;
  }


  public UpcomingInvoiceItem unitPriceCurrency(String unitPriceCurrency) {
    this.unitPriceCurrency = unitPriceCurrency;
    return this;
  }

  /**
   * ISO 4217 alphabetic currency code.
   * @return unitPriceCurrency
   */
  @javax.annotation.Nonnull
  public String getUnitPriceCurrency() {
    return unitPriceCurrency;
  }

  public void setUnitPriceCurrency(String unitPriceCurrency) {
    this.unitPriceCurrency = unitPriceCurrency;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    UpcomingInvoiceItem upcomingInvoiceItem = (UpcomingInvoiceItem) o;
    return Objects.equals(this.createdTime, upcomingInvoiceItem.createdTime) &&
        Objects.equals(this.description, upcomingInvoiceItem.description) &&
        Objects.equals(this.periodEndTime, upcomingInvoiceItem.periodEndTime) &&
        Objects.equals(this.periodStartTime, upcomingInvoiceItem.periodStartTime) &&
        Objects.equals(this.quantity, upcomingInvoiceItem.quantity) &&
        Objects.equals(this.type, upcomingInvoiceItem.type) &&
        Objects.equals(this.unitPriceAmount, upcomingInvoiceItem.unitPriceAmount) &&
        Objects.equals(this.unitPriceCurrency, upcomingInvoiceItem.unitPriceCurrency);
  }

  @Override
  public int hashCode() {
    return Objects.hash(createdTime, description, periodEndTime, periodStartTime, quantity, type, unitPriceAmount, unitPriceCurrency);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class UpcomingInvoiceItem {\n");
    sb.append("    createdTime: ").append(toIndentedString(createdTime)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    periodEndTime: ").append(toIndentedString(periodEndTime)).append("\n");
    sb.append("    periodStartTime: ").append(toIndentedString(periodStartTime)).append("\n");
    sb.append("    quantity: ").append(toIndentedString(quantity)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
    sb.append("    unitPriceAmount: ").append(toIndentedString(unitPriceAmount)).append("\n");
    sb.append("    unitPriceCurrency: ").append(toIndentedString(unitPriceCurrency)).append("\n");
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
    openapiFields.add("createdTime");
    openapiFields.add("description");
    openapiFields.add("periodEndTime");
    openapiFields.add("periodStartTime");
    openapiFields.add("quantity");
    openapiFields.add("type");
    openapiFields.add("unitPriceAmount");
    openapiFields.add("unitPriceCurrency");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("quantity");
    openapiRequiredFields.add("type");
    openapiRequiredFields.add("unitPriceAmount");
    openapiRequiredFields.add("unitPriceCurrency");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to UpcomingInvoiceItem
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!UpcomingInvoiceItem.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in UpcomingInvoiceItem is not found in the empty JSON string", UpcomingInvoiceItem.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!UpcomingInvoiceItem.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `UpcomingInvoiceItem` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : UpcomingInvoiceItem.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if (!jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
      // validate the required field `type`
      TypeEnum.validateJsonElement(jsonObj.get("type"));
      if (!jsonObj.get("unitPriceCurrency").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `unitPriceCurrency` to be a primitive type in the JSON string but got `%s`", jsonObj.get("unitPriceCurrency").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!UpcomingInvoiceItem.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'UpcomingInvoiceItem' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<UpcomingInvoiceItem> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(UpcomingInvoiceItem.class));

       return (TypeAdapter<T>) new TypeAdapter<UpcomingInvoiceItem>() {
           @Override
           public void write(JsonWriter out, UpcomingInvoiceItem value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public UpcomingInvoiceItem read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of UpcomingInvoiceItem given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of UpcomingInvoiceItem
   * @throws IOException if the JSON string is invalid with respect to UpcomingInvoiceItem
   */
  public static UpcomingInvoiceItem fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, UpcomingInvoiceItem.class);
  }

  /**
   * Convert an instance of UpcomingInvoiceItem to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

