/**
 * Authorized Partner API Specification
 * To access files in user’s DigiLocker account from your application, you must first obtain user’s authorization.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: support@digitallocker.gov.in
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIEaadharXamlSchema_KycRes_Signature_SignedInfo_CanonicalizationMethod.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIEaadharXamlSchema_KycRes_Signature_SignedInfo_CanonicalizationMethod::OAIEaadharXamlSchema_KycRes_Signature_SignedInfo_CanonicalizationMethod(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIEaadharXamlSchema_KycRes_Signature_SignedInfo_CanonicalizationMethod::OAIEaadharXamlSchema_KycRes_Signature_SignedInfo_CanonicalizationMethod() {
    this->initializeModel();
}

OAIEaadharXamlSchema_KycRes_Signature_SignedInfo_CanonicalizationMethod::~OAIEaadharXamlSchema_KycRes_Signature_SignedInfo_CanonicalizationMethod() {}

void OAIEaadharXamlSchema_KycRes_Signature_SignedInfo_CanonicalizationMethod::initializeModel() {

    m_algorithm_isSet = false;
    m_algorithm_isValid = false;
}

void OAIEaadharXamlSchema_KycRes_Signature_SignedInfo_CanonicalizationMethod::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIEaadharXamlSchema_KycRes_Signature_SignedInfo_CanonicalizationMethod::fromJsonObject(QJsonObject json) {

    m_algorithm_isValid = ::OpenAPI::fromJsonValue(m_algorithm, json[QString("Algorithm")]);
    m_algorithm_isSet = !json[QString("Algorithm")].isNull() && m_algorithm_isValid;
}

QString OAIEaadharXamlSchema_KycRes_Signature_SignedInfo_CanonicalizationMethod::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIEaadharXamlSchema_KycRes_Signature_SignedInfo_CanonicalizationMethod::asJsonObject() const {
    QJsonObject obj;
    if (m_algorithm_isSet) {
        obj.insert(QString("Algorithm"), ::OpenAPI::toJsonValue(m_algorithm));
    }
    return obj;
}

QString OAIEaadharXamlSchema_KycRes_Signature_SignedInfo_CanonicalizationMethod::getAlgorithm() const {
    return m_algorithm;
}
void OAIEaadharXamlSchema_KycRes_Signature_SignedInfo_CanonicalizationMethod::setAlgorithm(const QString &algorithm) {
    m_algorithm = algorithm;
    m_algorithm_isSet = true;
}

bool OAIEaadharXamlSchema_KycRes_Signature_SignedInfo_CanonicalizationMethod::is_algorithm_Set() const{
    return m_algorithm_isSet;
}

bool OAIEaadharXamlSchema_KycRes_Signature_SignedInfo_CanonicalizationMethod::is_algorithm_Valid() const{
    return m_algorithm_isValid;
}

bool OAIEaadharXamlSchema_KycRes_Signature_SignedInfo_CanonicalizationMethod::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_algorithm_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIEaadharXamlSchema_KycRes_Signature_SignedInfo_CanonicalizationMethod::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_algorithm_isValid && true;
}

} // namespace OpenAPI
