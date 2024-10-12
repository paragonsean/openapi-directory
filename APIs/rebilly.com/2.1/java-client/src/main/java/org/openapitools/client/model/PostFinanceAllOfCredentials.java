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
 * PostFinance credentials object.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:20:59.825309-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PostFinanceAllOfCredentials {
  public static final String SERIALIZED_NAME_KEY_PASSPHRASE = "keyPassphrase";
  @SerializedName(SERIALIZED_NAME_KEY_PASSPHRASE)
  private String keyPassphrase;

  public static final String SERIALIZED_NAME_MERCHANT_ID = "merchantId";
  @SerializedName(SERIALIZED_NAME_MERCHANT_ID)
  private String merchantId;

  public static final String SERIALIZED_NAME_PRIVATE_KEY = "privateKey";
  @SerializedName(SERIALIZED_NAME_PRIVATE_KEY)
  private String privateKey;

  public static final String SERIALIZED_NAME_PSP_ID = "pspId";
  @SerializedName(SERIALIZED_NAME_PSP_ID)
  private String pspId;

  public static final String SERIALIZED_NAME_PUBLIC_KEY = "publicKey";
  @SerializedName(SERIALIZED_NAME_PUBLIC_KEY)
  private String publicKey;

  public static final String SERIALIZED_NAME_SFTP_KEY_PASSPHRASE = "sftpKeyPassphrase";
  @SerializedName(SERIALIZED_NAME_SFTP_KEY_PASSPHRASE)
  private String sftpKeyPassphrase;

  public static final String SERIALIZED_NAME_SFTP_PRIVATE_KEY = "sftpPrivateKey";
  @SerializedName(SERIALIZED_NAME_SFTP_PRIVATE_KEY)
  private String sftpPrivateKey;

  public static final String SERIALIZED_NAME_SFTP_USERNAME = "sftpUsername";
  @SerializedName(SERIALIZED_NAME_SFTP_USERNAME)
  private String sftpUsername;

  public PostFinanceAllOfCredentials() {
  }

  public PostFinanceAllOfCredentials keyPassphrase(String keyPassphrase) {
    this.keyPassphrase = keyPassphrase;
    return this;
  }

  /**
   * Get keyPassphrase
   * @return keyPassphrase
   */
  @javax.annotation.Nonnull
  public String getKeyPassphrase() {
    return keyPassphrase;
  }

  public void setKeyPassphrase(String keyPassphrase) {
    this.keyPassphrase = keyPassphrase;
  }


  public PostFinanceAllOfCredentials merchantId(String merchantId) {
    this.merchantId = merchantId;
    return this;
  }

  /**
   * Get merchantId
   * @return merchantId
   */
  @javax.annotation.Nonnull
  public String getMerchantId() {
    return merchantId;
  }

  public void setMerchantId(String merchantId) {
    this.merchantId = merchantId;
  }


  public PostFinanceAllOfCredentials privateKey(String privateKey) {
    this.privateKey = privateKey;
    return this;
  }

  /**
   * Get privateKey
   * @return privateKey
   */
  @javax.annotation.Nonnull
  public String getPrivateKey() {
    return privateKey;
  }

  public void setPrivateKey(String privateKey) {
    this.privateKey = privateKey;
  }


  public PostFinanceAllOfCredentials pspId(String pspId) {
    this.pspId = pspId;
    return this;
  }

  /**
   * Get pspId
   * @return pspId
   */
  @javax.annotation.Nonnull
  public String getPspId() {
    return pspId;
  }

  public void setPspId(String pspId) {
    this.pspId = pspId;
  }


  public PostFinanceAllOfCredentials publicKey(String publicKey) {
    this.publicKey = publicKey;
    return this;
  }

  /**
   * Get publicKey
   * @return publicKey
   */
  @javax.annotation.Nonnull
  public String getPublicKey() {
    return publicKey;
  }

  public void setPublicKey(String publicKey) {
    this.publicKey = publicKey;
  }


  public PostFinanceAllOfCredentials sftpKeyPassphrase(String sftpKeyPassphrase) {
    this.sftpKeyPassphrase = sftpKeyPassphrase;
    return this;
  }

  /**
   * Get sftpKeyPassphrase
   * @return sftpKeyPassphrase
   */
  @javax.annotation.Nonnull
  public String getSftpKeyPassphrase() {
    return sftpKeyPassphrase;
  }

  public void setSftpKeyPassphrase(String sftpKeyPassphrase) {
    this.sftpKeyPassphrase = sftpKeyPassphrase;
  }


  public PostFinanceAllOfCredentials sftpPrivateKey(String sftpPrivateKey) {
    this.sftpPrivateKey = sftpPrivateKey;
    return this;
  }

  /**
   * Get sftpPrivateKey
   * @return sftpPrivateKey
   */
  @javax.annotation.Nonnull
  public String getSftpPrivateKey() {
    return sftpPrivateKey;
  }

  public void setSftpPrivateKey(String sftpPrivateKey) {
    this.sftpPrivateKey = sftpPrivateKey;
  }


  public PostFinanceAllOfCredentials sftpUsername(String sftpUsername) {
    this.sftpUsername = sftpUsername;
    return this;
  }

  /**
   * Get sftpUsername
   * @return sftpUsername
   */
  @javax.annotation.Nonnull
  public String getSftpUsername() {
    return sftpUsername;
  }

  public void setSftpUsername(String sftpUsername) {
    this.sftpUsername = sftpUsername;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PostFinanceAllOfCredentials postFinanceAllOfCredentials = (PostFinanceAllOfCredentials) o;
    return Objects.equals(this.keyPassphrase, postFinanceAllOfCredentials.keyPassphrase) &&
        Objects.equals(this.merchantId, postFinanceAllOfCredentials.merchantId) &&
        Objects.equals(this.privateKey, postFinanceAllOfCredentials.privateKey) &&
        Objects.equals(this.pspId, postFinanceAllOfCredentials.pspId) &&
        Objects.equals(this.publicKey, postFinanceAllOfCredentials.publicKey) &&
        Objects.equals(this.sftpKeyPassphrase, postFinanceAllOfCredentials.sftpKeyPassphrase) &&
        Objects.equals(this.sftpPrivateKey, postFinanceAllOfCredentials.sftpPrivateKey) &&
        Objects.equals(this.sftpUsername, postFinanceAllOfCredentials.sftpUsername);
  }

  @Override
  public int hashCode() {
    return Objects.hash(keyPassphrase, merchantId, privateKey, pspId, publicKey, sftpKeyPassphrase, sftpPrivateKey, sftpUsername);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PostFinanceAllOfCredentials {\n");
    sb.append("    keyPassphrase: ").append("*").append("\n");
    sb.append("    merchantId: ").append(toIndentedString(merchantId)).append("\n");
    sb.append("    privateKey: ").append("*").append("\n");
    sb.append("    pspId: ").append(toIndentedString(pspId)).append("\n");
    sb.append("    publicKey: ").append(toIndentedString(publicKey)).append("\n");
    sb.append("    sftpKeyPassphrase: ").append("*").append("\n");
    sb.append("    sftpPrivateKey: ").append("*").append("\n");
    sb.append("    sftpUsername: ").append(toIndentedString(sftpUsername)).append("\n");
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
    openapiFields.add("keyPassphrase");
    openapiFields.add("merchantId");
    openapiFields.add("privateKey");
    openapiFields.add("pspId");
    openapiFields.add("publicKey");
    openapiFields.add("sftpKeyPassphrase");
    openapiFields.add("sftpPrivateKey");
    openapiFields.add("sftpUsername");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("keyPassphrase");
    openapiRequiredFields.add("merchantId");
    openapiRequiredFields.add("privateKey");
    openapiRequiredFields.add("pspId");
    openapiRequiredFields.add("publicKey");
    openapiRequiredFields.add("sftpKeyPassphrase");
    openapiRequiredFields.add("sftpPrivateKey");
    openapiRequiredFields.add("sftpUsername");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PostFinanceAllOfCredentials
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PostFinanceAllOfCredentials.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PostFinanceAllOfCredentials is not found in the empty JSON string", PostFinanceAllOfCredentials.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PostFinanceAllOfCredentials.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PostFinanceAllOfCredentials` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : PostFinanceAllOfCredentials.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("keyPassphrase").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `keyPassphrase` to be a primitive type in the JSON string but got `%s`", jsonObj.get("keyPassphrase").toString()));
      }
      if (!jsonObj.get("merchantId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `merchantId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("merchantId").toString()));
      }
      if (!jsonObj.get("privateKey").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `privateKey` to be a primitive type in the JSON string but got `%s`", jsonObj.get("privateKey").toString()));
      }
      if (!jsonObj.get("pspId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `pspId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("pspId").toString()));
      }
      if (!jsonObj.get("publicKey").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `publicKey` to be a primitive type in the JSON string but got `%s`", jsonObj.get("publicKey").toString()));
      }
      if (!jsonObj.get("sftpKeyPassphrase").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `sftpKeyPassphrase` to be a primitive type in the JSON string but got `%s`", jsonObj.get("sftpKeyPassphrase").toString()));
      }
      if (!jsonObj.get("sftpPrivateKey").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `sftpPrivateKey` to be a primitive type in the JSON string but got `%s`", jsonObj.get("sftpPrivateKey").toString()));
      }
      if (!jsonObj.get("sftpUsername").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `sftpUsername` to be a primitive type in the JSON string but got `%s`", jsonObj.get("sftpUsername").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PostFinanceAllOfCredentials.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PostFinanceAllOfCredentials' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PostFinanceAllOfCredentials> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PostFinanceAllOfCredentials.class));

       return (TypeAdapter<T>) new TypeAdapter<PostFinanceAllOfCredentials>() {
           @Override
           public void write(JsonWriter out, PostFinanceAllOfCredentials value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PostFinanceAllOfCredentials read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PostFinanceAllOfCredentials given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PostFinanceAllOfCredentials
   * @throws IOException if the JSON string is invalid with respect to PostFinanceAllOfCredentials
   */
  public static PostFinanceAllOfCredentials fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PostFinanceAllOfCredentials.class);
  }

  /**
   * Convert an instance of PostFinanceAllOfCredentials to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

