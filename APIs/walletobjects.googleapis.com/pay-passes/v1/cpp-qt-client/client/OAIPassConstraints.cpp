/**
 * Google Pay Passes API
 * API for issuers to save and manage Google Wallet Objects.
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIPassConstraints.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPassConstraints::OAIPassConstraints(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPassConstraints::OAIPassConstraints() {
    this->initializeModel();
}

OAIPassConstraints::~OAIPassConstraints() {}

void OAIPassConstraints::initializeModel() {

    m_nfc_constraint_isSet = false;
    m_nfc_constraint_isValid = false;

    m_screenshot_eligibility_isSet = false;
    m_screenshot_eligibility_isValid = false;
}

void OAIPassConstraints::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPassConstraints::fromJsonObject(QJsonObject json) {

    m_nfc_constraint_isValid = ::OpenAPI::fromJsonValue(m_nfc_constraint, json[QString("nfcConstraint")]);
    m_nfc_constraint_isSet = !json[QString("nfcConstraint")].isNull() && m_nfc_constraint_isValid;

    m_screenshot_eligibility_isValid = ::OpenAPI::fromJsonValue(m_screenshot_eligibility, json[QString("screenshotEligibility")]);
    m_screenshot_eligibility_isSet = !json[QString("screenshotEligibility")].isNull() && m_screenshot_eligibility_isValid;
}

QString OAIPassConstraints::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPassConstraints::asJsonObject() const {
    QJsonObject obj;
    if (m_nfc_constraint.size() > 0) {
        obj.insert(QString("nfcConstraint"), ::OpenAPI::toJsonValue(m_nfc_constraint));
    }
    if (m_screenshot_eligibility_isSet) {
        obj.insert(QString("screenshotEligibility"), ::OpenAPI::toJsonValue(m_screenshot_eligibility));
    }
    return obj;
}

QList<QString> OAIPassConstraints::getNfcConstraint() const {
    return m_nfc_constraint;
}
void OAIPassConstraints::setNfcConstraint(const QList<QString> &nfc_constraint) {
    m_nfc_constraint = nfc_constraint;
    m_nfc_constraint_isSet = true;
}

bool OAIPassConstraints::is_nfc_constraint_Set() const{
    return m_nfc_constraint_isSet;
}

bool OAIPassConstraints::is_nfc_constraint_Valid() const{
    return m_nfc_constraint_isValid;
}

QString OAIPassConstraints::getScreenshotEligibility() const {
    return m_screenshot_eligibility;
}
void OAIPassConstraints::setScreenshotEligibility(const QString &screenshot_eligibility) {
    m_screenshot_eligibility = screenshot_eligibility;
    m_screenshot_eligibility_isSet = true;
}

bool OAIPassConstraints::is_screenshot_eligibility_Set() const{
    return m_screenshot_eligibility_isSet;
}

bool OAIPassConstraints::is_screenshot_eligibility_Valid() const{
    return m_screenshot_eligibility_isValid;
}

bool OAIPassConstraints::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_nfc_constraint.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_screenshot_eligibility_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPassConstraints::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
