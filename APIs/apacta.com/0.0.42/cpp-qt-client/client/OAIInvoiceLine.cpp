/**
 * Apacta
 * API for a tool to craftsmen used to register working hours, material usage and quality assurance. # Endpoint The endpoint `https://app.apacta.com/api/v1` should be used to communicate with the API. API access is only allowed with SSL encrypted connection (https). # Authentication URL query authentication with an API key is used, so appending `?api_key={api_key}` to the URL where `{api_key}` is found within Apacta settings is used for authentication # Pagination If the endpoint returns a `pagination` object it means the endpoint supports pagination - currently it's only possible to change pages with `?page={page_number}` but implementing custom page sizes are on the road map.   # Search/filter Is experimental but implemented in some cases - see the individual endpoints' docs for further explanation. # Ordering Is currently experimental, but on some endpoints it's implemented on URL querys so eg. to order Invoices by `invoice_number` appending `?sort=Invoices.invoice_number&direction=desc` would sort the list descending by the value of `invoice_number`. # Associations Is currently implemented on an experimental basis where you can append eg. `?include=Contacts,Projects`  to the `/api/v1/invoices/` endpoint to embed `Contact` and `Project` objects directly. # Project Files Currently project files can be retrieved from two endpoints. `/projects/{project_id}/files` handles files uploaded from wall posts or forms. `/projects/{project_id}/project_files` allows uploading and showing files, not belonging to specific form or wall post. # Errors/Exceptions ## 422 (Validation) Write something about how the `errors` object contains keys with the properties that failes validation like: ```   {       \"success\": false,       \"data\": {           \"code\": 422,           \"url\": \"/api/v1/contacts?api_key=5523be3b-30ef-425d-8203-04df7caaa93a\",           \"message\": \"A validation error occurred\",           \"errorCount\": 1,           \"errors\": {               \"contact_types\": [ ## Property name that failed validation                   \"Contacts must have at least one contact type\" ## Message with further explanation               ]           }       }   } ``` ## Code examples Running examples of how to retrieve the 5 most recent forms registered and embed the details of the User that made the form, and eventual products contained in the form ### Swift ``` ``` ### Java #### OkHttp ```   OkHttpClient client = new OkHttpClient();    Request request = new Request.Builder()     .url(\"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\")     .get()     .addHeader(\"x-auth-token\", \"{INSERT_YOUR_TOKEN}\")     .addHeader(\"accept\", \"application/json\")     .build();    Response response = client.newCall(request).execute(); ``` #### Unirest ```   HttpResponse<String> response = Unirest.get(\"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\")     .header(\"x-auth-token\", \"{INSERT_YOUR_TOKEN}\")     .header(\"accept\", \"application/json\")     .asString(); ``` ### Javascript #### Native ```   var data = null;    var xhr = new XMLHttpRequest();    xhr.addEventListener(\"readystatechange\", function () {     if (this.readyState === 4) {       console.log(this.responseText);     }   });    xhr.open(\"GET\", \"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\");   xhr.setRequestHeader(\"x-auth-token\", \"{INSERT_YOUR_TOKEN}\");   xhr.setRequestHeader(\"accept\", \"application/json\");    xhr.send(data); ``` #### jQuery ```   var settings = {     \"async\": true,     \"crossDomain\": true,     \"url\": \"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\",     \"method\": \"GET\",     \"headers\": {       \"x-auth-token\": \"{INSERT_YOUR_TOKEN}\",       \"accept\": \"application/json\",     }   }    $.ajax(settings).done(function (response) {     console.log(response);   }); ``` #### NodeJS (Request) ```   var request = require(\"request\");    var options = { method: 'GET',     url: 'https://app.apacta.com/api/v1/forms',     qs:      { extended: 'true',        sort: 'Forms.created',        direction: 'DESC',        include: 'Products,CreatedBy',        limit: '5' },     headers:      { accept: 'application/json',        'x-auth-token': '{INSERT_YOUR_TOKEN}' } };    request(options, function (error, response, body) {     if (error) throw new Error(error);      console.log(body);   });  ``` ### Python 3 ```   import http.client    conn = http.client.HTTPSConnection(\"app.apacta.com\")    payload = \"\"    headers = {       'x-auth-token': \"{INSERT_YOUR_TOKEN}\",       'accept': \"application/json\",       }    conn.request(\"GET\", \"/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\", payload, headers)    res = conn.getresponse()   data = res.read()    print(data.decode(\"utf-8\")) ``` ### C# #### RestSharp ```   var client = new RestClient(\"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\");   var request = new RestRequest(Method.GET);   request.AddHeader(\"accept\", \"application/json\");   request.AddHeader(\"x-auth-token\", \"{INSERT_YOUR_TOKEN}\");   IRestResponse response = client.Execute(request); ``` ### Ruby ```   require 'uri'   require 'net/http'    url = URI(\"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\")    http = Net::HTTP.new(url.host, url.port)   http.use_ssl = true   http.verify_mode = OpenSSL::SSL::VERIFY_NONE    request = Net::HTTP::Get.new(url)   request[\"x-auth-token\"] = '{INSERT_YOUR_TOKEN}'   request[\"accept\"] = 'application/json'    response = http.request(request)   puts response.read_body ``` ### PHP (HttpRequest) ```   <?php    $request = new HttpRequest();   $request->setUrl('https://app.apacta.com/api/v1/forms');   $request->setMethod(HTTP_METH_GET);    $request->setQueryData(array(     'extended' => 'true',     'sort' => 'Forms.created',     'direction' => 'DESC',     'include' => 'Products,CreatedBy',     'limit' => '5'   ));    $request->setHeaders(array(     'accept' => 'application/json',     'x-auth-token' => '{INSERT_YOUR_TOKEN}'   ));    try {     $response = $request->send();      echo $response->getBody();   } catch (HttpException $ex) {     echo $ex;   } ``` ### Shell (cURL) ```    $ curl --request GET --url 'https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5' --header 'accept: application/json' --header 'x-auth-token: {INSERT_YOUR_TOKEN}'  ```
 *
 * The version of the OpenAPI document: 0.0.42
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIInvoiceLine.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIInvoiceLine::OAIInvoiceLine(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIInvoiceLine::OAIInvoiceLine() {
    this->initializeModel();
}

OAIInvoiceLine::~OAIInvoiceLine() {}

void OAIInvoiceLine::initializeModel() {

    m_created_isSet = false;
    m_created_isValid = false;

    m_created_by_id_isSet = false;
    m_created_by_id_isValid = false;

    m_deleted_isSet = false;
    m_deleted_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_discount_percent_isSet = false;
    m_discount_percent_isValid = false;

    m_discount_text_isSet = false;
    m_discount_text_isValid = false;

    m_ean_product_id_isSet = false;
    m_ean_product_id_isValid = false;

    m_form_id_isSet = false;
    m_form_id_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_invoice_id_isSet = false;
    m_invoice_id_isValid = false;

    m_material_id_isSet = false;
    m_material_id_isValid = false;

    m_modified_isSet = false;
    m_modified_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_parent_id_isSet = false;
    m_parent_id_isValid = false;

    m_product_bundle_id_isSet = false;
    m_product_bundle_id_isValid = false;

    m_product_id_isSet = false;
    m_product_id_isValid = false;

    m_quantity_isSet = false;
    m_quantity_isValid = false;

    m_selling_price_isSet = false;
    m_selling_price_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;

    m_user_id_isSet = false;
    m_user_id_isValid = false;
}

void OAIInvoiceLine::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIInvoiceLine::fromJsonObject(QJsonObject json) {

    m_created_isValid = ::OpenAPI::fromJsonValue(m_created, json[QString("created")]);
    m_created_isSet = !json[QString("created")].isNull() && m_created_isValid;

    m_created_by_id_isValid = ::OpenAPI::fromJsonValue(m_created_by_id, json[QString("created_by_id")]);
    m_created_by_id_isSet = !json[QString("created_by_id")].isNull() && m_created_by_id_isValid;

    m_deleted_isValid = ::OpenAPI::fromJsonValue(m_deleted, json[QString("deleted")]);
    m_deleted_isSet = !json[QString("deleted")].isNull() && m_deleted_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_discount_percent_isValid = ::OpenAPI::fromJsonValue(m_discount_percent, json[QString("discount_percent")]);
    m_discount_percent_isSet = !json[QString("discount_percent")].isNull() && m_discount_percent_isValid;

    m_discount_text_isValid = ::OpenAPI::fromJsonValue(m_discount_text, json[QString("discount_text")]);
    m_discount_text_isSet = !json[QString("discount_text")].isNull() && m_discount_text_isValid;

    m_ean_product_id_isValid = ::OpenAPI::fromJsonValue(m_ean_product_id, json[QString("ean_product_id")]);
    m_ean_product_id_isSet = !json[QString("ean_product_id")].isNull() && m_ean_product_id_isValid;

    m_form_id_isValid = ::OpenAPI::fromJsonValue(m_form_id, json[QString("form_id")]);
    m_form_id_isSet = !json[QString("form_id")].isNull() && m_form_id_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_invoice_id_isValid = ::OpenAPI::fromJsonValue(m_invoice_id, json[QString("invoice_id")]);
    m_invoice_id_isSet = !json[QString("invoice_id")].isNull() && m_invoice_id_isValid;

    m_material_id_isValid = ::OpenAPI::fromJsonValue(m_material_id, json[QString("material_id")]);
    m_material_id_isSet = !json[QString("material_id")].isNull() && m_material_id_isValid;

    m_modified_isValid = ::OpenAPI::fromJsonValue(m_modified, json[QString("modified")]);
    m_modified_isSet = !json[QString("modified")].isNull() && m_modified_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_parent_id_isValid = ::OpenAPI::fromJsonValue(m_parent_id, json[QString("parent_id")]);
    m_parent_id_isSet = !json[QString("parent_id")].isNull() && m_parent_id_isValid;

    m_product_bundle_id_isValid = ::OpenAPI::fromJsonValue(m_product_bundle_id, json[QString("product_bundle_id")]);
    m_product_bundle_id_isSet = !json[QString("product_bundle_id")].isNull() && m_product_bundle_id_isValid;

    m_product_id_isValid = ::OpenAPI::fromJsonValue(m_product_id, json[QString("product_id")]);
    m_product_id_isSet = !json[QString("product_id")].isNull() && m_product_id_isValid;

    m_quantity_isValid = ::OpenAPI::fromJsonValue(m_quantity, json[QString("quantity")]);
    m_quantity_isSet = !json[QString("quantity")].isNull() && m_quantity_isValid;

    m_selling_price_isValid = ::OpenAPI::fromJsonValue(m_selling_price, json[QString("selling_price")]);
    m_selling_price_isSet = !json[QString("selling_price")].isNull() && m_selling_price_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;

    m_user_id_isValid = ::OpenAPI::fromJsonValue(m_user_id, json[QString("user_id")]);
    m_user_id_isSet = !json[QString("user_id")].isNull() && m_user_id_isValid;
}

QString OAIInvoiceLine::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIInvoiceLine::asJsonObject() const {
    QJsonObject obj;
    if (m_created_isSet) {
        obj.insert(QString("created"), ::OpenAPI::toJsonValue(m_created));
    }
    if (m_created_by_id_isSet) {
        obj.insert(QString("created_by_id"), ::OpenAPI::toJsonValue(m_created_by_id));
    }
    if (m_deleted_isSet) {
        obj.insert(QString("deleted"), ::OpenAPI::toJsonValue(m_deleted));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_discount_percent_isSet) {
        obj.insert(QString("discount_percent"), ::OpenAPI::toJsonValue(m_discount_percent));
    }
    if (m_discount_text_isSet) {
        obj.insert(QString("discount_text"), ::OpenAPI::toJsonValue(m_discount_text));
    }
    if (m_ean_product_id_isSet) {
        obj.insert(QString("ean_product_id"), ::OpenAPI::toJsonValue(m_ean_product_id));
    }
    if (m_form_id_isSet) {
        obj.insert(QString("form_id"), ::OpenAPI::toJsonValue(m_form_id));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_invoice_id_isSet) {
        obj.insert(QString("invoice_id"), ::OpenAPI::toJsonValue(m_invoice_id));
    }
    if (m_material_id_isSet) {
        obj.insert(QString("material_id"), ::OpenAPI::toJsonValue(m_material_id));
    }
    if (m_modified_isSet) {
        obj.insert(QString("modified"), ::OpenAPI::toJsonValue(m_modified));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_parent_id_isSet) {
        obj.insert(QString("parent_id"), ::OpenAPI::toJsonValue(m_parent_id));
    }
    if (m_product_bundle_id_isSet) {
        obj.insert(QString("product_bundle_id"), ::OpenAPI::toJsonValue(m_product_bundle_id));
    }
    if (m_product_id_isSet) {
        obj.insert(QString("product_id"), ::OpenAPI::toJsonValue(m_product_id));
    }
    if (m_quantity_isSet) {
        obj.insert(QString("quantity"), ::OpenAPI::toJsonValue(m_quantity));
    }
    if (m_selling_price_isSet) {
        obj.insert(QString("selling_price"), ::OpenAPI::toJsonValue(m_selling_price));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    if (m_user_id_isSet) {
        obj.insert(QString("user_id"), ::OpenAPI::toJsonValue(m_user_id));
    }
    return obj;
}

QString OAIInvoiceLine::getCreated() const {
    return m_created;
}
void OAIInvoiceLine::setCreated(const QString &created) {
    m_created = created;
    m_created_isSet = true;
}

bool OAIInvoiceLine::is_created_Set() const{
    return m_created_isSet;
}

bool OAIInvoiceLine::is_created_Valid() const{
    return m_created_isValid;
}

QString OAIInvoiceLine::getCreatedById() const {
    return m_created_by_id;
}
void OAIInvoiceLine::setCreatedById(const QString &created_by_id) {
    m_created_by_id = created_by_id;
    m_created_by_id_isSet = true;
}

bool OAIInvoiceLine::is_created_by_id_Set() const{
    return m_created_by_id_isSet;
}

bool OAIInvoiceLine::is_created_by_id_Valid() const{
    return m_created_by_id_isValid;
}

QString OAIInvoiceLine::getDeleted() const {
    return m_deleted;
}
void OAIInvoiceLine::setDeleted(const QString &deleted) {
    m_deleted = deleted;
    m_deleted_isSet = true;
}

bool OAIInvoiceLine::is_deleted_Set() const{
    return m_deleted_isSet;
}

bool OAIInvoiceLine::is_deleted_Valid() const{
    return m_deleted_isValid;
}

QString OAIInvoiceLine::getDescription() const {
    return m_description;
}
void OAIInvoiceLine::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIInvoiceLine::is_description_Set() const{
    return m_description_isSet;
}

bool OAIInvoiceLine::is_description_Valid() const{
    return m_description_isValid;
}

qint32 OAIInvoiceLine::getDiscountPercent() const {
    return m_discount_percent;
}
void OAIInvoiceLine::setDiscountPercent(const qint32 &discount_percent) {
    m_discount_percent = discount_percent;
    m_discount_percent_isSet = true;
}

bool OAIInvoiceLine::is_discount_percent_Set() const{
    return m_discount_percent_isSet;
}

bool OAIInvoiceLine::is_discount_percent_Valid() const{
    return m_discount_percent_isValid;
}

QString OAIInvoiceLine::getDiscountText() const {
    return m_discount_text;
}
void OAIInvoiceLine::setDiscountText(const QString &discount_text) {
    m_discount_text = discount_text;
    m_discount_text_isSet = true;
}

bool OAIInvoiceLine::is_discount_text_Set() const{
    return m_discount_text_isSet;
}

bool OAIInvoiceLine::is_discount_text_Valid() const{
    return m_discount_text_isValid;
}

QString OAIInvoiceLine::getEanProductId() const {
    return m_ean_product_id;
}
void OAIInvoiceLine::setEanProductId(const QString &ean_product_id) {
    m_ean_product_id = ean_product_id;
    m_ean_product_id_isSet = true;
}

bool OAIInvoiceLine::is_ean_product_id_Set() const{
    return m_ean_product_id_isSet;
}

bool OAIInvoiceLine::is_ean_product_id_Valid() const{
    return m_ean_product_id_isValid;
}

QString OAIInvoiceLine::getFormId() const {
    return m_form_id;
}
void OAIInvoiceLine::setFormId(const QString &form_id) {
    m_form_id = form_id;
    m_form_id_isSet = true;
}

bool OAIInvoiceLine::is_form_id_Set() const{
    return m_form_id_isSet;
}

bool OAIInvoiceLine::is_form_id_Valid() const{
    return m_form_id_isValid;
}

QString OAIInvoiceLine::getId() const {
    return m_id;
}
void OAIInvoiceLine::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIInvoiceLine::is_id_Set() const{
    return m_id_isSet;
}

bool OAIInvoiceLine::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIInvoiceLine::getInvoiceId() const {
    return m_invoice_id;
}
void OAIInvoiceLine::setInvoiceId(const QString &invoice_id) {
    m_invoice_id = invoice_id;
    m_invoice_id_isSet = true;
}

bool OAIInvoiceLine::is_invoice_id_Set() const{
    return m_invoice_id_isSet;
}

bool OAIInvoiceLine::is_invoice_id_Valid() const{
    return m_invoice_id_isValid;
}

QString OAIInvoiceLine::getMaterialId() const {
    return m_material_id;
}
void OAIInvoiceLine::setMaterialId(const QString &material_id) {
    m_material_id = material_id;
    m_material_id_isSet = true;
}

bool OAIInvoiceLine::is_material_id_Set() const{
    return m_material_id_isSet;
}

bool OAIInvoiceLine::is_material_id_Valid() const{
    return m_material_id_isValid;
}

QString OAIInvoiceLine::getModified() const {
    return m_modified;
}
void OAIInvoiceLine::setModified(const QString &modified) {
    m_modified = modified;
    m_modified_isSet = true;
}

bool OAIInvoiceLine::is_modified_Set() const{
    return m_modified_isSet;
}

bool OAIInvoiceLine::is_modified_Valid() const{
    return m_modified_isValid;
}

QString OAIInvoiceLine::getName() const {
    return m_name;
}
void OAIInvoiceLine::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIInvoiceLine::is_name_Set() const{
    return m_name_isSet;
}

bool OAIInvoiceLine::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIInvoiceLine::getParentId() const {
    return m_parent_id;
}
void OAIInvoiceLine::setParentId(const QString &parent_id) {
    m_parent_id = parent_id;
    m_parent_id_isSet = true;
}

bool OAIInvoiceLine::is_parent_id_Set() const{
    return m_parent_id_isSet;
}

bool OAIInvoiceLine::is_parent_id_Valid() const{
    return m_parent_id_isValid;
}

QString OAIInvoiceLine::getProductBundleId() const {
    return m_product_bundle_id;
}
void OAIInvoiceLine::setProductBundleId(const QString &product_bundle_id) {
    m_product_bundle_id = product_bundle_id;
    m_product_bundle_id_isSet = true;
}

bool OAIInvoiceLine::is_product_bundle_id_Set() const{
    return m_product_bundle_id_isSet;
}

bool OAIInvoiceLine::is_product_bundle_id_Valid() const{
    return m_product_bundle_id_isValid;
}

QString OAIInvoiceLine::getProductId() const {
    return m_product_id;
}
void OAIInvoiceLine::setProductId(const QString &product_id) {
    m_product_id = product_id;
    m_product_id_isSet = true;
}

bool OAIInvoiceLine::is_product_id_Set() const{
    return m_product_id_isSet;
}

bool OAIInvoiceLine::is_product_id_Valid() const{
    return m_product_id_isValid;
}

qint32 OAIInvoiceLine::getQuantity() const {
    return m_quantity;
}
void OAIInvoiceLine::setQuantity(const qint32 &quantity) {
    m_quantity = quantity;
    m_quantity_isSet = true;
}

bool OAIInvoiceLine::is_quantity_Set() const{
    return m_quantity_isSet;
}

bool OAIInvoiceLine::is_quantity_Valid() const{
    return m_quantity_isValid;
}

float OAIInvoiceLine::getSellingPrice() const {
    return m_selling_price;
}
void OAIInvoiceLine::setSellingPrice(const float &selling_price) {
    m_selling_price = selling_price;
    m_selling_price_isSet = true;
}

bool OAIInvoiceLine::is_selling_price_Set() const{
    return m_selling_price_isSet;
}

bool OAIInvoiceLine::is_selling_price_Valid() const{
    return m_selling_price_isValid;
}

QString OAIInvoiceLine::getType() const {
    return m_type;
}
void OAIInvoiceLine::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIInvoiceLine::is_type_Set() const{
    return m_type_isSet;
}

bool OAIInvoiceLine::is_type_Valid() const{
    return m_type_isValid;
}

QString OAIInvoiceLine::getUserId() const {
    return m_user_id;
}
void OAIInvoiceLine::setUserId(const QString &user_id) {
    m_user_id = user_id;
    m_user_id_isSet = true;
}

bool OAIInvoiceLine::is_user_id_Set() const{
    return m_user_id_isSet;
}

bool OAIInvoiceLine::is_user_id_Valid() const{
    return m_user_id_isValid;
}

bool OAIInvoiceLine::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_created_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_by_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_deleted_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_discount_percent_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_discount_text_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ean_product_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_form_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_invoice_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_material_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_modified_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_parent_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_product_bundle_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_product_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_quantity_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_selling_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIInvoiceLine::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
