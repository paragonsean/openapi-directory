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
import org.openapitools.client.model.SubscriptionChangeItemsInner;

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
 * SubscriptionChange
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:20:59.825309-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class SubscriptionChange {
  public static final String SERIALIZED_NAME_EFFECTIVE_TIME = "effectiveTime";
  @SerializedName(SERIALIZED_NAME_EFFECTIVE_TIME)
  private OffsetDateTime effectiveTime;

  public static final String SERIALIZED_NAME_ITEMS = "items";
  @SerializedName(SERIALIZED_NAME_ITEMS)
  private List<SubscriptionChangeItemsInner> items = new ArrayList<>();

  public static final String SERIALIZED_NAME_KEEP_TRIAL = "keepTrial";
  @SerializedName(SERIALIZED_NAME_KEEP_TRIAL)
  private Boolean keepTrial = false;

  public static final String SERIALIZED_NAME_PREVIEW = "preview";
  @SerializedName(SERIALIZED_NAME_PREVIEW)
  private Boolean preview = false;

  public static final String SERIALIZED_NAME_PRORATED = "prorated";
  @SerializedName(SERIALIZED_NAME_PRORATED)
  private Boolean prorated;

  /**
   * The value determines whether the subscription retains its current &#x60;renewalTime&#x60; or resets it to a newly calculated &#x60;renewalTime&#x60;.
   */
  @JsonAdapter(RenewalPolicyEnum.Adapter.class)
  public enum RenewalPolicyEnum {
    RESET("reset"),
    
    RETAIN("retain");

    private String value;

    RenewalPolicyEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static RenewalPolicyEnum fromValue(String value) {
      for (RenewalPolicyEnum b : RenewalPolicyEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<RenewalPolicyEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final RenewalPolicyEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public RenewalPolicyEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return RenewalPolicyEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      RenewalPolicyEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_RENEWAL_POLICY = "renewalPolicy";
  @SerializedName(SERIALIZED_NAME_RENEWAL_POLICY)
  private RenewalPolicyEnum renewalPolicy;

  public SubscriptionChange() {
  }

  public SubscriptionChange effectiveTime(OffsetDateTime effectiveTime) {
    this.effectiveTime = effectiveTime;
    return this;
  }

  /**
   * The date from which the renewal time (for &#x60;reset&#x60; operations) and proration calculations are made.  If omitted, it will default to the current time.
   * @return effectiveTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getEffectiveTime() {
    return effectiveTime;
  }

  public void setEffectiveTime(OffsetDateTime effectiveTime) {
    this.effectiveTime = effectiveTime;
  }


  public SubscriptionChange items(List<SubscriptionChangeItemsInner> items) {
    this.items = items;
    return this;
  }

  public SubscriptionChange addItemsItem(SubscriptionChangeItemsInner itemsItem) {
    if (this.items == null) {
      this.items = new ArrayList<>();
    }
    this.items.add(itemsItem);
    return this;
  }

  /**
   * Get items
   * @return items
   */
  @javax.annotation.Nonnull
  public List<SubscriptionChangeItemsInner> getItems() {
    return items;
  }

  public void setItems(List<SubscriptionChangeItemsInner> items) {
    this.items = items;
  }


  public SubscriptionChange keepTrial(Boolean keepTrial) {
    this.keepTrial = keepTrial;
    return this;
  }

  /**
   * If set to true and the subscription order has an active trial, it will use that trial further. Works with &#39;retain&#39; renewalPolicy only.
   * @return keepTrial
   */
  @javax.annotation.Nullable
  public Boolean getKeepTrial() {
    return keepTrial;
  }

  public void setKeepTrial(Boolean keepTrial) {
    this.keepTrial = keepTrial;
  }


  public SubscriptionChange preview(Boolean preview) {
    this.preview = preview;
    return this;
  }

  /**
   * If set to true, it will not change the subscription.  It allows for a way to preview the changes that would be made to a subscription.
   * @return preview
   */
  @javax.annotation.Nullable
  public Boolean getPreview() {
    return preview;
  }

  public void setPreview(Boolean preview) {
    this.preview = preview;
  }


  public SubscriptionChange prorated(Boolean prorated) {
    this.prorated = prorated;
    return this;
  }

  /**
   * Whether or not to give a pro rata credit for the amount of time remaining between the &#x60;effectiveTime&#x60; and the end of the current period. In addition, if the &#x60;renewalTime&#x60; is retained (by setting the &#x60;renewalPolicy&#x60; to &#x60;retain&#x60;), then a pro rata debit will occur as well, for the amount between the &#x60;effectiveTime&#x60; and the &#x60;renewalTime&#x60; as a percentage of the normal period size. 
   * @return prorated
   */
  @javax.annotation.Nonnull
  public Boolean getProrated() {
    return prorated;
  }

  public void setProrated(Boolean prorated) {
    this.prorated = prorated;
  }


  public SubscriptionChange renewalPolicy(RenewalPolicyEnum renewalPolicy) {
    this.renewalPolicy = renewalPolicy;
    return this;
  }

  /**
   * The value determines whether the subscription retains its current &#x60;renewalTime&#x60; or resets it to a newly calculated &#x60;renewalTime&#x60;.
   * @return renewalPolicy
   */
  @javax.annotation.Nonnull
  public RenewalPolicyEnum getRenewalPolicy() {
    return renewalPolicy;
  }

  public void setRenewalPolicy(RenewalPolicyEnum renewalPolicy) {
    this.renewalPolicy = renewalPolicy;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    SubscriptionChange subscriptionChange = (SubscriptionChange) o;
    return Objects.equals(this.effectiveTime, subscriptionChange.effectiveTime) &&
        Objects.equals(this.items, subscriptionChange.items) &&
        Objects.equals(this.keepTrial, subscriptionChange.keepTrial) &&
        Objects.equals(this.preview, subscriptionChange.preview) &&
        Objects.equals(this.prorated, subscriptionChange.prorated) &&
        Objects.equals(this.renewalPolicy, subscriptionChange.renewalPolicy);
  }

  @Override
  public int hashCode() {
    return Objects.hash(effectiveTime, items, keepTrial, preview, prorated, renewalPolicy);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class SubscriptionChange {\n");
    sb.append("    effectiveTime: ").append(toIndentedString(effectiveTime)).append("\n");
    sb.append("    items: ").append(toIndentedString(items)).append("\n");
    sb.append("    keepTrial: ").append(toIndentedString(keepTrial)).append("\n");
    sb.append("    preview: ").append(toIndentedString(preview)).append("\n");
    sb.append("    prorated: ").append(toIndentedString(prorated)).append("\n");
    sb.append("    renewalPolicy: ").append(toIndentedString(renewalPolicy)).append("\n");
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
    openapiFields.add("effectiveTime");
    openapiFields.add("items");
    openapiFields.add("keepTrial");
    openapiFields.add("preview");
    openapiFields.add("prorated");
    openapiFields.add("renewalPolicy");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("items");
    openapiRequiredFields.add("prorated");
    openapiRequiredFields.add("renewalPolicy");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to SubscriptionChange
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!SubscriptionChange.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in SubscriptionChange is not found in the empty JSON string", SubscriptionChange.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!SubscriptionChange.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `SubscriptionChange` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : SubscriptionChange.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the json data is an array
      if (!jsonObj.get("items").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `items` to be an array in the JSON string but got `%s`", jsonObj.get("items").toString()));
      }

      JsonArray jsonArrayitems = jsonObj.getAsJsonArray("items");
      // validate the required field `items` (array)
      for (int i = 0; i < jsonArrayitems.size(); i++) {
        SubscriptionChangeItemsInner.validateJsonElement(jsonArrayitems.get(i));
      };
      if (!jsonObj.get("renewalPolicy").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `renewalPolicy` to be a primitive type in the JSON string but got `%s`", jsonObj.get("renewalPolicy").toString()));
      }
      // validate the required field `renewalPolicy`
      RenewalPolicyEnum.validateJsonElement(jsonObj.get("renewalPolicy"));
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!SubscriptionChange.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'SubscriptionChange' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<SubscriptionChange> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(SubscriptionChange.class));

       return (TypeAdapter<T>) new TypeAdapter<SubscriptionChange>() {
           @Override
           public void write(JsonWriter out, SubscriptionChange value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public SubscriptionChange read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of SubscriptionChange given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of SubscriptionChange
   * @throws IOException if the JSON string is invalid with respect to SubscriptionChange
   */
  public static SubscriptionChange fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, SubscriptionChange.class);
  }

  /**
   * Convert an instance of SubscriptionChange to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

