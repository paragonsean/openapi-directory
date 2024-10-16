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

#include "OAIAuthorizationCodes_Shared_Models_CodeValidationModel.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAuthorizationCodes_Shared_Models_CodeValidationModel::OAIAuthorizationCodes_Shared_Models_CodeValidationModel(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAuthorizationCodes_Shared_Models_CodeValidationModel::OAIAuthorizationCodes_Shared_Models_CodeValidationModel() {
    this->initializeModel();
}

OAIAuthorizationCodes_Shared_Models_CodeValidationModel::~OAIAuthorizationCodes_Shared_Models_CodeValidationModel() {}

void OAIAuthorizationCodes_Shared_Models_CodeValidationModel::initializeModel() {

    m_expiration_date_isSet = false;
    m_expiration_date_isValid = false;

    m_is_valid_isSet = false;
    m_is_valid_isValid = false;
}

void OAIAuthorizationCodes_Shared_Models_CodeValidationModel::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAuthorizationCodes_Shared_Models_CodeValidationModel::fromJsonObject(QJsonObject json) {

    m_expiration_date_isValid = ::OpenAPI::fromJsonValue(m_expiration_date, json[QString("ExpirationDate")]);
    m_expiration_date_isSet = !json[QString("ExpirationDate")].isNull() && m_expiration_date_isValid;

    m_is_valid_isValid = ::OpenAPI::fromJsonValue(m_is_valid, json[QString("IsValid")]);
    m_is_valid_isSet = !json[QString("IsValid")].isNull() && m_is_valid_isValid;
}

QString OAIAuthorizationCodes_Shared_Models_CodeValidationModel::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAuthorizationCodes_Shared_Models_CodeValidationModel::asJsonObject() const {
    QJsonObject obj;
    if (m_expiration_date_isSet) {
        obj.insert(QString("ExpirationDate"), ::OpenAPI::toJsonValue(m_expiration_date));
    }
    if (m_is_valid_isSet) {
        obj.insert(QString("IsValid"), ::OpenAPI::toJsonValue(m_is_valid));
    }
    return obj;
}

QDateTime OAIAuthorizationCodes_Shared_Models_CodeValidationModel::getExpirationDate() const {
    return m_expiration_date;
}
void OAIAuthorizationCodes_Shared_Models_CodeValidationModel::setExpirationDate(const QDateTime &expiration_date) {
    m_expiration_date = expiration_date;
    m_expiration_date_isSet = true;
}

bool OAIAuthorizationCodes_Shared_Models_CodeValidationModel::is_expiration_date_Set() const{
    return m_expiration_date_isSet;
}

bool OAIAuthorizationCodes_Shared_Models_CodeValidationModel::is_expiration_date_Valid() const{
    return m_expiration_date_isValid;
}

bool OAIAuthorizationCodes_Shared_Models_CodeValidationModel::isIsValid() const {
    return m_is_valid;
}
void OAIAuthorizationCodes_Shared_Models_CodeValidationModel::setIsValid(const bool &is_valid) {
    m_is_valid = is_valid;
    m_is_valid_isSet = true;
}

bool OAIAuthorizationCodes_Shared_Models_CodeValidationModel::is_is_valid_Set() const{
    return m_is_valid_isSet;
}

bool OAIAuthorizationCodes_Shared_Models_CodeValidationModel::is_is_valid_Valid() const{
    return m_is_valid_isValid;
}

bool OAIAuthorizationCodes_Shared_Models_CodeValidationModel::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_expiration_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_valid_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAuthorizationCodes_Shared_Models_CodeValidationModel::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
