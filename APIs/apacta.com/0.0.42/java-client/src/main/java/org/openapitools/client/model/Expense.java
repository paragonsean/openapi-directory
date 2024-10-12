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
 * Expense
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:16.415087-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Expense {
  public static final String SERIALIZED_NAME_ACTIVITY_ID = "activity_id";
  @SerializedName(SERIALIZED_NAME_ACTIVITY_ID)
  private UUID activityId;

  public static final String SERIALIZED_NAME_COMMENT = "comment";
  @SerializedName(SERIALIZED_NAME_COMMENT)
  private String comment;

  public static final String SERIALIZED_NAME_COMPANY_ID = "company_id";
  @SerializedName(SERIALIZED_NAME_COMPANY_ID)
  private UUID companyId;

  public static final String SERIALIZED_NAME_CONTACT_ID = "contact_id";
  @SerializedName(SERIALIZED_NAME_CONTACT_ID)
  private UUID contactId;

  public static final String SERIALIZED_NAME_CREATED = "created";
  @SerializedName(SERIALIZED_NAME_CREATED)
  private String created;

  public static final String SERIALIZED_NAME_CREATED_BY_ID = "created_by_id";
  @SerializedName(SERIALIZED_NAME_CREATED_BY_ID)
  private UUID createdById;

  public static final String SERIALIZED_NAME_CURRENCY_ID = "currency_id";
  @SerializedName(SERIALIZED_NAME_CURRENCY_ID)
  private UUID currencyId;

  public static final String SERIALIZED_NAME_DELETED = "deleted";
  @SerializedName(SERIALIZED_NAME_DELETED)
  private String deleted;

  public static final String SERIALIZED_NAME_DELIVERY_DATE = "delivery_date";
  @SerializedName(SERIALIZED_NAME_DELIVERY_DATE)
  private LocalDate deliveryDate;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_DUE_DATE = "due_date";
  @SerializedName(SERIALIZED_NAME_DUE_DATE)
  private LocalDate dueDate;

  public static final String SERIALIZED_NAME_FILE_REFERENCE = "file_reference";
  @SerializedName(SERIALIZED_NAME_FILE_REFERENCE)
  private String fileReference;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private UUID id;

  public static final String SERIALIZED_NAME_IS_IMPORTED = "is_imported";
  @SerializedName(SERIALIZED_NAME_IS_IMPORTED)
  private String isImported;

  public static final String SERIALIZED_NAME_MODIFIED = "modified";
  @SerializedName(SERIALIZED_NAME_MODIFIED)
  private String modified;

  public static final String SERIALIZED_NAME_ORDER_NUMBER = "order_number";
  @SerializedName(SERIALIZED_NAME_ORDER_NUMBER)
  private String orderNumber;

  public static final String SERIALIZED_NAME_PROJECT_ID = "project_id";
  @SerializedName(SERIALIZED_NAME_PROJECT_ID)
  private UUID projectId;

  public static final String SERIALIZED_NAME_READSOFT_ID = "readsoft_id";
  @SerializedName(SERIALIZED_NAME_READSOFT_ID)
  private String readsoftId;

  public static final String SERIALIZED_NAME_REFERENCE = "reference";
  @SerializedName(SERIALIZED_NAME_REFERENCE)
  private String reference;

  public static final String SERIALIZED_NAME_ROGER_ID = "roger_id";
  @SerializedName(SERIALIZED_NAME_ROGER_ID)
  private UUID rogerId;

  public static final String SERIALIZED_NAME_SENT_TO_EMAIL = "sent_to_email";
  @SerializedName(SERIALIZED_NAME_SENT_TO_EMAIL)
  private String sentToEmail;

  public static final String SERIALIZED_NAME_SHORT_TEXT = "short_text";
  @SerializedName(SERIALIZED_NAME_SHORT_TEXT)
  private String shortText;

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private String status;

  public static final String SERIALIZED_NAME_SUPPLIER_INVOICE_NUMBER = "supplier_invoice_number";
  @SerializedName(SERIALIZED_NAME_SUPPLIER_INVOICE_NUMBER)
  private String supplierInvoiceNumber;

  public static final String SERIALIZED_NAME_TOTAL_BUYING_PRICE = "total_buying_price";
  @SerializedName(SERIALIZED_NAME_TOTAL_BUYING_PRICE)
  private Float totalBuyingPrice;

  public static final String SERIALIZED_NAME_TOTAL_SELLING_PRICE = "total_selling_price";
  @SerializedName(SERIALIZED_NAME_TOTAL_SELLING_PRICE)
  private Float totalSellingPrice;

  public Expense() {
  }

  public Expense(
     String created, 
     String deleted, 
     String modified
  ) {
    this();
    this.created = created;
    this.deleted = deleted;
    this.modified = modified;
  }

  public Expense activityId(UUID activityId) {
    this.activityId = activityId;
    return this;
  }

  /**
   * Get activityId
   * @return activityId
   */
  @javax.annotation.Nullable
  public UUID getActivityId() {
    return activityId;
  }

  public void setActivityId(UUID activityId) {
    this.activityId = activityId;
  }


  public Expense comment(String comment) {
    this.comment = comment;
    return this;
  }

  /**
   * Get comment
   * @return comment
   */
  @javax.annotation.Nullable
  public String getComment() {
    return comment;
  }

  public void setComment(String comment) {
    this.comment = comment;
  }


  public Expense companyId(UUID companyId) {
    this.companyId = companyId;
    return this;
  }

  /**
   * Read-only
   * @return companyId
   */
  @javax.annotation.Nullable
  public UUID getCompanyId() {
    return companyId;
  }

  public void setCompanyId(UUID companyId) {
    this.companyId = companyId;
  }


  public Expense contactId(UUID contactId) {
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


  /**
   * Get created
   * @return created
   */
  @javax.annotation.Nullable
  public String getCreated() {
    return created;
  }



  public Expense createdById(UUID createdById) {
    this.createdById = createdById;
    return this;
  }

  /**
   * Read-only
   * @return createdById
   */
  @javax.annotation.Nullable
  public UUID getCreatedById() {
    return createdById;
  }

  public void setCreatedById(UUID createdById) {
    this.createdById = createdById;
  }


  public Expense currencyId(UUID currencyId) {
    this.currencyId = currencyId;
    return this;
  }

  /**
   * Get currencyId
   * @return currencyId
   */
  @javax.annotation.Nullable
  public UUID getCurrencyId() {
    return currencyId;
  }

  public void setCurrencyId(UUID currencyId) {
    this.currencyId = currencyId;
  }


  /**
   * Only present if it&#39;s a deleted object
   * @return deleted
   */
  @javax.annotation.Nullable
  public String getDeleted() {
    return deleted;
  }



  public Expense deliveryDate(LocalDate deliveryDate) {
    this.deliveryDate = deliveryDate;
    return this;
  }

  /**
   * Get deliveryDate
   * @return deliveryDate
   */
  @javax.annotation.Nullable
  public LocalDate getDeliveryDate() {
    return deliveryDate;
  }

  public void setDeliveryDate(LocalDate deliveryDate) {
    this.deliveryDate = deliveryDate;
  }


  public Expense description(String description) {
    this.description = description;
    return this;
  }

  /**
   * Get description
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public Expense dueDate(LocalDate dueDate) {
    this.dueDate = dueDate;
    return this;
  }

  /**
   * Get dueDate
   * @return dueDate
   */
  @javax.annotation.Nullable
  public LocalDate getDueDate() {
    return dueDate;
  }

  public void setDueDate(LocalDate dueDate) {
    this.dueDate = dueDate;
  }


  public Expense fileReference(String fileReference) {
    this.fileReference = fileReference;
    return this;
  }

  /**
   * Get fileReference
   * @return fileReference
   */
  @javax.annotation.Nullable
  public String getFileReference() {
    return fileReference;
  }

  public void setFileReference(String fileReference) {
    this.fileReference = fileReference;
  }


  public Expense id(UUID id) {
    this.id = id;
    return this;
  }

  /**
   * Read-only
   * @return id
   */
  @javax.annotation.Nullable
  public UUID getId() {
    return id;
  }

  public void setId(UUID id) {
    this.id = id;
  }


  public Expense isImported(String isImported) {
    this.isImported = isImported;
    return this;
  }

  /**
   * Get isImported
   * @return isImported
   */
  @javax.annotation.Nullable
  public String getIsImported() {
    return isImported;
  }

  public void setIsImported(String isImported) {
    this.isImported = isImported;
  }


  /**
   * Get modified
   * @return modified
   */
  @javax.annotation.Nullable
  public String getModified() {
    return modified;
  }



  public Expense orderNumber(String orderNumber) {
    this.orderNumber = orderNumber;
    return this;
  }

  /**
   * Get orderNumber
   * @return orderNumber
   */
  @javax.annotation.Nullable
  public String getOrderNumber() {
    return orderNumber;
  }

  public void setOrderNumber(String orderNumber) {
    this.orderNumber = orderNumber;
  }


  public Expense projectId(UUID projectId) {
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


  public Expense readsoftId(String readsoftId) {
    this.readsoftId = readsoftId;
    return this;
  }

  /**
   * Get readsoftId
   * @return readsoftId
   */
  @javax.annotation.Nullable
  public String getReadsoftId() {
    return readsoftId;
  }

  public void setReadsoftId(String readsoftId) {
    this.readsoftId = readsoftId;
  }


  public Expense reference(String reference) {
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


  public Expense rogerId(UUID rogerId) {
    this.rogerId = rogerId;
    return this;
  }

  /**
   * Get rogerId
   * @return rogerId
   */
  @javax.annotation.Nullable
  public UUID getRogerId() {
    return rogerId;
  }

  public void setRogerId(UUID rogerId) {
    this.rogerId = rogerId;
  }


  public Expense sentToEmail(String sentToEmail) {
    this.sentToEmail = sentToEmail;
    return this;
  }

  /**
   * Get sentToEmail
   * @return sentToEmail
   */
  @javax.annotation.Nullable
  public String getSentToEmail() {
    return sentToEmail;
  }

  public void setSentToEmail(String sentToEmail) {
    this.sentToEmail = sentToEmail;
  }


  public Expense shortText(String shortText) {
    this.shortText = shortText;
    return this;
  }

  /**
   * Get shortText
   * @return shortText
   */
  @javax.annotation.Nullable
  public String getShortText() {
    return shortText;
  }

  public void setShortText(String shortText) {
    this.shortText = shortText;
  }


  public Expense status(String status) {
    this.status = status;
    return this;
  }

  /**
   * Get status
   * @return status
   */
  @javax.annotation.Nullable
  public String getStatus() {
    return status;
  }

  public void setStatus(String status) {
    this.status = status;
  }


  public Expense supplierInvoiceNumber(String supplierInvoiceNumber) {
    this.supplierInvoiceNumber = supplierInvoiceNumber;
    return this;
  }

  /**
   * Get supplierInvoiceNumber
   * @return supplierInvoiceNumber
   */
  @javax.annotation.Nullable
  public String getSupplierInvoiceNumber() {
    return supplierInvoiceNumber;
  }

  public void setSupplierInvoiceNumber(String supplierInvoiceNumber) {
    this.supplierInvoiceNumber = supplierInvoiceNumber;
  }


  public Expense totalBuyingPrice(Float totalBuyingPrice) {
    this.totalBuyingPrice = totalBuyingPrice;
    return this;
  }

  /**
   * Sum of all &#x60;buying_price&#x60; from expense lines
   * @return totalBuyingPrice
   */
  @javax.annotation.Nullable
  public Float getTotalBuyingPrice() {
    return totalBuyingPrice;
  }

  public void setTotalBuyingPrice(Float totalBuyingPrice) {
    this.totalBuyingPrice = totalBuyingPrice;
  }


  public Expense totalSellingPrice(Float totalSellingPrice) {
    this.totalSellingPrice = totalSellingPrice;
    return this;
  }

  /**
   * Sum of all &#x60;selling_price&#x60; from expense lines
   * @return totalSellingPrice
   */
  @javax.annotation.Nullable
  public Float getTotalSellingPrice() {
    return totalSellingPrice;
  }

  public void setTotalSellingPrice(Float totalSellingPrice) {
    this.totalSellingPrice = totalSellingPrice;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Expense expense = (Expense) o;
    return Objects.equals(this.activityId, expense.activityId) &&
        Objects.equals(this.comment, expense.comment) &&
        Objects.equals(this.companyId, expense.companyId) &&
        Objects.equals(this.contactId, expense.contactId) &&
        Objects.equals(this.created, expense.created) &&
        Objects.equals(this.createdById, expense.createdById) &&
        Objects.equals(this.currencyId, expense.currencyId) &&
        Objects.equals(this.deleted, expense.deleted) &&
        Objects.equals(this.deliveryDate, expense.deliveryDate) &&
        Objects.equals(this.description, expense.description) &&
        Objects.equals(this.dueDate, expense.dueDate) &&
        Objects.equals(this.fileReference, expense.fileReference) &&
        Objects.equals(this.id, expense.id) &&
        Objects.equals(this.isImported, expense.isImported) &&
        Objects.equals(this.modified, expense.modified) &&
        Objects.equals(this.orderNumber, expense.orderNumber) &&
        Objects.equals(this.projectId, expense.projectId) &&
        Objects.equals(this.readsoftId, expense.readsoftId) &&
        Objects.equals(this.reference, expense.reference) &&
        Objects.equals(this.rogerId, expense.rogerId) &&
        Objects.equals(this.sentToEmail, expense.sentToEmail) &&
        Objects.equals(this.shortText, expense.shortText) &&
        Objects.equals(this.status, expense.status) &&
        Objects.equals(this.supplierInvoiceNumber, expense.supplierInvoiceNumber) &&
        Objects.equals(this.totalBuyingPrice, expense.totalBuyingPrice) &&
        Objects.equals(this.totalSellingPrice, expense.totalSellingPrice);
  }

  @Override
  public int hashCode() {
    return Objects.hash(activityId, comment, companyId, contactId, created, createdById, currencyId, deleted, deliveryDate, description, dueDate, fileReference, id, isImported, modified, orderNumber, projectId, readsoftId, reference, rogerId, sentToEmail, shortText, status, supplierInvoiceNumber, totalBuyingPrice, totalSellingPrice);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Expense {\n");
    sb.append("    activityId: ").append(toIndentedString(activityId)).append("\n");
    sb.append("    comment: ").append(toIndentedString(comment)).append("\n");
    sb.append("    companyId: ").append(toIndentedString(companyId)).append("\n");
    sb.append("    contactId: ").append(toIndentedString(contactId)).append("\n");
    sb.append("    created: ").append(toIndentedString(created)).append("\n");
    sb.append("    createdById: ").append(toIndentedString(createdById)).append("\n");
    sb.append("    currencyId: ").append(toIndentedString(currencyId)).append("\n");
    sb.append("    deleted: ").append(toIndentedString(deleted)).append("\n");
    sb.append("    deliveryDate: ").append(toIndentedString(deliveryDate)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    dueDate: ").append(toIndentedString(dueDate)).append("\n");
    sb.append("    fileReference: ").append(toIndentedString(fileReference)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    isImported: ").append(toIndentedString(isImported)).append("\n");
    sb.append("    modified: ").append(toIndentedString(modified)).append("\n");
    sb.append("    orderNumber: ").append(toIndentedString(orderNumber)).append("\n");
    sb.append("    projectId: ").append(toIndentedString(projectId)).append("\n");
    sb.append("    readsoftId: ").append(toIndentedString(readsoftId)).append("\n");
    sb.append("    reference: ").append(toIndentedString(reference)).append("\n");
    sb.append("    rogerId: ").append(toIndentedString(rogerId)).append("\n");
    sb.append("    sentToEmail: ").append(toIndentedString(sentToEmail)).append("\n");
    sb.append("    shortText: ").append(toIndentedString(shortText)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    supplierInvoiceNumber: ").append(toIndentedString(supplierInvoiceNumber)).append("\n");
    sb.append("    totalBuyingPrice: ").append(toIndentedString(totalBuyingPrice)).append("\n");
    sb.append("    totalSellingPrice: ").append(toIndentedString(totalSellingPrice)).append("\n");
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
    openapiFields.add("activity_id");
    openapiFields.add("comment");
    openapiFields.add("company_id");
    openapiFields.add("contact_id");
    openapiFields.add("created");
    openapiFields.add("created_by_id");
    openapiFields.add("currency_id");
    openapiFields.add("deleted");
    openapiFields.add("delivery_date");
    openapiFields.add("description");
    openapiFields.add("due_date");
    openapiFields.add("file_reference");
    openapiFields.add("id");
    openapiFields.add("is_imported");
    openapiFields.add("modified");
    openapiFields.add("order_number");
    openapiFields.add("project_id");
    openapiFields.add("readsoft_id");
    openapiFields.add("reference");
    openapiFields.add("roger_id");
    openapiFields.add("sent_to_email");
    openapiFields.add("short_text");
    openapiFields.add("status");
    openapiFields.add("supplier_invoice_number");
    openapiFields.add("total_buying_price");
    openapiFields.add("total_selling_price");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Expense
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Expense.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Expense is not found in the empty JSON string", Expense.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Expense.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Expense` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("activity_id") != null && !jsonObj.get("activity_id").isJsonNull()) && !jsonObj.get("activity_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `activity_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("activity_id").toString()));
      }
      if ((jsonObj.get("comment") != null && !jsonObj.get("comment").isJsonNull()) && !jsonObj.get("comment").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `comment` to be a primitive type in the JSON string but got `%s`", jsonObj.get("comment").toString()));
      }
      if ((jsonObj.get("company_id") != null && !jsonObj.get("company_id").isJsonNull()) && !jsonObj.get("company_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `company_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("company_id").toString()));
      }
      if ((jsonObj.get("contact_id") != null && !jsonObj.get("contact_id").isJsonNull()) && !jsonObj.get("contact_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `contact_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("contact_id").toString()));
      }
      if ((jsonObj.get("created") != null && !jsonObj.get("created").isJsonNull()) && !jsonObj.get("created").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `created` to be a primitive type in the JSON string but got `%s`", jsonObj.get("created").toString()));
      }
      if ((jsonObj.get("created_by_id") != null && !jsonObj.get("created_by_id").isJsonNull()) && !jsonObj.get("created_by_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `created_by_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("created_by_id").toString()));
      }
      if ((jsonObj.get("currency_id") != null && !jsonObj.get("currency_id").isJsonNull()) && !jsonObj.get("currency_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `currency_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("currency_id").toString()));
      }
      if ((jsonObj.get("deleted") != null && !jsonObj.get("deleted").isJsonNull()) && !jsonObj.get("deleted").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `deleted` to be a primitive type in the JSON string but got `%s`", jsonObj.get("deleted").toString()));
      }
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if ((jsonObj.get("file_reference") != null && !jsonObj.get("file_reference").isJsonNull()) && !jsonObj.get("file_reference").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `file_reference` to be a primitive type in the JSON string but got `%s`", jsonObj.get("file_reference").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("is_imported") != null && !jsonObj.get("is_imported").isJsonNull()) && !jsonObj.get("is_imported").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `is_imported` to be a primitive type in the JSON string but got `%s`", jsonObj.get("is_imported").toString()));
      }
      if ((jsonObj.get("modified") != null && !jsonObj.get("modified").isJsonNull()) && !jsonObj.get("modified").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `modified` to be a primitive type in the JSON string but got `%s`", jsonObj.get("modified").toString()));
      }
      if ((jsonObj.get("order_number") != null && !jsonObj.get("order_number").isJsonNull()) && !jsonObj.get("order_number").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `order_number` to be a primitive type in the JSON string but got `%s`", jsonObj.get("order_number").toString()));
      }
      if ((jsonObj.get("project_id") != null && !jsonObj.get("project_id").isJsonNull()) && !jsonObj.get("project_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `project_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("project_id").toString()));
      }
      if ((jsonObj.get("readsoft_id") != null && !jsonObj.get("readsoft_id").isJsonNull()) && !jsonObj.get("readsoft_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `readsoft_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("readsoft_id").toString()));
      }
      if ((jsonObj.get("reference") != null && !jsonObj.get("reference").isJsonNull()) && !jsonObj.get("reference").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `reference` to be a primitive type in the JSON string but got `%s`", jsonObj.get("reference").toString()));
      }
      if ((jsonObj.get("roger_id") != null && !jsonObj.get("roger_id").isJsonNull()) && !jsonObj.get("roger_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `roger_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("roger_id").toString()));
      }
      if ((jsonObj.get("sent_to_email") != null && !jsonObj.get("sent_to_email").isJsonNull()) && !jsonObj.get("sent_to_email").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `sent_to_email` to be a primitive type in the JSON string but got `%s`", jsonObj.get("sent_to_email").toString()));
      }
      if ((jsonObj.get("short_text") != null && !jsonObj.get("short_text").isJsonNull()) && !jsonObj.get("short_text").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `short_text` to be a primitive type in the JSON string but got `%s`", jsonObj.get("short_text").toString()));
      }
      if ((jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) && !jsonObj.get("status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("status").toString()));
      }
      if ((jsonObj.get("supplier_invoice_number") != null && !jsonObj.get("supplier_invoice_number").isJsonNull()) && !jsonObj.get("supplier_invoice_number").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `supplier_invoice_number` to be a primitive type in the JSON string but got `%s`", jsonObj.get("supplier_invoice_number").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Expense.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Expense' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Expense> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Expense.class));

       return (TypeAdapter<T>) new TypeAdapter<Expense>() {
           @Override
           public void write(JsonWriter out, Expense value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Expense read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Expense given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Expense
   * @throws IOException if the JSON string is invalid with respect to Expense
   */
  public static Expense fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Expense.class);
  }

  /**
   * Convert an instance of Expense to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

