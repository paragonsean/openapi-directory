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
import org.openapitools.client.model.KycDocumentRejection;
import org.openapitools.client.model.KycDocumentSubtypes;
import org.openapitools.client.model.KycDocumentTypes;
import org.openapitools.client.model.ProofOfAddressAllOfDocumentMatches;
import org.openapitools.client.model.ProofOfAddressAllOfLinks;
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
 * ProofOfAddress
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:20:59.825309-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ProofOfAddress {
  public static final String SERIALIZED_NAME_LINKS = "_links";
  @SerializedName(SERIALIZED_NAME_LINKS)
  private List<ProofOfAddressAllOfLinks> links = new ArrayList<>();

  public static final String SERIALIZED_NAME_CREATED_TIME = "createdTime";
  @SerializedName(SERIALIZED_NAME_CREATED_TIME)
  private OffsetDateTime createdTime;

  public static final String SERIALIZED_NAME_DOCUMENT_SUBTYPE = "documentSubtype";
  @SerializedName(SERIALIZED_NAME_DOCUMENT_SUBTYPE)
  private KycDocumentSubtypes documentSubtype;

  public static final String SERIALIZED_NAME_DOCUMENT_TYPE = "documentType";
  @SerializedName(SERIALIZED_NAME_DOCUMENT_TYPE)
  private KycDocumentTypes documentType;

  public static final String SERIALIZED_NAME_FILE_ID = "fileId";
  @Deprecated
  @SerializedName(SERIALIZED_NAME_FILE_ID)
  private String fileId;

  public static final String SERIALIZED_NAME_FILE_IDS = "fileIds";
  @SerializedName(SERIALIZED_NAME_FILE_IDS)
  private List<String> fileIds = new ArrayList<>();

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_PROCESSED_TIME = "processedTime";
  @SerializedName(SERIALIZED_NAME_PROCESSED_TIME)
  private OffsetDateTime processedTime;

  public static final String SERIALIZED_NAME_REJECTION_REASON = "rejectionReason";
  @SerializedName(SERIALIZED_NAME_REJECTION_REASON)
  private KycDocumentRejection rejectionReason;

  public static final String SERIALIZED_NAME_REQUEST_ID = "requestId";
  @SerializedName(SERIALIZED_NAME_REQUEST_ID)
  private String requestId;

  /**
   * Status of the validation.
   */
  @JsonAdapter(StatusEnum.Adapter.class)
  public enum StatusEnum {
    PENDING("pending"),
    
    IN_PROGRESS("in-progress"),
    
    ACCEPTED("accepted"),
    
    REJECTED("rejected");

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

  public static final String SERIALIZED_NAME_CUSTOMER_ID = "customerId";
  @SerializedName(SERIALIZED_NAME_CUSTOMER_ID)
  private String customerId;

  public static final String SERIALIZED_NAME_MATCH_LEVEL = "matchLevel";
  @SerializedName(SERIALIZED_NAME_MATCH_LEVEL)
  private Integer matchLevel;

  public static final String SERIALIZED_NAME_NOTES = "notes";
  @SerializedName(SERIALIZED_NAME_NOTES)
  private String notes;

  public static final String SERIALIZED_NAME_REASON = "reason";
  @SerializedName(SERIALIZED_NAME_REASON)
  private String reason;

  public static final String SERIALIZED_NAME_REVIEW_TIME = "reviewTime";
  @SerializedName(SERIALIZED_NAME_REVIEW_TIME)
  private OffsetDateTime reviewTime;

  public static final String SERIALIZED_NAME_REVIEWER_ID = "reviewerId";
  @SerializedName(SERIALIZED_NAME_REVIEWER_ID)
  private String reviewerId;

  public static final String SERIALIZED_NAME_REVIEWER_NAME = "reviewerName";
  @SerializedName(SERIALIZED_NAME_REVIEWER_NAME)
  private String reviewerName;

  public static final String SERIALIZED_NAME_DOCUMENT_MATCHES = "documentMatches";
  @SerializedName(SERIALIZED_NAME_DOCUMENT_MATCHES)
  private ProofOfAddressAllOfDocumentMatches documentMatches;

  public static final String SERIALIZED_NAME_PARSED_DATA = "parsedData";
  @SerializedName(SERIALIZED_NAME_PARSED_DATA)
  private ProofOfAddressAllOfDocumentMatches parsedData;

  public ProofOfAddress() {
  }

  public ProofOfAddress(
     List<ProofOfAddressAllOfLinks> links, 
     OffsetDateTime createdTime, 
     String id, 
     OffsetDateTime processedTime, 
     String requestId, 
     StatusEnum status, 
     OffsetDateTime updatedTime, 
     OffsetDateTime reviewTime, 
     String reviewerId, 
     String reviewerName
  ) {
    this();
    this.links = links;
    this.createdTime = createdTime;
    this.id = id;
    this.processedTime = processedTime;
    this.requestId = requestId;
    this.status = status;
    this.updatedTime = updatedTime;
    this.reviewTime = reviewTime;
    this.reviewerId = reviewerId;
    this.reviewerName = reviewerName;
  }

  /**
   * The links related to resource.
   * @return links
   */
  @javax.annotation.Nullable
  public List<ProofOfAddressAllOfLinks> getLinks() {
    return links;
  }



  /**
   * Creation date/time.
   * @return createdTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getCreatedTime() {
    return createdTime;
  }



  public ProofOfAddress documentSubtype(KycDocumentSubtypes documentSubtype) {
    this.documentSubtype = documentSubtype;
    return this;
  }

  /**
   * Document subtype submitted for validation.
   * @return documentSubtype
   */
  @javax.annotation.Nullable
  public KycDocumentSubtypes getDocumentSubtype() {
    return documentSubtype;
  }

  public void setDocumentSubtype(KycDocumentSubtypes documentSubtype) {
    this.documentSubtype = documentSubtype;
  }


  public ProofOfAddress documentType(KycDocumentTypes documentType) {
    this.documentType = documentType;
    return this;
  }

  /**
   * Document type submitted for validation, only identity-proof type is analyzed in an automated manner.
   * @return documentType
   */
  @javax.annotation.Nonnull
  public KycDocumentTypes getDocumentType() {
    return documentType;
  }

  public void setDocumentType(KycDocumentTypes documentType) {
    this.documentType = documentType;
  }


  @Deprecated
  public ProofOfAddress fileId(String fileId) {
    this.fileId = fileId;
    return this;
  }

  /**
   * Linked file object id.
   * @return fileId
   * @deprecated
   */
  @Deprecated
  @javax.annotation.Nullable
  public String getFileId() {
    return fileId;
  }

  @Deprecated
  public void setFileId(String fileId) {
    this.fileId = fileId;
  }


  public ProofOfAddress fileIds(List<String> fileIds) {
    this.fileIds = fileIds;
    return this;
  }

  public ProofOfAddress addFileIdsItem(String fileIdsItem) {
    if (this.fileIds == null) {
      this.fileIds = new ArrayList<>();
    }
    this.fileIds.add(fileIdsItem);
    return this;
  }

  /**
   * Linked file object id&#39;s.
   * @return fileIds
   */
  @javax.annotation.Nullable
  public List<String> getFileIds() {
    return fileIds;
  }

  public void setFileIds(List<String> fileIds) {
    this.fileIds = fileIds;
  }


  /**
   * The resource ID. Defaults to UUID v4.
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }



  /**
   * Processing date/time.
   * @return processedTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getProcessedTime() {
    return processedTime;
  }



  public ProofOfAddress rejectionReason(KycDocumentRejection rejectionReason) {
    this.rejectionReason = rejectionReason;
    return this;
  }

  /**
   * Get rejectionReason
   * @return rejectionReason
   */
  @javax.annotation.Nullable
  public KycDocumentRejection getRejectionReason() {
    return rejectionReason;
  }

  public void setRejectionReason(KycDocumentRejection rejectionReason) {
    this.rejectionReason = rejectionReason;
  }


  /**
   * KYC request identifier string.
   * @return requestId
   */
  @javax.annotation.Nullable
  public String getRequestId() {
    return requestId;
  }



  /**
   * Status of the validation.
   * @return status
   */
  @javax.annotation.Nonnull
  public StatusEnum getStatus() {
    return status;
  }



  /**
   * Latest update date/time.
   * @return updatedTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getUpdatedTime() {
    return updatedTime;
  }



  public ProofOfAddress customerId(String customerId) {
    this.customerId = customerId;
    return this;
  }

  /**
   * The сustomer&#39;s ID.
   * @return customerId
   */
  @javax.annotation.Nonnull
  public String getCustomerId() {
    return customerId;
  }

  public void setCustomerId(String customerId) {
    this.customerId = customerId;
  }


  public ProofOfAddress matchLevel(Integer matchLevel) {
    this.matchLevel = matchLevel;
    return this;
  }

  /**
   * The level of strictness for the document matches.
   * minimum: 1
   * maximum: 2
   * @return matchLevel
   */
  @javax.annotation.Nullable
  public Integer getMatchLevel() {
    return matchLevel;
  }

  public void setMatchLevel(Integer matchLevel) {
    this.matchLevel = matchLevel;
  }


  public ProofOfAddress notes(String notes) {
    this.notes = notes;
    return this;
  }

  /**
   * Reviewer notes.
   * @return notes
   */
  @javax.annotation.Nullable
  public String getNotes() {
    return notes;
  }

  public void setNotes(String notes) {
    this.notes = notes;
  }


  public ProofOfAddress reason(String reason) {
    this.reason = reason;
    return this;
  }

  /**
   * Reason for uploading.
   * @return reason
   */
  @javax.annotation.Nullable
  public String getReason() {
    return reason;
  }

  public void setReason(String reason) {
    this.reason = reason;
  }


  /**
   * Date and time of manual review.
   * @return reviewTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getReviewTime() {
    return reviewTime;
  }



  /**
   * Reviewer&#39;s user ID.
   * @return reviewerId
   */
  @javax.annotation.Nullable
  public String getReviewerId() {
    return reviewerId;
  }



  /**
   * Reviewer&#39;s first and last name.
   * @return reviewerName
   */
  @javax.annotation.Nullable
  public String getReviewerName() {
    return reviewerName;
  }



  public ProofOfAddress documentMatches(ProofOfAddressAllOfDocumentMatches documentMatches) {
    this.documentMatches = documentMatches;
    return this;
  }

  /**
   * Get documentMatches
   * @return documentMatches
   */
  @javax.annotation.Nullable
  public ProofOfAddressAllOfDocumentMatches getDocumentMatches() {
    return documentMatches;
  }

  public void setDocumentMatches(ProofOfAddressAllOfDocumentMatches documentMatches) {
    this.documentMatches = documentMatches;
  }


  public ProofOfAddress parsedData(ProofOfAddressAllOfDocumentMatches parsedData) {
    this.parsedData = parsedData;
    return this;
  }

  /**
   * Get parsedData
   * @return parsedData
   */
  @javax.annotation.Nullable
  public ProofOfAddressAllOfDocumentMatches getParsedData() {
    return parsedData;
  }

  public void setParsedData(ProofOfAddressAllOfDocumentMatches parsedData) {
    this.parsedData = parsedData;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ProofOfAddress proofOfAddress = (ProofOfAddress) o;
    return Objects.equals(this.links, proofOfAddress.links) &&
        Objects.equals(this.createdTime, proofOfAddress.createdTime) &&
        Objects.equals(this.documentSubtype, proofOfAddress.documentSubtype) &&
        Objects.equals(this.documentType, proofOfAddress.documentType) &&
        Objects.equals(this.fileId, proofOfAddress.fileId) &&
        Objects.equals(this.fileIds, proofOfAddress.fileIds) &&
        Objects.equals(this.id, proofOfAddress.id) &&
        Objects.equals(this.processedTime, proofOfAddress.processedTime) &&
        Objects.equals(this.rejectionReason, proofOfAddress.rejectionReason) &&
        Objects.equals(this.requestId, proofOfAddress.requestId) &&
        Objects.equals(this.status, proofOfAddress.status) &&
        Objects.equals(this.updatedTime, proofOfAddress.updatedTime) &&
        Objects.equals(this.customerId, proofOfAddress.customerId) &&
        Objects.equals(this.matchLevel, proofOfAddress.matchLevel) &&
        Objects.equals(this.notes, proofOfAddress.notes) &&
        Objects.equals(this.reason, proofOfAddress.reason) &&
        Objects.equals(this.reviewTime, proofOfAddress.reviewTime) &&
        Objects.equals(this.reviewerId, proofOfAddress.reviewerId) &&
        Objects.equals(this.reviewerName, proofOfAddress.reviewerName) &&
        Objects.equals(this.documentMatches, proofOfAddress.documentMatches) &&
        Objects.equals(this.parsedData, proofOfAddress.parsedData);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(links, createdTime, documentSubtype, documentType, fileId, fileIds, id, processedTime, rejectionReason, requestId, status, updatedTime, customerId, matchLevel, notes, reason, reviewTime, reviewerId, reviewerName, documentMatches, parsedData);
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
    sb.append("class ProofOfAddress {\n");
    sb.append("    links: ").append(toIndentedString(links)).append("\n");
    sb.append("    createdTime: ").append(toIndentedString(createdTime)).append("\n");
    sb.append("    documentSubtype: ").append(toIndentedString(documentSubtype)).append("\n");
    sb.append("    documentType: ").append(toIndentedString(documentType)).append("\n");
    sb.append("    fileId: ").append(toIndentedString(fileId)).append("\n");
    sb.append("    fileIds: ").append(toIndentedString(fileIds)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    processedTime: ").append(toIndentedString(processedTime)).append("\n");
    sb.append("    rejectionReason: ").append(toIndentedString(rejectionReason)).append("\n");
    sb.append("    requestId: ").append(toIndentedString(requestId)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    updatedTime: ").append(toIndentedString(updatedTime)).append("\n");
    sb.append("    customerId: ").append(toIndentedString(customerId)).append("\n");
    sb.append("    matchLevel: ").append(toIndentedString(matchLevel)).append("\n");
    sb.append("    notes: ").append(toIndentedString(notes)).append("\n");
    sb.append("    reason: ").append(toIndentedString(reason)).append("\n");
    sb.append("    reviewTime: ").append(toIndentedString(reviewTime)).append("\n");
    sb.append("    reviewerId: ").append(toIndentedString(reviewerId)).append("\n");
    sb.append("    reviewerName: ").append(toIndentedString(reviewerName)).append("\n");
    sb.append("    documentMatches: ").append(toIndentedString(documentMatches)).append("\n");
    sb.append("    parsedData: ").append(toIndentedString(parsedData)).append("\n");
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
    openapiFields.add("documentSubtype");
    openapiFields.add("documentType");
    openapiFields.add("fileId");
    openapiFields.add("fileIds");
    openapiFields.add("id");
    openapiFields.add("processedTime");
    openapiFields.add("rejectionReason");
    openapiFields.add("requestId");
    openapiFields.add("status");
    openapiFields.add("updatedTime");
    openapiFields.add("customerId");
    openapiFields.add("matchLevel");
    openapiFields.add("notes");
    openapiFields.add("reason");
    openapiFields.add("reviewTime");
    openapiFields.add("reviewerId");
    openapiFields.add("reviewerName");
    openapiFields.add("documentMatches");
    openapiFields.add("parsedData");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("documentType");
    openapiRequiredFields.add("status");
    openapiRequiredFields.add("customerId");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ProofOfAddress
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ProofOfAddress.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ProofOfAddress is not found in the empty JSON string", ProofOfAddress.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ProofOfAddress.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ProofOfAddress` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : ProofOfAddress.openapiRequiredFields) {
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
            ProofOfAddressAllOfLinks.validateJsonElement(jsonArraylinks.get(i));
          };
        }
      }
      // validate the optional field `documentSubtype`
      if (jsonObj.get("documentSubtype") != null && !jsonObj.get("documentSubtype").isJsonNull()) {
        KycDocumentSubtypes.validateJsonElement(jsonObj.get("documentSubtype"));
      }
      // validate the required field `documentType`
      KycDocumentTypes.validateJsonElement(jsonObj.get("documentType"));
      if ((jsonObj.get("fileId") != null && !jsonObj.get("fileId").isJsonNull()) && !jsonObj.get("fileId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `fileId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("fileId").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("fileIds") != null && !jsonObj.get("fileIds").isJsonNull() && !jsonObj.get("fileIds").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `fileIds` to be an array in the JSON string but got `%s`", jsonObj.get("fileIds").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      // validate the optional field `rejectionReason`
      if (jsonObj.get("rejectionReason") != null && !jsonObj.get("rejectionReason").isJsonNull()) {
        KycDocumentRejection.validateJsonElement(jsonObj.get("rejectionReason"));
      }
      if ((jsonObj.get("requestId") != null && !jsonObj.get("requestId").isJsonNull()) && !jsonObj.get("requestId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `requestId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("requestId").toString()));
      }
      if (!jsonObj.get("status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("status").toString()));
      }
      // validate the required field `status`
      StatusEnum.validateJsonElement(jsonObj.get("status"));
      if (!jsonObj.get("customerId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `customerId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("customerId").toString()));
      }
      if ((jsonObj.get("notes") != null && !jsonObj.get("notes").isJsonNull()) && !jsonObj.get("notes").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `notes` to be a primitive type in the JSON string but got `%s`", jsonObj.get("notes").toString()));
      }
      if ((jsonObj.get("reason") != null && !jsonObj.get("reason").isJsonNull()) && !jsonObj.get("reason").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `reason` to be a primitive type in the JSON string but got `%s`", jsonObj.get("reason").toString()));
      }
      if ((jsonObj.get("reviewerId") != null && !jsonObj.get("reviewerId").isJsonNull()) && !jsonObj.get("reviewerId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `reviewerId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("reviewerId").toString()));
      }
      if ((jsonObj.get("reviewerName") != null && !jsonObj.get("reviewerName").isJsonNull()) && !jsonObj.get("reviewerName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `reviewerName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("reviewerName").toString()));
      }
      // validate the optional field `documentMatches`
      if (jsonObj.get("documentMatches") != null && !jsonObj.get("documentMatches").isJsonNull()) {
        ProofOfAddressAllOfDocumentMatches.validateJsonElement(jsonObj.get("documentMatches"));
      }
      // validate the optional field `parsedData`
      if (jsonObj.get("parsedData") != null && !jsonObj.get("parsedData").isJsonNull()) {
        ProofOfAddressAllOfDocumentMatches.validateJsonElement(jsonObj.get("parsedData"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ProofOfAddress.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ProofOfAddress' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ProofOfAddress> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ProofOfAddress.class));

       return (TypeAdapter<T>) new TypeAdapter<ProofOfAddress>() {
           @Override
           public void write(JsonWriter out, ProofOfAddress value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ProofOfAddress read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ProofOfAddress given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ProofOfAddress
   * @throws IOException if the JSON string is invalid with respect to ProofOfAddress
   */
  public static ProofOfAddress fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ProofOfAddress.class);
  }

  /**
   * Convert an instance of ProofOfAddress to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

