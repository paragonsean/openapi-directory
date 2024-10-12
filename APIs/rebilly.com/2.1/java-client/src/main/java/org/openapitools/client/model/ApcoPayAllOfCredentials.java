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
 * ApcoPay credentials object.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:20:59.825309-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ApcoPayAllOfCredentials {
  public static final String SERIALIZED_NAME_MERCHANT_I_D = "MerchantID";
  @SerializedName(SERIALIZED_NAME_MERCHANT_I_D)
  private String merchantID;

  public static final String SERIALIZED_NAME_MERCHANT_PASSWORD = "MerchantPassword";
  @SerializedName(SERIALIZED_NAME_MERCHANT_PASSWORD)
  private String merchantPassword;

  public static final String SERIALIZED_NAME_PROFILE_I_D = "profileID";
  @SerializedName(SERIALIZED_NAME_PROFILE_I_D)
  private String profileID;

  public static final String SERIALIZED_NAME_SECRET_WORD = "secretWord";
  @SerializedName(SERIALIZED_NAME_SECRET_WORD)
  private String secretWord;

  public ApcoPayAllOfCredentials() {
  }

  public ApcoPayAllOfCredentials merchantID(String merchantID) {
    this.merchantID = merchantID;
    return this;
  }

  /**
   * ApcoPay merchant ID.
   * @return merchantID
   */
  @javax.annotation.Nonnull
  public String getMerchantID() {
    return merchantID;
  }

  public void setMerchantID(String merchantID) {
    this.merchantID = merchantID;
  }


  public ApcoPayAllOfCredentials merchantPassword(String merchantPassword) {
    this.merchantPassword = merchantPassword;
    return this;
  }

  /**
   * ApcoPay merchant password.
   * @return merchantPassword
   */
  @javax.annotation.Nonnull
  public String getMerchantPassword() {
    return merchantPassword;
  }

  public void setMerchantPassword(String merchantPassword) {
    this.merchantPassword = merchantPassword;
  }


  public ApcoPayAllOfCredentials profileID(String profileID) {
    this.profileID = profileID;
    return this;
  }

  /**
   * ApcoPay profile ID.
   * @return profileID
   */
  @javax.annotation.Nonnull
  public String getProfileID() {
    return profileID;
  }

  public void setProfileID(String profileID) {
    this.profileID = profileID;
  }


  public ApcoPayAllOfCredentials secretWord(String secretWord) {
    this.secretWord = secretWord;
    return this;
  }

  /**
   * ApcoPay secret word.
   * @return secretWord
   */
  @javax.annotation.Nonnull
  public String getSecretWord() {
    return secretWord;
  }

  public void setSecretWord(String secretWord) {
    this.secretWord = secretWord;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ApcoPayAllOfCredentials apcoPayAllOfCredentials = (ApcoPayAllOfCredentials) o;
    return Objects.equals(this.merchantID, apcoPayAllOfCredentials.merchantID) &&
        Objects.equals(this.merchantPassword, apcoPayAllOfCredentials.merchantPassword) &&
        Objects.equals(this.profileID, apcoPayAllOfCredentials.profileID) &&
        Objects.equals(this.secretWord, apcoPayAllOfCredentials.secretWord);
  }

  @Override
  public int hashCode() {
    return Objects.hash(merchantID, merchantPassword, profileID, secretWord);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ApcoPayAllOfCredentials {\n");
    sb.append("    merchantID: ").append(toIndentedString(merchantID)).append("\n");
    sb.append("    merchantPassword: ").append("*").append("\n");
    sb.append("    profileID: ").append(toIndentedString(profileID)).append("\n");
    sb.append("    secretWord: ").append("*").append("\n");
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
    openapiFields.add("MerchantID");
    openapiFields.add("MerchantPassword");
    openapiFields.add("profileID");
    openapiFields.add("secretWord");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("MerchantID");
    openapiRequiredFields.add("MerchantPassword");
    openapiRequiredFields.add("profileID");
    openapiRequiredFields.add("secretWord");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ApcoPayAllOfCredentials
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ApcoPayAllOfCredentials.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ApcoPayAllOfCredentials is not found in the empty JSON string", ApcoPayAllOfCredentials.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ApcoPayAllOfCredentials.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ApcoPayAllOfCredentials` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : ApcoPayAllOfCredentials.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("MerchantID").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `MerchantID` to be a primitive type in the JSON string but got `%s`", jsonObj.get("MerchantID").toString()));
      }
      if (!jsonObj.get("MerchantPassword").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `MerchantPassword` to be a primitive type in the JSON string but got `%s`", jsonObj.get("MerchantPassword").toString()));
      }
      if (!jsonObj.get("profileID").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `profileID` to be a primitive type in the JSON string but got `%s`", jsonObj.get("profileID").toString()));
      }
      if (!jsonObj.get("secretWord").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `secretWord` to be a primitive type in the JSON string but got `%s`", jsonObj.get("secretWord").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ApcoPayAllOfCredentials.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ApcoPayAllOfCredentials' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ApcoPayAllOfCredentials> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ApcoPayAllOfCredentials.class));

       return (TypeAdapter<T>) new TypeAdapter<ApcoPayAllOfCredentials>() {
           @Override
           public void write(JsonWriter out, ApcoPayAllOfCredentials value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ApcoPayAllOfCredentials read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ApcoPayAllOfCredentials given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ApcoPayAllOfCredentials
   * @throws IOException if the JSON string is invalid with respect to ApcoPayAllOfCredentials
   */
  public static ApcoPayAllOfCredentials fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ApcoPayAllOfCredentials.class);
  }

  /**
   * Convert an instance of ApcoPayAllOfCredentials to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

