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
 * EMS credentials object.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:20:59.825309-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class EMSAllOfCredentials {
  public static final String SERIALIZED_NAME_CLIENT_CERTIFICATE = "clientCertificate";
  @SerializedName(SERIALIZED_NAME_CLIENT_CERTIFICATE)
  private String clientCertificate;

  public static final String SERIALIZED_NAME_CLIENT_CERTIFICATE_PASSWORD = "clientCertificatePassword";
  @SerializedName(SERIALIZED_NAME_CLIENT_CERTIFICATE_PASSWORD)
  private String clientCertificatePassword;

  public static final String SERIALIZED_NAME_MERCHANT_NAME = "merchantName";
  @SerializedName(SERIALIZED_NAME_MERCHANT_NAME)
  private String merchantName;

  public static final String SERIALIZED_NAME_PASSWORD = "password";
  @SerializedName(SERIALIZED_NAME_PASSWORD)
  private String password;

  public static final String SERIALIZED_NAME_PRIVATE_KEY = "privateKey";
  @SerializedName(SERIALIZED_NAME_PRIVATE_KEY)
  private String privateKey;

  public static final String SERIALIZED_NAME_PRIVATE_KEY_PASSWORD = "privateKeyPassword";
  @SerializedName(SERIALIZED_NAME_PRIVATE_KEY_PASSWORD)
  private String privateKeyPassword;

  public static final String SERIALIZED_NAME_SERVER_CERTIFICATE = "serverCertificate";
  @SerializedName(SERIALIZED_NAME_SERVER_CERTIFICATE)
  private String serverCertificate;

  public static final String SERIALIZED_NAME_SFTP_PRIVATE_KEY = "sftpPrivateKey";
  @SerializedName(SERIALIZED_NAME_SFTP_PRIVATE_KEY)
  private String sftpPrivateKey;

  public static final String SERIALIZED_NAME_STORE_ID = "storeId";
  @SerializedName(SERIALIZED_NAME_STORE_ID)
  private String storeId;

  public static final String SERIALIZED_NAME_USER_ID = "userId";
  @SerializedName(SERIALIZED_NAME_USER_ID)
  private String userId;

  public EMSAllOfCredentials() {
  }

  public EMSAllOfCredentials clientCertificate(String clientCertificate) {
    this.clientCertificate = clientCertificate;
    return this;
  }

  /**
   * Client Certificate.
   * @return clientCertificate
   */
  @javax.annotation.Nonnull
  public String getClientCertificate() {
    return clientCertificate;
  }

  public void setClientCertificate(String clientCertificate) {
    this.clientCertificate = clientCertificate;
  }


  public EMSAllOfCredentials clientCertificatePassword(String clientCertificatePassword) {
    this.clientCertificatePassword = clientCertificatePassword;
    return this;
  }

  /**
   * Client Certificate password.
   * @return clientCertificatePassword
   */
  @javax.annotation.Nonnull
  public String getClientCertificatePassword() {
    return clientCertificatePassword;
  }

  public void setClientCertificatePassword(String clientCertificatePassword) {
    this.clientCertificatePassword = clientCertificatePassword;
  }


  public EMSAllOfCredentials merchantName(String merchantName) {
    this.merchantName = merchantName;
    return this;
  }

  /**
   * Merchant Name for SFTP reconciliation.
   * @return merchantName
   */
  @javax.annotation.Nullable
  public String getMerchantName() {
    return merchantName;
  }

  public void setMerchantName(String merchantName) {
    this.merchantName = merchantName;
  }


  public EMSAllOfCredentials password(String password) {
    this.password = password;
    return this;
  }

  /**
   * EMS password.
   * @return password
   */
  @javax.annotation.Nonnull
  public String getPassword() {
    return password;
  }

  public void setPassword(String password) {
    this.password = password;
  }


  public EMSAllOfCredentials privateKey(String privateKey) {
    this.privateKey = privateKey;
    return this;
  }

  /**
   * Private Key.
   * @return privateKey
   */
  @javax.annotation.Nonnull
  public String getPrivateKey() {
    return privateKey;
  }

  public void setPrivateKey(String privateKey) {
    this.privateKey = privateKey;
  }


  public EMSAllOfCredentials privateKeyPassword(String privateKeyPassword) {
    this.privateKeyPassword = privateKeyPassword;
    return this;
  }

  /**
   * Private key password.
   * @return privateKeyPassword
   */
  @javax.annotation.Nonnull
  public String getPrivateKeyPassword() {
    return privateKeyPassword;
  }

  public void setPrivateKeyPassword(String privateKeyPassword) {
    this.privateKeyPassword = privateKeyPassword;
  }


  public EMSAllOfCredentials serverCertificate(String serverCertificate) {
    this.serverCertificate = serverCertificate;
    return this;
  }

  /**
   * Server Certificate.
   * @return serverCertificate
   */
  @javax.annotation.Nonnull
  public String getServerCertificate() {
    return serverCertificate;
  }

  public void setServerCertificate(String serverCertificate) {
    this.serverCertificate = serverCertificate;
  }


  public EMSAllOfCredentials sftpPrivateKey(String sftpPrivateKey) {
    this.sftpPrivateKey = sftpPrivateKey;
    return this;
  }

  /**
   * SFTP reconciliation private key.
   * @return sftpPrivateKey
   */
  @javax.annotation.Nullable
  public String getSftpPrivateKey() {
    return sftpPrivateKey;
  }

  public void setSftpPrivateKey(String sftpPrivateKey) {
    this.sftpPrivateKey = sftpPrivateKey;
  }


  public EMSAllOfCredentials storeId(String storeId) {
    this.storeId = storeId;
    return this;
  }

  /**
   * EMS store id.
   * @return storeId
   */
  @javax.annotation.Nonnull
  public String getStoreId() {
    return storeId;
  }

  public void setStoreId(String storeId) {
    this.storeId = storeId;
  }


  public EMSAllOfCredentials userId(String userId) {
    this.userId = userId;
    return this;
  }

  /**
   * EMS account id.
   * @return userId
   */
  @javax.annotation.Nonnull
  public String getUserId() {
    return userId;
  }

  public void setUserId(String userId) {
    this.userId = userId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    EMSAllOfCredentials emSAllOfCredentials = (EMSAllOfCredentials) o;
    return Objects.equals(this.clientCertificate, emSAllOfCredentials.clientCertificate) &&
        Objects.equals(this.clientCertificatePassword, emSAllOfCredentials.clientCertificatePassword) &&
        Objects.equals(this.merchantName, emSAllOfCredentials.merchantName) &&
        Objects.equals(this.password, emSAllOfCredentials.password) &&
        Objects.equals(this.privateKey, emSAllOfCredentials.privateKey) &&
        Objects.equals(this.privateKeyPassword, emSAllOfCredentials.privateKeyPassword) &&
        Objects.equals(this.serverCertificate, emSAllOfCredentials.serverCertificate) &&
        Objects.equals(this.sftpPrivateKey, emSAllOfCredentials.sftpPrivateKey) &&
        Objects.equals(this.storeId, emSAllOfCredentials.storeId) &&
        Objects.equals(this.userId, emSAllOfCredentials.userId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(clientCertificate, clientCertificatePassword, merchantName, password, privateKey, privateKeyPassword, serverCertificate, sftpPrivateKey, storeId, userId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class EMSAllOfCredentials {\n");
    sb.append("    clientCertificate: ").append(toIndentedString(clientCertificate)).append("\n");
    sb.append("    clientCertificatePassword: ").append("*").append("\n");
    sb.append("    merchantName: ").append(toIndentedString(merchantName)).append("\n");
    sb.append("    password: ").append("*").append("\n");
    sb.append("    privateKey: ").append("*").append("\n");
    sb.append("    privateKeyPassword: ").append("*").append("\n");
    sb.append("    serverCertificate: ").append(toIndentedString(serverCertificate)).append("\n");
    sb.append("    sftpPrivateKey: ").append("*").append("\n");
    sb.append("    storeId: ").append(toIndentedString(storeId)).append("\n");
    sb.append("    userId: ").append(toIndentedString(userId)).append("\n");
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
    openapiFields.add("clientCertificate");
    openapiFields.add("clientCertificatePassword");
    openapiFields.add("merchantName");
    openapiFields.add("password");
    openapiFields.add("privateKey");
    openapiFields.add("privateKeyPassword");
    openapiFields.add("serverCertificate");
    openapiFields.add("sftpPrivateKey");
    openapiFields.add("storeId");
    openapiFields.add("userId");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("clientCertificate");
    openapiRequiredFields.add("clientCertificatePassword");
    openapiRequiredFields.add("password");
    openapiRequiredFields.add("privateKey");
    openapiRequiredFields.add("privateKeyPassword");
    openapiRequiredFields.add("serverCertificate");
    openapiRequiredFields.add("storeId");
    openapiRequiredFields.add("userId");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to EMSAllOfCredentials
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!EMSAllOfCredentials.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in EMSAllOfCredentials is not found in the empty JSON string", EMSAllOfCredentials.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!EMSAllOfCredentials.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `EMSAllOfCredentials` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : EMSAllOfCredentials.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("clientCertificate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `clientCertificate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("clientCertificate").toString()));
      }
      if (!jsonObj.get("clientCertificatePassword").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `clientCertificatePassword` to be a primitive type in the JSON string but got `%s`", jsonObj.get("clientCertificatePassword").toString()));
      }
      if ((jsonObj.get("merchantName") != null && !jsonObj.get("merchantName").isJsonNull()) && !jsonObj.get("merchantName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `merchantName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("merchantName").toString()));
      }
      if (!jsonObj.get("password").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `password` to be a primitive type in the JSON string but got `%s`", jsonObj.get("password").toString()));
      }
      if (!jsonObj.get("privateKey").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `privateKey` to be a primitive type in the JSON string but got `%s`", jsonObj.get("privateKey").toString()));
      }
      if (!jsonObj.get("privateKeyPassword").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `privateKeyPassword` to be a primitive type in the JSON string but got `%s`", jsonObj.get("privateKeyPassword").toString()));
      }
      if (!jsonObj.get("serverCertificate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `serverCertificate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("serverCertificate").toString()));
      }
      if ((jsonObj.get("sftpPrivateKey") != null && !jsonObj.get("sftpPrivateKey").isJsonNull()) && !jsonObj.get("sftpPrivateKey").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `sftpPrivateKey` to be a primitive type in the JSON string but got `%s`", jsonObj.get("sftpPrivateKey").toString()));
      }
      if (!jsonObj.get("storeId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `storeId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("storeId").toString()));
      }
      if (!jsonObj.get("userId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `userId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("userId").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!EMSAllOfCredentials.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'EMSAllOfCredentials' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<EMSAllOfCredentials> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(EMSAllOfCredentials.class));

       return (TypeAdapter<T>) new TypeAdapter<EMSAllOfCredentials>() {
           @Override
           public void write(JsonWriter out, EMSAllOfCredentials value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public EMSAllOfCredentials read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of EMSAllOfCredentials given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of EMSAllOfCredentials
   * @throws IOException if the JSON string is invalid with respect to EMSAllOfCredentials
   */
  public static EMSAllOfCredentials fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, EMSAllOfCredentials.class);
  }

  /**
   * Convert an instance of EMSAllOfCredentials to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

