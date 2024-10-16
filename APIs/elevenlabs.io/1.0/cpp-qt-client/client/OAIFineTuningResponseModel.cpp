/**
 * ElevenLabs API Documentation
 * This is the documentation for the ElevenLabs API. You can use this API to use our service programmatically, this is done by using your xi-api-key. <br/> You can view your xi-api-key using the 'Profile' tab on https://beta.elevenlabs.io. Our API is experimental so all endpoints are subject to change.
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIFineTuningResponseModel.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIFineTuningResponseModel::OAIFineTuningResponseModel(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIFineTuningResponseModel::OAIFineTuningResponseModel() {
    this->initializeModel();
}

OAIFineTuningResponseModel::~OAIFineTuningResponseModel() {}

void OAIFineTuningResponseModel::initializeModel() {

    m_fine_tuning_requested_isSet = false;
    m_fine_tuning_requested_isValid = false;

    m_finetuning_state_isSet = false;
    m_finetuning_state_isValid = false;

    m_is_allowed_to_fine_tune_isSet = false;
    m_is_allowed_to_fine_tune_isValid = false;

    m_model_id_isSet = false;
    m_model_id_isValid = false;

    m_slice_ids_isSet = false;
    m_slice_ids_isValid = false;

    m_verification_attempts_isSet = false;
    m_verification_attempts_isValid = false;

    m_verification_attempts_count_isSet = false;
    m_verification_attempts_count_isValid = false;

    m_verification_failures_isSet = false;
    m_verification_failures_isValid = false;
}

void OAIFineTuningResponseModel::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIFineTuningResponseModel::fromJsonObject(QJsonObject json) {

    m_fine_tuning_requested_isValid = ::OpenAPI::fromJsonValue(m_fine_tuning_requested, json[QString("fine_tuning_requested")]);
    m_fine_tuning_requested_isSet = !json[QString("fine_tuning_requested")].isNull() && m_fine_tuning_requested_isValid;

    m_finetuning_state_isValid = ::OpenAPI::fromJsonValue(m_finetuning_state, json[QString("finetuning_state")]);
    m_finetuning_state_isSet = !json[QString("finetuning_state")].isNull() && m_finetuning_state_isValid;

    m_is_allowed_to_fine_tune_isValid = ::OpenAPI::fromJsonValue(m_is_allowed_to_fine_tune, json[QString("is_allowed_to_fine_tune")]);
    m_is_allowed_to_fine_tune_isSet = !json[QString("is_allowed_to_fine_tune")].isNull() && m_is_allowed_to_fine_tune_isValid;

    m_model_id_isValid = ::OpenAPI::fromJsonValue(m_model_id, json[QString("model_id")]);
    m_model_id_isSet = !json[QString("model_id")].isNull() && m_model_id_isValid;

    m_slice_ids_isValid = ::OpenAPI::fromJsonValue(m_slice_ids, json[QString("slice_ids")]);
    m_slice_ids_isSet = !json[QString("slice_ids")].isNull() && m_slice_ids_isValid;

    m_verification_attempts_isValid = ::OpenAPI::fromJsonValue(m_verification_attempts, json[QString("verification_attempts")]);
    m_verification_attempts_isSet = !json[QString("verification_attempts")].isNull() && m_verification_attempts_isValid;

    m_verification_attempts_count_isValid = ::OpenAPI::fromJsonValue(m_verification_attempts_count, json[QString("verification_attempts_count")]);
    m_verification_attempts_count_isSet = !json[QString("verification_attempts_count")].isNull() && m_verification_attempts_count_isValid;

    m_verification_failures_isValid = ::OpenAPI::fromJsonValue(m_verification_failures, json[QString("verification_failures")]);
    m_verification_failures_isSet = !json[QString("verification_failures")].isNull() && m_verification_failures_isValid;
}

QString OAIFineTuningResponseModel::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIFineTuningResponseModel::asJsonObject() const {
    QJsonObject obj;
    if (m_fine_tuning_requested_isSet) {
        obj.insert(QString("fine_tuning_requested"), ::OpenAPI::toJsonValue(m_fine_tuning_requested));
    }
    if (m_finetuning_state_isSet) {
        obj.insert(QString("finetuning_state"), ::OpenAPI::toJsonValue(m_finetuning_state));
    }
    if (m_is_allowed_to_fine_tune_isSet) {
        obj.insert(QString("is_allowed_to_fine_tune"), ::OpenAPI::toJsonValue(m_is_allowed_to_fine_tune));
    }
    if (m_model_id_isSet) {
        obj.insert(QString("model_id"), ::OpenAPI::toJsonValue(m_model_id));
    }
    if (m_slice_ids.size() > 0) {
        obj.insert(QString("slice_ids"), ::OpenAPI::toJsonValue(m_slice_ids));
    }
    if (m_verification_attempts.size() > 0) {
        obj.insert(QString("verification_attempts"), ::OpenAPI::toJsonValue(m_verification_attempts));
    }
    if (m_verification_attempts_count_isSet) {
        obj.insert(QString("verification_attempts_count"), ::OpenAPI::toJsonValue(m_verification_attempts_count));
    }
    if (m_verification_failures.size() > 0) {
        obj.insert(QString("verification_failures"), ::OpenAPI::toJsonValue(m_verification_failures));
    }
    return obj;
}

bool OAIFineTuningResponseModel::isFineTuningRequested() const {
    return m_fine_tuning_requested;
}
void OAIFineTuningResponseModel::setFineTuningRequested(const bool &fine_tuning_requested) {
    m_fine_tuning_requested = fine_tuning_requested;
    m_fine_tuning_requested_isSet = true;
}

bool OAIFineTuningResponseModel::is_fine_tuning_requested_Set() const{
    return m_fine_tuning_requested_isSet;
}

bool OAIFineTuningResponseModel::is_fine_tuning_requested_Valid() const{
    return m_fine_tuning_requested_isValid;
}

QString OAIFineTuningResponseModel::getFinetuningState() const {
    return m_finetuning_state;
}
void OAIFineTuningResponseModel::setFinetuningState(const QString &finetuning_state) {
    m_finetuning_state = finetuning_state;
    m_finetuning_state_isSet = true;
}

bool OAIFineTuningResponseModel::is_finetuning_state_Set() const{
    return m_finetuning_state_isSet;
}

bool OAIFineTuningResponseModel::is_finetuning_state_Valid() const{
    return m_finetuning_state_isValid;
}

bool OAIFineTuningResponseModel::isIsAllowedToFineTune() const {
    return m_is_allowed_to_fine_tune;
}
void OAIFineTuningResponseModel::setIsAllowedToFineTune(const bool &is_allowed_to_fine_tune) {
    m_is_allowed_to_fine_tune = is_allowed_to_fine_tune;
    m_is_allowed_to_fine_tune_isSet = true;
}

bool OAIFineTuningResponseModel::is_is_allowed_to_fine_tune_Set() const{
    return m_is_allowed_to_fine_tune_isSet;
}

bool OAIFineTuningResponseModel::is_is_allowed_to_fine_tune_Valid() const{
    return m_is_allowed_to_fine_tune_isValid;
}

QString OAIFineTuningResponseModel::getModelId() const {
    return m_model_id;
}
void OAIFineTuningResponseModel::setModelId(const QString &model_id) {
    m_model_id = model_id;
    m_model_id_isSet = true;
}

bool OAIFineTuningResponseModel::is_model_id_Set() const{
    return m_model_id_isSet;
}

bool OAIFineTuningResponseModel::is_model_id_Valid() const{
    return m_model_id_isValid;
}

QList<QString> OAIFineTuningResponseModel::getSliceIds() const {
    return m_slice_ids;
}
void OAIFineTuningResponseModel::setSliceIds(const QList<QString> &slice_ids) {
    m_slice_ids = slice_ids;
    m_slice_ids_isSet = true;
}

bool OAIFineTuningResponseModel::is_slice_ids_Set() const{
    return m_slice_ids_isSet;
}

bool OAIFineTuningResponseModel::is_slice_ids_Valid() const{
    return m_slice_ids_isValid;
}

QList<OAIVerificationAttemptResponseModel> OAIFineTuningResponseModel::getVerificationAttempts() const {
    return m_verification_attempts;
}
void OAIFineTuningResponseModel::setVerificationAttempts(const QList<OAIVerificationAttemptResponseModel> &verification_attempts) {
    m_verification_attempts = verification_attempts;
    m_verification_attempts_isSet = true;
}

bool OAIFineTuningResponseModel::is_verification_attempts_Set() const{
    return m_verification_attempts_isSet;
}

bool OAIFineTuningResponseModel::is_verification_attempts_Valid() const{
    return m_verification_attempts_isValid;
}

qint32 OAIFineTuningResponseModel::getVerificationAttemptsCount() const {
    return m_verification_attempts_count;
}
void OAIFineTuningResponseModel::setVerificationAttemptsCount(const qint32 &verification_attempts_count) {
    m_verification_attempts_count = verification_attempts_count;
    m_verification_attempts_count_isSet = true;
}

bool OAIFineTuningResponseModel::is_verification_attempts_count_Set() const{
    return m_verification_attempts_count_isSet;
}

bool OAIFineTuningResponseModel::is_verification_attempts_count_Valid() const{
    return m_verification_attempts_count_isValid;
}

QList<QString> OAIFineTuningResponseModel::getVerificationFailures() const {
    return m_verification_failures;
}
void OAIFineTuningResponseModel::setVerificationFailures(const QList<QString> &verification_failures) {
    m_verification_failures = verification_failures;
    m_verification_failures_isSet = true;
}

bool OAIFineTuningResponseModel::is_verification_failures_Set() const{
    return m_verification_failures_isSet;
}

bool OAIFineTuningResponseModel::is_verification_failures_Valid() const{
    return m_verification_failures_isValid;
}

bool OAIFineTuningResponseModel::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_fine_tuning_requested_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_finetuning_state_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_allowed_to_fine_tune_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_model_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_slice_ids.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_verification_attempts.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_verification_attempts_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_verification_failures.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIFineTuningResponseModel::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_fine_tuning_requested_isValid && m_finetuning_state_isValid && m_is_allowed_to_fine_tune_isValid && m_model_id_isValid && m_slice_ids_isValid && m_verification_attempts_isValid && m_verification_attempts_count_isValid && m_verification_failures_isValid && true;
}

} // namespace OpenAPI
