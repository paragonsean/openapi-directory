/**
 * Personnel Data
 * API for reading and writing personnel data incl. data about attendances and absences
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAbsenceEntitlement_value_inner_attributes.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAbsenceEntitlement_value_inner_attributes::OAIAbsenceEntitlement_value_inner_attributes(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAbsenceEntitlement_value_inner_attributes::OAIAbsenceEntitlement_value_inner_attributes() {
    this->initializeModel();
}

OAIAbsenceEntitlement_value_inner_attributes::~OAIAbsenceEntitlement_value_inner_attributes() {}

void OAIAbsenceEntitlement_value_inner_attributes::initializeModel() {

    m_entitlement_isSet = false;
    m_entitlement_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;
}

void OAIAbsenceEntitlement_value_inner_attributes::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAbsenceEntitlement_value_inner_attributes::fromJsonObject(QJsonObject json) {

    m_entitlement_isValid = ::OpenAPI::fromJsonValue(m_entitlement, json[QString("entitlement")]);
    m_entitlement_isSet = !json[QString("entitlement")].isNull() && m_entitlement_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;
}

QString OAIAbsenceEntitlement_value_inner_attributes::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAbsenceEntitlement_value_inner_attributes::asJsonObject() const {
    QJsonObject obj;
    if (m_entitlement_isSet) {
        obj.insert(QString("entitlement"), ::OpenAPI::toJsonValue(m_entitlement));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    return obj;
}

double OAIAbsenceEntitlement_value_inner_attributes::getEntitlement() const {
    return m_entitlement;
}
void OAIAbsenceEntitlement_value_inner_attributes::setEntitlement(const double &entitlement) {
    m_entitlement = entitlement;
    m_entitlement_isSet = true;
}

bool OAIAbsenceEntitlement_value_inner_attributes::is_entitlement_Set() const{
    return m_entitlement_isSet;
}

bool OAIAbsenceEntitlement_value_inner_attributes::is_entitlement_Valid() const{
    return m_entitlement_isValid;
}

qint32 OAIAbsenceEntitlement_value_inner_attributes::getId() const {
    return m_id;
}
void OAIAbsenceEntitlement_value_inner_attributes::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIAbsenceEntitlement_value_inner_attributes::is_id_Set() const{
    return m_id_isSet;
}

bool OAIAbsenceEntitlement_value_inner_attributes::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIAbsenceEntitlement_value_inner_attributes::getName() const {
    return m_name;
}
void OAIAbsenceEntitlement_value_inner_attributes::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIAbsenceEntitlement_value_inner_attributes::is_name_Set() const{
    return m_name_isSet;
}

bool OAIAbsenceEntitlement_value_inner_attributes::is_name_Valid() const{
    return m_name_isValid;
}

bool OAIAbsenceEntitlement_value_inner_attributes::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_entitlement_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
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

bool OAIAbsenceEntitlement_value_inner_attributes::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
