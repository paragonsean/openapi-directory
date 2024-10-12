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
import java.util.Arrays;
import org.openapitools.client.model.CommonScheduleInstruction;
import org.openapitools.client.model.CustomEventScheduleInstruction;
import org.openapitools.client.model.DayOfWeekLong;
import org.openapitools.client.model.InvoiceRetryScheduleInstruction;
import org.openapitools.client.model.ServicePeriodAnchorInstruction;

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
 * DayOfWeek
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:20:59.825309-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class DayOfWeek extends CommonScheduleInstruction {
  /**
   * Gets or Sets method
   */
  @JsonAdapter(MethodEnum.Adapter.class)
  public enum MethodEnum {
    INTELLIGENT("intelligent"),
    
    IMMEDIATELY("immediately"),
    
    DATE_INTERVAL("date-interval"),
    
    DAY_OF_MONTH("day-of-month"),
    
    DAY_OF_WEEK("day-of-week");

    private String value;

    MethodEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static MethodEnum fromValue(String value) {
      for (MethodEnum b : MethodEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<MethodEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final MethodEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public MethodEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return MethodEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      MethodEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_METHOD = "method";
  @SerializedName(SERIALIZED_NAME_METHOD)
  protected MethodEnum method;

  public static final String SERIALIZED_NAME_DAY = "day";
  @SerializedName(SERIALIZED_NAME_DAY)
  private DayOfWeekLong day;

  public static final String SERIALIZED_NAME_TIME = "time";
  @SerializedName(SERIALIZED_NAME_TIME)
  private String time;

  /**
   * Gets or Sets week
   */
  @JsonAdapter(WeekEnum.Adapter.class)
  public enum WeekEnum {
    NEXT("next"),
    
    FIRST_IN_MONTH("first-in-month"),
    
    LAST_IN_MONTH("last-in-month");

    private String value;

    WeekEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static WeekEnum fromValue(String value) {
      for (WeekEnum b : WeekEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<WeekEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final WeekEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public WeekEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return WeekEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      WeekEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_WEEK = "week";
  @SerializedName(SERIALIZED_NAME_WEEK)
  private WeekEnum week = WeekEnum.NEXT;

  public DayOfWeek() {
    this.method = this.getClass().getSimpleName();
  }

  public DayOfWeek method(MethodEnum method) {
    this.method = method;
    return this;
  }

  /**
   * Get method
   * @return method
   */
  @javax.annotation.Nonnull
  public MethodEnum getMethod() {
    return method;
  }

  public void setMethod(MethodEnum method) {
    this.method = method;
  }


  public DayOfWeek day(DayOfWeekLong day) {
    this.day = day;
    return this;
  }

  /**
   * Get day
   * @return day
   */
  @javax.annotation.Nonnull
  public DayOfWeekLong getDay() {
    return day;
  }

  public void setDay(DayOfWeekLong day) {
    this.day = day;
  }


  public DayOfWeek time(String time) {
    this.time = time;
    return this;
  }

  /**
   * Extended ISO-8601 format of time.
   * @return time
   */
  @javax.annotation.Nullable
  public String getTime() {
    return time;
  }

  public void setTime(String time) {
    this.time = time;
  }


  public DayOfWeek week(WeekEnum week) {
    this.week = week;
    return this;
  }

  /**
   * Get week
   * @return week
   */
  @javax.annotation.Nullable
  public WeekEnum getWeek() {
    return week;
  }

  public void setWeek(WeekEnum week) {
    this.week = week;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    DayOfWeek dayOfWeek = (DayOfWeek) o;
    return Objects.equals(this.method, dayOfWeek.method) &&
        Objects.equals(this.day, dayOfWeek.day) &&
        Objects.equals(this.time, dayOfWeek.time) &&
        Objects.equals(this.week, dayOfWeek.week) &&
        super.equals(o);
  }

  @Override
  public int hashCode() {
    return Objects.hash(method, day, time, week, super.hashCode());
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class DayOfWeek {\n");
    sb.append("    ").append(toIndentedString(super.toString())).append("\n");
    sb.append("    method: ").append(toIndentedString(method)).append("\n");
    sb.append("    day: ").append(toIndentedString(day)).append("\n");
    sb.append("    time: ").append(toIndentedString(time)).append("\n");
    sb.append("    week: ").append(toIndentedString(week)).append("\n");
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
    openapiFields.add("method");
    openapiFields.add("day");
    openapiFields.add("time");
    openapiFields.add("week");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("method");
    openapiRequiredFields.add("day");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to DayOfWeek
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!DayOfWeek.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in DayOfWeek is not found in the empty JSON string", DayOfWeek.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!DayOfWeek.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `DayOfWeek` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : DayOfWeek.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!DayOfWeek.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'DayOfWeek' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<DayOfWeek> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(DayOfWeek.class));

       return (TypeAdapter<T>) new TypeAdapter<DayOfWeek>() {
           @Override
           public void write(JsonWriter out, DayOfWeek value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public DayOfWeek read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of DayOfWeek given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of DayOfWeek
   * @throws IOException if the JSON string is invalid with respect to DayOfWeek
   */
  public static DayOfWeek fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, DayOfWeek.class);
  }

  /**
   * Convert an instance of DayOfWeek to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

