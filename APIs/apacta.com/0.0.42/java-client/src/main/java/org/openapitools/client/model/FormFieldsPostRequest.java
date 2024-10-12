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
 * FormFieldsPostRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:16.415087-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class FormFieldsPostRequest {
  public static final String SERIALIZED_NAME_COMMENT = "comment";
  @SerializedName(SERIALIZED_NAME_COMMENT)
  private String comment;

  public static final String SERIALIZED_NAME_CONTENT_VALUE = "content_value";
  @SerializedName(SERIALIZED_NAME_CONTENT_VALUE)
  private String contentValue;

  public static final String SERIALIZED_NAME_FILE_ID = "file_id";
  @SerializedName(SERIALIZED_NAME_FILE_ID)
  private UUID fileId;

  public static final String SERIALIZED_NAME_FORM_FIELD_TYPE_ID = "form_field_type_id";
  @SerializedName(SERIALIZED_NAME_FORM_FIELD_TYPE_ID)
  private UUID formFieldTypeId;

  public static final String SERIALIZED_NAME_FORM_ID = "form_id";
  @SerializedName(SERIALIZED_NAME_FORM_ID)
  private UUID formId;

  public static final String SERIALIZED_NAME_FORM_TEMPLATE_FIELD_ID = "form_template_field_id";
  @SerializedName(SERIALIZED_NAME_FORM_TEMPLATE_FIELD_ID)
  private UUID formTemplateFieldId;

  public static final String SERIALIZED_NAME_PLACEMENT = "placement";
  @SerializedName(SERIALIZED_NAME_PLACEMENT)
  private Integer placement;

  public FormFieldsPostRequest() {
  }

  public FormFieldsPostRequest comment(String comment) {
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


  public FormFieldsPostRequest contentValue(String contentValue) {
    this.contentValue = contentValue;
    return this;
  }

  /**
   * Get contentValue
   * @return contentValue
   */
  @javax.annotation.Nullable
  public String getContentValue() {
    return contentValue;
  }

  public void setContentValue(String contentValue) {
    this.contentValue = contentValue;
  }


  public FormFieldsPostRequest fileId(UUID fileId) {
    this.fileId = fileId;
    return this;
  }

  /**
   * Get fileId
   * @return fileId
   */
  @javax.annotation.Nullable
  public UUID getFileId() {
    return fileId;
  }

  public void setFileId(UUID fileId) {
    this.fileId = fileId;
  }


  public FormFieldsPostRequest formFieldTypeId(UUID formFieldTypeId) {
    this.formFieldTypeId = formFieldTypeId;
    return this;
  }

  /**
   * Get formFieldTypeId
   * @return formFieldTypeId
   */
  @javax.annotation.Nullable
  public UUID getFormFieldTypeId() {
    return formFieldTypeId;
  }

  public void setFormFieldTypeId(UUID formFieldTypeId) {
    this.formFieldTypeId = formFieldTypeId;
  }


  public FormFieldsPostRequest formId(UUID formId) {
    this.formId = formId;
    return this;
  }

  /**
   * Get formId
   * @return formId
   */
  @javax.annotation.Nullable
  public UUID getFormId() {
    return formId;
  }

  public void setFormId(UUID formId) {
    this.formId = formId;
  }


  public FormFieldsPostRequest formTemplateFieldId(UUID formTemplateFieldId) {
    this.formTemplateFieldId = formTemplateFieldId;
    return this;
  }

  /**
   * Get formTemplateFieldId
   * @return formTemplateFieldId
   */
  @javax.annotation.Nullable
  public UUID getFormTemplateFieldId() {
    return formTemplateFieldId;
  }

  public void setFormTemplateFieldId(UUID formTemplateFieldId) {
    this.formTemplateFieldId = formTemplateFieldId;
  }


  public FormFieldsPostRequest placement(Integer placement) {
    this.placement = placement;
    return this;
  }

  /**
   * Get placement
   * @return placement
   */
  @javax.annotation.Nullable
  public Integer getPlacement() {
    return placement;
  }

  public void setPlacement(Integer placement) {
    this.placement = placement;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    FormFieldsPostRequest formFieldsPostRequest = (FormFieldsPostRequest) o;
    return Objects.equals(this.comment, formFieldsPostRequest.comment) &&
        Objects.equals(this.contentValue, formFieldsPostRequest.contentValue) &&
        Objects.equals(this.fileId, formFieldsPostRequest.fileId) &&
        Objects.equals(this.formFieldTypeId, formFieldsPostRequest.formFieldTypeId) &&
        Objects.equals(this.formId, formFieldsPostRequest.formId) &&
        Objects.equals(this.formTemplateFieldId, formFieldsPostRequest.formTemplateFieldId) &&
        Objects.equals(this.placement, formFieldsPostRequest.placement);
  }

  @Override
  public int hashCode() {
    return Objects.hash(comment, contentValue, fileId, formFieldTypeId, formId, formTemplateFieldId, placement);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class FormFieldsPostRequest {\n");
    sb.append("    comment: ").append(toIndentedString(comment)).append("\n");
    sb.append("    contentValue: ").append(toIndentedString(contentValue)).append("\n");
    sb.append("    fileId: ").append(toIndentedString(fileId)).append("\n");
    sb.append("    formFieldTypeId: ").append(toIndentedString(formFieldTypeId)).append("\n");
    sb.append("    formId: ").append(toIndentedString(formId)).append("\n");
    sb.append("    formTemplateFieldId: ").append(toIndentedString(formTemplateFieldId)).append("\n");
    sb.append("    placement: ").append(toIndentedString(placement)).append("\n");
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
    openapiFields.add("comment");
    openapiFields.add("content_value");
    openapiFields.add("file_id");
    openapiFields.add("form_field_type_id");
    openapiFields.add("form_id");
    openapiFields.add("form_template_field_id");
    openapiFields.add("placement");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to FormFieldsPostRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!FormFieldsPostRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in FormFieldsPostRequest is not found in the empty JSON string", FormFieldsPostRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!FormFieldsPostRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `FormFieldsPostRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("comment") != null && !jsonObj.get("comment").isJsonNull()) && !jsonObj.get("comment").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `comment` to be a primitive type in the JSON string but got `%s`", jsonObj.get("comment").toString()));
      }
      if ((jsonObj.get("content_value") != null && !jsonObj.get("content_value").isJsonNull()) && !jsonObj.get("content_value").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `content_value` to be a primitive type in the JSON string but got `%s`", jsonObj.get("content_value").toString()));
      }
      if ((jsonObj.get("file_id") != null && !jsonObj.get("file_id").isJsonNull()) && !jsonObj.get("file_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `file_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("file_id").toString()));
      }
      if ((jsonObj.get("form_field_type_id") != null && !jsonObj.get("form_field_type_id").isJsonNull()) && !jsonObj.get("form_field_type_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `form_field_type_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("form_field_type_id").toString()));
      }
      if ((jsonObj.get("form_id") != null && !jsonObj.get("form_id").isJsonNull()) && !jsonObj.get("form_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `form_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("form_id").toString()));
      }
      if ((jsonObj.get("form_template_field_id") != null && !jsonObj.get("form_template_field_id").isJsonNull()) && !jsonObj.get("form_template_field_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `form_template_field_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("form_template_field_id").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!FormFieldsPostRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'FormFieldsPostRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<FormFieldsPostRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(FormFieldsPostRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<FormFieldsPostRequest>() {
           @Override
           public void write(JsonWriter out, FormFieldsPostRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public FormFieldsPostRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of FormFieldsPostRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of FormFieldsPostRequest
   * @throws IOException if the JSON string is invalid with respect to FormFieldsPostRequest
   */
  public static FormFieldsPostRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, FormFieldsPostRequest.class);
  }

  /**
   * Convert an instance of FormFieldsPostRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

