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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.CouponRestriction;
import org.openapitools.client.model.Discount;
import org.openapitools.client.model.SelfLink;

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
 * Coupons and Discounts.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:20:59.825309-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Coupon {
  public static final String SERIALIZED_NAME_LINKS = "_links";
  @SerializedName(SERIALIZED_NAME_LINKS)
  private List<SelfLink> links = new ArrayList<>();

  public static final String SERIALIZED_NAME_CREATED_TIME = "createdTime";
  @SerializedName(SERIALIZED_NAME_CREATED_TIME)
  private OffsetDateTime createdTime;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_DISCOUNT = "discount";
  @SerializedName(SERIALIZED_NAME_DISCOUNT)
  private Discount discount;

  public static final String SERIALIZED_NAME_EXPIRED_TIME = "expiredTime";
  @SerializedName(SERIALIZED_NAME_EXPIRED_TIME)
  private OffsetDateTime expiredTime;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_ISSUED_TIME = "issuedTime";
  @SerializedName(SERIALIZED_NAME_ISSUED_TIME)
  private OffsetDateTime issuedTime;

  public static final String SERIALIZED_NAME_REDEMPTIONS_COUNT = "redemptionsCount";
  @SerializedName(SERIALIZED_NAME_REDEMPTIONS_COUNT)
  private Integer redemptionsCount;

  public static final String SERIALIZED_NAME_RESTRICTIONS = "restrictions";
  @SerializedName(SERIALIZED_NAME_RESTRICTIONS)
  private List<CouponRestriction> restrictions = new ArrayList<>();

  /**
   * If coupon enabled.
   */
  @JsonAdapter(StatusEnum.Adapter.class)
  public enum StatusEnum {
    DRAFT("draft"),
    
    ISSUED("issued"),
    
    EXPIRED("expired");

    private String value;

    StatusEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static StatusEnum fromValue(String value) {
      for (StatusEnum b : StatusEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<StatusEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final StatusEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public StatusEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return StatusEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      StatusEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private StatusEnum status;

  public static final String SERIALIZED_NAME_UPDATED_TIME = "updatedTime";
  @SerializedName(SERIALIZED_NAME_UPDATED_TIME)
  private OffsetDateTime updatedTime;

  public Coupon() {
  }

  public Coupon(
     List<SelfLink> links, 
     OffsetDateTime createdTime, 
     String id, 
     Integer redemptionsCount, 
     StatusEnum status, 
     OffsetDateTime updatedTime
  ) {
    this();
    this.links = links;
    this.createdTime = createdTime;
    this.id = id;
    this.redemptionsCount = redemptionsCount;
    this.status = status;
    this.updatedTime = updatedTime;
  }

  /**
   * The links related to resource.
   * @return links
   */
  @javax.annotation.Nullable
  public List<SelfLink> getLinks() {
    return links;
  }



  /**
   * Coupon created time.
   * @return createdTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getCreatedTime() {
    return createdTime;
  }



  public Coupon description(String description) {
    this.description = description;
    return this;
  }

  /**
   * Your coupon description. When it is not empty this is used for invoice discount item description, otherwise the item&#39;s description uses coupon&#39;s ID like &#39;Coupon \&quot;COUPON-ID\&quot;&#39;. 
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public Coupon discount(Discount discount) {
    this.discount = discount;
    return this;
  }

  /**
   * Get discount
   * @return discount
   */
  @javax.annotation.Nonnull
  public Discount getDiscount() {
    return discount;
  }

  public void setDiscount(Discount discount) {
    this.discount = discount;
  }


  public Coupon expiredTime(OffsetDateTime expiredTime) {
    this.expiredTime = expiredTime;
    return this;
  }

  /**
   * Coupon&#39;s expire time (end time).
   * @return expiredTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getExpiredTime() {
    return expiredTime;
  }

  public void setExpiredTime(OffsetDateTime expiredTime) {
    this.expiredTime = expiredTime;
  }


  /**
   * Coupon&#39;s ID a.k.a redemption code.
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }



  public Coupon issuedTime(OffsetDateTime issuedTime) {
    this.issuedTime = issuedTime;
    return this;
  }

  /**
   * Coupon&#39;s issued time (start time).
   * @return issuedTime
   */
  @javax.annotation.Nonnull
  public OffsetDateTime getIssuedTime() {
    return issuedTime;
  }

  public void setIssuedTime(OffsetDateTime issuedTime) {
    this.issuedTime = issuedTime;
  }


  /**
   * Coupon&#39;s redemptions count.
   * minimum: 0
   * @return redemptionsCount
   */
  @javax.annotation.Nullable
  public Integer getRedemptionsCount() {
    return redemptionsCount;
  }



  public Coupon restrictions(List<CouponRestriction> restrictions) {
    this.restrictions = restrictions;
    return this;
  }

  public Coupon addRestrictionsItem(CouponRestriction restrictionsItem) {
    if (this.restrictions == null) {
      this.restrictions = new ArrayList<>();
    }
    this.restrictions.add(restrictionsItem);
    return this;
  }

  /**
   * Coupon restrictions.
   * @return restrictions
   */
  @javax.annotation.Nullable
  public List<CouponRestriction> getRestrictions() {
    return restrictions;
  }

  public void setRestrictions(List<CouponRestriction> restrictions) {
    this.restrictions = restrictions;
  }


  /**
   * If coupon enabled.
   * @return status
   */
  @javax.annotation.Nullable
  public StatusEnum getStatus() {
    return status;
  }



  /**
   * Coupon updated time.
   * @return updatedTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getUpdatedTime() {
    return updatedTime;
  }




  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Coupon coupon = (Coupon) o;
    return Objects.equals(this.links, coupon.links) &&
        Objects.equals(this.createdTime, coupon.createdTime) &&
        Objects.equals(this.description, coupon.description) &&
        Objects.equals(this.discount, coupon.discount) &&
        Objects.equals(this.expiredTime, coupon.expiredTime) &&
        Objects.equals(this.id, coupon.id) &&
        Objects.equals(this.issuedTime, coupon.issuedTime) &&
        Objects.equals(this.redemptionsCount, coupon.redemptionsCount) &&
        Objects.equals(this.restrictions, coupon.restrictions) &&
        Objects.equals(this.status, coupon.status) &&
        Objects.equals(this.updatedTime, coupon.updatedTime);
  }

  @Override
  public int hashCode() {
    return Objects.hash(links, createdTime, description, discount, expiredTime, id, issuedTime, redemptionsCount, restrictions, status, updatedTime);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Coupon {\n");
    sb.append("    links: ").append(toIndentedString(links)).append("\n");
    sb.append("    createdTime: ").append(toIndentedString(createdTime)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    discount: ").append(toIndentedString(discount)).append("\n");
    sb.append("    expiredTime: ").append(toIndentedString(expiredTime)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    issuedTime: ").append(toIndentedString(issuedTime)).append("\n");
    sb.append("    redemptionsCount: ").append(toIndentedString(redemptionsCount)).append("\n");
    sb.append("    restrictions: ").append(toIndentedString(restrictions)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    updatedTime: ").append(toIndentedString(updatedTime)).append("\n");
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
    openapiFields.add("_links");
    openapiFields.add("createdTime");
    openapiFields.add("description");
    openapiFields.add("discount");
    openapiFields.add("expiredTime");
    openapiFields.add("id");
    openapiFields.add("issuedTime");
    openapiFields.add("redemptionsCount");
    openapiFields.add("restrictions");
    openapiFields.add("status");
    openapiFields.add("updatedTime");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("discount");
    openapiRequiredFields.add("issuedTime");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Coupon
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Coupon.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Coupon is not found in the empty JSON string", Coupon.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Coupon.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Coupon` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : Coupon.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("_links") != null && !jsonObj.get("_links").isJsonNull()) {
        JsonArray jsonArraylinks = jsonObj.getAsJsonArray("_links");
        if (jsonArraylinks != null) {
          // ensure the json data is an array
          if (!jsonObj.get("_links").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `_links` to be an array in the JSON string but got `%s`", jsonObj.get("_links").toString()));
          }

          // validate the optional field `_links` (array)
          for (int i = 0; i < jsonArraylinks.size(); i++) {
            SelfLink.validateJsonElement(jsonArraylinks.get(i));
          };
        }
      }
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      // validate the required field `discount`
      Discount.validateJsonElement(jsonObj.get("discount"));
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if (jsonObj.get("restrictions") != null && !jsonObj.get("restrictions").isJsonNull()) {
        JsonArray jsonArrayrestrictions = jsonObj.getAsJsonArray("restrictions");
        if (jsonArrayrestrictions != null) {
          // ensure the json data is an array
          if (!jsonObj.get("restrictions").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `restrictions` to be an array in the JSON string but got `%s`", jsonObj.get("restrictions").toString()));
          }

          // validate the optional field `restrictions` (array)
          for (int i = 0; i < jsonArrayrestrictions.size(); i++) {
            CouponRestriction.validateJsonElement(jsonArrayrestrictions.get(i));
          };
        }
      }
      if ((jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) && !jsonObj.get("status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("status").toString()));
      }
      // validate the optional field `status`
      if (jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) {
        StatusEnum.validateJsonElement(jsonObj.get("status"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Coupon.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Coupon' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Coupon> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Coupon.class));

       return (TypeAdapter<T>) new TypeAdapter<Coupon>() {
           @Override
           public void write(JsonWriter out, Coupon value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Coupon read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Coupon given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Coupon
   * @throws IOException if the JSON string is invalid with respect to Coupon
   */
  public static Coupon fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Coupon.class);
  }

  /**
   * Convert an instance of Coupon to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

