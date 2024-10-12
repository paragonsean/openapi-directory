/**
 * AGCO API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAuthorizationCodes_Shared_Models_Category.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAuthorizationCodes_Shared_Models_Category::OAIAuthorizationCodes_Shared_Models_Category(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAuthorizationCodes_Shared_Models_Category::OAIAuthorizationCodes_Shared_Models_Category() {
    this->initializeModel();
}

OAIAuthorizationCodes_Shared_Models_Category::~OAIAuthorizationCodes_Shared_Models_Category() {}

void OAIAuthorizationCodes_Shared_Models_Category::initializeModel() {

    m_description_isSet = false;
    m_description_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;
}

void OAIAuthorizationCodes_Shared_Models_Category::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAuthorizationCodes_Shared_Models_Category::fromJsonObject(QJsonObject json) {

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("Description")]);
    m_description_isSet = !json[QString("Description")].isNull() && m_description_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("ID")]);
    m_id_isSet = !json[QString("ID")].isNull() && m_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("Name")]);
    m_name_isSet = !json[QString("Name")].isNull() && m_name_isValid;
}

QString OAIAuthorizationCodes_Shared_Models_Category::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAuthorizationCodes_Shared_Models_Category::asJsonObject() const {
    QJsonObject obj;
    if (m_description_isSet) {
        obj.insert(QString("Description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_id_isSet) {
        obj.insert(QString("ID"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("Name"), ::OpenAPI::toJsonValue(m_name));
    }
    return obj;
}

QString OAIAuthorizationCodes_Shared_Models_Category::getDescription() const {
    return m_description;
}
void OAIAuthorizationCodes_Shared_Models_Category::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIAuthorizationCodes_Shared_Models_Category::is_description_Set() const{
    return m_description_isSet;
}

bool OAIAuthorizationCodes_Shared_Models_Category::is_description_Valid() const{
    return m_description_isValid;
}

QString OAIAuthorizationCodes_Shared_Models_Category::getId() const {
    return m_id;
}
void OAIAuthorizationCodes_Shared_Models_Category::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIAuthorizationCodes_Shared_Models_Category::is_id_Set() const{
    return m_id_isSet;
}

bool OAIAuthorizationCodes_Shared_Models_Category::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIAuthorizationCodes_Shared_Models_Category::getName() const {
    return m_name;
}
void OAIAuthorizationCodes_Shared_Models_Category::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIAuthorizationCodes_Shared_Models_Category::is_name_Set() const{
    return m_name_isSet;
}

bool OAIAuthorizationCodes_Shared_Models_Category::is_name_Valid() const{
    return m_name_isValid;
}

bool OAIAuthorizationCodes_Shared_Models_Category::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_description_isSet) {
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

bool OAIAuthorizationCodes_Shared_Models_Category::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
