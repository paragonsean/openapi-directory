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

#include "OAIProduct.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIProduct::OAIProduct(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIProduct::OAIProduct() {
    this->initializeModel();
}

OAIProduct::~OAIProduct() {}

void OAIProduct::initializeModel() {

    m_average_cost_price_isSet = false;
    m_average_cost_price_isValid = false;

    m_barcode_isSet = false;
    m_barcode_isValid = false;

    m_buying_price_isSet = false;
    m_buying_price_isValid = false;

    m_centiga_id_isSet = false;
    m_centiga_id_isValid = false;

    m_company_id_isSet = false;
    m_company_id_isValid = false;

    m_created_isSet = false;
    m_created_isValid = false;

    m_created_by_id_isSet = false;
    m_created_by_id_isValid = false;

    m_deleted_isSet = false;
    m_deleted_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_erp_id_isSet = false;
    m_erp_id_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_modified_isSet = false;
    m_modified_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_pogo_id_isSet = false;
    m_pogo_id_isValid = false;

    m_product_number_isSet = false;
    m_product_number_isValid = false;

    m_project_status_type_id_isSet = false;
    m_project_status_type_id_isValid = false;

    m_selling_price_isSet = false;
    m_selling_price_isValid = false;

    m_tripletex_id_isSet = false;
    m_tripletex_id_isValid = false;
}

void OAIProduct::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIProduct::fromJsonObject(QJsonObject json) {

    m_average_cost_price_isValid = ::OpenAPI::fromJsonValue(m_average_cost_price, json[QString("average_cost_price")]);
    m_average_cost_price_isSet = !json[QString("average_cost_price")].isNull() && m_average_cost_price_isValid;

    m_barcode_isValid = ::OpenAPI::fromJsonValue(m_barcode, json[QString("barcode")]);
    m_barcode_isSet = !json[QString("barcode")].isNull() && m_barcode_isValid;

    m_buying_price_isValid = ::OpenAPI::fromJsonValue(m_buying_price, json[QString("buying_price")]);
    m_buying_price_isSet = !json[QString("buying_price")].isNull() && m_buying_price_isValid;

    m_centiga_id_isValid = ::OpenAPI::fromJsonValue(m_centiga_id, json[QString("centiga_id")]);
    m_centiga_id_isSet = !json[QString("centiga_id")].isNull() && m_centiga_id_isValid;

    m_company_id_isValid = ::OpenAPI::fromJsonValue(m_company_id, json[QString("company_id")]);
    m_company_id_isSet = !json[QString("company_id")].isNull() && m_company_id_isValid;

    m_created_isValid = ::OpenAPI::fromJsonValue(m_created, json[QString("created")]);
    m_created_isSet = !json[QString("created")].isNull() && m_created_isValid;

    m_created_by_id_isValid = ::OpenAPI::fromJsonValue(m_created_by_id, json[QString("created_by_id")]);
    m_created_by_id_isSet = !json[QString("created_by_id")].isNull() && m_created_by_id_isValid;

    m_deleted_isValid = ::OpenAPI::fromJsonValue(m_deleted, json[QString("deleted")]);
    m_deleted_isSet = !json[QString("deleted")].isNull() && m_deleted_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_erp_id_isValid = ::OpenAPI::fromJsonValue(m_erp_id, json[QString("erp_id")]);
    m_erp_id_isSet = !json[QString("erp_id")].isNull() && m_erp_id_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_modified_isValid = ::OpenAPI::fromJsonValue(m_modified, json[QString("modified")]);
    m_modified_isSet = !json[QString("modified")].isNull() && m_modified_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_pogo_id_isValid = ::OpenAPI::fromJsonValue(m_pogo_id, json[QString("pogo_id")]);
    m_pogo_id_isSet = !json[QString("pogo_id")].isNull() && m_pogo_id_isValid;

    m_product_number_isValid = ::OpenAPI::fromJsonValue(m_product_number, json[QString("product_number")]);
    m_product_number_isSet = !json[QString("product_number")].isNull() && m_product_number_isValid;

    m_project_status_type_id_isValid = ::OpenAPI::fromJsonValue(m_project_status_type_id, json[QString("project_status_type_id")]);
    m_project_status_type_id_isSet = !json[QString("project_status_type_id")].isNull() && m_project_status_type_id_isValid;

    m_selling_price_isValid = ::OpenAPI::fromJsonValue(m_selling_price, json[QString("selling_price")]);
    m_selling_price_isSet = !json[QString("selling_price")].isNull() && m_selling_price_isValid;

    m_tripletex_id_isValid = ::OpenAPI::fromJsonValue(m_tripletex_id, json[QString("tripletex_id")]);
    m_tripletex_id_isSet = !json[QString("tripletex_id")].isNull() && m_tripletex_id_isValid;
}

QString OAIProduct::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIProduct::asJsonObject() const {
    QJsonObject obj;
    if (m_average_cost_price_isSet) {
        obj.insert(QString("average_cost_price"), ::OpenAPI::toJsonValue(m_average_cost_price));
    }
    if (m_barcode_isSet) {
        obj.insert(QString("barcode"), ::OpenAPI::toJsonValue(m_barcode));
    }
    if (m_buying_price_isSet) {
        obj.insert(QString("buying_price"), ::OpenAPI::toJsonValue(m_buying_price));
    }
    if (m_centiga_id_isSet) {
        obj.insert(QString("centiga_id"), ::OpenAPI::toJsonValue(m_centiga_id));
    }
    if (m_company_id_isSet) {
        obj.insert(QString("company_id"), ::OpenAPI::toJsonValue(m_company_id));
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
    if (m_erp_id_isSet) {
        obj.insert(QString("erp_id"), ::OpenAPI::toJsonValue(m_erp_id));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_modified_isSet) {
        obj.insert(QString("modified"), ::OpenAPI::toJsonValue(m_modified));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_pogo_id_isSet) {
        obj.insert(QString("pogo_id"), ::OpenAPI::toJsonValue(m_pogo_id));
    }
    if (m_product_number_isSet) {
        obj.insert(QString("product_number"), ::OpenAPI::toJsonValue(m_product_number));
    }
    if (m_project_status_type_id_isSet) {
        obj.insert(QString("project_status_type_id"), ::OpenAPI::toJsonValue(m_project_status_type_id));
    }
    if (m_selling_price_isSet) {
        obj.insert(QString("selling_price"), ::OpenAPI::toJsonValue(m_selling_price));
    }
    if (m_tripletex_id_isSet) {
        obj.insert(QString("tripletex_id"), ::OpenAPI::toJsonValue(m_tripletex_id));
    }
    return obj;
}

double OAIProduct::getAverageCostPrice() const {
    return m_average_cost_price;
}
void OAIProduct::setAverageCostPrice(const double &average_cost_price) {
    m_average_cost_price = average_cost_price;
    m_average_cost_price_isSet = true;
}

bool OAIProduct::is_average_cost_price_Set() const{
    return m_average_cost_price_isSet;
}

bool OAIProduct::is_average_cost_price_Valid() const{
    return m_average_cost_price_isValid;
}

QString OAIProduct::getBarcode() const {
    return m_barcode;
}
void OAIProduct::setBarcode(const QString &barcode) {
    m_barcode = barcode;
    m_barcode_isSet = true;
}

bool OAIProduct::is_barcode_Set() const{
    return m_barcode_isSet;
}

bool OAIProduct::is_barcode_Valid() const{
    return m_barcode_isValid;
}

double OAIProduct::getBuyingPrice() const {
    return m_buying_price;
}
void OAIProduct::setBuyingPrice(const double &buying_price) {
    m_buying_price = buying_price;
    m_buying_price_isSet = true;
}

bool OAIProduct::is_buying_price_Set() const{
    return m_buying_price_isSet;
}

bool OAIProduct::is_buying_price_Valid() const{
    return m_buying_price_isValid;
}

QString OAIProduct::getCentigaId() const {
    return m_centiga_id;
}
void OAIProduct::setCentigaId(const QString &centiga_id) {
    m_centiga_id = centiga_id;
    m_centiga_id_isSet = true;
}

bool OAIProduct::is_centiga_id_Set() const{
    return m_centiga_id_isSet;
}

bool OAIProduct::is_centiga_id_Valid() const{
    return m_centiga_id_isValid;
}

QString OAIProduct::getCompanyId() const {
    return m_company_id;
}
void OAIProduct::setCompanyId(const QString &company_id) {
    m_company_id = company_id;
    m_company_id_isSet = true;
}

bool OAIProduct::is_company_id_Set() const{
    return m_company_id_isSet;
}

bool OAIProduct::is_company_id_Valid() const{
    return m_company_id_isValid;
}

QString OAIProduct::getCreated() const {
    return m_created;
}
void OAIProduct::setCreated(const QString &created) {
    m_created = created;
    m_created_isSet = true;
}

bool OAIProduct::is_created_Set() const{
    return m_created_isSet;
}

bool OAIProduct::is_created_Valid() const{
    return m_created_isValid;
}

QString OAIProduct::getCreatedById() const {
    return m_created_by_id;
}
void OAIProduct::setCreatedById(const QString &created_by_id) {
    m_created_by_id = created_by_id;
    m_created_by_id_isSet = true;
}

bool OAIProduct::is_created_by_id_Set() const{
    return m_created_by_id_isSet;
}

bool OAIProduct::is_created_by_id_Valid() const{
    return m_created_by_id_isValid;
}

QString OAIProduct::getDeleted() const {
    return m_deleted;
}
void OAIProduct::setDeleted(const QString &deleted) {
    m_deleted = deleted;
    m_deleted_isSet = true;
}

bool OAIProduct::is_deleted_Set() const{
    return m_deleted_isSet;
}

bool OAIProduct::is_deleted_Valid() const{
    return m_deleted_isValid;
}

QString OAIProduct::getDescription() const {
    return m_description;
}
void OAIProduct::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIProduct::is_description_Set() const{
    return m_description_isSet;
}

bool OAIProduct::is_description_Valid() const{
    return m_description_isValid;
}

QString OAIProduct::getErpId() const {
    return m_erp_id;
}
void OAIProduct::setErpId(const QString &erp_id) {
    m_erp_id = erp_id;
    m_erp_id_isSet = true;
}

bool OAIProduct::is_erp_id_Set() const{
    return m_erp_id_isSet;
}

bool OAIProduct::is_erp_id_Valid() const{
    return m_erp_id_isValid;
}

QString OAIProduct::getId() const {
    return m_id;
}
void OAIProduct::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIProduct::is_id_Set() const{
    return m_id_isSet;
}

bool OAIProduct::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIProduct::getModified() const {
    return m_modified;
}
void OAIProduct::setModified(const QString &modified) {
    m_modified = modified;
    m_modified_isSet = true;
}

bool OAIProduct::is_modified_Set() const{
    return m_modified_isSet;
}

bool OAIProduct::is_modified_Valid() const{
    return m_modified_isValid;
}

QString OAIProduct::getName() const {
    return m_name;
}
void OAIProduct::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIProduct::is_name_Set() const{
    return m_name_isSet;
}

bool OAIProduct::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIProduct::getPogoId() const {
    return m_pogo_id;
}
void OAIProduct::setPogoId(const QString &pogo_id) {
    m_pogo_id = pogo_id;
    m_pogo_id_isSet = true;
}

bool OAIProduct::is_pogo_id_Set() const{
    return m_pogo_id_isSet;
}

bool OAIProduct::is_pogo_id_Valid() const{
    return m_pogo_id_isValid;
}

QString OAIProduct::getProductNumber() const {
    return m_product_number;
}
void OAIProduct::setProductNumber(const QString &product_number) {
    m_product_number = product_number;
    m_product_number_isSet = true;
}

bool OAIProduct::is_product_number_Set() const{
    return m_product_number_isSet;
}

bool OAIProduct::is_product_number_Valid() const{
    return m_product_number_isValid;
}

QString OAIProduct::getProjectStatusTypeId() const {
    return m_project_status_type_id;
}
void OAIProduct::setProjectStatusTypeId(const QString &project_status_type_id) {
    m_project_status_type_id = project_status_type_id;
    m_project_status_type_id_isSet = true;
}

bool OAIProduct::is_project_status_type_id_Set() const{
    return m_project_status_type_id_isSet;
}

bool OAIProduct::is_project_status_type_id_Valid() const{
    return m_project_status_type_id_isValid;
}

double OAIProduct::getSellingPrice() const {
    return m_selling_price;
}
void OAIProduct::setSellingPrice(const double &selling_price) {
    m_selling_price = selling_price;
    m_selling_price_isSet = true;
}

bool OAIProduct::is_selling_price_Set() const{
    return m_selling_price_isSet;
}

bool OAIProduct::is_selling_price_Valid() const{
    return m_selling_price_isValid;
}

QString OAIProduct::getTripletexId() const {
    return m_tripletex_id;
}
void OAIProduct::setTripletexId(const QString &tripletex_id) {
    m_tripletex_id = tripletex_id;
    m_tripletex_id_isSet = true;
}

bool OAIProduct::is_tripletex_id_Set() const{
    return m_tripletex_id_isSet;
}

bool OAIProduct::is_tripletex_id_Valid() const{
    return m_tripletex_id_isValid;
}

bool OAIProduct::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_average_cost_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_barcode_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_buying_price_isSet) {
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

        if (m_erp_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
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

        if (m_pogo_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_product_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_project_status_type_id_isSet) {
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

bool OAIProduct::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
