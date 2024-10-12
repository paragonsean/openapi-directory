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

#include "OAIMaterial.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIMaterial::OAIMaterial(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIMaterial::OAIMaterial() {
    this->initializeModel();
}

OAIMaterial::~OAIMaterial() {}

void OAIMaterial::initializeModel() {

    m_barcode_isSet = false;
    m_barcode_isValid = false;

    m_billing_cycle_isSet = false;
    m_billing_cycle_isValid = false;

    m_centiga_id_isSet = false;
    m_centiga_id_isValid = false;

    m_company_id_isSet = false;
    m_company_id_isValid = false;

    m_cost_price_isSet = false;
    m_cost_price_isValid = false;

    m_created_isSet = false;
    m_created_isValid = false;

    m_created_by_id_isSet = false;
    m_created_by_id_isValid = false;

    m_deleted_isSet = false;
    m_deleted_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_is_single_usage_isSet = false;
    m_is_single_usage_isValid = false;

    m_modified_isSet = false;
    m_modified_isValid = false;

    m_modified_by_id_isSet = false;
    m_modified_by_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_pogo_id_isSet = false;
    m_pogo_id_isValid = false;

    m_selling_price_isSet = false;
    m_selling_price_isValid = false;

    m_tripletex_id_isSet = false;
    m_tripletex_id_isValid = false;
}

void OAIMaterial::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIMaterial::fromJsonObject(QJsonObject json) {

    m_barcode_isValid = ::OpenAPI::fromJsonValue(m_barcode, json[QString("barcode")]);
    m_barcode_isSet = !json[QString("barcode")].isNull() && m_barcode_isValid;

    m_billing_cycle_isValid = ::OpenAPI::fromJsonValue(m_billing_cycle, json[QString("billing_cycle")]);
    m_billing_cycle_isSet = !json[QString("billing_cycle")].isNull() && m_billing_cycle_isValid;

    m_centiga_id_isValid = ::OpenAPI::fromJsonValue(m_centiga_id, json[QString("centiga_id")]);
    m_centiga_id_isSet = !json[QString("centiga_id")].isNull() && m_centiga_id_isValid;

    m_company_id_isValid = ::OpenAPI::fromJsonValue(m_company_id, json[QString("company_id")]);
    m_company_id_isSet = !json[QString("company_id")].isNull() && m_company_id_isValid;

    m_cost_price_isValid = ::OpenAPI::fromJsonValue(m_cost_price, json[QString("cost_price")]);
    m_cost_price_isSet = !json[QString("cost_price")].isNull() && m_cost_price_isValid;

    m_created_isValid = ::OpenAPI::fromJsonValue(m_created, json[QString("created")]);
    m_created_isSet = !json[QString("created")].isNull() && m_created_isValid;

    m_created_by_id_isValid = ::OpenAPI::fromJsonValue(m_created_by_id, json[QString("created_by_id")]);
    m_created_by_id_isSet = !json[QString("created_by_id")].isNull() && m_created_by_id_isValid;

    m_deleted_isValid = ::OpenAPI::fromJsonValue(m_deleted, json[QString("deleted")]);
    m_deleted_isSet = !json[QString("deleted")].isNull() && m_deleted_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_is_single_usage_isValid = ::OpenAPI::fromJsonValue(m_is_single_usage, json[QString("is_single_usage")]);
    m_is_single_usage_isSet = !json[QString("is_single_usage")].isNull() && m_is_single_usage_isValid;

    m_modified_isValid = ::OpenAPI::fromJsonValue(m_modified, json[QString("modified")]);
    m_modified_isSet = !json[QString("modified")].isNull() && m_modified_isValid;

    m_modified_by_id_isValid = ::OpenAPI::fromJsonValue(m_modified_by_id, json[QString("modified_by_id")]);
    m_modified_by_id_isSet = !json[QString("modified_by_id")].isNull() && m_modified_by_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_pogo_id_isValid = ::OpenAPI::fromJsonValue(m_pogo_id, json[QString("pogo_id")]);
    m_pogo_id_isSet = !json[QString("pogo_id")].isNull() && m_pogo_id_isValid;

    m_selling_price_isValid = ::OpenAPI::fromJsonValue(m_selling_price, json[QString("selling_price")]);
    m_selling_price_isSet = !json[QString("selling_price")].isNull() && m_selling_price_isValid;

    m_tripletex_id_isValid = ::OpenAPI::fromJsonValue(m_tripletex_id, json[QString("tripletex_id")]);
    m_tripletex_id_isSet = !json[QString("tripletex_id")].isNull() && m_tripletex_id_isValid;
}

QString OAIMaterial::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIMaterial::asJsonObject() const {
    QJsonObject obj;
    if (m_barcode_isSet) {
        obj.insert(QString("barcode"), ::OpenAPI::toJsonValue(m_barcode));
    }
    if (m_billing_cycle_isSet) {
        obj.insert(QString("billing_cycle"), ::OpenAPI::toJsonValue(m_billing_cycle));
    }
    if (m_centiga_id_isSet) {
        obj.insert(QString("centiga_id"), ::OpenAPI::toJsonValue(m_centiga_id));
    }
    if (m_company_id_isSet) {
        obj.insert(QString("company_id"), ::OpenAPI::toJsonValue(m_company_id));
    }
    if (m_cost_price_isSet) {
        obj.insert(QString("cost_price"), ::OpenAPI::toJsonValue(m_cost_price));
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
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_is_single_usage_isSet) {
        obj.insert(QString("is_single_usage"), ::OpenAPI::toJsonValue(m_is_single_usage));
    }
    if (m_modified_isSet) {
        obj.insert(QString("modified"), ::OpenAPI::toJsonValue(m_modified));
    }
    if (m_modified_by_id_isSet) {
        obj.insert(QString("modified_by_id"), ::OpenAPI::toJsonValue(m_modified_by_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_pogo_id_isSet) {
        obj.insert(QString("pogo_id"), ::OpenAPI::toJsonValue(m_pogo_id));
    }
    if (m_selling_price_isSet) {
        obj.insert(QString("selling_price"), ::OpenAPI::toJsonValue(m_selling_price));
    }
    if (m_tripletex_id_isSet) {
        obj.insert(QString("tripletex_id"), ::OpenAPI::toJsonValue(m_tripletex_id));
    }
    return obj;
}

QString OAIMaterial::getBarcode() const {
    return m_barcode;
}
void OAIMaterial::setBarcode(const QString &barcode) {
    m_barcode = barcode;
    m_barcode_isSet = true;
}

bool OAIMaterial::is_barcode_Set() const{
    return m_barcode_isSet;
}

bool OAIMaterial::is_barcode_Valid() const{
    return m_barcode_isValid;
}

QString OAIMaterial::getBillingCycle() const {
    return m_billing_cycle;
}
void OAIMaterial::setBillingCycle(const QString &billing_cycle) {
    m_billing_cycle = billing_cycle;
    m_billing_cycle_isSet = true;
}

bool OAIMaterial::is_billing_cycle_Set() const{
    return m_billing_cycle_isSet;
}

bool OAIMaterial::is_billing_cycle_Valid() const{
    return m_billing_cycle_isValid;
}

QString OAIMaterial::getCentigaId() const {
    return m_centiga_id;
}
void OAIMaterial::setCentigaId(const QString &centiga_id) {
    m_centiga_id = centiga_id;
    m_centiga_id_isSet = true;
}

bool OAIMaterial::is_centiga_id_Set() const{
    return m_centiga_id_isSet;
}

bool OAIMaterial::is_centiga_id_Valid() const{
    return m_centiga_id_isValid;
}

QString OAIMaterial::getCompanyId() const {
    return m_company_id;
}
void OAIMaterial::setCompanyId(const QString &company_id) {
    m_company_id = company_id;
    m_company_id_isSet = true;
}

bool OAIMaterial::is_company_id_Set() const{
    return m_company_id_isSet;
}

bool OAIMaterial::is_company_id_Valid() const{
    return m_company_id_isValid;
}

float OAIMaterial::getCostPrice() const {
    return m_cost_price;
}
void OAIMaterial::setCostPrice(const float &cost_price) {
    m_cost_price = cost_price;
    m_cost_price_isSet = true;
}

bool OAIMaterial::is_cost_price_Set() const{
    return m_cost_price_isSet;
}

bool OAIMaterial::is_cost_price_Valid() const{
    return m_cost_price_isValid;
}

QString OAIMaterial::getCreated() const {
    return m_created;
}
void OAIMaterial::setCreated(const QString &created) {
    m_created = created;
    m_created_isSet = true;
}

bool OAIMaterial::is_created_Set() const{
    return m_created_isSet;
}

bool OAIMaterial::is_created_Valid() const{
    return m_created_isValid;
}

QString OAIMaterial::getCreatedById() const {
    return m_created_by_id;
}
void OAIMaterial::setCreatedById(const QString &created_by_id) {
    m_created_by_id = created_by_id;
    m_created_by_id_isSet = true;
}

bool OAIMaterial::is_created_by_id_Set() const{
    return m_created_by_id_isSet;
}

bool OAIMaterial::is_created_by_id_Valid() const{
    return m_created_by_id_isValid;
}

QString OAIMaterial::getDeleted() const {
    return m_deleted;
}
void OAIMaterial::setDeleted(const QString &deleted) {
    m_deleted = deleted;
    m_deleted_isSet = true;
}

bool OAIMaterial::is_deleted_Set() const{
    return m_deleted_isSet;
}

bool OAIMaterial::is_deleted_Valid() const{
    return m_deleted_isValid;
}

QString OAIMaterial::getDescription() const {
    return m_description;
}
void OAIMaterial::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIMaterial::is_description_Set() const{
    return m_description_isSet;
}

bool OAIMaterial::is_description_Valid() const{
    return m_description_isValid;
}

QString OAIMaterial::getId() const {
    return m_id;
}
void OAIMaterial::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIMaterial::is_id_Set() const{
    return m_id_isSet;
}

bool OAIMaterial::is_id_Valid() const{
    return m_id_isValid;
}

bool OAIMaterial::isIsSingleUsage() const {
    return m_is_single_usage;
}
void OAIMaterial::setIsSingleUsage(const bool &is_single_usage) {
    m_is_single_usage = is_single_usage;
    m_is_single_usage_isSet = true;
}

bool OAIMaterial::is_is_single_usage_Set() const{
    return m_is_single_usage_isSet;
}

bool OAIMaterial::is_is_single_usage_Valid() const{
    return m_is_single_usage_isValid;
}

QString OAIMaterial::getModified() const {
    return m_modified;
}
void OAIMaterial::setModified(const QString &modified) {
    m_modified = modified;
    m_modified_isSet = true;
}

bool OAIMaterial::is_modified_Set() const{
    return m_modified_isSet;
}

bool OAIMaterial::is_modified_Valid() const{
    return m_modified_isValid;
}

QString OAIMaterial::getModifiedById() const {
    return m_modified_by_id;
}
void OAIMaterial::setModifiedById(const QString &modified_by_id) {
    m_modified_by_id = modified_by_id;
    m_modified_by_id_isSet = true;
}

bool OAIMaterial::is_modified_by_id_Set() const{
    return m_modified_by_id_isSet;
}

bool OAIMaterial::is_modified_by_id_Valid() const{
    return m_modified_by_id_isValid;
}

QString OAIMaterial::getName() const {
    return m_name;
}
void OAIMaterial::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIMaterial::is_name_Set() const{
    return m_name_isSet;
}

bool OAIMaterial::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIMaterial::getPogoId() const {
    return m_pogo_id;
}
void OAIMaterial::setPogoId(const QString &pogo_id) {
    m_pogo_id = pogo_id;
    m_pogo_id_isSet = true;
}

bool OAIMaterial::is_pogo_id_Set() const{
    return m_pogo_id_isSet;
}

bool OAIMaterial::is_pogo_id_Valid() const{
    return m_pogo_id_isValid;
}

float OAIMaterial::getSellingPrice() const {
    return m_selling_price;
}
void OAIMaterial::setSellingPrice(const float &selling_price) {
    m_selling_price = selling_price;
    m_selling_price_isSet = true;
}

bool OAIMaterial::is_selling_price_Set() const{
    return m_selling_price_isSet;
}

bool OAIMaterial::is_selling_price_Valid() const{
    return m_selling_price_isValid;
}

QString OAIMaterial::getTripletexId() const {
    return m_tripletex_id;
}
void OAIMaterial::setTripletexId(const QString &tripletex_id) {
    m_tripletex_id = tripletex_id;
    m_tripletex_id_isSet = true;
}

bool OAIMaterial::is_tripletex_id_Set() const{
    return m_tripletex_id_isSet;
}

bool OAIMaterial::is_tripletex_id_Valid() const{
    return m_tripletex_id_isValid;
}

bool OAIMaterial::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_barcode_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_billing_cycle_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_centiga_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_company_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_cost_price_isSet) {
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

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_single_usage_isSet) {
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

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pogo_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_selling_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tripletex_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIMaterial::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
