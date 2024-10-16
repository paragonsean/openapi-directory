/**
 * GOV.UK Pay API
 * GOV.UK Pay API (This version is no longer maintained. See openapi/publicapi_spec.json for latest API specification)
 *
 * The version of the OpenAPI document: 1.0.3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAISearchNavigationLinks.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISearchNavigationLinks::OAISearchNavigationLinks(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISearchNavigationLinks::OAISearchNavigationLinks() {
    this->initializeModel();
}

OAISearchNavigationLinks::~OAISearchNavigationLinks() {}

void OAISearchNavigationLinks::initializeModel() {

    m_first_page_isSet = false;
    m_first_page_isValid = false;

    m_last_page_isSet = false;
    m_last_page_isValid = false;

    m_next_page_isSet = false;
    m_next_page_isValid = false;

    m_prev_page_isSet = false;
    m_prev_page_isValid = false;

    m_self_isSet = false;
    m_self_isValid = false;
}

void OAISearchNavigationLinks::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISearchNavigationLinks::fromJsonObject(QJsonObject json) {

    m_first_page_isValid = ::OpenAPI::fromJsonValue(m_first_page, json[QString("first_page")]);
    m_first_page_isSet = !json[QString("first_page")].isNull() && m_first_page_isValid;

    m_last_page_isValid = ::OpenAPI::fromJsonValue(m_last_page, json[QString("last_page")]);
    m_last_page_isSet = !json[QString("last_page")].isNull() && m_last_page_isValid;

    m_next_page_isValid = ::OpenAPI::fromJsonValue(m_next_page, json[QString("next_page")]);
    m_next_page_isSet = !json[QString("next_page")].isNull() && m_next_page_isValid;

    m_prev_page_isValid = ::OpenAPI::fromJsonValue(m_prev_page, json[QString("prev_page")]);
    m_prev_page_isSet = !json[QString("prev_page")].isNull() && m_prev_page_isValid;

    m_self_isValid = ::OpenAPI::fromJsonValue(m_self, json[QString("self")]);
    m_self_isSet = !json[QString("self")].isNull() && m_self_isValid;
}

QString OAISearchNavigationLinks::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISearchNavigationLinks::asJsonObject() const {
    QJsonObject obj;
    if (m_first_page.isSet()) {
        obj.insert(QString("first_page"), ::OpenAPI::toJsonValue(m_first_page));
    }
    if (m_last_page.isSet()) {
        obj.insert(QString("last_page"), ::OpenAPI::toJsonValue(m_last_page));
    }
    if (m_next_page.isSet()) {
        obj.insert(QString("next_page"), ::OpenAPI::toJsonValue(m_next_page));
    }
    if (m_prev_page.isSet()) {
        obj.insert(QString("prev_page"), ::OpenAPI::toJsonValue(m_prev_page));
    }
    if (m_self.isSet()) {
        obj.insert(QString("self"), ::OpenAPI::toJsonValue(m_self));
    }
    return obj;
}

OAILink OAISearchNavigationLinks::getFirstPage() const {
    return m_first_page;
}
void OAISearchNavigationLinks::setFirstPage(const OAILink &first_page) {
    m_first_page = first_page;
    m_first_page_isSet = true;
}

bool OAISearchNavigationLinks::is_first_page_Set() const{
    return m_first_page_isSet;
}

bool OAISearchNavigationLinks::is_first_page_Valid() const{
    return m_first_page_isValid;
}

OAILink OAISearchNavigationLinks::getLastPage() const {
    return m_last_page;
}
void OAISearchNavigationLinks::setLastPage(const OAILink &last_page) {
    m_last_page = last_page;
    m_last_page_isSet = true;
}

bool OAISearchNavigationLinks::is_last_page_Set() const{
    return m_last_page_isSet;
}

bool OAISearchNavigationLinks::is_last_page_Valid() const{
    return m_last_page_isValid;
}

OAILink OAISearchNavigationLinks::getNextPage() const {
    return m_next_page;
}
void OAISearchNavigationLinks::setNextPage(const OAILink &next_page) {
    m_next_page = next_page;
    m_next_page_isSet = true;
}

bool OAISearchNavigationLinks::is_next_page_Set() const{
    return m_next_page_isSet;
}

bool OAISearchNavigationLinks::is_next_page_Valid() const{
    return m_next_page_isValid;
}

OAILink OAISearchNavigationLinks::getPrevPage() const {
    return m_prev_page;
}
void OAISearchNavigationLinks::setPrevPage(const OAILink &prev_page) {
    m_prev_page = prev_page;
    m_prev_page_isSet = true;
}

bool OAISearchNavigationLinks::is_prev_page_Set() const{
    return m_prev_page_isSet;
}

bool OAISearchNavigationLinks::is_prev_page_Valid() const{
    return m_prev_page_isValid;
}

OAILink OAISearchNavigationLinks::getSelf() const {
    return m_self;
}
void OAISearchNavigationLinks::setSelf(const OAILink &self) {
    m_self = self;
    m_self_isSet = true;
}

bool OAISearchNavigationLinks::is_self_Set() const{
    return m_self_isSet;
}

bool OAISearchNavigationLinks::is_self_Valid() const{
    return m_self_isValid;
}

bool OAISearchNavigationLinks::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_first_page.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_page.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_next_page.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_prev_page.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_self.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISearchNavigationLinks::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
