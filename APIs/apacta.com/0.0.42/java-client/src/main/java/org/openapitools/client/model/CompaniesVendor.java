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
import java.util.Arrays;
import java.util.UUID;
import org.openapitools.client.model.Vendor;

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
 * CompaniesVendor
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:16.415087-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CompaniesVendor {
  public static final String SERIALIZED_NAME_COMPANY_ID = "company_id";
  @SerializedName(SERIALIZED_NAME_COMPANY_ID)
  private UUID companyId;

  public static final String SERIALIZED_NAME_COMPANY_PASSWORD = "company_password";
  @SerializedName(SERIALIZED_NAME_COMPANY_PASSWORD)
  private String companyPassword;

  public static final String SERIALIZED_NAME_CREATED = "created";
  @SerializedName(SERIALIZED_NAME_CREATED)
  private String created;

  public static final String SERIALIZED_NAME_CREATED_BY_ID = "created_by_id";
  @SerializedName(SERIALIZED_NAME_CREATED_BY_ID)
  private UUID createdById;

  public static final String SERIALIZED_NAME_DELETED = "deleted";
  @SerializedName(SERIALIZED_NAME_DELETED)
  private String deleted;

  public static final String SERIALIZED_NAME_DELIVERY_PRICE = "delivery_price";
  @SerializedName(SERIALIZED_NAME_DELIVERY_PRICE)
  private Float deliveryPrice;

  public static final String SERIALIZED_NAME_FREE_DELIVERY_PRICE = "free_delivery_price";
  @SerializedName(SERIALIZED_NAME_FREE_DELIVERY_PRICE)
  private Float freeDeliveryPrice;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private UUID id;

  public static final String SERIALIZED_NAME_IS_ACTIVE = "is_active";
  @SerializedName(SERIALIZED_NAME_IS_ACTIVE)
  private Boolean isActive;

  public static final String SERIALIZED_NAME_MODIFIED = "modified";
  @SerializedName(SERIALIZED_NAME_MODIFIED)
  private String modified;

  public static final String SERIALIZED_NAME_MODIFIED_BY_ID = "modified_by_id";
  @SerializedName(SERIALIZED_NAME_MODIFIED_BY_ID)
  private UUID modifiedById;

  public static final String SERIALIZED_NAME_RECEIVE_AUTOMATIC_PRICE_FILES = "receive_automatic_price_files";
  @SerializedName(SERIALIZED_NAME_RECEIVE_AUTOMATIC_PRICE_FILES)
  private Boolean receiveAutomaticPriceFiles;

  public static final String SERIALIZED_NAME_RECEIVE_INVOICE_MAILS = "receive_invoice_mails";
  @SerializedName(SERIALIZED_NAME_RECEIVE_INVOICE_MAILS)
  private Boolean receiveInvoiceMails;

  public static final String SERIALIZED_NAME_REVIEWED = "reviewed";
  @SerializedName(SERIALIZED_NAME_REVIEWED)
  private Boolean reviewed;

  public static final String SERIALIZED_NAME_USE_PRICE_FILES = "use_price_files";
  @SerializedName(SERIALIZED_NAME_USE_PRICE_FILES)
  private Boolean usePriceFiles;

  public static final String SERIALIZED_NAME_USERNAME = "username";
  @SerializedName(SERIALIZED_NAME_USERNAME)
  private String username;

  public static final String SERIALIZED_NAME_VENDOR = "vendor";
  @SerializedName(SERIALIZED_NAME_VENDOR)
  private Vendor vendor;

  public static final String SERIALIZED_NAME_VENDOR_ACCOUNT_REFERENCE = "vendor_account_reference";
  @SerializedName(SERIALIZED_NAME_VENDOR_ACCOUNT_REFERENCE)
  private String vendorAccountReference;

  public static final String SERIALIZED_NAME_VENDOR_DEPARTMENT_ID = "vendor_department_id";
  @SerializedName(SERIALIZED_NAME_VENDOR_DEPARTMENT_ID)
  private UUID vendorDepartmentId;

  public static final String SERIALIZED_NAME_VENDOR_EMAIL = "vendor_email";
  @SerializedName(SERIALIZED_NAME_VENDOR_EMAIL)
  private String vendorEmail;

  public static final String SERIALIZED_NAME_VENDOR_ID = "vendor_id";
  @SerializedName(SERIALIZED_NAME_VENDOR_ID)
  private UUID vendorId;

  public static final String SERIALIZED_NAME_VENDOR_NAME = "vendor_name";
  @SerializedName(SERIALIZED_NAME_VENDOR_NAME)
  private String vendorName;

  public CompaniesVendor() {
  }

  public CompaniesVendor(
     String created, 
     UUID createdById, 
     String deleted, 
     String modified, 
     UUID modifiedById
  ) {
    this();
    this.created = created;
    this.createdById = createdById;
    this.deleted = deleted;
    this.modified = modified;
    this.modifiedById = modifiedById;
  }

  public CompaniesVendor companyId(UUID companyId) {
    this.companyId = companyId;
    return this;
  }

  /**
   * Get companyId
   * @return companyId
   */
  @javax.annotation.Nullable
  public UUID getCompanyId() {
    return companyId;
  }

  public void setCompanyId(UUID companyId) {
    this.companyId = companyId;
  }


  public CompaniesVendor companyPassword(String companyPassword) {
    this.companyPassword = companyPassword;
    return this;
  }

  /**
   * Get companyPassword
   * @return companyPassword
   */
  @javax.annotation.Nullable
  public String getCompanyPassword() {
    return companyPassword;
  }

  public void setCompanyPassword(String companyPassword) {
    this.companyPassword = companyPassword;
  }


  /**
   * Get created
   * @return created
   */
  @javax.annotation.Nullable
  public String getCreated() {
    return created;
  }



  /**
   * Get createdById
   * @return createdById
   */
  @javax.annotation.Nullable
  public UUID getCreatedById() {
    return createdById;
  }



  /**
   * Only present if it&#39;s a deleted object
   * @return deleted
   */
  @javax.annotation.Nullable
  public String getDeleted() {
    return deleted;
  }



  public CompaniesVendor deliveryPrice(Float deliveryPrice) {
    this.deliveryPrice = deliveryPrice;
    return this;
  }

  /**
   * Get deliveryPrice
   * @return deliveryPrice
   */
  @javax.annotation.Nullable
  public Float getDeliveryPrice() {
    return deliveryPrice;
  }

  public void setDeliveryPrice(Float deliveryPrice) {
    this.deliveryPrice = deliveryPrice;
  }


  public CompaniesVendor freeDeliveryPrice(Float freeDeliveryPrice) {
    this.freeDeliveryPrice = freeDeliveryPrice;
    return this;
  }

  /**
   * Get freeDeliveryPrice
   * @return freeDeliveryPrice
   */
  @javax.annotation.Nullable
  public Float getFreeDeliveryPrice() {
    return freeDeliveryPrice;
  }

  public void setFreeDeliveryPrice(Float freeDeliveryPrice) {
    this.freeDeliveryPrice = freeDeliveryPrice;
  }


  public CompaniesVendor id(UUID id) {
    this.id = id;
    return this;
  }

  /**
   * Get id
   * @return id
   */
  @javax.annotation.Nullable
  public UUID getId() {
    return id;
  }

  public void setId(UUID id) {
    this.id = id;
  }


  public CompaniesVendor isActive(Boolean isActive) {
    this.isActive = isActive;
    return this;
  }

  /**
   * Get isActive
   * @return isActive
   */
  @javax.annotation.Nullable
  public Boolean getIsActive() {
    return isActive;
  }

  public void setIsActive(Boolean isActive) {
    this.isActive = isActive;
  }


  /**
   * Get modified
   * @return modified
   */
  @javax.annotation.Nullable
  public String getModified() {
    return modified;
  }



  /**
   * Get modifiedById
   * @return modifiedById
   */
  @javax.annotation.Nullable
  public UUID getModifiedById() {
    return modifiedById;
  }



  public CompaniesVendor receiveAutomaticPriceFiles(Boolean receiveAutomaticPriceFiles) {
    this.receiveAutomaticPriceFiles = receiveAutomaticPriceFiles;
    return this;
  }

  /**
   * Get receiveAutomaticPriceFiles
   * @return receiveAutomaticPriceFiles
   */
  @javax.annotation.Nullable
  public Boolean getReceiveAutomaticPriceFiles() {
    return receiveAutomaticPriceFiles;
  }

  public void setReceiveAutomaticPriceFiles(Boolean receiveAutomaticPriceFiles) {
    this.receiveAutomaticPriceFiles = receiveAutomaticPriceFiles;
  }


  public CompaniesVendor receiveInvoiceMails(Boolean receiveInvoiceMails) {
    this.receiveInvoiceMails = receiveInvoiceMails;
    return this;
  }

  /**
   * Get receiveInvoiceMails
   * @return receiveInvoiceMails
   */
  @javax.annotation.Nullable
  public Boolean getReceiveInvoiceMails() {
    return receiveInvoiceMails;
  }

  public void setReceiveInvoiceMails(Boolean receiveInvoiceMails) {
    this.receiveInvoiceMails = receiveInvoiceMails;
  }


  public CompaniesVendor reviewed(Boolean reviewed) {
    this.reviewed = reviewed;
    return this;
  }

  /**
   * Get reviewed
   * @return reviewed
   */
  @javax.annotation.Nullable
  public Boolean getReviewed() {
    return reviewed;
  }

  public void setReviewed(Boolean reviewed) {
    this.reviewed = reviewed;
  }


  public CompaniesVendor usePriceFiles(Boolean usePriceFiles) {
    this.usePriceFiles = usePriceFiles;
    return this;
  }

  /**
   * Get usePriceFiles
   * @return usePriceFiles
   */
  @javax.annotation.Nullable
  public Boolean getUsePriceFiles() {
    return usePriceFiles;
  }

  public void setUsePriceFiles(Boolean usePriceFiles) {
    this.usePriceFiles = usePriceFiles;
  }


  public CompaniesVendor username(String username) {
    this.username = username;
    return this;
  }

  /**
   * Get username
   * @return username
   */
  @javax.annotation.Nullable
  public String getUsername() {
    return username;
  }

  public void setUsername(String username) {
    this.username = username;
  }


  public CompaniesVendor vendor(Vendor vendor) {
    this.vendor = vendor;
    return this;
  }

  /**
   * Get vendor
   * @return vendor
   */
  @javax.annotation.Nullable
  public Vendor getVendor() {
    return vendor;
  }

  public void setVendor(Vendor vendor) {
    this.vendor = vendor;
  }


  public CompaniesVendor vendorAccountReference(String vendorAccountReference) {
    this.vendorAccountReference = vendorAccountReference;
    return this;
  }

  /**
   * Get vendorAccountReference
   * @return vendorAccountReference
   */
  @javax.annotation.Nullable
  public String getVendorAccountReference() {
    return vendorAccountReference;
  }

  public void setVendorAccountReference(String vendorAccountReference) {
    this.vendorAccountReference = vendorAccountReference;
  }


  public CompaniesVendor vendorDepartmentId(UUID vendorDepartmentId) {
    this.vendorDepartmentId = vendorDepartmentId;
    return this;
  }

  /**
   * Get vendorDepartmentId
   * @return vendorDepartmentId
   */
  @javax.annotation.Nullable
  public UUID getVendorDepartmentId() {
    return vendorDepartmentId;
  }

  public void setVendorDepartmentId(UUID vendorDepartmentId) {
    this.vendorDepartmentId = vendorDepartmentId;
  }


  public CompaniesVendor vendorEmail(String vendorEmail) {
    this.vendorEmail = vendorEmail;
    return this;
  }

  /**
   * Get vendorEmail
   * @return vendorEmail
   */
  @javax.annotation.Nullable
  public String getVendorEmail() {
    return vendorEmail;
  }

  public void setVendorEmail(String vendorEmail) {
    this.vendorEmail = vendorEmail;
  }


  public CompaniesVendor vendorId(UUID vendorId) {
    this.vendorId = vendorId;
    return this;
  }

  /**
   * Get vendorId
   * @return vendorId
   */
  @javax.annotation.Nullable
  public UUID getVendorId() {
    return vendorId;
  }

  public void setVendorId(UUID vendorId) {
    this.vendorId = vendorId;
  }


  public CompaniesVendor vendorName(String vendorName) {
    this.vendorName = vendorName;
    return this;
  }

  /**
   * Get vendorName
   * @return vendorName
   */
  @javax.annotation.Nullable
  public String getVendorName() {
    return vendorName;
  }

  public void setVendorName(String vendorName) {
    this.vendorName = vendorName;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CompaniesVendor companiesVendor = (CompaniesVendor) o;
    return Objects.equals(this.companyId, companiesVendor.companyId) &&
        Objects.equals(this.companyPassword, companiesVendor.companyPassword) &&
        Objects.equals(this.created, companiesVendor.created) &&
        Objects.equals(this.createdById, companiesVendor.createdById) &&
        Objects.equals(this.deleted, companiesVendor.deleted) &&
        Objects.equals(this.deliveryPrice, companiesVendor.deliveryPrice) &&
        Objects.equals(this.freeDeliveryPrice, companiesVendor.freeDeliveryPrice) &&
        Objects.equals(this.id, companiesVendor.id) &&
        Objects.equals(this.isActive, companiesVendor.isActive) &&
        Objects.equals(this.modified, companiesVendor.modified) &&
        Objects.equals(this.modifiedById, companiesVendor.modifiedById) &&
        Objects.equals(this.receiveAutomaticPriceFiles, companiesVendor.receiveAutomaticPriceFiles) &&
        Objects.equals(this.receiveInvoiceMails, companiesVendor.receiveInvoiceMails) &&
        Objects.equals(this.reviewed, companiesVendor.reviewed) &&
        Objects.equals(this.usePriceFiles, companiesVendor.usePriceFiles) &&
        Objects.equals(this.username, companiesVendor.username) &&
        Objects.equals(this.vendor, companiesVendor.vendor) &&
        Objects.equals(this.vendorAccountReference, companiesVendor.vendorAccountReference) &&
        Objects.equals(this.vendorDepartmentId, companiesVendor.vendorDepartmentId) &&
        Objects.equals(this.vendorEmail, companiesVendor.vendorEmail) &&
        Objects.equals(this.vendorId, companiesVendor.vendorId) &&
        Objects.equals(this.vendorName, companiesVendor.vendorName);
  }

  @Override
  public int hashCode() {
    return Objects.hash(companyId, companyPassword, created, createdById, deleted, deliveryPrice, freeDeliveryPrice, id, isActive, modified, modifiedById, receiveAutomaticPriceFiles, receiveInvoiceMails, reviewed, usePriceFiles, username, vendor, vendorAccountReference, vendorDepartmentId, vendorEmail, vendorId, vendorName);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CompaniesVendor {\n");
    sb.append("    companyId: ").append(toIndentedString(companyId)).append("\n");
    sb.append("    companyPassword: ").append(toIndentedString(companyPassword)).append("\n");
    sb.append("    created: ").append(toIndentedString(created)).append("\n");
    sb.append("    createdById: ").append(toIndentedString(createdById)).append("\n");
    sb.append("    deleted: ").append(toIndentedString(deleted)).append("\n");
    sb.append("    deliveryPrice: ").append(toIndentedString(deliveryPrice)).append("\n");
    sb.append("    freeDeliveryPrice: ").append(toIndentedString(freeDeliveryPrice)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    isActive: ").append(toIndentedString(isActive)).append("\n");
    sb.append("    modified: ").append(toIndentedString(modified)).append("\n");
    sb.append("    modifiedById: ").append(toIndentedString(modifiedById)).append("\n");
    sb.append("    receiveAutomaticPriceFiles: ").append(toIndentedString(receiveAutomaticPriceFiles)).append("\n");
    sb.append("    receiveInvoiceMails: ").append(toIndentedString(receiveInvoiceMails)).append("\n");
    sb.append("    reviewed: ").append(toIndentedString(reviewed)).append("\n");
    sb.append("    usePriceFiles: ").append(toIndentedString(usePriceFiles)).append("\n");
    sb.append("    username: ").append(toIndentedString(username)).append("\n");
    sb.append("    vendor: ").append(toIndentedString(vendor)).append("\n");
    sb.append("    vendorAccountReference: ").append(toIndentedString(vendorAccountReference)).append("\n");
    sb.append("    vendorDepartmentId: ").append(toIndentedString(vendorDepartmentId)).append("\n");
    sb.append("    vendorEmail: ").append(toIndentedString(vendorEmail)).append("\n");
    sb.append("    vendorId: ").append(toIndentedString(vendorId)).append("\n");
    sb.append("    vendorName: ").append(toIndentedString(vendorName)).append("\n");
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
    openapiFields.add("company_id");
    openapiFields.add("company_password");
    openapiFields.add("created");
    openapiFields.add("created_by_id");
    openapiFields.add("deleted");
    openapiFields.add("delivery_price");
    openapiFields.add("free_delivery_price");
    openapiFields.add("id");
    openapiFields.add("is_active");
    openapiFields.add("modified");
    openapiFields.add("modified_by_id");
    openapiFields.add("receive_automatic_price_files");
    openapiFields.add("receive_invoice_mails");
    openapiFields.add("reviewed");
    openapiFields.add("use_price_files");
    openapiFields.add("username");
    openapiFields.add("vendor");
    openapiFields.add("vendor_account_reference");
    openapiFields.add("vendor_department_id");
    openapiFields.add("vendor_email");
    openapiFields.add("vendor_id");
    openapiFields.add("vendor_name");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CompaniesVendor
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CompaniesVendor.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CompaniesVendor is not found in the empty JSON string", CompaniesVendor.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CompaniesVendor.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CompaniesVendor` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("company_id") != null && !jsonObj.get("company_id").isJsonNull()) && !jsonObj.get("company_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `company_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("company_id").toString()));
      }
      if ((jsonObj.get("company_password") != null && !jsonObj.get("company_password").isJsonNull()) && !jsonObj.get("company_password").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `company_password` to be a primitive type in the JSON string but got `%s`", jsonObj.get("company_password").toString()));
      }
      if ((jsonObj.get("created") != null && !jsonObj.get("created").isJsonNull()) && !jsonObj.get("created").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `created` to be a primitive type in the JSON string but got `%s`", jsonObj.get("created").toString()));
      }
      if ((jsonObj.get("created_by_id") != null && !jsonObj.get("created_by_id").isJsonNull()) && !jsonObj.get("created_by_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `created_by_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("created_by_id").toString()));
      }
      if ((jsonObj.get("deleted") != null && !jsonObj.get("deleted").isJsonNull()) && !jsonObj.get("deleted").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `deleted` to be a primitive type in the JSON string but got `%s`", jsonObj.get("deleted").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("modified") != null && !jsonObj.get("modified").isJsonNull()) && !jsonObj.get("modified").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `modified` to be a primitive type in the JSON string but got `%s`", jsonObj.get("modified").toString()));
      }
      if ((jsonObj.get("modified_by_id") != null && !jsonObj.get("modified_by_id").isJsonNull()) && !jsonObj.get("modified_by_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `modified_by_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("modified_by_id").toString()));
      }
      if ((jsonObj.get("username") != null && !jsonObj.get("username").isJsonNull()) && !jsonObj.get("username").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `username` to be a primitive type in the JSON string but got `%s`", jsonObj.get("username").toString()));
      }
      // validate the optional field `vendor`
      if (jsonObj.get("vendor") != null && !jsonObj.get("vendor").isJsonNull()) {
        Vendor.validateJsonElement(jsonObj.get("vendor"));
      }
      if ((jsonObj.get("vendor_account_reference") != null && !jsonObj.get("vendor_account_reference").isJsonNull()) && !jsonObj.get("vendor_account_reference").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `vendor_account_reference` to be a primitive type in the JSON string but got `%s`", jsonObj.get("vendor_account_reference").toString()));
      }
      if ((jsonObj.get("vendor_department_id") != null && !jsonObj.get("vendor_department_id").isJsonNull()) && !jsonObj.get("vendor_department_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `vendor_department_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("vendor_department_id").toString()));
      }
      if ((jsonObj.get("vendor_email") != null && !jsonObj.get("vendor_email").isJsonNull()) && !jsonObj.get("vendor_email").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `vendor_email` to be a primitive type in the JSON string but got `%s`", jsonObj.get("vendor_email").toString()));
      }
      if ((jsonObj.get("vendor_id") != null && !jsonObj.get("vendor_id").isJsonNull()) && !jsonObj.get("vendor_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `vendor_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("vendor_id").toString()));
      }
      if ((jsonObj.get("vendor_name") != null && !jsonObj.get("vendor_name").isJsonNull()) && !jsonObj.get("vendor_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `vendor_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("vendor_name").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CompaniesVendor.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CompaniesVendor' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CompaniesVendor> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CompaniesVendor.class));

       return (TypeAdapter<T>) new TypeAdapter<CompaniesVendor>() {
           @Override
           public void write(JsonWriter out, CompaniesVendor value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CompaniesVendor read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CompaniesVendor given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CompaniesVendor
   * @throws IOException if the JSON string is invalid with respect to CompaniesVendor
   */
  public static CompaniesVendor fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CompaniesVendor.class);
  }

  /**
   * Convert an instance of CompaniesVendor to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

