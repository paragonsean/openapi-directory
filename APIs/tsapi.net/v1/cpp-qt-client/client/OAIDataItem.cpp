/**
 * TSAPI
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIDataItem.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIDataItem::OAIDataItem(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIDataItem::OAIDataItem() {
    this->initializeModel();
}

OAIDataItem::~OAIDataItem() {}

void OAIDataItem::initializeModel() {

    m_ident_isSet = false;
    m_ident_isValid = false;

    m_parent_ident_isSet = false;
    m_parent_ident_isValid = false;

    m_values_isSet = false;
    m_values_isValid = false;
}

void OAIDataItem::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIDataItem::fromJsonObject(QJsonObject json) {

    m_ident_isValid = ::OpenAPI::fromJsonValue(m_ident, json[QString("ident")]);
    m_ident_isSet = !json[QString("ident")].isNull() && m_ident_isValid;

    m_parent_ident_isValid = ::OpenAPI::fromJsonValue(m_parent_ident, json[QString("parentIdent")]);
    m_parent_ident_isSet = !json[QString("parentIdent")].isNull() && m_parent_ident_isValid;

    m_values_isValid = ::OpenAPI::fromJsonValue(m_values, json[QString("values")]);
    m_values_isSet = !json[QString("values")].isNull() && m_values_isValid;
}

QString OAIDataItem::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIDataItem::asJsonObject() const {
    QJsonObject obj;
    if (m_ident_isSet) {
        obj.insert(QString("ident"), ::OpenAPI::toJsonValue(m_ident));
    }
    if (m_parent_ident.isSet()) {
        obj.insert(QString("parentIdent"), ::OpenAPI::toJsonValue(m_parent_ident));
    }
    if (m_values.size() > 0) {
        obj.insert(QString("values"), ::OpenAPI::toJsonValue(m_values));
    }
    return obj;
}

QString OAIDataItem::getIdent() const {
    return m_ident;
}
void OAIDataItem::setIdent(const QString &ident) {
    m_ident = ident;
    m_ident_isSet = true;
}

bool OAIDataItem::is_ident_Set() const{
    return m_ident_isSet;
}

bool OAIDataItem::is_ident_Valid() const{
    return m_ident_isValid;
}

OAIParentRef OAIDataItem::getParentIdent() const {
    return m_parent_ident;
}
void OAIDataItem::setParentIdent(const OAIParentRef &parent_ident) {
    m_parent_ident = parent_ident;
    m_parent_ident_isSet = true;
}

bool OAIDataItem::is_parent_ident_Set() const{
    return m_parent_ident_isSet;
}

bool OAIDataItem::is_parent_ident_Valid() const{
    return m_parent_ident_isValid;
}

QList<QString> OAIDataItem::getValues() const {
    return m_values;
}
void OAIDataItem::setValues(const QList<QString> &values) {
    m_values = values;
    m_values_isSet = true;
}

bool OAIDataItem::is_values_Set() const{
    return m_values_isSet;
}

bool OAIDataItem::is_values_Valid() const{
    return m_values_isValid;
}

bool OAIDataItem::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_ident_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_parent_ident.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_values.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIDataItem::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
