/**
 * Fire Financial Services Business API
 * The fire.com API allows you to deeply integrate Business Account features into your application or back-office systems.  The API provides read access to your profile, accounts and transactions, event-driven notifications of activity on the account and payment initiation via batches. Each feature has its own HTTP endpoint and every endpoint has its own permission.   The API exposes 3 main areas of functionality: financial functions, service information and service configuration. ## Financial Functions These functions provide access to your account details, transactions, payee accounts, payment initiation etc. ## Service Functions These provide information about the fees and limits applied to your account. ## Service configuration These provide information about your service configs - applications, webhooks, API tokens, etc. 
 *
 * The version of the OpenAPI document: 1.0
 * Contact: api@fire.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIBatchApprovers.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIBatchApprovers::OAIBatchApprovers(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIBatchApprovers::OAIBatchApprovers() {
    this->initializeModel();
}

OAIBatchApprovers::~OAIBatchApprovers() {}

void OAIBatchApprovers::initializeModel() {

    m_approvals_isSet = false;
    m_approvals_isValid = false;
}

void OAIBatchApprovers::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIBatchApprovers::fromJsonObject(QJsonObject json) {

    m_approvals_isValid = ::OpenAPI::fromJsonValue(m_approvals, json[QString("approvals")]);
    m_approvals_isSet = !json[QString("approvals")].isNull() && m_approvals_isValid;
}

QString OAIBatchApprovers::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIBatchApprovers::asJsonObject() const {
    QJsonObject obj;
    if (m_approvals.size() > 0) {
        obj.insert(QString("approvals"), ::OpenAPI::toJsonValue(m_approvals));
    }
    return obj;
}

QList<OAIBatchApprovers_approvals_inner> OAIBatchApprovers::getApprovals() const {
    return m_approvals;
}
void OAIBatchApprovers::setApprovals(const QList<OAIBatchApprovers_approvals_inner> &approvals) {
    m_approvals = approvals;
    m_approvals_isSet = true;
}

bool OAIBatchApprovers::is_approvals_Set() const{
    return m_approvals_isSet;
}

bool OAIBatchApprovers::is_approvals_Valid() const{
    return m_approvals_isValid;
}

bool OAIBatchApprovers::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_approvals.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIBatchApprovers::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
