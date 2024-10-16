/**
 * Travel Partner API
 * The Travel Partner API provides you with a RESTful interface to the Google Hotel Center platform. It enables an app to efficiently retrieve and change Hotel Center data, and is thus suitable for managing large or complex accounts.
 *
 * The version of the OpenAPI document: v3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIListReconciliationReportsResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIListReconciliationReportsResponse::OAIListReconciliationReportsResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIListReconciliationReportsResponse::OAIListReconciliationReportsResponse() {
    this->initializeModel();
}

OAIListReconciliationReportsResponse::~OAIListReconciliationReportsResponse() {}

void OAIListReconciliationReportsResponse::initializeModel() {

    m_reconciliation_reports_isSet = false;
    m_reconciliation_reports_isValid = false;
}

void OAIListReconciliationReportsResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIListReconciliationReportsResponse::fromJsonObject(QJsonObject json) {

    m_reconciliation_reports_isValid = ::OpenAPI::fromJsonValue(m_reconciliation_reports, json[QString("reconciliationReports")]);
    m_reconciliation_reports_isSet = !json[QString("reconciliationReports")].isNull() && m_reconciliation_reports_isValid;
}

QString OAIListReconciliationReportsResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIListReconciliationReportsResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_reconciliation_reports.size() > 0) {
        obj.insert(QString("reconciliationReports"), ::OpenAPI::toJsonValue(m_reconciliation_reports));
    }
    return obj;
}

QList<OAIReconciliationReport> OAIListReconciliationReportsResponse::getReconciliationReports() const {
    return m_reconciliation_reports;
}
void OAIListReconciliationReportsResponse::setReconciliationReports(const QList<OAIReconciliationReport> &reconciliation_reports) {
    m_reconciliation_reports = reconciliation_reports;
    m_reconciliation_reports_isSet = true;
}

bool OAIListReconciliationReportsResponse::is_reconciliation_reports_Set() const{
    return m_reconciliation_reports_isSet;
}

bool OAIListReconciliationReportsResponse::is_reconciliation_reports_Valid() const{
    return m_reconciliation_reports_isValid;
}

bool OAIListReconciliationReportsResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_reconciliation_reports.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIListReconciliationReportsResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
