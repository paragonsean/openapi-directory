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

#include "OAIRequest.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIRequest::OAIRequest(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIRequest::OAIRequest() {
    this->initializeModel();
}

OAIRequest::~OAIRequest() {}

void OAIRequest::initializeModel() {

    m_body_isSet = false;
    m_body_isValid = false;

    m_content_length_isSet = false;
    m_content_length_isValid = false;

    m_date_isSet = false;
    m_date_isValid = false;

    m_headers_isSet = false;
    m_headers_isValid = false;

    m_method_isSet = false;
    m_method_isValid = false;

    m_path_isSet = false;
    m_path_isValid = false;

    m_query_isSet = false;
    m_query_isValid = false;
}

void OAIRequest::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIRequest::fromJsonObject(QJsonObject json) {

    m_body_isValid = ::OpenAPI::fromJsonValue(m_body, json[QString("body")]);
    m_body_isSet = !json[QString("body")].isNull() && m_body_isValid;

    m_content_length_isValid = ::OpenAPI::fromJsonValue(m_content_length, json[QString("content_length")]);
    m_content_length_isSet = !json[QString("content_length")].isNull() && m_content_length_isValid;

    m_date_isValid = ::OpenAPI::fromJsonValue(m_date, json[QString("date")]);
    m_date_isSet = !json[QString("date")].isNull() && m_date_isValid;

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

    m_method_isValid = ::OpenAPI::fromJsonValue(m_method, json[QString("method")]);
    m_method_isSet = !json[QString("method")].isNull() && m_method_isValid;

    m_path_isValid = ::OpenAPI::fromJsonValue(m_path, json[QString("path")]);
    m_path_isSet = !json[QString("path")].isNull() && m_path_isValid;

    m_query_isValid = ::OpenAPI::fromJsonValue(m_query, json[QString("query")]);
    m_query_isSet = !json[QString("query")].isNull() && m_query_isValid;
}

QString OAIRequest::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIRequest::asJsonObject() const {
    QJsonObject obj;
    if (m_body_isSet) {
        obj.insert(QString("body"), ::OpenAPI::toJsonValue(m_body));
    }
    if (m_content_length_isSet) {
        obj.insert(QString("content_length"), ::OpenAPI::toJsonValue(m_content_length));
    }
    if (m_date_isSet) {
        obj.insert(QString("date"), ::OpenAPI::toJsonValue(m_date));
    }
    if (m_headers.size() > 0) {
        
        obj.insert(QString("headers"), toJsonValue(m_headers));
    }
    if (m_method_isSet) {
        obj.insert(QString("method"), ::OpenAPI::toJsonValue(m_method));
    }
    if (m_path_isSet) {
        obj.insert(QString("path"), ::OpenAPI::toJsonValue(m_path));
    }
    if (m_query_isSet) {
        obj.insert(QString("query"), ::OpenAPI::toJsonValue(m_query));
    }
    return obj;
}

QString OAIRequest::getBody() const {
    return m_body;
}
void OAIRequest::setBody(const QString &body) {
    m_body = body;
    m_body_isSet = true;
}

bool OAIRequest::is_body_Set() const{
    return m_body_isSet;
}

bool OAIRequest::is_body_Valid() const{
    return m_body_isValid;
}

qint32 OAIRequest::getContentLength() const {
    return m_content_length;
}
void OAIRequest::setContentLength(const qint32 &content_length) {
    m_content_length = content_length;
    m_content_length_isSet = true;
}

bool OAIRequest::is_content_length_Set() const{
    return m_content_length_isSet;
}

bool OAIRequest::is_content_length_Valid() const{
    return m_content_length_isValid;
}

qint64 OAIRequest::getDate() const {
    return m_date;
}
void OAIRequest::setDate(const qint64 &date) {
    m_date = date;
    m_date_isSet = true;
}

bool OAIRequest::is_date_Set() const{
    return m_date_isSet;
}

bool OAIRequest::is_date_Valid() const{
    return m_date_isValid;
}

QMap<QString, QList<QString>> OAIRequest::getHeaders() const {
    return m_headers;
}
void OAIRequest::setHeaders(const QMap<QString, QList<QString>> &headers) {
    m_headers = headers;
    m_headers_isSet = true;
}

bool OAIRequest::is_headers_Set() const{
    return m_headers_isSet;
}

bool OAIRequest::is_headers_Valid() const{
    return m_headers_isValid;
}

QString OAIRequest::getMethod() const {
    return m_method;
}
void OAIRequest::setMethod(const QString &method) {
    m_method = method;
    m_method_isSet = true;
}

bool OAIRequest::is_method_Set() const{
    return m_method_isSet;
}

bool OAIRequest::is_method_Valid() const{
    return m_method_isValid;
}

QString OAIRequest::getPath() const {
    return m_path;
}
void OAIRequest::setPath(const QString &path) {
    m_path = path;
    m_path_isSet = true;
}

bool OAIRequest::is_path_Set() const{
    return m_path_isSet;
}

bool OAIRequest::is_path_Valid() const{
    return m_path_isValid;
}

QString OAIRequest::getQuery() const {
    return m_query;
}
void OAIRequest::setQuery(const QString &query) {
    m_query = query;
    m_query_isSet = true;
}

bool OAIRequest::is_query_Set() const{
    return m_query_isSet;
}

bool OAIRequest::is_query_Valid() const{
    return m_query_isValid;
}

bool OAIRequest::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_body_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_content_length_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_headers.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_method_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_path_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_query_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIRequest::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
