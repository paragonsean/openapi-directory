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

#include "OAIForm.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIForm::OAIForm(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIForm::OAIForm() {
    this->initializeModel();
}

OAIForm::~OAIForm() {}

void OAIForm::initializeModel() {

    m_approved_by_id_isSet = false;
    m_approved_by_id_isValid = false;

    m_company_id_isSet = false;
    m_company_id_isValid = false;

    m_created_isSet = false;
    m_created_isValid = false;

    m_created_by_id_isSet = false;
    m_created_by_id_isValid = false;

    m_deleted_isSet = false;
    m_deleted_isValid = false;

    m_form_date_isSet = false;
    m_form_date_isValid = false;

    m_form_template_id_isSet = false;
    m_form_template_id_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_is_draft_isSet = false;
    m_is_draft_isValid = false;

    m_is_invoiced_isSet = false;
    m_is_invoiced_isValid = false;

    m_is_shared_isSet = false;
    m_is_shared_isValid = false;

    m_mass_form_id_isSet = false;
    m_mass_form_id_isValid = false;

    m_modified_isSet = false;
    m_modified_isValid = false;

    m_project_id_isSet = false;
    m_project_id_isValid = false;
}

void OAIForm::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIForm::fromJsonObject(QJsonObject json) {

    m_approved_by_id_isValid = ::OpenAPI::fromJsonValue(m_approved_by_id, json[QString("approved_by_id")]);
    m_approved_by_id_isSet = !json[QString("approved_by_id")].isNull() && m_approved_by_id_isValid;

    m_company_id_isValid = ::OpenAPI::fromJsonValue(m_company_id, json[QString("company_id")]);
    m_company_id_isSet = !json[QString("company_id")].isNull() && m_company_id_isValid;

    m_created_isValid = ::OpenAPI::fromJsonValue(m_created, json[QString("created")]);
    m_created_isSet = !json[QString("created")].isNull() && m_created_isValid;

    m_created_by_id_isValid = ::OpenAPI::fromJsonValue(m_created_by_id, json[QString("created_by_id")]);
    m_created_by_id_isSet = !json[QString("created_by_id")].isNull() && m_created_by_id_isValid;

    m_deleted_isValid = ::OpenAPI::fromJsonValue(m_deleted, json[QString("deleted")]);
    m_deleted_isSet = !json[QString("deleted")].isNull() && m_deleted_isValid;

    m_form_date_isValid = ::OpenAPI::fromJsonValue(m_form_date, json[QString("form_date")]);
    m_form_date_isSet = !json[QString("form_date")].isNull() && m_form_date_isValid;

    m_form_template_id_isValid = ::OpenAPI::fromJsonValue(m_form_template_id, json[QString("form_template_id")]);
    m_form_template_id_isSet = !json[QString("form_template_id")].isNull() && m_form_template_id_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_is_draft_isValid = ::OpenAPI::fromJsonValue(m_is_draft, json[QString("is_draft")]);
    m_is_draft_isSet = !json[QString("is_draft")].isNull() && m_is_draft_isValid;

    m_is_invoiced_isValid = ::OpenAPI::fromJsonValue(m_is_invoiced, json[QString("is_invoiced")]);
    m_is_invoiced_isSet = !json[QString("is_invoiced")].isNull() && m_is_invoiced_isValid;

    m_is_shared_isValid = ::OpenAPI::fromJsonValue(m_is_shared, json[QString("is_shared")]);
    m_is_shared_isSet = !json[QString("is_shared")].isNull() && m_is_shared_isValid;

    m_mass_form_id_isValid = ::OpenAPI::fromJsonValue(m_mass_form_id, json[QString("mass_form_id")]);
    m_mass_form_id_isSet = !json[QString("mass_form_id")].isNull() && m_mass_form_id_isValid;

    m_modified_isValid = ::OpenAPI::fromJsonValue(m_modified, json[QString("modified")]);
    m_modified_isSet = !json[QString("modified")].isNull() && m_modified_isValid;

    m_project_id_isValid = ::OpenAPI::fromJsonValue(m_project_id, json[QString("project_id")]);
    m_project_id_isSet = !json[QString("project_id")].isNull() && m_project_id_isValid;
}

QString OAIForm::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIForm::asJsonObject() const {
    QJsonObject obj;
    if (m_approved_by_id_isSet) {
        obj.insert(QString("approved_by_id"), ::OpenAPI::toJsonValue(m_approved_by_id));
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
    if (m_form_date_isSet) {
        obj.insert(QString("form_date"), ::OpenAPI::toJsonValue(m_form_date));
    }
    if (m_form_template_id_isSet) {
        obj.insert(QString("form_template_id"), ::OpenAPI::toJsonValue(m_form_template_id));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_is_draft_isSet) {
        obj.insert(QString("is_draft"), ::OpenAPI::toJsonValue(m_is_draft));
    }
    if (m_is_invoiced_isSet) {
        obj.insert(QString("is_invoiced"), ::OpenAPI::toJsonValue(m_is_invoiced));
    }
    if (m_is_shared_isSet) {
        obj.insert(QString("is_shared"), ::OpenAPI::toJsonValue(m_is_shared));
    }
    if (m_mass_form_id_isSet) {
        obj.insert(QString("mass_form_id"), ::OpenAPI::toJsonValue(m_mass_form_id));
    }
    if (m_modified_isSet) {
        obj.insert(QString("modified"), ::OpenAPI::toJsonValue(m_modified));
    }
    if (m_project_id_isSet) {
        obj.insert(QString("project_id"), ::OpenAPI::toJsonValue(m_project_id));
    }
    return obj;
}

QString OAIForm::getApprovedById() const {
    return m_approved_by_id;
}
void OAIForm::setApprovedById(const QString &approved_by_id) {
    m_approved_by_id = approved_by_id;
    m_approved_by_id_isSet = true;
}

bool OAIForm::is_approved_by_id_Set() const{
    return m_approved_by_id_isSet;
}

bool OAIForm::is_approved_by_id_Valid() const{
    return m_approved_by_id_isValid;
}

QString OAIForm::getCompanyId() const {
    return m_company_id;
}
void OAIForm::setCompanyId(const QString &company_id) {
    m_company_id = company_id;
    m_company_id_isSet = true;
}

bool OAIForm::is_company_id_Set() const{
    return m_company_id_isSet;
}

bool OAIForm::is_company_id_Valid() const{
    return m_company_id_isValid;
}

QString OAIForm::getCreated() const {
    return m_created;
}
void OAIForm::setCreated(const QString &created) {
    m_created = created;
    m_created_isSet = true;
}

bool OAIForm::is_created_Set() const{
    return m_created_isSet;
}

bool OAIForm::is_created_Valid() const{
    return m_created_isValid;
}

QString OAIForm::getCreatedById() const {
    return m_created_by_id;
}
void OAIForm::setCreatedById(const QString &created_by_id) {
    m_created_by_id = created_by_id;
    m_created_by_id_isSet = true;
}

bool OAIForm::is_created_by_id_Set() const{
    return m_created_by_id_isSet;
}

bool OAIForm::is_created_by_id_Valid() const{
    return m_created_by_id_isValid;
}

QString OAIForm::getDeleted() const {
    return m_deleted;
}
void OAIForm::setDeleted(const QString &deleted) {
    m_deleted = deleted;
    m_deleted_isSet = true;
}

bool OAIForm::is_deleted_Set() const{
    return m_deleted_isSet;
}

bool OAIForm::is_deleted_Valid() const{
    return m_deleted_isValid;
}

QDate OAIForm::getFormDate() const {
    return m_form_date;
}
void OAIForm::setFormDate(const QDate &form_date) {
    m_form_date = form_date;
    m_form_date_isSet = true;
}

bool OAIForm::is_form_date_Set() const{
    return m_form_date_isSet;
}

bool OAIForm::is_form_date_Valid() const{
    return m_form_date_isValid;
}

QString OAIForm::getFormTemplateId() const {
    return m_form_template_id;
}
void OAIForm::setFormTemplateId(const QString &form_template_id) {
    m_form_template_id = form_template_id;
    m_form_template_id_isSet = true;
}

bool OAIForm::is_form_template_id_Set() const{
    return m_form_template_id_isSet;
}

bool OAIForm::is_form_template_id_Valid() const{
    return m_form_template_id_isValid;
}

QString OAIForm::getId() const {
    return m_id;
}
void OAIForm::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIForm::is_id_Set() const{
    return m_id_isSet;
}

bool OAIForm::is_id_Valid() const{
    return m_id_isValid;
}

bool OAIForm::isIsDraft() const {
    return m_is_draft;
}
void OAIForm::setIsDraft(const bool &is_draft) {
    m_is_draft = is_draft;
    m_is_draft_isSet = true;
}

bool OAIForm::is_is_draft_Set() const{
    return m_is_draft_isSet;
}

bool OAIForm::is_is_draft_Valid() const{
    return m_is_draft_isValid;
}

QString OAIForm::getIsInvoiced() const {
    return m_is_invoiced;
}
void OAIForm::setIsInvoiced(const QString &is_invoiced) {
    m_is_invoiced = is_invoiced;
    m_is_invoiced_isSet = true;
}

bool OAIForm::is_is_invoiced_Set() const{
    return m_is_invoiced_isSet;
}

bool OAIForm::is_is_invoiced_Valid() const{
    return m_is_invoiced_isValid;
}

bool OAIForm::isIsShared() const {
    return m_is_shared;
}
void OAIForm::setIsShared(const bool &is_shared) {
    m_is_shared = is_shared;
    m_is_shared_isSet = true;
}

bool OAIForm::is_is_shared_Set() const{
    return m_is_shared_isSet;
}

bool OAIForm::is_is_shared_Valid() const{
    return m_is_shared_isValid;
}

QString OAIForm::getMassFormId() const {
    return m_mass_form_id;
}
void OAIForm::setMassFormId(const QString &mass_form_id) {
    m_mass_form_id = mass_form_id;
    m_mass_form_id_isSet = true;
}

bool OAIForm::is_mass_form_id_Set() const{
    return m_mass_form_id_isSet;
}

bool OAIForm::is_mass_form_id_Valid() const{
    return m_mass_form_id_isValid;
}

QString OAIForm::getModified() const {
    return m_modified;
}
void OAIForm::setModified(const QString &modified) {
    m_modified = modified;
    m_modified_isSet = true;
}

bool OAIForm::is_modified_Set() const{
    return m_modified_isSet;
}

bool OAIForm::is_modified_Valid() const{
    return m_modified_isValid;
}

QString OAIForm::getProjectId() const {
    return m_project_id;
}
void OAIForm::setProjectId(const QString &project_id) {
    m_project_id = project_id;
    m_project_id_isSet = true;
}

bool OAIForm::is_project_id_Set() const{
    return m_project_id_isSet;
}

bool OAIForm::is_project_id_Valid() const{
    return m_project_id_isValid;
}

bool OAIForm::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_approved_by_id_isSet) {
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

        if (m_form_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_form_template_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_draft_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_invoiced_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_shared_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_mass_form_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_modified_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_project_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIForm::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
