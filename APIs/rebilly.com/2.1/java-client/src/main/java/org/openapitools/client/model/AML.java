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
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.AMLAddressInner;
import org.openapitools.client.model.AMLAliasesInner;
import org.openapitools.client.model.AMLPassportInner;
import org.openapitools.client.model.SelfLink;
import org.openapitools.jackson.nullable.JsonNullable;

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
 * AML
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:20:59.825309-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AML {
  public static final String SERIALIZED_NAME_LINKS = "_links";
  @SerializedName(SERIALIZED_NAME_LINKS)
  private List<SelfLink> links = new ArrayList<>();

  public static final String SERIALIZED_NAME_ADDRESS = "address";
  @SerializedName(SERIALIZED_NAME_ADDRESS)
  private List<AMLAddressInner> address = new ArrayList<>();

  public static final String SERIALIZED_NAME_ALIASES = "aliases";
  @SerializedName(SERIALIZED_NAME_ALIASES)
  private List<AMLAliasesInner> aliases = new ArrayList<>();

  public static final String SERIALIZED_NAME_COMMENTS = "comments";
  @SerializedName(SERIALIZED_NAME_COMMENTS)
  private String comments;

  /**
   * The source list&#39;s confidence in information.
   */
  @JsonAdapter(ConfidenceEnum.Adapter.class)
  public enum ConfidenceEnum {
    WEAK("weak"),
    
    MEDIUM("medium"),
    
    STRONG("strong"),
    
    VERY_STRONG("very-strong");

    private String value;

    ConfidenceEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static ConfidenceEnum fromValue(String value) {
      for (ConfidenceEnum b : ConfidenceEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<ConfidenceEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final ConfidenceEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public ConfidenceEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return ConfidenceEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      ConfidenceEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_CONFIDENCE = "confidence";
  @SerializedName(SERIALIZED_NAME_CONFIDENCE)
  private ConfidenceEnum confidence;

  public static final String SERIALIZED_NAME_DOB = "dob";
  @SerializedName(SERIALIZED_NAME_DOB)
  private List<LocalDate> dob = new ArrayList<>();

  public static final String SERIALIZED_NAME_FIRST_NAME = "firstName";
  @SerializedName(SERIALIZED_NAME_FIRST_NAME)
  private String firstName;

  public static final String SERIALIZED_NAME_GENDER = "gender";
  @SerializedName(SERIALIZED_NAME_GENDER)
  private String gender;

  public static final String SERIALIZED_NAME_LAST_NAME = "lastName";
  @SerializedName(SERIALIZED_NAME_LAST_NAME)
  private String lastName;

  public static final String SERIALIZED_NAME_LEGAL_BASIS = "legalBasis";
  @SerializedName(SERIALIZED_NAME_LEGAL_BASIS)
  private List<String> legalBasis = new ArrayList<>();

  public static final String SERIALIZED_NAME_NATIONALITY = "nationality";
  @SerializedName(SERIALIZED_NAME_NATIONALITY)
  private String nationality;

  public static final String SERIALIZED_NAME_PASSPORT = "passport";
  @SerializedName(SERIALIZED_NAME_PASSPORT)
  private List<AMLPassportInner> passport = new ArrayList<>();

  public static final String SERIALIZED_NAME_REGIME = "regime";
  @SerializedName(SERIALIZED_NAME_REGIME)
  private String regime;

  public static final String SERIALIZED_NAME_SOURCE = "source";
  @SerializedName(SERIALIZED_NAME_SOURCE)
  private String source;

  /**
   * The list type.
   */
  @JsonAdapter(SourceTypeEnum.Adapter.class)
  public enum SourceTypeEnum {
    PEP("pep"),
    
    SANCTIONS("sanctions"),
    
    ADVERSE_MEDIA("adverse-media");

    private String value;

    SourceTypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static SourceTypeEnum fromValue(String value) {
      for (SourceTypeEnum b : SourceTypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<SourceTypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final SourceTypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public SourceTypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return SourceTypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      SourceTypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_SOURCE_TYPE = "sourceType";
  @SerializedName(SERIALIZED_NAME_SOURCE_TYPE)
  private SourceTypeEnum sourceType;

  public static final String SERIALIZED_NAME_TITLE = "title";
  @SerializedName(SERIALIZED_NAME_TITLE)
  private List<String> title;

  /**
   * The record type.
   */
  @JsonAdapter(TypeEnum.Adapter.class)
  public enum TypeEnum {
    INDIVIDUAL("individual"),
    
    ENTITY("entity");

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

  public AML() {
  }

  public AML(
     List<SelfLink> links, 
     List<AMLAddressInner> address, 
     List<AMLAliasesInner> aliases, 
     String comments, 
     ConfidenceEnum confidence, 
     List<LocalDate> dob, 
     String firstName, 
     String gender, 
     String lastName, 
     List<String> legalBasis, 
     String nationality, 
     List<AMLPassportInner> passport, 
     String regime, 
     String source, 
     SourceTypeEnum sourceType, 
     List<String> title, 
     TypeEnum type
  ) {
    this();
    this.links = links;
    this.address = address;
    this.aliases = aliases;
    this.comments = comments;
    this.confidence = confidence;
    this.dob = dob;
    this.firstName = firstName;
    this.gender = gender;
    this.lastName = lastName;
    this.legalBasis = legalBasis;
    this.nationality = nationality;
    this.passport = passport;
    this.regime = regime;
    this.source = source;
    this.sourceType = sourceType;
    this.title = title;
    this.type = type;
  }

  /**
   * The links related to resource, including links provided by the list.
   * @return links
   */
  @javax.annotation.Nullable
  public List<SelfLink> getLinks() {
    return links;
  }



  /**
   * Addresses related to the identity.
   * @return address
   */
  @javax.annotation.Nullable
  public List<AMLAddressInner> getAddress() {
    return address;
  }



  /**
   * List of aliases, if any.
   * @return aliases
   */
  @javax.annotation.Nullable
  public List<AMLAliasesInner> getAliases() {
    return aliases;
  }



  /**
   * Extra information (the content varies per list).
   * @return comments
   */
  @javax.annotation.Nullable
  public String getComments() {
    return comments;
  }



  /**
   * The source list&#39;s confidence in information.
   * @return confidence
   */
  @javax.annotation.Nullable
  public ConfidenceEnum getConfidence() {
    return confidence;
  }



  /**
   * One or more possible dates of birth.
   * @return dob
   */
  @javax.annotation.Nullable
  public List<LocalDate> getDob() {
    return dob;
  }



  /**
   * First Name.
   * @return firstName
   */
  @javax.annotation.Nullable
  public String getFirstName() {
    return firstName;
  }



  /**
   * Gender of returned identity (if &#x60;type&#x60; is &#x60;individual&#x60;).
   * @return gender
   */
  @javax.annotation.Nullable
  public String getGender() {
    return gender;
  }



  /**
   * Last Name. &#x60;null&#x60; if it is a single-name entity.
   * @return lastName
   */
  @javax.annotation.Nullable
  public String getLastName() {
    return lastName;
  }



  /**
   * List of references to legal documents if they exist.
   * @return legalBasis
   */
  @javax.annotation.Nullable
  public List<String> getLegalBasis() {
    return legalBasis;
  }



  /**
   * The nationality of the identity.
   * @return nationality
   */
  @javax.annotation.Nullable
  public String getNationality() {
    return nationality;
  }



  /**
   * Passport information.
   * @return passport
   */
  @javax.annotation.Nullable
  public List<AMLPassportInner> getPassport() {
    return passport;
  }



  /**
   * Regime.
   * @return regime
   */
  @javax.annotation.Nullable
  public String getRegime() {
    return regime;
  }



  /**
   * Which list this came from.
   * @return source
   */
  @javax.annotation.Nullable
  public String getSource() {
    return source;
  }



  /**
   * The list type.
   * @return sourceType
   */
  @javax.annotation.Nullable
  public SourceTypeEnum getSourceType() {
    return sourceType;
  }



  /**
   * The title of their position.
   * @return title
   */
  @javax.annotation.Nullable
  public List<String> getTitle() {
    return title;
  }



  /**
   * The record type.
   * @return type
   */
  @javax.annotation.Nullable
  public TypeEnum getType() {
    return type;
  }




  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AML AML = (AML) o;
    return Objects.equals(this.links, AML.links) &&
        Objects.equals(this.address, AML.address) &&
        Objects.equals(this.aliases, AML.aliases) &&
        Objects.equals(this.comments, AML.comments) &&
        Objects.equals(this.confidence, AML.confidence) &&
        Objects.equals(this.dob, AML.dob) &&
        Objects.equals(this.firstName, AML.firstName) &&
        Objects.equals(this.gender, AML.gender) &&
        Objects.equals(this.lastName, AML.lastName) &&
        Objects.equals(this.legalBasis, AML.legalBasis) &&
        Objects.equals(this.nationality, AML.nationality) &&
        Objects.equals(this.passport, AML.passport) &&
        Objects.equals(this.regime, AML.regime) &&
        Objects.equals(this.source, AML.source) &&
        Objects.equals(this.sourceType, AML.sourceType) &&
        Objects.equals(this.title, AML.title) &&
        Objects.equals(this.type, AML.type);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(links, address, aliases, comments, confidence, dob, firstName, gender, lastName, legalBasis, nationality, passport, regime, source, sourceType, title, type);
  }

  private static <T> int hashCodeNullable(JsonNullable<T> a) {
    if (a == null) {
      return 1;
    }
    return a.isPresent() ? Arrays.deepHashCode(new Object[]{a.get()}) : 31;
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AML {\n");
    sb.append("    links: ").append(toIndentedString(links)).append("\n");
    sb.append("    address: ").append(toIndentedString(address)).append("\n");
    sb.append("    aliases: ").append(toIndentedString(aliases)).append("\n");
    sb.append("    comments: ").append(toIndentedString(comments)).append("\n");
    sb.append("    confidence: ").append(toIndentedString(confidence)).append("\n");
    sb.append("    dob: ").append(toIndentedString(dob)).append("\n");
    sb.append("    firstName: ").append(toIndentedString(firstName)).append("\n");
    sb.append("    gender: ").append(toIndentedString(gender)).append("\n");
    sb.append("    lastName: ").append(toIndentedString(lastName)).append("\n");
    sb.append("    legalBasis: ").append(toIndentedString(legalBasis)).append("\n");
    sb.append("    nationality: ").append(toIndentedString(nationality)).append("\n");
    sb.append("    passport: ").append(toIndentedString(passport)).append("\n");
    sb.append("    regime: ").append(toIndentedString(regime)).append("\n");
    sb.append("    source: ").append(toIndentedString(source)).append("\n");
    sb.append("    sourceType: ").append(toIndentedString(sourceType)).append("\n");
    sb.append("    title: ").append(toIndentedString(title)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
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
    openapiFields.add("aliases");
    openapiFields.add("comments");
    openapiFields.add("confidence");
    openapiFields.add("dob");
    openapiFields.add("firstName");
    openapiFields.add("gender");
    openapiFields.add("lastName");
    openapiFields.add("legalBasis");
    openapiFields.add("nationality");
    openapiFields.add("passport");
    openapiFields.add("regime");
    openapiFields.add("source");
    openapiFields.add("sourceType");
    openapiFields.add("title");
    openapiFields.add("type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AML
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AML.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AML is not found in the empty JSON string", AML.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AML.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AML` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
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
      if (jsonObj.get("address") != null && !jsonObj.get("address").isJsonNull()) {
        JsonArray jsonArrayaddress = jsonObj.getAsJsonArray("address");
        if (jsonArrayaddress != null) {
          // ensure the json data is an array
          if (!jsonObj.get("address").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `address` to be an array in the JSON string but got `%s`", jsonObj.get("address").toString()));
          }

          // validate the optional field `address` (array)
          for (int i = 0; i < jsonArrayaddress.size(); i++) {
            AMLAddressInner.validateJsonElement(jsonArrayaddress.get(i));
          };
        }
      }
      if (jsonObj.get("aliases") != null && !jsonObj.get("aliases").isJsonNull()) {
        JsonArray jsonArrayaliases = jsonObj.getAsJsonArray("aliases");
        if (jsonArrayaliases != null) {
          // ensure the json data is an array
          if (!jsonObj.get("aliases").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `aliases` to be an array in the JSON string but got `%s`", jsonObj.get("aliases").toString()));
          }

          // validate the optional field `aliases` (array)
          for (int i = 0; i < jsonArrayaliases.size(); i++) {
            AMLAliasesInner.validateJsonElement(jsonArrayaliases.get(i));
          };
        }
      }
      if ((jsonObj.get("comments") != null && !jsonObj.get("comments").isJsonNull()) && !jsonObj.get("comments").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `comments` to be a primitive type in the JSON string but got `%s`", jsonObj.get("comments").toString()));
      }
      if ((jsonObj.get("confidence") != null && !jsonObj.get("confidence").isJsonNull()) && !jsonObj.get("confidence").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `confidence` to be a primitive type in the JSON string but got `%s`", jsonObj.get("confidence").toString()));
      }
      // validate the optional field `confidence`
      if (jsonObj.get("confidence") != null && !jsonObj.get("confidence").isJsonNull()) {
        ConfidenceEnum.validateJsonElement(jsonObj.get("confidence"));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("dob") != null && !jsonObj.get("dob").isJsonNull() && !jsonObj.get("dob").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `dob` to be an array in the JSON string but got `%s`", jsonObj.get("dob").toString()));
      }
      if ((jsonObj.get("firstName") != null && !jsonObj.get("firstName").isJsonNull()) && !jsonObj.get("firstName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `firstName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("firstName").toString()));
      }
      if ((jsonObj.get("gender") != null && !jsonObj.get("gender").isJsonNull()) && !jsonObj.get("gender").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `gender` to be a primitive type in the JSON string but got `%s`", jsonObj.get("gender").toString()));
      }
      if ((jsonObj.get("lastName") != null && !jsonObj.get("lastName").isJsonNull()) && !jsonObj.get("lastName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `lastName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("lastName").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("legalBasis") != null && !jsonObj.get("legalBasis").isJsonNull() && !jsonObj.get("legalBasis").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `legalBasis` to be an array in the JSON string but got `%s`", jsonObj.get("legalBasis").toString()));
      }
      if ((jsonObj.get("nationality") != null && !jsonObj.get("nationality").isJsonNull()) && !jsonObj.get("nationality").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `nationality` to be a primitive type in the JSON string but got `%s`", jsonObj.get("nationality").toString()));
      }
      if (jsonObj.get("passport") != null && !jsonObj.get("passport").isJsonNull()) {
        JsonArray jsonArraypassport = jsonObj.getAsJsonArray("passport");
        if (jsonArraypassport != null) {
          // ensure the json data is an array
          if (!jsonObj.get("passport").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `passport` to be an array in the JSON string but got `%s`", jsonObj.get("passport").toString()));
          }

          // validate the optional field `passport` (array)
          for (int i = 0; i < jsonArraypassport.size(); i++) {
            AMLPassportInner.validateJsonElement(jsonArraypassport.get(i));
          };
        }
      }
      if ((jsonObj.get("regime") != null && !jsonObj.get("regime").isJsonNull()) && !jsonObj.get("regime").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `regime` to be a primitive type in the JSON string but got `%s`", jsonObj.get("regime").toString()));
      }
      if ((jsonObj.get("source") != null && !jsonObj.get("source").isJsonNull()) && !jsonObj.get("source").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `source` to be a primitive type in the JSON string but got `%s`", jsonObj.get("source").toString()));
      }
      if ((jsonObj.get("sourceType") != null && !jsonObj.get("sourceType").isJsonNull()) && !jsonObj.get("sourceType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `sourceType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("sourceType").toString()));
      }
      // validate the optional field `sourceType`
      if (jsonObj.get("sourceType") != null && !jsonObj.get("sourceType").isJsonNull()) {
        SourceTypeEnum.validateJsonElement(jsonObj.get("sourceType"));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("title") != null && !jsonObj.get("title").isJsonNull() && !jsonObj.get("title").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `title` to be an array in the JSON string but got `%s`", jsonObj.get("title").toString()));
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
       if (!AML.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AML' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AML> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AML.class));

       return (TypeAdapter<T>) new TypeAdapter<AML>() {
           @Override
           public void write(JsonWriter out, AML value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AML read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AML given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AML
   * @throws IOException if the JSON string is invalid with respect to AML
   */
  public static AML fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AML.class);
  }

  /**
   * Convert an instance of AML to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

