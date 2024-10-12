/**
 * Zalando Shop
 * The shop API empowers developers to build amazing new apps or websites using Zalando shop data and services.
 *
 * The version of the OpenAPI document: v1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAICategories.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICategories::OAICategories(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICategories::OAICategories() {
    this->initializeModel();
}

OAICategories::~OAICategories() {}

void OAICategories::initializeModel() {

    m_content_isSet = false;
    m_content_isValid = false;

    m_page_isSet = false;
    m_page_isValid = false;

    m_size_isSet = false;
    m_size_isValid = false;

    m_total_elements_isSet = false;
    m_total_elements_isValid = false;

    m_total_pages_isSet = false;
    m_total_pages_isValid = false;
}

void OAICategories::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICategories::fromJsonObject(QJsonObject json) {

    m_content_isValid = ::OpenAPI::fromJsonValue(m_content, json[QString("content")]);
    m_content_isSet = !json[QString("content")].isNull() && m_content_isValid;

    m_page_isValid = ::OpenAPI::fromJsonValue(m_page, json[QString("page")]);
    m_page_isSet = !json[QString("page")].isNull() && m_page_isValid;

    m_size_isValid = ::OpenAPI::fromJsonValue(m_size, json[QString("size")]);
    m_size_isSet = !json[QString("size")].isNull() && m_size_isValid;

    m_total_elements_isValid = ::OpenAPI::fromJsonValue(m_total_elements, json[QString("totalElements")]);
    m_total_elements_isSet = !json[QString("totalElements")].isNull() && m_total_elements_isValid;

    m_total_pages_isValid = ::OpenAPI::fromJsonValue(m_total_pages, json[QString("totalPages")]);
    m_total_pages_isSet = !json[QString("totalPages")].isNull() && m_total_pages_isValid;
}

QString OAICategories::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICategories::asJsonObject() const {
    QJsonObject obj;
    if (m_content.size() > 0) {
        obj.insert(QString("content"), ::OpenAPI::toJsonValue(m_content));
    }
    if (m_page_isSet) {
        obj.insert(QString("page"), ::OpenAPI::toJsonValue(m_page));
    }
    if (m_size_isSet) {
        obj.insert(QString("size"), ::OpenAPI::toJsonValue(m_size));
    }
    if (m_total_elements_isSet) {
        obj.insert(QString("totalElements"), ::OpenAPI::toJsonValue(m_total_elements));
    }
    if (m_total_pages_isSet) {
        obj.insert(QString("totalPages"), ::OpenAPI::toJsonValue(m_total_pages));
    }
    return obj;
}

QList<OAICategory> OAICategories::getContent() const {
    return m_content;
}
void OAICategories::setContent(const QList<OAICategory> &content) {
    m_content = content;
    m_content_isSet = true;
}

bool OAICategories::is_content_Set() const{
    return m_content_isSet;
}

bool OAICategories::is_content_Valid() const{
    return m_content_isValid;
}

qint32 OAICategories::getPage() const {
    return m_page;
}
void OAICategories::setPage(const qint32 &page) {
    m_page = page;
    m_page_isSet = true;
}

bool OAICategories::is_page_Set() const{
    return m_page_isSet;
}

bool OAICategories::is_page_Valid() const{
    return m_page_isValid;
}

qint32 OAICategories::getSize() const {
    return m_size;
}
void OAICategories::setSize(const qint32 &size) {
    m_size = size;
    m_size_isSet = true;
}

bool OAICategories::is_size_Set() const{
    return m_size_isSet;
}

bool OAICategories::is_size_Valid() const{
    return m_size_isValid;
}

qint32 OAICategories::getTotalElements() const {
    return m_total_elements;
}
void OAICategories::setTotalElements(const qint32 &total_elements) {
    m_total_elements = total_elements;
    m_total_elements_isSet = true;
}

bool OAICategories::is_total_elements_Set() const{
    return m_total_elements_isSet;
}

bool OAICategories::is_total_elements_Valid() const{
    return m_total_elements_isValid;
}

qint32 OAICategories::getTotalPages() const {
    return m_total_pages;
}
void OAICategories::setTotalPages(const qint32 &total_pages) {
    m_total_pages = total_pages;
    m_total_pages_isSet = true;
}

bool OAICategories::is_total_pages_Set() const{
    return m_total_pages_isSet;
}

bool OAICategories::is_total_pages_Valid() const{
    return m_total_pages_isValid;
}

bool OAICategories::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_content.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_page_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_size_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_elements_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_pages_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICategories::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_content_isValid && m_page_isValid && m_size_isValid && m_total_elements_isValid && m_total_pages_isValid && true;
}

} // namespace OpenAPI
