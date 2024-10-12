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
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import org.openapitools.client.model.AclInner;
import org.openapitools.client.model.CustomerLink;

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
 * CustomerJWT
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:20:59.825309-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CustomerJWT {
  public static final String SERIALIZED_NAME_LINKS = "_links";
  @SerializedName(SERIALIZED_NAME_LINKS)
  private List<CustomerLink> links = new ArrayList<>();

  public static final String SERIALIZED_NAME_ACL = "acl";
  @SerializedName(SERIALIZED_NAME_ACL)
  private List<AclInner> acl = new ArrayList<>();

  public static final String SERIALIZED_NAME_CREATED_TIME = "createdTime";
  @SerializedName(SERIALIZED_NAME_CREATED_TIME)
  private OffsetDateTime createdTime;

  public static final String SERIALIZED_NAME_CUSTOM_CLAIMS = "customClaims";
  @SerializedName(SERIALIZED_NAME_CUSTOM_CLAIMS)
  private Map<String, Object> customClaims = new HashMap<>();

  public static final String SERIALIZED_NAME_CUSTOMER_ID = "customerId";
  @SerializedName(SERIALIZED_NAME_CUSTOMER_ID)
  private String customerId;

  public static final String SERIALIZED_NAME_EXPIRED_TIME = "expiredTime";
  @SerializedName(SERIALIZED_NAME_EXPIRED_TIME)
  private OffsetDateTime expiredTime;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_INVALIDATE = "invalidate";
  @SerializedName(SERIALIZED_NAME_INVALIDATE)
  private Boolean invalidate = true;

  public static final String SERIALIZED_NAME_ONE_TIME_PASSWORD = "oneTimePassword";
  @SerializedName(SERIALIZED_NAME_ONE_TIME_PASSWORD)
  private String oneTimePassword;

  public static final String SERIALIZED_NAME_TOKEN = "token";
  @SerializedName(SERIALIZED_NAME_TOKEN)
  private String token;

  /**
   * Session type.
   */
  @JsonAdapter(TypeEnum.Adapter.class)
  public enum TypeEnum {
    CUSTOMER("customer");

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

  public static final String SERIALIZED_NAME_UPDATED_TIME = "updatedTime";
  @SerializedName(SERIALIZED_NAME_UPDATED_TIME)
  private OffsetDateTime updatedTime;

  public CustomerJWT() {
  }

  public CustomerJWT(
     List<CustomerLink> links, 
     OffsetDateTime createdTime, 
     String customerId, 
     String id, 
     String token, 
     TypeEnum type, 
     OffsetDateTime updatedTime
  ) {
    this();
    this.links = links;
    this.createdTime = createdTime;
    this.customerId = customerId;
    this.id = id;
    this.token = token;
    this.type = type;
    this.updatedTime = updatedTime;
  }

  /**
   * The links related to resource.
   * @return links
   */
  @javax.annotation.Nullable
  public List<CustomerLink> getLinks() {
    return links;
  }



  public CustomerJWT acl(List<AclInner> acl) {
    this.acl = acl;
    return this;
  }

  public CustomerJWT addAclItem(AclInner aclItem) {
    if (this.acl == null) {
      this.acl = new ArrayList<>();
    }
    this.acl.add(aclItem);
    return this;
  }

  /**
   * Get acl
   * @return acl
   */
  @javax.annotation.Nullable
  public List<AclInner> getAcl() {
    return acl;
  }

  public void setAcl(List<AclInner> acl) {
    this.acl = acl;
  }


  /**
   * Session created time.
   * @return createdTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getCreatedTime() {
    return createdTime;
  }



  public CustomerJWT customClaims(Map<String, Object> customClaims) {
    this.customClaims = customClaims;
    return this;
  }

  public CustomerJWT putCustomClaimsItem(String key, Object customClaimsItem) {
    if (this.customClaims == null) {
      this.customClaims = new HashMap<>();
    }
    this.customClaims.put(key, customClaimsItem);
    return this;
  }

  /**
   * Get customClaims
   * @return customClaims
   */
  @javax.annotation.Nullable
  public Map<String, Object> getCustomClaims() {
    return customClaims;
  }

  public void setCustomClaims(Map<String, Object> customClaims) {
    this.customClaims = customClaims;
  }


  /**
   * The customer&#39;s ID.
   * @return customerId
   */
  @javax.annotation.Nullable
  public String getCustomerId() {
    return customerId;
  }



  public CustomerJWT expiredTime(OffsetDateTime expiredTime) {
    this.expiredTime = expiredTime;
    return this;
  }

  /**
   * Session expired time. Defaults to one hour.
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
   * The session identifier string.
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }



  public CustomerJWT invalidate(Boolean invalidate) {
    this.invalidate = invalidate;
    return this;
  }

  /**
   * Whether to invalidate token after exchange or not.
   * @return invalidate
   */
  @javax.annotation.Nullable
  public Boolean getInvalidate() {
    return invalidate;
  }

  public void setInvalidate(Boolean invalidate) {
    this.invalidate = invalidate;
  }


  public CustomerJWT oneTimePassword(String oneTimePassword) {
    this.oneTimePassword = oneTimePassword;
    return this;
  }

  /**
   * The one time password sent via an email. Should contain digits only.
   * @return oneTimePassword
   */
  @javax.annotation.Nullable
  public String getOneTimePassword() {
    return oneTimePassword;
  }

  public void setOneTimePassword(String oneTimePassword) {
    this.oneTimePassword = oneTimePassword;
  }


  /**
   * The session&#39;s token used for authentication.
   * @return token
   */
  @javax.annotation.Nullable
  public String getToken() {
    return token;
  }



  /**
   * Session type.
   * @return type
   */
  @javax.annotation.Nullable
  public TypeEnum getType() {
    return type;
  }



  /**
   * Session updated time.
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
    CustomerJWT customerJWT = (CustomerJWT) o;
    return Objects.equals(this.links, customerJWT.links) &&
        Objects.equals(this.acl, customerJWT.acl) &&
        Objects.equals(this.createdTime, customerJWT.createdTime) &&
        Objects.equals(this.customClaims, customerJWT.customClaims) &&
        Objects.equals(this.customerId, customerJWT.customerId) &&
        Objects.equals(this.expiredTime, customerJWT.expiredTime) &&
        Objects.equals(this.id, customerJWT.id) &&
        Objects.equals(this.invalidate, customerJWT.invalidate) &&
        Objects.equals(this.oneTimePassword, customerJWT.oneTimePassword) &&
        Objects.equals(this.token, customerJWT.token) &&
        Objects.equals(this.type, customerJWT.type) &&
        Objects.equals(this.updatedTime, customerJWT.updatedTime);
  }

  @Override
  public int hashCode() {
    return Objects.hash(links, acl, createdTime, customClaims, customerId, expiredTime, id, invalidate, oneTimePassword, token, type, updatedTime);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CustomerJWT {\n");
    sb.append("    links: ").append(toIndentedString(links)).append("\n");
    sb.append("    acl: ").append(toIndentedString(acl)).append("\n");
    sb.append("    createdTime: ").append(toIndentedString(createdTime)).append("\n");
    sb.append("    customClaims: ").append(toIndentedString(customClaims)).append("\n");
    sb.append("    customerId: ").append(toIndentedString(customerId)).append("\n");
    sb.append("    expiredTime: ").append(toIndentedString(expiredTime)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    invalidate: ").append(toIndentedString(invalidate)).append("\n");
    sb.append("    oneTimePassword: ").append(toIndentedString(oneTimePassword)).append("\n");
    sb.append("    token: ").append(toIndentedString(token)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
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
    openapiFields.add("acl");
    openapiFields.add("createdTime");
    openapiFields.add("customClaims");
    openapiFields.add("customerId");
    openapiFields.add("expiredTime");
    openapiFields.add("id");
    openapiFields.add("invalidate");
    openapiFields.add("oneTimePassword");
    openapiFields.add("token");
    openapiFields.add("type");
    openapiFields.add("updatedTime");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CustomerJWT
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CustomerJWT.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CustomerJWT is not found in the empty JSON string", CustomerJWT.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CustomerJWT.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CustomerJWT` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
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
            CustomerLink.validateJsonElement(jsonArraylinks.get(i));
          };
        }
      }
      if (jsonObj.get("acl") != null && !jsonObj.get("acl").isJsonNull()) {
        JsonArray jsonArrayacl = jsonObj.getAsJsonArray("acl");
        if (jsonArrayacl != null) {
          // ensure the json data is an array
          if (!jsonObj.get("acl").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `acl` to be an array in the JSON string but got `%s`", jsonObj.get("acl").toString()));
          }

          // validate the optional field `acl` (array)
          for (int i = 0; i < jsonArrayacl.size(); i++) {
            AclInner.validateJsonElement(jsonArrayacl.get(i));
          };
        }
      }
      if ((jsonObj.get("customerId") != null && !jsonObj.get("customerId").isJsonNull()) && !jsonObj.get("customerId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `customerId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("customerId").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("oneTimePassword") != null && !jsonObj.get("oneTimePassword").isJsonNull()) && !jsonObj.get("oneTimePassword").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `oneTimePassword` to be a primitive type in the JSON string but got `%s`", jsonObj.get("oneTimePassword").toString()));
      }
      if ((jsonObj.get("token") != null && !jsonObj.get("token").isJsonNull()) && !jsonObj.get("token").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `token` to be a primitive type in the JSON string but got `%s`", jsonObj.get("token").toString()));
      }
      if ((jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) && !jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
      // validate the optional field `type`
      if (jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) {
        TypeEnum.validateJsonElement(jsonObj.get("type"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CustomerJWT.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CustomerJWT' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CustomerJWT> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CustomerJWT.class));

       return (TypeAdapter<T>) new TypeAdapter<CustomerJWT>() {
           @Override
           public void write(JsonWriter out, CustomerJWT value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CustomerJWT read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CustomerJWT given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CustomerJWT
   * @throws IOException if the JSON string is invalid with respect to CustomerJWT
   */
  public static CustomerJWT fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CustomerJWT.class);
  }

  /**
   * Convert an instance of CustomerJWT to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

