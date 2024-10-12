/*
 * Apacta
 * API for a tool to craftsmen used to register working hours, material usage and quality assurance. # Endpoint The endpoint `https://app.apacta.com/api/v1` should be used to communicate with the API. API access is only allowed with SSL encrypted connection (https). # Authentication URL query authentication with an API key is used, so appending `?api_key={api_key}` to the URL where `{api_key}` is found within Apacta settings is used for authentication # Pagination If the endpoint returns a `pagination` object it means the endpoint supports pagination - currently it's only possible to change pages with `?page={page_number}` but implementing custom page sizes are on the road map.   # Search/filter Is experimental but implemented in some cases - see the individual endpoints' docs for further explanation. # Ordering Is currently experimental, but on some endpoints it's implemented on URL querys so eg. to order Invoices by `invoice_number` appending `?sort=Invoices.invoice_number&direction=desc` would sort the list descending by the value of `invoice_number`. # Associations Is currently implemented on an experimental basis where you can append eg. `?include=Contacts,Projects`  to the `/api/v1/invoices/` endpoint to embed `Contact` and `Project` objects directly. # Project Files Currently project files can be retrieved from two endpoints. `/projects/{project_id}/files` handles files uploaded from wall posts or forms. `/projects/{project_id}/project_files` allows uploading and showing files, not belonging to specific form or wall post. # Errors/Exceptions ## 422 (Validation) Write something about how the `errors` object contains keys with the properties that failes validation like: ```   {       \"success\": false,       \"data\": {           \"code\": 422,           \"url\": \"/api/v1/contacts?api_key=5523be3b-30ef-425d-8203-04df7caaa93a\",           \"message\": \"A validation error occurred\",           \"errorCount\": 1,           \"errors\": {               \"contact_types\": [ ## Property name that failed validation                   \"Contacts must have at least one contact type\" ## Message with further explanation               ]           }       }   } ``` ## Code examples Running examples of how to retrieve the 5 most recent forms registered and embed the details of the User that made the form, and eventual products contained in the form ### Swift ``` ``` ### Java #### OkHttp ```   OkHttpClient client = new OkHttpClient();    Request request = new Request.Builder()     .url(\"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\")     .get()     .addHeader(\"x-auth-token\", \"{INSERT_YOUR_TOKEN}\")     .addHeader(\"accept\", \"application/json\")     .build();    Response response = client.newCall(request).execute(); ``` #### Unirest ```   HttpResponse<String> response = Unirest.get(\"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\")     .header(\"x-auth-token\", \"{INSERT_YOUR_TOKEN}\")     .header(\"accept\", \"application/json\")     .asString(); ``` ### Javascript #### Native ```   var data = null;    var xhr = new XMLHttpRequest();    xhr.addEventListener(\"readystatechange\", function () {     if (this.readyState === 4) {       console.log(this.responseText);     }   });    xhr.open(\"GET\", \"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\");   xhr.setRequestHeader(\"x-auth-token\", \"{INSERT_YOUR_TOKEN}\");   xhr.setRequestHeader(\"accept\", \"application/json\");    xhr.send(data); ``` #### jQuery ```   var settings = {     \"async\": true,     \"crossDomain\": true,     \"url\": \"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\",     \"method\": \"GET\",     \"headers\": {       \"x-auth-token\": \"{INSERT_YOUR_TOKEN}\",       \"accept\": \"application/json\",     }   }    $.ajax(settings).done(function (response) {     console.log(response);   }); ``` #### NodeJS (Request) ```   var request = require(\"request\");    var options = { method: 'GET',     url: 'https://app.apacta.com/api/v1/forms',     qs:      { extended: 'true',        sort: 'Forms.created',        direction: 'DESC',        include: 'Products,CreatedBy',        limit: '5' },     headers:      { accept: 'application/json',        'x-auth-token': '{INSERT_YOUR_TOKEN}' } };    request(options, function (error, response, body) {     if (error) throw new Error(error);      console.log(body);   });  ``` ### Python 3 ```   import http.client    conn = http.client.HTTPSConnection(\"app.apacta.com\")    payload = \"\"    headers = {       'x-auth-token': \"{INSERT_YOUR_TOKEN}\",       'accept': \"application/json\",       }    conn.request(\"GET\", \"/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\", payload, headers)    res = conn.getresponse()   data = res.read()    print(data.decode(\"utf-8\")) ``` ### C# #### RestSharp ```   var client = new RestClient(\"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\");   var request = new RestRequest(Method.GET);   request.AddHeader(\"accept\", \"application/json\");   request.AddHeader(\"x-auth-token\", \"{INSERT_YOUR_TOKEN}\");   IRestResponse response = client.Execute(request); ``` ### Ruby ```   require 'uri'   require 'net/http'    url = URI(\"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\")    http = Net::HTTP.new(url.host, url.port)   http.use_ssl = true   http.verify_mode = OpenSSL::SSL::VERIFY_NONE    request = Net::HTTP::Get.new(url)   request[\"x-auth-token\"] = '{INSERT_YOUR_TOKEN}'   request[\"accept\"] = 'application/json'    response = http.request(request)   puts response.read_body ``` ### PHP (HttpRequest) ```   <?php    $request = new HttpRequest();   $request->setUrl('https://app.apacta.com/api/v1/forms');   $request->setMethod(HTTP_METH_GET);    $request->setQueryData(array(     'extended' => 'true',     'sort' => 'Forms.created',     'direction' => 'DESC',     'include' => 'Products,CreatedBy',     'limit' => '5'   ));    $request->setHeaders(array(     'accept' => 'application/json',     'x-auth-token' => '{INSERT_YOUR_TOKEN}'   ));    try {     $response = $request->send();      echo $response->getBody();   } catch (HttpException $ex) {     echo $ex;   } ``` ### Shell (cURL) ```    $ curl --request GET --url 'https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5' --header 'accept: application/json' --header 'x-auth-token: {INSERT_YOUR_TOKEN}'  ```
 *
 * The version of the OpenAPI document: 0.0.42
 * 
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
import java.util.Arrays;
import java.util.UUID;

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
 * InvoicesPostRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:16.415087-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class InvoicesPostRequest {
  public static final String SERIALIZED_NAME_CONTACT_ID = "contact_id";
  @SerializedName(SERIALIZED_NAME_CONTACT_ID)
  private UUID contactId;

  public static final String SERIALIZED_NAME_CREATED_OR_MODIFIED_GTE = "created_or_modified_gte";
  @SerializedName(SERIALIZED_NAME_CREATED_OR_MODIFIED_GTE)
  private LocalDate createdOrModifiedGte;

  public static final String SERIALIZED_NAME_DATE_FROM = "date_from";
  @SerializedName(SERIALIZED_NAME_DATE_FROM)
  private LocalDate dateFrom;

  public static final String SERIALIZED_NAME_DATE_TO = "date_to";
  @SerializedName(SERIALIZED_NAME_DATE_TO)
  private LocalDate dateTo;

  public static final String SERIALIZED_NAME_ERP_ID = "erp_id";
  @SerializedName(SERIALIZED_NAME_ERP_ID)
  private String erpId;

  public static final String SERIALIZED_NAME_ERP_PAYMENT_TERM_ID = "erp_payment_term_id";
  @SerializedName(SERIALIZED_NAME_ERP_PAYMENT_TERM_ID)
  private String erpPaymentTermId;

  public static final String SERIALIZED_NAME_INVOICE_NUMBER = "invoice_number";
  @SerializedName(SERIALIZED_NAME_INVOICE_NUMBER)
  private Integer invoiceNumber;

  public static final String SERIALIZED_NAME_IS_DRAFT = "is_draft";
  @SerializedName(SERIALIZED_NAME_IS_DRAFT)
  private Boolean isDraft;

  public static final String SERIALIZED_NAME_IS_LOCKED = "is_locked";
  @SerializedName(SERIALIZED_NAME_IS_LOCKED)
  private Boolean isLocked;

  public static final String SERIALIZED_NAME_IS_OFFER = "is_offer";
  @SerializedName(SERIALIZED_NAME_IS_OFFER)
  private Boolean isOffer;

  public static final String SERIALIZED_NAME_ISSUED_DATE = "issued_date";
  @SerializedName(SERIALIZED_NAME_ISSUED_DATE)
  private LocalDate issuedDate;

  public static final String SERIALIZED_NAME_MESSAGE = "message";
  @SerializedName(SERIALIZED_NAME_MESSAGE)
  private String message;

  public static final String SERIALIZED_NAME_OFFER_NUMBER = "offer_number";
  @SerializedName(SERIALIZED_NAME_OFFER_NUMBER)
  private Integer offerNumber;

  public static final String SERIALIZED_NAME_PAYMENT_DUE_DATE = "payment_due_date";
  @SerializedName(SERIALIZED_NAME_PAYMENT_DUE_DATE)
  private LocalDate paymentDueDate;

  public static final String SERIALIZED_NAME_PAYMENT_TERM_ID = "payment_term_id";
  @SerializedName(SERIALIZED_NAME_PAYMENT_TERM_ID)
  private UUID paymentTermId;

  public static final String SERIALIZED_NAME_PROJECT_ID = "project_id";
  @SerializedName(SERIALIZED_NAME_PROJECT_ID)
  private UUID projectId;

  public static final String SERIALIZED_NAME_REFERENCE = "reference";
  @SerializedName(SERIALIZED_NAME_REFERENCE)
  private String reference;

  public static final String SERIALIZED_NAME_VAT_PERCENT = "vat_percent";
  @SerializedName(SERIALIZED_NAME_VAT_PERCENT)
  private Integer vatPercent;

  public InvoicesPostRequest() {
  }

  public InvoicesPostRequest contactId(UUID contactId) {
    this.contactId = contactId;
    return this;
  }

  /**
   * Get contactId
   * @return contactId
   */
  @javax.annotation.Nullable
  public UUID getContactId() {
    return contactId;
  }

  public void setContactId(UUID contactId) {
    this.contactId = contactId;
  }


  public InvoicesPostRequest createdOrModifiedGte(LocalDate createdOrModifiedGte) {
    this.createdOrModifiedGte = createdOrModifiedGte;
    return this;
  }

  /**
   * Get createdOrModifiedGte
   * @return createdOrModifiedGte
   */
  @javax.annotation.Nullable
  public LocalDate getCreatedOrModifiedGte() {
    return createdOrModifiedGte;
  }

  public void setCreatedOrModifiedGte(LocalDate createdOrModifiedGte) {
    this.createdOrModifiedGte = createdOrModifiedGte;
  }


  public InvoicesPostRequest dateFrom(LocalDate dateFrom) {
    this.dateFrom = dateFrom;
    return this;
  }

  /**
   * Get dateFrom
   * @return dateFrom
   */
  @javax.annotation.Nullable
  public LocalDate getDateFrom() {
    return dateFrom;
  }

  public void setDateFrom(LocalDate dateFrom) {
    this.dateFrom = dateFrom;
  }


  public InvoicesPostRequest dateTo(LocalDate dateTo) {
    this.dateTo = dateTo;
    return this;
  }

  /**
   * Get dateTo
   * @return dateTo
   */
  @javax.annotation.Nullable
  public LocalDate getDateTo() {
    return dateTo;
  }

  public void setDateTo(LocalDate dateTo) {
    this.dateTo = dateTo;
  }


  public InvoicesPostRequest erpId(String erpId) {
    this.erpId = erpId;
    return this;
  }

  /**
   * Get erpId
   * @return erpId
   */
  @javax.annotation.Nullable
  public String getErpId() {
    return erpId;
  }

  public void setErpId(String erpId) {
    this.erpId = erpId;
  }


  public InvoicesPostRequest erpPaymentTermId(String erpPaymentTermId) {
    this.erpPaymentTermId = erpPaymentTermId;
    return this;
  }

  /**
   * Get erpPaymentTermId
   * @return erpPaymentTermId
   */
  @javax.annotation.Nullable
  public String getErpPaymentTermId() {
    return erpPaymentTermId;
  }

  public void setErpPaymentTermId(String erpPaymentTermId) {
    this.erpPaymentTermId = erpPaymentTermId;
  }


  public InvoicesPostRequest invoiceNumber(Integer invoiceNumber) {
    this.invoiceNumber = invoiceNumber;
    return this;
  }

  /**
   * Get invoiceNumber
   * @return invoiceNumber
   */
  @javax.annotation.Nullable
  public Integer getInvoiceNumber() {
    return invoiceNumber;
  }

  public void setInvoiceNumber(Integer invoiceNumber) {
    this.invoiceNumber = invoiceNumber;
  }


  public InvoicesPostRequest isDraft(Boolean isDraft) {
    this.isDraft = isDraft;
    return this;
  }

  /**
   * Get isDraft
   * @return isDraft
   */
  @javax.annotation.Nullable
  public Boolean getIsDraft() {
    return isDraft;
  }

  public void setIsDraft(Boolean isDraft) {
    this.isDraft = isDraft;
  }


  public InvoicesPostRequest isLocked(Boolean isLocked) {
    this.isLocked = isLocked;
    return this;
  }

  /**
   * Get isLocked
   * @return isLocked
   */
  @javax.annotation.Nullable
  public Boolean getIsLocked() {
    return isLocked;
  }

  public void setIsLocked(Boolean isLocked) {
    this.isLocked = isLocked;
  }


  public InvoicesPostRequest isOffer(Boolean isOffer) {
    this.isOffer = isOffer;
    return this;
  }

  /**
   * Get isOffer
   * @return isOffer
   */
  @javax.annotation.Nullable
  public Boolean getIsOffer() {
    return isOffer;
  }

  public void setIsOffer(Boolean isOffer) {
    this.isOffer = isOffer;
  }


  public InvoicesPostRequest issuedDate(LocalDate issuedDate) {
    this.issuedDate = issuedDate;
    return this;
  }

  /**
   * Get issuedDate
   * @return issuedDate
   */
  @javax.annotation.Nullable
  public LocalDate getIssuedDate() {
    return issuedDate;
  }

  public void setIssuedDate(LocalDate issuedDate) {
    this.issuedDate = issuedDate;
  }


  public InvoicesPostRequest message(String message) {
    this.message = message;
    return this;
  }

  /**
   * Get message
   * @return message
   */
  @javax.annotation.Nullable
  public String getMessage() {
    return message;
  }

  public void setMessage(String message) {
    this.message = message;
  }


  public InvoicesPostRequest offerNumber(Integer offerNumber) {
    this.offerNumber = offerNumber;
    return this;
  }

  /**
   * Get offerNumber
   * @return offerNumber
   */
  @javax.annotation.Nullable
  public Integer getOfferNumber() {
    return offerNumber;
  }

  public void setOfferNumber(Integer offerNumber) {
    this.offerNumber = offerNumber;
  }


  public InvoicesPostRequest paymentDueDate(LocalDate paymentDueDate) {
    this.paymentDueDate = paymentDueDate;
    return this;
  }

  /**
   * Get paymentDueDate
   * @return paymentDueDate
   */
  @javax.annotation.Nullable
  public LocalDate getPaymentDueDate() {
    return paymentDueDate;
  }

  public void setPaymentDueDate(LocalDate paymentDueDate) {
    this.paymentDueDate = paymentDueDate;
  }


  public InvoicesPostRequest paymentTermId(UUID paymentTermId) {
    this.paymentTermId = paymentTermId;
    return this;
  }

  /**
   * Get paymentTermId
   * @return paymentTermId
   */
  @javax.annotation.Nullable
  public UUID getPaymentTermId() {
    return paymentTermId;
  }

  public void setPaymentTermId(UUID paymentTermId) {
    this.paymentTermId = paymentTermId;
  }


  public InvoicesPostRequest projectId(UUID projectId) {
    this.projectId = projectId;
    return this;
  }

  /**
   * Get projectId
   * @return projectId
   */
  @javax.annotation.Nullable
  public UUID getProjectId() {
    return projectId;
  }

  public void setProjectId(UUID projectId) {
    this.projectId = projectId;
  }


  public InvoicesPostRequest reference(String reference) {
    this.reference = reference;
    return this;
  }

  /**
   * Get reference
   * @return reference
   */
  @javax.annotation.Nullable
  public String getReference() {
    return reference;
  }

  public void setReference(String reference) {
    this.reference = reference;
  }


  public InvoicesPostRequest vatPercent(Integer vatPercent) {
    this.vatPercent = vatPercent;
    return this;
  }

  /**
   * Get vatPercent
   * @return vatPercent
   */
  @javax.annotation.Nullable
  public Integer getVatPercent() {
    return vatPercent;
  }

  public void setVatPercent(Integer vatPercent) {
    this.vatPercent = vatPercent;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    InvoicesPostRequest invoicesPostRequest = (InvoicesPostRequest) o;
    return Objects.equals(this.contactId, invoicesPostRequest.contactId) &&
        Objects.equals(this.createdOrModifiedGte, invoicesPostRequest.createdOrModifiedGte) &&
        Objects.equals(this.dateFrom, invoicesPostRequest.dateFrom) &&
        Objects.equals(this.dateTo, invoicesPostRequest.dateTo) &&
        Objects.equals(this.erpId, invoicesPostRequest.erpId) &&
        Objects.equals(this.erpPaymentTermId, invoicesPostRequest.erpPaymentTermId) &&
        Objects.equals(this.invoiceNumber, invoicesPostRequest.invoiceNumber) &&
        Objects.equals(this.isDraft, invoicesPostRequest.isDraft) &&
        Objects.equals(this.isLocked, invoicesPostRequest.isLocked) &&
        Objects.equals(this.isOffer, invoicesPostRequest.isOffer) &&
        Objects.equals(this.issuedDate, invoicesPostRequest.issuedDate) &&
        Objects.equals(this.message, invoicesPostRequest.message) &&
        Objects.equals(this.offerNumber, invoicesPostRequest.offerNumber) &&
        Objects.equals(this.paymentDueDate, invoicesPostRequest.paymentDueDate) &&
        Objects.equals(this.paymentTermId, invoicesPostRequest.paymentTermId) &&
        Objects.equals(this.projectId, invoicesPostRequest.projectId) &&
        Objects.equals(this.reference, invoicesPostRequest.reference) &&
        Objects.equals(this.vatPercent, invoicesPostRequest.vatPercent);
  }

  @Override
  public int hashCode() {
    return Objects.hash(contactId, createdOrModifiedGte, dateFrom, dateTo, erpId, erpPaymentTermId, invoiceNumber, isDraft, isLocked, isOffer, issuedDate, message, offerNumber, paymentDueDate, paymentTermId, projectId, reference, vatPercent);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class InvoicesPostRequest {\n");
    sb.append("    contactId: ").append(toIndentedString(contactId)).append("\n");
    sb.append("    createdOrModifiedGte: ").append(toIndentedString(createdOrModifiedGte)).append("\n");
    sb.append("    dateFrom: ").append(toIndentedString(dateFrom)).append("\n");
    sb.append("    dateTo: ").append(toIndentedString(dateTo)).append("\n");
    sb.append("    erpId: ").append(toIndentedString(erpId)).append("\n");
    sb.append("    erpPaymentTermId: ").append(toIndentedString(erpPaymentTermId)).append("\n");
    sb.append("    invoiceNumber: ").append(toIndentedString(invoiceNumber)).append("\n");
    sb.append("    isDraft: ").append(toIndentedString(isDraft)).append("\n");
    sb.append("    isLocked: ").append(toIndentedString(isLocked)).append("\n");
    sb.append("    isOffer: ").append(toIndentedString(isOffer)).append("\n");
    sb.append("    issuedDate: ").append(toIndentedString(issuedDate)).append("\n");
    sb.append("    message: ").append(toIndentedString(message)).append("\n");
    sb.append("    offerNumber: ").append(toIndentedString(offerNumber)).append("\n");
    sb.append("    paymentDueDate: ").append(toIndentedString(paymentDueDate)).append("\n");
    sb.append("    paymentTermId: ").append(toIndentedString(paymentTermId)).append("\n");
    sb.append("    projectId: ").append(toIndentedString(projectId)).append("\n");
    sb.append("    reference: ").append(toIndentedString(reference)).append("\n");
    sb.append("    vatPercent: ").append(toIndentedString(vatPercent)).append("\n");
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
    openapiFields.add("contact_id");
    openapiFields.add("created_or_modified_gte");
    openapiFields.add("date_from");
    openapiFields.add("date_to");
    openapiFields.add("erp_id");
    openapiFields.add("erp_payment_term_id");
    openapiFields.add("invoice_number");
    openapiFields.add("is_draft");
    openapiFields.add("is_locked");
    openapiFields.add("is_offer");
    openapiFields.add("issued_date");
    openapiFields.add("message");
    openapiFields.add("offer_number");
    openapiFields.add("payment_due_date");
    openapiFields.add("payment_term_id");
    openapiFields.add("project_id");
    openapiFields.add("reference");
    openapiFields.add("vat_percent");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to InvoicesPostRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!InvoicesPostRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in InvoicesPostRequest is not found in the empty JSON string", InvoicesPostRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!InvoicesPostRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `InvoicesPostRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("contact_id") != null && !jsonObj.get("contact_id").isJsonNull()) && !jsonObj.get("contact_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `contact_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("contact_id").toString()));
      }
      if ((jsonObj.get("erp_id") != null && !jsonObj.get("erp_id").isJsonNull()) && !jsonObj.get("erp_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `erp_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("erp_id").toString()));
      }
      if ((jsonObj.get("erp_payment_term_id") != null && !jsonObj.get("erp_payment_term_id").isJsonNull()) && !jsonObj.get("erp_payment_term_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `erp_payment_term_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("erp_payment_term_id").toString()));
      }
      if ((jsonObj.get("message") != null && !jsonObj.get("message").isJsonNull()) && !jsonObj.get("message").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `message` to be a primitive type in the JSON string but got `%s`", jsonObj.get("message").toString()));
      }
      if ((jsonObj.get("payment_term_id") != null && !jsonObj.get("payment_term_id").isJsonNull()) && !jsonObj.get("payment_term_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `payment_term_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("payment_term_id").toString()));
      }
      if ((jsonObj.get("project_id") != null && !jsonObj.get("project_id").isJsonNull()) && !jsonObj.get("project_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `project_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("project_id").toString()));
      }
      if ((jsonObj.get("reference") != null && !jsonObj.get("reference").isJsonNull()) && !jsonObj.get("reference").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `reference` to be a primitive type in the JSON string but got `%s`", jsonObj.get("reference").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!InvoicesPostRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'InvoicesPostRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<InvoicesPostRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(InvoicesPostRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<InvoicesPostRequest>() {
           @Override
           public void write(JsonWriter out, InvoicesPostRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public InvoicesPostRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of InvoicesPostRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of InvoicesPostRequest
   * @throws IOException if the JSON string is invalid with respect to InvoicesPostRequest
   */
  public static InvoicesPostRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, InvoicesPostRequest.class);
  }

  /**
   * Convert an instance of InvoicesPostRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

