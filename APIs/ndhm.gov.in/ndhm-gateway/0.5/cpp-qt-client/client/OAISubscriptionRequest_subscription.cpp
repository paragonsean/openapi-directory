/**
 * Gateway
 * Gateway is the hub that routes/orchestrates the interaction between consent managers and API bridges. There are 5 categories of APIs; discovery, link, consent flow, data flow and  monitoring. To reflect the consumers of APIs, the above apis are also categorized under cm facing, hiu facing and hip facing  
 *
 * The version of the OpenAPI document: 0.5
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAISubscriptionRequest_subscription.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISubscriptionRequest_subscription::OAISubscriptionRequest_subscription(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISubscriptionRequest_subscription::OAISubscriptionRequest_subscription() {
    this->initializeModel();
}

OAISubscriptionRequest_subscription::~OAISubscriptionRequest_subscription() {}

void OAISubscriptionRequest_subscription::initializeModel() {

    m_categories_isSet = false;
    m_categories_isValid = false;

    m_hips_isSet = false;
    m_hips_isValid = false;

    m_hiu_isSet = false;
    m_hiu_isValid = false;

    m_patient_isSet = false;
    m_patient_isValid = false;

    m_period_isSet = false;
    m_period_isValid = false;

    m_purpose_isSet = false;
    m_purpose_isValid = false;
}

void OAISubscriptionRequest_subscription::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISubscriptionRequest_subscription::fromJsonObject(QJsonObject json) {

    m_categories_isValid = ::OpenAPI::fromJsonValue(m_categories, json[QString("categories")]);
    m_categories_isSet = !json[QString("categories")].isNull() && m_categories_isValid;

    m_hips_isValid = ::OpenAPI::fromJsonValue(m_hips, json[QString("hips")]);
    m_hips_isSet = !json[QString("hips")].isNull() && m_hips_isValid;

    m_hiu_isValid = ::OpenAPI::fromJsonValue(m_hiu, json[QString("hiu")]);
    m_hiu_isSet = !json[QString("hiu")].isNull() && m_hiu_isValid;

    m_patient_isValid = ::OpenAPI::fromJsonValue(m_patient, json[QString("patient")]);
    m_patient_isSet = !json[QString("patient")].isNull() && m_patient_isValid;

    m_period_isValid = ::OpenAPI::fromJsonValue(m_period, json[QString("period")]);
    m_period_isSet = !json[QString("period")].isNull() && m_period_isValid;

    m_purpose_isValid = ::OpenAPI::fromJsonValue(m_purpose, json[QString("purpose")]);
    m_purpose_isSet = !json[QString("purpose")].isNull() && m_purpose_isValid;
}

QString OAISubscriptionRequest_subscription::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISubscriptionRequest_subscription::asJsonObject() const {
    QJsonObject obj;
    if (m_categories.size() > 0) {
        obj.insert(QString("categories"), ::OpenAPI::toJsonValue(m_categories));
    }
    if (m_hips.size() > 0) {
        obj.insert(QString("hips"), ::OpenAPI::toJsonValue(m_hips));
    }
    if (m_hiu.isSet()) {
        obj.insert(QString("hiu"), ::OpenAPI::toJsonValue(m_hiu));
    }
    if (m_patient.isSet()) {
        obj.insert(QString("patient"), ::OpenAPI::toJsonValue(m_patient));
    }
    if (m_period.isSet()) {
        obj.insert(QString("period"), ::OpenAPI::toJsonValue(m_period));
    }
    if (m_purpose.isSet()) {
        obj.insert(QString("purpose"), ::OpenAPI::toJsonValue(m_purpose));
    }
    return obj;
}

QList<OAISubscriptionCategory> OAISubscriptionRequest_subscription::getCategories() const {
    return m_categories;
}
void OAISubscriptionRequest_subscription::setCategories(const QList<OAISubscriptionCategory> &categories) {
    m_categories = categories;
    m_categories_isSet = true;
}

bool OAISubscriptionRequest_subscription::is_categories_Set() const{
    return m_categories_isSet;
}

bool OAISubscriptionRequest_subscription::is_categories_Valid() const{
    return m_categories_isValid;
}

QList<OAIOrganizationRepresentation> OAISubscriptionRequest_subscription::getHips() const {
    return m_hips;
}
void OAISubscriptionRequest_subscription::setHips(const QList<OAIOrganizationRepresentation> &hips) {
    m_hips = hips;
    m_hips_isSet = true;
}

bool OAISubscriptionRequest_subscription::is_hips_Set() const{
    return m_hips_isSet;
}

bool OAISubscriptionRequest_subscription::is_hips_Valid() const{
    return m_hips_isValid;
}

OAIOrganizationRepresentation OAISubscriptionRequest_subscription::getHiu() const {
    return m_hiu;
}
void OAISubscriptionRequest_subscription::setHiu(const OAIOrganizationRepresentation &hiu) {
    m_hiu = hiu;
    m_hiu_isSet = true;
}

bool OAISubscriptionRequest_subscription::is_hiu_Set() const{
    return m_hiu_isSet;
}

bool OAISubscriptionRequest_subscription::is_hiu_Valid() const{
    return m_hiu_isValid;
}

OAIConsentManagerPatientID OAISubscriptionRequest_subscription::getPatient() const {
    return m_patient;
}
void OAISubscriptionRequest_subscription::setPatient(const OAIConsentManagerPatientID &patient) {
    m_patient = patient;
    m_patient_isSet = true;
}

bool OAISubscriptionRequest_subscription::is_patient_Set() const{
    return m_patient_isSet;
}

bool OAISubscriptionRequest_subscription::is_patient_Valid() const{
    return m_patient_isValid;
}

OAISubscriptionPeriod OAISubscriptionRequest_subscription::getPeriod() const {
    return m_period;
}
void OAISubscriptionRequest_subscription::setPeriod(const OAISubscriptionPeriod &period) {
    m_period = period;
    m_period_isSet = true;
}

bool OAISubscriptionRequest_subscription::is_period_Set() const{
    return m_period_isSet;
}

bool OAISubscriptionRequest_subscription::is_period_Valid() const{
    return m_period_isValid;
}

OAIUsePurpose OAISubscriptionRequest_subscription::getPurpose() const {
    return m_purpose;
}
void OAISubscriptionRequest_subscription::setPurpose(const OAIUsePurpose &purpose) {
    m_purpose = purpose;
    m_purpose_isSet = true;
}

bool OAISubscriptionRequest_subscription::is_purpose_Set() const{
    return m_purpose_isSet;
}

bool OAISubscriptionRequest_subscription::is_purpose_Valid() const{
    return m_purpose_isValid;
}

bool OAISubscriptionRequest_subscription::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_categories.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_hips.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_hiu.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_patient.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_period.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_purpose.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISubscriptionRequest_subscription::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_categories_isValid && m_hiu_isValid && m_patient_isValid && m_period_isValid && m_purpose_isValid && true;
}

} // namespace OpenAPI
