/**
 * Request Baskets API
 * RESTful API of [Request Baskets](https://rbaskets.in) service.  Request Baskets is an open source project of a service to collect HTTP requests and inspect them via RESTful API or web UI.  Check out the [project page](https://github.com/darklynx/request-baskets) for more detailed description. 
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIResponse::OAIResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIResponse::OAIResponse() {
    this->initializeModel();
}

OAIResponse::~OAIResponse() {}

void OAIResponse::initializeModel() {

    m_body_isSet = false;
    m_body_isValid = false;

    m_headers_isSet = false;
    m_headers_isValid = false;

    m_is_template_isSet = false;
    m_is_template_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;
}

void OAIResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIResponse::fromJsonObject(QJsonObject json) {

    m_body_isValid = ::OpenAPI::fromJsonValue(m_body, json[QString("body")]);
    m_body_isSet = !json[QString("body")].isNull() && m_body_isValid;

    if(json["headers"].isObject()){
        auto varmap = json["headers"].toObject().toVariantMap();
        m_headers_isValid = true;
        if(varmap.count() > 0){
            for(auto val : varmap.keys()){
                QList<QString> item;
                auto jval = QJsonValue::fromVariant(varmap.value(val));
                m_headers_isValid &= ::OpenAPI::fromJsonValue(item, jval);
                m_headers_isSet &= !jval.isNull() && m_headers_isValid;
                m_headers.insert(m_headers.end(), val, item);
            }
        }
    }

    m_is_template_isValid = ::OpenAPI::fromJsonValue(m_is_template, json[QString("is_template")]);
    m_is_template_isSet = !json[QString("is_template")].isNull() && m_is_template_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;
}

QString OAIResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_body_isSet) {
        obj.insert(QString("body"), ::OpenAPI::toJsonValue(m_body));
    }
    if (m_headers.size() > 0) {
        
        obj.insert(QString("headers"), toJsonValue(m_headers));
    }
    if (m_is_template_isSet) {
        obj.insert(QString("is_template"), ::OpenAPI::toJsonValue(m_is_template));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    return obj;
}

QString OAIResponse::getBody() const {
    return m_body;
}
void OAIResponse::setBody(const QString &body) {
    m_body = body;
    m_body_isSet = true;
}

bool OAIResponse::is_body_Set() const{
    return m_body_isSet;
}

bool OAIResponse::is_body_Valid() const{
    return m_body_isValid;
}

QMap<QString, QList<QString>> OAIResponse::getHeaders() const {
    return m_headers;
}
void OAIResponse::setHeaders(const QMap<QString, QList<QString>> &headers) {
    m_headers = headers;
    m_headers_isSet = true;
}

bool OAIResponse::is_headers_Set() const{
    return m_headers_isSet;
}

bool OAIResponse::is_headers_Valid() const{
    return m_headers_isValid;
}

bool OAIResponse::isIsTemplate() const {
    return m_is_template;
}
void OAIResponse::setIsTemplate(const bool &is_template) {
    m_is_template = is_template;
    m_is_template_isSet = true;
}

bool OAIResponse::is_is_template_Set() const{
    return m_is_template_isSet;
}

bool OAIResponse::is_is_template_Valid() const{
    return m_is_template_isValid;
}

qint32 OAIResponse::getStatus() const {
    return m_status;
}
void OAIResponse::setStatus(const qint32 &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIResponse::is_status_Set() const{
    return m_status_isSet;
}

bool OAIResponse::is_status_Valid() const{
    return m_status_isValid;
}

bool OAIResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_body_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_headers.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_template_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
