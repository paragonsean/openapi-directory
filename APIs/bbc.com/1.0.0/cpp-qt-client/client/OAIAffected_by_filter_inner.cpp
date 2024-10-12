/**
 * BBC Nitro API
 * BBC Nitro is the BBC's application programming interface (API) for BBC Programmes Metadata.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: nitro@bbc.co.uk
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAffected_by_filter_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAffected_by_filter_inner::OAIAffected_by_filter_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAffected_by_filter_inner::OAIAffected_by_filter_inner() {
    this->initializeModel();
}

OAIAffected_by_filter_inner::~OAIAffected_by_filter_inner() {}

void OAIAffected_by_filter_inner::initializeModel() {

    m_description_isSet = false;
    m_description_isValid = false;

    m_filter_isSet = false;
    m_filter_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;
}

void OAIAffected_by_filter_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAffected_by_filter_inner::fromJsonObject(QJsonObject json) {

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_filter_isValid = ::OpenAPI::fromJsonValue(m_filter, json[QString("filter")]);
    m_filter_isSet = !json[QString("filter")].isNull() && m_filter_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;
}

QString OAIAffected_by_filter_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAffected_by_filter_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_filter.size() > 0) {
        obj.insert(QString("filter"), ::OpenAPI::toJsonValue(m_filter));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    return obj;
}

QString OAIAffected_by_filter_inner::getDescription() const {
    return m_description;
}
void OAIAffected_by_filter_inner::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIAffected_by_filter_inner::is_description_Set() const{
    return m_description_isSet;
}

bool OAIAffected_by_filter_inner::is_description_Valid() const{
    return m_description_isValid;
}

QList<OAIAffected_by_filter_inner_filter_inner> OAIAffected_by_filter_inner::getFilter() const {
    return m_filter;
}
void OAIAffected_by_filter_inner::setFilter(const QList<OAIAffected_by_filter_inner_filter_inner> &filter) {
    m_filter = filter;
    m_filter_isSet = true;
}

bool OAIAffected_by_filter_inner::is_filter_Set() const{
    return m_filter_isSet;
}

bool OAIAffected_by_filter_inner::is_filter_Valid() const{
    return m_filter_isValid;
}

QString OAIAffected_by_filter_inner::getName() const {
    return m_name;
}
void OAIAffected_by_filter_inner::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIAffected_by_filter_inner::is_name_Set() const{
    return m_name_isSet;
}

bool OAIAffected_by_filter_inner::is_name_Valid() const{
    return m_name_isValid;
}

bool OAIAffected_by_filter_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_filter.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAffected_by_filter_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_description_isValid && m_name_isValid && true;
}

} // namespace OpenAPI
