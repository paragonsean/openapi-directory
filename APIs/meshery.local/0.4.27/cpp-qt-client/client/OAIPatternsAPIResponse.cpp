/**
 * Meshery API.
 * the purpose of this application is to provide an application that is using plain go code to define an API  This should demonstrate all the possible comment annotations that are available to turn go code into a fully compliant swagger 2.0 spec
 *
 * The version of the OpenAPI document: 0.4.27
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIPatternsAPIResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPatternsAPIResponse::OAIPatternsAPIResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPatternsAPIResponse::OAIPatternsAPIResponse() {
    this->initializeModel();
}

OAIPatternsAPIResponse::~OAIPatternsAPIResponse() {}

void OAIPatternsAPIResponse::initializeModel() {

    m_page_isSet = false;
    m_page_isValid = false;

    m_page_size_isSet = false;
    m_page_size_isValid = false;

    m_patterns_isSet = false;
    m_patterns_isValid = false;

    m_total_count_isSet = false;
    m_total_count_isValid = false;
}

void OAIPatternsAPIResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPatternsAPIResponse::fromJsonObject(QJsonObject json) {

    m_page_isValid = ::OpenAPI::fromJsonValue(m_page, json[QString("page")]);
    m_page_isSet = !json[QString("page")].isNull() && m_page_isValid;

    m_page_size_isValid = ::OpenAPI::fromJsonValue(m_page_size, json[QString("page_size")]);
    m_page_size_isSet = !json[QString("page_size")].isNull() && m_page_size_isValid;

    m_patterns_isValid = ::OpenAPI::fromJsonValue(m_patterns, json[QString("patterns")]);
    m_patterns_isSet = !json[QString("patterns")].isNull() && m_patterns_isValid;

    m_total_count_isValid = ::OpenAPI::fromJsonValue(m_total_count, json[QString("total_count")]);
    m_total_count_isSet = !json[QString("total_count")].isNull() && m_total_count_isValid;
}

QString OAIPatternsAPIResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPatternsAPIResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_page_isSet) {
        obj.insert(QString("page"), ::OpenAPI::toJsonValue(m_page));
    }
    if (m_page_size_isSet) {
        obj.insert(QString("page_size"), ::OpenAPI::toJsonValue(m_page_size));
    }
    if (m_patterns.size() > 0) {
        obj.insert(QString("patterns"), ::OpenAPI::toJsonValue(m_patterns));
    }
    if (m_total_count_isSet) {
        obj.insert(QString("total_count"), ::OpenAPI::toJsonValue(m_total_count));
    }
    return obj;
}

qint32 OAIPatternsAPIResponse::getPage() const {
    return m_page;
}
void OAIPatternsAPIResponse::setPage(const qint32 &page) {
    m_page = page;
    m_page_isSet = true;
}

bool OAIPatternsAPIResponse::is_page_Set() const{
    return m_page_isSet;
}

bool OAIPatternsAPIResponse::is_page_Valid() const{
    return m_page_isValid;
}

qint32 OAIPatternsAPIResponse::getPageSize() const {
    return m_page_size;
}
void OAIPatternsAPIResponse::setPageSize(const qint32 &page_size) {
    m_page_size = page_size;
    m_page_size_isSet = true;
}

bool OAIPatternsAPIResponse::is_page_size_Set() const{
    return m_page_size_isSet;
}

bool OAIPatternsAPIResponse::is_page_size_Valid() const{
    return m_page_size_isValid;
}

QList<OAIMesheryPattern> OAIPatternsAPIResponse::getPatterns() const {
    return m_patterns;
}
void OAIPatternsAPIResponse::setPatterns(const QList<OAIMesheryPattern> &patterns) {
    m_patterns = patterns;
    m_patterns_isSet = true;
}

bool OAIPatternsAPIResponse::is_patterns_Set() const{
    return m_patterns_isSet;
}

bool OAIPatternsAPIResponse::is_patterns_Valid() const{
    return m_patterns_isValid;
}

qint32 OAIPatternsAPIResponse::getTotalCount() const {
    return m_total_count;
}
void OAIPatternsAPIResponse::setTotalCount(const qint32 &total_count) {
    m_total_count = total_count;
    m_total_count_isSet = true;
}

bool OAIPatternsAPIResponse::is_total_count_Set() const{
    return m_total_count_isSet;
}

bool OAIPatternsAPIResponse::is_total_count_Valid() const{
    return m_total_count_isValid;
}

bool OAIPatternsAPIResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_page_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_page_size_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_patterns.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_count_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPatternsAPIResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
