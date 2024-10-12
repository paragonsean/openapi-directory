/**
 * Hubhopper Partner Integration API(s) - Production
 * This is an interactive document explaining the API(s) that could be used to fetch data from [Hubhopper](https://hubhopper.com). Use the api key provided to authorize `x-api-key` and test the API(s). The output data models are also available for reference.
 *
 * The version of the OpenAPI document: v5
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAILanguageList.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAILanguageList::OAILanguageList(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAILanguageList::OAILanguageList() {
    this->initializeModel();
}

OAILanguageList::~OAILanguageList() {}

void OAILanguageList::initializeModel() {

    m_languages_isSet = false;
    m_languages_isValid = false;

    m_no_of_pages_isSet = false;
    m_no_of_pages_isValid = false;

    m_page_isSet = false;
    m_page_isValid = false;

    m_page_size_isSet = false;
    m_page_size_isValid = false;

    m_total_isSet = false;
    m_total_isValid = false;
}

void OAILanguageList::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAILanguageList::fromJsonObject(QJsonObject json) {

    m_languages_isValid = ::OpenAPI::fromJsonValue(m_languages, json[QString("languages")]);
    m_languages_isSet = !json[QString("languages")].isNull() && m_languages_isValid;

    m_no_of_pages_isValid = ::OpenAPI::fromJsonValue(m_no_of_pages, json[QString("noOfPages")]);
    m_no_of_pages_isSet = !json[QString("noOfPages")].isNull() && m_no_of_pages_isValid;

    m_page_isValid = ::OpenAPI::fromJsonValue(m_page, json[QString("page")]);
    m_page_isSet = !json[QString("page")].isNull() && m_page_isValid;

    m_page_size_isValid = ::OpenAPI::fromJsonValue(m_page_size, json[QString("pageSize")]);
    m_page_size_isSet = !json[QString("pageSize")].isNull() && m_page_size_isValid;

    m_total_isValid = ::OpenAPI::fromJsonValue(m_total, json[QString("total")]);
    m_total_isSet = !json[QString("total")].isNull() && m_total_isValid;
}

QString OAILanguageList::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAILanguageList::asJsonObject() const {
    QJsonObject obj;
    if (m_languages.size() > 0) {
        obj.insert(QString("languages"), ::OpenAPI::toJsonValue(m_languages));
    }
    if (m_no_of_pages_isSet) {
        obj.insert(QString("noOfPages"), ::OpenAPI::toJsonValue(m_no_of_pages));
    }
    if (m_page_isSet) {
        obj.insert(QString("page"), ::OpenAPI::toJsonValue(m_page));
    }
    if (m_page_size_isSet) {
        obj.insert(QString("pageSize"), ::OpenAPI::toJsonValue(m_page_size));
    }
    if (m_total_isSet) {
        obj.insert(QString("total"), ::OpenAPI::toJsonValue(m_total));
    }
    return obj;
}

QList<OAILanguageItem> OAILanguageList::getLanguages() const {
    return m_languages;
}
void OAILanguageList::setLanguages(const QList<OAILanguageItem> &languages) {
    m_languages = languages;
    m_languages_isSet = true;
}

bool OAILanguageList::is_languages_Set() const{
    return m_languages_isSet;
}

bool OAILanguageList::is_languages_Valid() const{
    return m_languages_isValid;
}

qint32 OAILanguageList::getNoOfPages() const {
    return m_no_of_pages;
}
void OAILanguageList::setNoOfPages(const qint32 &no_of_pages) {
    m_no_of_pages = no_of_pages;
    m_no_of_pages_isSet = true;
}

bool OAILanguageList::is_no_of_pages_Set() const{
    return m_no_of_pages_isSet;
}

bool OAILanguageList::is_no_of_pages_Valid() const{
    return m_no_of_pages_isValid;
}

qint32 OAILanguageList::getPage() const {
    return m_page;
}
void OAILanguageList::setPage(const qint32 &page) {
    m_page = page;
    m_page_isSet = true;
}

bool OAILanguageList::is_page_Set() const{
    return m_page_isSet;
}

bool OAILanguageList::is_page_Valid() const{
    return m_page_isValid;
}

qint32 OAILanguageList::getPageSize() const {
    return m_page_size;
}
void OAILanguageList::setPageSize(const qint32 &page_size) {
    m_page_size = page_size;
    m_page_size_isSet = true;
}

bool OAILanguageList::is_page_size_Set() const{
    return m_page_size_isSet;
}

bool OAILanguageList::is_page_size_Valid() const{
    return m_page_size_isValid;
}

qint32 OAILanguageList::getTotal() const {
    return m_total;
}
void OAILanguageList::setTotal(const qint32 &total) {
    m_total = total;
    m_total_isSet = true;
}

bool OAILanguageList::is_total_Set() const{
    return m_total_isSet;
}

bool OAILanguageList::is_total_Valid() const{
    return m_total_isValid;
}

bool OAILanguageList::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_languages.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_no_of_pages_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_page_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_page_size_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAILanguageList::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
