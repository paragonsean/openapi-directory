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
import org.openapitools.client.model.ContactEmailsInner;
import org.openapitools.client.model.ContactPhoneNumbersInner;
import org.openapitools.client.model.OrganizationQuestionnaire;
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
 * Organization
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:20:59.825309-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Organization {
  public static final String SERIALIZED_NAME_LINKS = "_links";
  @SerializedName(SERIALIZED_NAME_LINKS)
  private List<SelfLink> links = new ArrayList<>();

  public static final String SERIALIZED_NAME_ADDRESS = "address";
  @SerializedName(SERIALIZED_NAME_ADDRESS)
  private String address;

  public static final String SERIALIZED_NAME_ADDRESS2 = "address2";
  @SerializedName(SERIALIZED_NAME_ADDRESS2)
  private String address2;

  public static final String SERIALIZED_NAME_CITY = "city";
  @SerializedName(SERIALIZED_NAME_CITY)
  private String city;

  public static final String SERIALIZED_NAME_COUNTRY = "country";
  @SerializedName(SERIALIZED_NAME_COUNTRY)
  private String country;

  public static final String SERIALIZED_NAME_CREATED_TIME = "createdTime";
  @SerializedName(SERIALIZED_NAME_CREATED_TIME)
  private OffsetDateTime createdTime;

  public static final String SERIALIZED_NAME_EMAILS = "emails";
  @SerializedName(SERIALIZED_NAME_EMAILS)
  private List<ContactEmailsInner> emails = new ArrayList<>();

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_INVOICE_TIME_ZONE = "invoiceTimeZone";
  @SerializedName(SERIALIZED_NAME_INVOICE_TIME_ZONE)
  private String invoiceTimeZone;

  public static final String SERIALIZED_NAME_IS_PRIMARY = "isPrimary";
  @SerializedName(SERIALIZED_NAME_IS_PRIMARY)
  private Boolean isPrimary;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_PHONE_NUMBERS = "phoneNumbers";
  @SerializedName(SERIALIZED_NAME_PHONE_NUMBERS)
  private List<ContactPhoneNumbersInner> phoneNumbers = new ArrayList<>();

  public static final String SERIALIZED_NAME_POSTAL_CODE = "postalCode";
  @SerializedName(SERIALIZED_NAME_POSTAL_CODE)
  private String postalCode;

  public static final String SERIALIZED_NAME_QUESTIONNAIRE = "questionnaire";
  @SerializedName(SERIALIZED_NAME_QUESTIONNAIRE)
  private OrganizationQuestionnaire questionnaire;

  public static final String SERIALIZED_NAME_REGION = "region";
  @SerializedName(SERIALIZED_NAME_REGION)
  private String region;

  public static final String SERIALIZED_NAME_TAX_DESCRIPTOR = "taxDescriptor";
  @SerializedName(SERIALIZED_NAME_TAX_DESCRIPTOR)
  private String taxDescriptor;

  public static final String SERIALIZED_NAME_UPDATED_TIME = "updatedTime";
  @SerializedName(SERIALIZED_NAME_UPDATED_TIME)
  private OffsetDateTime updatedTime;

  public Organization() {
  }

  public Organization(
     List<SelfLink> links, 
     OffsetDateTime createdTime, 
     String id, 
     OffsetDateTime updatedTime
  ) {
    this();
    this.links = links;
    this.createdTime = createdTime;
    this.id = id;
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



  public Organization address(String address) {
    this.address = address;
    return this;
  }

  /**
   * The organization street address.
   * @return address
   */
  @javax.annotation.Nullable
  public String getAddress() {
    return address;
  }

  public void setAddress(String address) {
    this.address = address;
  }


  public Organization address2(String address2) {
    this.address2 = address2;
    return this;
  }

  /**
   * The organization street address.
   * @return address2
   */
  @javax.annotation.Nullable
  public String getAddress2() {
    return address2;
  }

  public void setAddress2(String address2) {
    this.address2 = address2;
  }


  public Organization city(String city) {
    this.city = city;
    return this;
  }

  /**
   * The organization city.
   * @return city
   */
  @javax.annotation.Nullable
  public String getCity() {
    return city;
  }

  public void setCity(String city) {
    this.city = city;
  }


  public Organization country(String country) {
    this.country = country;
    return this;
  }

  /**
   * The organization country ISO Alpha-2 code.
   * @return country
   */
  @javax.annotation.Nonnull
  public String getCountry() {
    return country;
  }

  public void setCountry(String country) {
    this.country = country;
  }


  /**
   * The organization created time.
   * @return createdTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getCreatedTime() {
    return createdTime;
  }



  public Organization emails(List<ContactEmailsInner> emails) {
    this.emails = emails;
    return this;
  }

  public Organization addEmailsItem(ContactEmailsInner emailsItem) {
    if (this.emails == null) {
      this.emails = new ArrayList<>();
    }
    this.emails.add(emailsItem);
    return this;
  }

  /**
   * The list of emails.
   * @return emails
   */
  @javax.annotation.Nullable
  public List<ContactEmailsInner> getEmails() {
    return emails;
  }

  public void setEmails(List<ContactEmailsInner> emails) {
    this.emails = emails;
  }


  /**
   * The organization identifier string.
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }



  public Organization invoiceTimeZone(String invoiceTimeZone) {
    this.invoiceTimeZone = invoiceTimeZone;
    return this;
  }

  /**
   * Invoice will use this time zone to display time otherwise UTC will be used. Example \&quot;America/New_York\&quot;.
   * @return invoiceTimeZone
   */
  @javax.annotation.Nullable
  public String getInvoiceTimeZone() {
    return invoiceTimeZone;
  }

  public void setInvoiceTimeZone(String invoiceTimeZone) {
    this.invoiceTimeZone = invoiceTimeZone;
  }


  public Organization isPrimary(Boolean isPrimary) {
    this.isPrimary = isPrimary;
    return this;
  }

  /**
   * True, if Organization is primary (available to set as true only, other organizations will become as isPrimary&#x3D;false).
   * @return isPrimary
   */
  @javax.annotation.Nullable
  public Boolean getIsPrimary() {
    return isPrimary;
  }

  public void setIsPrimary(Boolean isPrimary) {
    this.isPrimary = isPrimary;
  }


  public Organization name(String name) {
    this.name = name;
    return this;
  }

  /**
   * The organization name.
   * @return name
   */
  @javax.annotation.Nonnull
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public Organization phoneNumbers(List<ContactPhoneNumbersInner> phoneNumbers) {
    this.phoneNumbers = phoneNumbers;
    return this;
  }

  public Organization addPhoneNumbersItem(ContactPhoneNumbersInner phoneNumbersItem) {
    if (this.phoneNumbers == null) {
      this.phoneNumbers = new ArrayList<>();
    }
    this.phoneNumbers.add(phoneNumbersItem);
    return this;
  }

  /**
   * The list of phone numbers.
   * @return phoneNumbers
   */
  @javax.annotation.Nullable
  public List<ContactPhoneNumbersInner> getPhoneNumbers() {
    return phoneNumbers;
  }

  public void setPhoneNumbers(List<ContactPhoneNumbersInner> phoneNumbers) {
    this.phoneNumbers = phoneNumbers;
  }


  public Organization postalCode(String postalCode) {
    this.postalCode = postalCode;
    return this;
  }

  /**
   * The organization postal code.
   * @return postalCode
   */
  @javax.annotation.Nullable
  public String getPostalCode() {
    return postalCode;
  }

  public void setPostalCode(String postalCode) {
    this.postalCode = postalCode;
  }


  public Organization questionnaire(OrganizationQuestionnaire questionnaire) {
    this.questionnaire = questionnaire;
    return this;
  }

  /**
   * Get questionnaire
   * @return questionnaire
   */
  @javax.annotation.Nullable
  public OrganizationQuestionnaire getQuestionnaire() {
    return questionnaire;
  }

  public void setQuestionnaire(OrganizationQuestionnaire questionnaire) {
    this.questionnaire = questionnaire;
  }


  public Organization region(String region) {
    this.region = region;
    return this;
  }

  /**
   * The organization region (state).
   * @return region
   */
  @javax.annotation.Nullable
  public String getRegion() {
    return region;
  }

  public void setRegion(String region) {
    this.region = region;
  }


  public Organization taxDescriptor(String taxDescriptor) {
    this.taxDescriptor = taxDescriptor;
    return this;
  }

  /**
   * The organization&#39;s tax label. This will be displayed on the invoice.
   * @return taxDescriptor
   */
  @javax.annotation.Nullable
  public String getTaxDescriptor() {
    return taxDescriptor;
  }

  public void setTaxDescriptor(String taxDescriptor) {
    this.taxDescriptor = taxDescriptor;
  }


  /**
   * The organization updated time.
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
    Organization organization = (Organization) o;
    return Objects.equals(this.links, organization.links) &&
        Objects.equals(this.address, organization.address) &&
        Objects.equals(this.address2, organization.address2) &&
        Objects.equals(this.city, organization.city) &&
        Objects.equals(this.country, organization.country) &&
        Objects.equals(this.createdTime, organization.createdTime) &&
        Objects.equals(this.emails, organization.emails) &&
        Objects.equals(this.id, organization.id) &&
        Objects.equals(this.invoiceTimeZone, organization.invoiceTimeZone) &&
        Objects.equals(this.isPrimary, organization.isPrimary) &&
        Objects.equals(this.name, organization.name) &&
        Objects.equals(this.phoneNumbers, organization.phoneNumbers) &&
        Objects.equals(this.postalCode, organization.postalCode) &&
        Objects.equals(this.questionnaire, organization.questionnaire) &&
        Objects.equals(this.region, organization.region) &&
        Objects.equals(this.taxDescriptor, organization.taxDescriptor) &&
        Objects.equals(this.updatedTime, organization.updatedTime);
  }

  @Override
  public int hashCode() {
    return Objects.hash(links, address, address2, city, country, createdTime, emails, id, invoiceTimeZone, isPrimary, name, phoneNumbers, postalCode, questionnaire, region, taxDescriptor, updatedTime);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Organization {\n");
    sb.append("    links: ").append(toIndentedString(links)).append("\n");
    sb.append("    address: ").append(toIndentedString(address)).append("\n");
    sb.append("    address2: ").append(toIndentedString(address2)).append("\n");
    sb.append("    city: ").append(toIndentedString(city)).append("\n");
    sb.append("    country: ").append(toIndentedString(country)).append("\n");
    sb.append("    createdTime: ").append(toIndentedString(createdTime)).append("\n");
    sb.append("    emails: ").append(toIndentedString(emails)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    invoiceTimeZone: ").append(toIndentedString(invoiceTimeZone)).append("\n");
    sb.append("    isPrimary: ").append(toIndentedString(isPrimary)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    phoneNumbers: ").append(toIndentedString(phoneNumbers)).append("\n");
    sb.append("    postalCode: ").append(toIndentedString(postalCode)).append("\n");
    sb.append("    questionnaire: ").append(toIndentedString(questionnaire)).append("\n");
    sb.append("    region: ").append(toIndentedString(region)).append("\n");
    sb.append("    taxDescriptor: ").append(toIndentedString(taxDescriptor)).append("\n");
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
    openapiFields.add("address");
    openapiFields.add("address2");
    openapiFields.add("city");
    openapiFields.add("country");
    openapiFields.add("createdTime");
    openapiFields.add("emails");
    openapiFields.add("id");
    openapiFields.add("invoiceTimeZone");
    openapiFields.add("isPrimary");
    openapiFields.add("name");
    openapiFields.add("phoneNumbers");
    openapiFields.add("postalCode");
    openapiFields.add("questionnaire");
    openapiFields.add("region");
    openapiFields.add("taxDescriptor");
    openapiFields.add("updatedTime");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("country");
    openapiRequiredFields.add("name");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Organization
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Organization.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Organization is not found in the empty JSON string", Organization.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Organization.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Organization` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : Organization.openapiRequiredFields) {
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
      if ((jsonObj.get("address") != null && !jsonObj.get("address").isJsonNull()) && !jsonObj.get("address").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `address` to be a primitive type in the JSON string but got `%s`", jsonObj.get("address").toString()));
      }
      if ((jsonObj.get("address2") != null && !jsonObj.get("address2").isJsonNull()) && !jsonObj.get("address2").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `address2` to be a primitive type in the JSON string but got `%s`", jsonObj.get("address2").toString()));
      }
      if ((jsonObj.get("city") != null && !jsonObj.get("city").isJsonNull()) && !jsonObj.get("city").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `city` to be a primitive type in the JSON string but got `%s`", jsonObj.get("city").toString()));
      }
      if (!jsonObj.get("country").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `country` to be a primitive type in the JSON string but got `%s`", jsonObj.get("country").toString()));
      }
      if (jsonObj.get("emails") != null && !jsonObj.get("emails").isJsonNull()) {
        JsonArray jsonArrayemails = jsonObj.getAsJsonArray("emails");
        if (jsonArrayemails != null) {
          // ensure the json data is an array
          if (!jsonObj.get("emails").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `emails` to be an array in the JSON string but got `%s`", jsonObj.get("emails").toString()));
          }

          // validate the optional field `emails` (array)
          for (int i = 0; i < jsonArrayemails.size(); i++) {
            ContactEmailsInner.validateJsonElement(jsonArrayemails.get(i));
          };
        }
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("invoiceTimeZone") != null && !jsonObj.get("invoiceTimeZone").isJsonNull()) && !jsonObj.get("invoiceTimeZone").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `invoiceTimeZone` to be a primitive type in the JSON string but got `%s`", jsonObj.get("invoiceTimeZone").toString()));
      }
      if (!jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if (jsonObj.get("phoneNumbers") != null && !jsonObj.get("phoneNumbers").isJsonNull()) {
        JsonArray jsonArrayphoneNumbers = jsonObj.getAsJsonArray("phoneNumbers");
        if (jsonArrayphoneNumbers != null) {
          // ensure the json data is an array
          if (!jsonObj.get("phoneNumbers").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `phoneNumbers` to be an array in the JSON string but got `%s`", jsonObj.get("phoneNumbers").toString()));
          }

          // validate the optional field `phoneNumbers` (array)
          for (int i = 0; i < jsonArrayphoneNumbers.size(); i++) {
            ContactPhoneNumbersInner.validateJsonElement(jsonArrayphoneNumbers.get(i));
          };
        }
      }
      if ((jsonObj.get("postalCode") != null && !jsonObj.get("postalCode").isJsonNull()) && !jsonObj.get("postalCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `postalCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("postalCode").toString()));
      }
      // validate the optional field `questionnaire`
      if (jsonObj.get("questionnaire") != null && !jsonObj.get("questionnaire").isJsonNull()) {
        OrganizationQuestionnaire.validateJsonElement(jsonObj.get("questionnaire"));
      }
      if ((jsonObj.get("region") != null && !jsonObj.get("region").isJsonNull()) && !jsonObj.get("region").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `region` to be a primitive type in the JSON string but got `%s`", jsonObj.get("region").toString()));
      }
      if ((jsonObj.get("taxDescriptor") != null && !jsonObj.get("taxDescriptor").isJsonNull()) && !jsonObj.get("taxDescriptor").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `taxDescriptor` to be a primitive type in the JSON string but got `%s`", jsonObj.get("taxDescriptor").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Organization.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Organization' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Organization> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Organization.class));

       return (TypeAdapter<T>) new TypeAdapter<Organization>() {
           @Override
           public void write(JsonWriter out, Organization value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Organization read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Organization given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Organization
   * @throws IOException if the JSON string is invalid with respect to Organization
   */
  public static Organization fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Organization.class);
  }

  /**
   * Convert an instance of Organization to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

