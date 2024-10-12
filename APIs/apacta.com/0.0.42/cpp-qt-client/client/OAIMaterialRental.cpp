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

#include "OAIMaterialRental.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIMaterialRental::OAIMaterialRental(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIMaterialRental::OAIMaterialRental() {
    this->initializeModel();
}

OAIMaterialRental::~OAIMaterialRental() {}

void OAIMaterialRental::initializeModel() {

    m_amount_isSet = false;
    m_amount_isValid = false;

    m_created_isSet = false;
    m_created_isValid = false;

    m_created_by_id_isSet = false;
    m_created_by_id_isValid = false;

    m_deleted_isSet = false;
    m_deleted_isValid = false;

    m_from_date_isSet = false;
    m_from_date_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_is_invoiced_isSet = false;
    m_is_invoiced_isValid = false;

    m_material_id_isSet = false;
    m_material_id_isValid = false;

    m_modified_isSet = false;
    m_modified_isValid = false;

    m_modified_by_id_isSet = false;
    m_modified_by_id_isValid = false;

    m_project_id_isSet = false;
    m_project_id_isValid = false;

    m_quantity_isSet = false;
    m_quantity_isValid = false;

    m_to_date_isSet = false;
    m_to_date_isValid = false;
}

void OAIMaterialRental::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIMaterialRental::fromJsonObject(QJsonObject json) {

    m_amount_isValid = ::OpenAPI::fromJsonValue(m_amount, json[QString("amount")]);
    m_amount_isSet = !json[QString("amount")].isNull() && m_amount_isValid;

    m_created_isValid = ::OpenAPI::fromJsonValue(m_created, json[QString("created")]);
    m_created_isSet = !json[QString("created")].isNull() && m_created_isValid;

    m_created_by_id_isValid = ::OpenAPI::fromJsonValue(m_created_by_id, json[QString("created_by_id")]);
    m_created_by_id_isSet = !json[QString("created_by_id")].isNull() && m_created_by_id_isValid;

    m_deleted_isValid = ::OpenAPI::fromJsonValue(m_deleted, json[QString("deleted")]);
    m_deleted_isSet = !json[QString("deleted")].isNull() && m_deleted_isValid;

    m_from_date_isValid = ::OpenAPI::fromJsonValue(m_from_date, json[QString("from_date")]);
    m_from_date_isSet = !json[QString("from_date")].isNull() && m_from_date_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_is_invoiced_isValid = ::OpenAPI::fromJsonValue(m_is_invoiced, json[QString("is_invoiced")]);
    m_is_invoiced_isSet = !json[QString("is_invoiced")].isNull() && m_is_invoiced_isValid;

    m_material_id_isValid = ::OpenAPI::fromJsonValue(m_material_id, json[QString("material_id")]);
    m_material_id_isSet = !json[QString("material_id")].isNull() && m_material_id_isValid;

    m_modified_isValid = ::OpenAPI::fromJsonValue(m_modified, json[QString("modified")]);
    m_modified_isSet = !json[QString("modified")].isNull() && m_modified_isValid;

    m_modified_by_id_isValid = ::OpenAPI::fromJsonValue(m_modified_by_id, json[QString("modified_by_id")]);
    m_modified_by_id_isSet = !json[QString("modified_by_id")].isNull() && m_modified_by_id_isValid;

    m_project_id_isValid = ::OpenAPI::fromJsonValue(m_project_id, json[QString("project_id")]);
    m_project_id_isSet = !json[QString("project_id")].isNull() && m_project_id_isValid;

    m_quantity_isValid = ::OpenAPI::fromJsonValue(m_quantity, json[QString("quantity")]);
    m_quantity_isSet = !json[QString("quantity")].isNull() && m_quantity_isValid;

    m_to_date_isValid = ::OpenAPI::fromJsonValue(m_to_date, json[QString("to_date")]);
    m_to_date_isSet = !json[QString("to_date")].isNull() && m_to_date_isValid;
}

QString OAIMaterialRental::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIMaterialRental::asJsonObject() const {
    QJsonObject obj;
    if (m_amount_isSet) {
        obj.insert(QString("amount"), ::OpenAPI::toJsonValue(m_amount));
    }
    if (m_created_isSet) {
        obj.insert(QString("created"), ::OpenAPI::toJsonValue(m_created));
    }
    if (m_created_by_id_isSet) {
        obj.insert(QString("created_by_id"), ::OpenAPI::toJsonValue(m_created_by_id));
    }
    if (m_deleted_isSet) {
        obj.insert(QString("deleted"), ::OpenAPI::toJsonValue(m_deleted));
    }
    if (m_from_date_isSet) {
        obj.insert(QString("from_date"), ::OpenAPI::toJsonValue(m_from_date));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_is_invoiced_isSet) {
        obj.insert(QString("is_invoiced"), ::OpenAPI::toJsonValue(m_is_invoiced));
    }
    if (m_material_id_isSet) {
        obj.insert(QString("material_id"), ::OpenAPI::toJsonValue(m_material_id));
    }
    if (m_modified_isSet) {
        obj.insert(QString("modified"), ::OpenAPI::toJsonValue(m_modified));
    }
    if (m_modified_by_id_isSet) {
        obj.insert(QString("modified_by_id"), ::OpenAPI::toJsonValue(m_modified_by_id));
    }
    if (m_project_id_isSet) {
        obj.insert(QString("project_id"), ::OpenAPI::toJsonValue(m_project_id));
    }
    if (m_quantity_isSet) {
        obj.insert(QString("quantity"), ::OpenAPI::toJsonValue(m_quantity));
    }
    if (m_to_date_isSet) {
        obj.insert(QString("to_date"), ::OpenAPI::toJsonValue(m_to_date));
    }
    return obj;
}

float OAIMaterialRental::getAmount() const {
    return m_amount;
}
void OAIMaterialRental::setAmount(const float &amount) {
    m_amount = amount;
    m_amount_isSet = true;
}

bool OAIMaterialRental::is_amount_Set() const{
    return m_amount_isSet;
}

bool OAIMaterialRental::is_amount_Valid() const{
    return m_amount_isValid;
}

QString OAIMaterialRental::getCreated() const {
    return m_created;
}
void OAIMaterialRental::setCreated(const QString &created) {
    m_created = created;
    m_created_isSet = true;
}

bool OAIMaterialRental::is_created_Set() const{
    return m_created_isSet;
}

bool OAIMaterialRental::is_created_Valid() const{
    return m_created_isValid;
}

QString OAIMaterialRental::getCreatedById() const {
    return m_created_by_id;
}
void OAIMaterialRental::setCreatedById(const QString &created_by_id) {
    m_created_by_id = created_by_id;
    m_created_by_id_isSet = true;
}

bool OAIMaterialRental::is_created_by_id_Set() const{
    return m_created_by_id_isSet;
}

bool OAIMaterialRental::is_created_by_id_Valid() const{
    return m_created_by_id_isValid;
}

QString OAIMaterialRental::getDeleted() const {
    return m_deleted;
}
void OAIMaterialRental::setDeleted(const QString &deleted) {
    m_deleted = deleted;
    m_deleted_isSet = true;
}

bool OAIMaterialRental::is_deleted_Set() const{
    return m_deleted_isSet;
}

bool OAIMaterialRental::is_deleted_Valid() const{
    return m_deleted_isValid;
}

QString OAIMaterialRental::getFromDate() const {
    return m_from_date;
}
void OAIMaterialRental::setFromDate(const QString &from_date) {
    m_from_date = from_date;
    m_from_date_isSet = true;
}

bool OAIMaterialRental::is_from_date_Set() const{
    return m_from_date_isSet;
}

bool OAIMaterialRental::is_from_date_Valid() const{
    return m_from_date_isValid;
}

QString OAIMaterialRental::getId() const {
    return m_id;
}
void OAIMaterialRental::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIMaterialRental::is_id_Set() const{
    return m_id_isSet;
}

bool OAIMaterialRental::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIMaterialRental::getIsInvoiced() const {
    return m_is_invoiced;
}
void OAIMaterialRental::setIsInvoiced(const QString &is_invoiced) {
    m_is_invoiced = is_invoiced;
    m_is_invoiced_isSet = true;
}

bool OAIMaterialRental::is_is_invoiced_Set() const{
    return m_is_invoiced_isSet;
}

bool OAIMaterialRental::is_is_invoiced_Valid() const{
    return m_is_invoiced_isValid;
}

QString OAIMaterialRental::getMaterialId() const {
    return m_material_id;
}
void OAIMaterialRental::setMaterialId(const QString &material_id) {
    m_material_id = material_id;
    m_material_id_isSet = true;
}

bool OAIMaterialRental::is_material_id_Set() const{
    return m_material_id_isSet;
}

bool OAIMaterialRental::is_material_id_Valid() const{
    return m_material_id_isValid;
}

QString OAIMaterialRental::getModified() const {
    return m_modified;
}
void OAIMaterialRental::setModified(const QString &modified) {
    m_modified = modified;
    m_modified_isSet = true;
}

bool OAIMaterialRental::is_modified_Set() const{
    return m_modified_isSet;
}

bool OAIMaterialRental::is_modified_Valid() const{
    return m_modified_isValid;
}

QString OAIMaterialRental::getModifiedById() const {
    return m_modified_by_id;
}
void OAIMaterialRental::setModifiedById(const QString &modified_by_id) {
    m_modified_by_id = modified_by_id;
    m_modified_by_id_isSet = true;
}

bool OAIMaterialRental::is_modified_by_id_Set() const{
    return m_modified_by_id_isSet;
}

bool OAIMaterialRental::is_modified_by_id_Valid() const{
    return m_modified_by_id_isValid;
}

QString OAIMaterialRental::getProjectId() const {
    return m_project_id;
}
void OAIMaterialRental::setProjectId(const QString &project_id) {
    m_project_id = project_id;
    m_project_id_isSet = true;
}

bool OAIMaterialRental::is_project_id_Set() const{
    return m_project_id_isSet;
}

bool OAIMaterialRental::is_project_id_Valid() const{
    return m_project_id_isValid;
}

float OAIMaterialRental::getQuantity() const {
    return m_quantity;
}
void OAIMaterialRental::setQuantity(const float &quantity) {
    m_quantity = quantity;
    m_quantity_isSet = true;
}

bool OAIMaterialRental::is_quantity_Set() const{
    return m_quantity_isSet;
}

bool OAIMaterialRental::is_quantity_Valid() const{
    return m_quantity_isValid;
}

QString OAIMaterialRental::getToDate() const {
    return m_to_date;
}
void OAIMaterialRental::setToDate(const QString &to_date) {
    m_to_date = to_date;
    m_to_date_isSet = true;
}

bool OAIMaterialRental::is_to_date_Set() const{
    return m_to_date_isSet;
}

bool OAIMaterialRental::is_to_date_Valid() const{
    return m_to_date_isValid;
}

bool OAIMaterialRental::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

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

        if (m_from_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_invoiced_isSet) {
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

        if (m_modified_by_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_project_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_quantity_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_to_date_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIMaterialRental::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
