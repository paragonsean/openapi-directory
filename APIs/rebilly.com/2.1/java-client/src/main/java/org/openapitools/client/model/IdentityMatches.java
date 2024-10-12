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
 * IdentityMatches
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:20:59.825309-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class IdentityMatches {
  public static final String SERIALIZED_NAME_CONTAINS_IMAGE = "containsImage";
  @SerializedName(SERIALIZED_NAME_CONTAINS_IMAGE)
  private Boolean containsImage;

  public static final String SERIALIZED_NAME_DATE_OF_BIRTH = "dateOfBirth";
  @SerializedName(SERIALIZED_NAME_DATE_OF_BIRTH)
  private OffsetDateTime dateOfBirth;

  public static final String SERIALIZED_NAME_EXPIRY_DATE = "expiryDate";
  @SerializedName(SERIALIZED_NAME_EXPIRY_DATE)
  private OffsetDateTime expiryDate;

  public static final String SERIALIZED_NAME_FIRST_NAME = "firstName";
  @SerializedName(SERIALIZED_NAME_FIRST_NAME)
  private String firstName;

  public static final String SERIALIZED_NAME_HAS_MINIMAL_AGE = "hasMinimalAge";
  @SerializedName(SERIALIZED_NAME_HAS_MINIMAL_AGE)
  private Boolean hasMinimalAge;

  public static final String SERIALIZED_NAME_IS_IDENTITY_DOCUMENT = "isIdentityDocument";
  @SerializedName(SERIALIZED_NAME_IS_IDENTITY_DOCUMENT)
  private Boolean isIdentityDocument;

  public static final String SERIALIZED_NAME_IS_PUBLISHED_ONLINE = "isPublishedOnline";
  @SerializedName(SERIALIZED_NAME_IS_PUBLISHED_ONLINE)
  private Boolean isPublishedOnline;

  public static final String SERIALIZED_NAME_ISSUE_DATE = "issueDate";
  @SerializedName(SERIALIZED_NAME_ISSUE_DATE)
  private OffsetDateTime issueDate;

  public static final String SERIALIZED_NAME_LAST_NAME = "lastName";
  @SerializedName(SERIALIZED_NAME_LAST_NAME)
  private String lastName;

  public static final String SERIALIZED_NAME_NATIONALITY = "nationality";
  @SerializedName(SERIALIZED_NAME_NATIONALITY)
  private String nationality;

  public IdentityMatches() {
  }

  public IdentityMatches(
     Boolean hasMinimalAge
  ) {
    this();
    this.hasMinimalAge = hasMinimalAge;
  }

  public IdentityMatches containsImage(Boolean containsImage) {
    this.containsImage = containsImage;
    return this;
  }

  /**
   * Flag that indicates if there is an image that contains a face on it.
   * @return containsImage
   */
  @javax.annotation.Nullable
  public Boolean getContainsImage() {
    return containsImage;
  }

  public void setContainsImage(Boolean containsImage) {
    this.containsImage = containsImage;
  }


  public IdentityMatches dateOfBirth(OffsetDateTime dateOfBirth) {
    this.dateOfBirth = dateOfBirth;
    return this;
  }

  /**
   * The date of birth found on the document, null if not found.
   * @return dateOfBirth
   */
  @javax.annotation.Nullable
  public OffsetDateTime getDateOfBirth() {
    return dateOfBirth;
  }

  public void setDateOfBirth(OffsetDateTime dateOfBirth) {
    this.dateOfBirth = dateOfBirth;
  }


  public IdentityMatches expiryDate(OffsetDateTime expiryDate) {
    this.expiryDate = expiryDate;
    return this;
  }

  /**
   * The expiry date found on the document, null if not found.
   * @return expiryDate
   */
  @javax.annotation.Nullable
  public OffsetDateTime getExpiryDate() {
    return expiryDate;
  }

  public void setExpiryDate(OffsetDateTime expiryDate) {
    this.expiryDate = expiryDate;
  }


  public IdentityMatches firstName(String firstName) {
    this.firstName = firstName;
    return this;
  }

  /**
   * The customer first name if it was matched, null otherwise.
   * @return firstName
   */
  @javax.annotation.Nullable
  public String getFirstName() {
    return firstName;
  }

  public void setFirstName(String firstName) {
    this.firstName = firstName;
  }


  /**
   * Checks the minimal age, 21+ for USA and 18+ for all other countries. Null if dateOfBirth could not be determined.
   * @return hasMinimalAge
   */
  @javax.annotation.Nullable
  public Boolean getHasMinimalAge() {
    return hasMinimalAge;
  }



  public IdentityMatches isIdentityDocument(Boolean isIdentityDocument) {
    this.isIdentityDocument = isIdentityDocument;
    return this;
  }

  /**
   * Flag that indicates if this looks like and ID.
   * @return isIdentityDocument
   */
  @javax.annotation.Nullable
  public Boolean getIsIdentityDocument() {
    return isIdentityDocument;
  }

  public void setIsIdentityDocument(Boolean isIdentityDocument) {
    this.isIdentityDocument = isIdentityDocument;
  }


  public IdentityMatches isPublishedOnline(Boolean isPublishedOnline) {
    this.isPublishedOnline = isPublishedOnline;
    return this;
  }

  /**
   * If there is an exact match found online.
   * @return isPublishedOnline
   */
  @javax.annotation.Nullable
  public Boolean getIsPublishedOnline() {
    return isPublishedOnline;
  }

  public void setIsPublishedOnline(Boolean isPublishedOnline) {
    this.isPublishedOnline = isPublishedOnline;
  }


  public IdentityMatches issueDate(OffsetDateTime issueDate) {
    this.issueDate = issueDate;
    return this;
  }

  /**
   * The issued date found on the document, null if not found.
   * @return issueDate
   */
  @javax.annotation.Nullable
  public OffsetDateTime getIssueDate() {
    return issueDate;
  }

  public void setIssueDate(OffsetDateTime issueDate) {
    this.issueDate = issueDate;
  }


  public IdentityMatches lastName(String lastName) {
    this.lastName = lastName;
    return this;
  }

  /**
   * The customer last name if it was matched, null otherwise.
   * @return lastName
   */
  @javax.annotation.Nullable
  public String getLastName() {
    return lastName;
  }

  public void setLastName(String lastName) {
    this.lastName = lastName;
  }


  public IdentityMatches nationality(String nationality) {
    this.nationality = nationality;
    return this;
  }

  /**
   * The nationality found on the document, null otherwise.
   * @return nationality
   */
  @javax.annotation.Nullable
  public String getNationality() {
    return nationality;
  }

  public void setNationality(String nationality) {
    this.nationality = nationality;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    IdentityMatches identityMatches = (IdentityMatches) o;
    return Objects.equals(this.containsImage, identityMatches.containsImage) &&
        Objects.equals(this.dateOfBirth, identityMatches.dateOfBirth) &&
        Objects.equals(this.expiryDate, identityMatches.expiryDate) &&
        Objects.equals(this.firstName, identityMatches.firstName) &&
        Objects.equals(this.hasMinimalAge, identityMatches.hasMinimalAge) &&
        Objects.equals(this.isIdentityDocument, identityMatches.isIdentityDocument) &&
        Objects.equals(this.isPublishedOnline, identityMatches.isPublishedOnline) &&
        Objects.equals(this.issueDate, identityMatches.issueDate) &&
        Objects.equals(this.lastName, identityMatches.lastName) &&
        Objects.equals(this.nationality, identityMatches.nationality);
  }

  @Override
  public int hashCode() {
    return Objects.hash(containsImage, dateOfBirth, expiryDate, firstName, hasMinimalAge, isIdentityDocument, isPublishedOnline, issueDate, lastName, nationality);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class IdentityMatches {\n");
    sb.append("    containsImage: ").append(toIndentedString(containsImage)).append("\n");
    sb.append("    dateOfBirth: ").append(toIndentedString(dateOfBirth)).append("\n");
    sb.append("    expiryDate: ").append(toIndentedString(expiryDate)).append("\n");
    sb.append("    firstName: ").append(toIndentedString(firstName)).append("\n");
    sb.append("    hasMinimalAge: ").append(toIndentedString(hasMinimalAge)).append("\n");
    sb.append("    isIdentityDocument: ").append(toIndentedString(isIdentityDocument)).append("\n");
    sb.append("    isPublishedOnline: ").append(toIndentedString(isPublishedOnline)).append("\n");
    sb.append("    issueDate: ").append(toIndentedString(issueDate)).append("\n");
    sb.append("    lastName: ").append(toIndentedString(lastName)).append("\n");
    sb.append("    nationality: ").append(toIndentedString(nationality)).append("\n");
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
    openapiFields.add("containsImage");
    openapiFields.add("dateOfBirth");
    openapiFields.add("expiryDate");
    openapiFields.add("firstName");
    openapiFields.add("hasMinimalAge");
    openapiFields.add("isIdentityDocument");
    openapiFields.add("isPublishedOnline");
    openapiFields.add("issueDate");
    openapiFields.add("lastName");
    openapiFields.add("nationality");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to IdentityMatches
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!IdentityMatches.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in IdentityMatches is not found in the empty JSON string", IdentityMatches.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!IdentityMatches.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `IdentityMatches` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("firstName") != null && !jsonObj.get("firstName").isJsonNull()) && !jsonObj.get("firstName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `firstName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("firstName").toString()));
      }
      if ((jsonObj.get("lastName") != null && !jsonObj.get("lastName").isJsonNull()) && !jsonObj.get("lastName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `lastName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("lastName").toString()));
      }
      if ((jsonObj.get("nationality") != null && !jsonObj.get("nationality").isJsonNull()) && !jsonObj.get("nationality").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `nationality` to be a primitive type in the JSON string but got `%s`", jsonObj.get("nationality").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!IdentityMatches.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'IdentityMatches' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<IdentityMatches> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(IdentityMatches.class));

       return (TypeAdapter<T>) new TypeAdapter<IdentityMatches>() {
           @Override
           public void write(JsonWriter out, IdentityMatches value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public IdentityMatches read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of IdentityMatches given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of IdentityMatches
   * @throws IOException if the JSON string is invalid with respect to IdentityMatches
   */
  public static IdentityMatches fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, IdentityMatches.class);
  }

  /**
   * Convert an instance of IdentityMatches to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

