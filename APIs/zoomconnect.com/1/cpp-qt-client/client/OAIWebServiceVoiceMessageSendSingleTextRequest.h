/**
 * www.zoomconnect.com
 * The world's greatest SMS API
 *
 * The version of the OpenAPI document: 1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIWebServiceVoiceMessageSendSingleTextRequest.h
 *
 * WebServiceVoiceMessageSendSingleTextRequest
 */

#ifndef OAIWebServiceVoiceMessageSendSingleTextRequest_H
#define OAIWebServiceVoiceMessageSendSingleTextRequest_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIWebServiceVoiceMessageSendSingleTextRequest : public OAIObject {
public:
    OAIWebServiceVoiceMessageSendSingleTextRequest();
    OAIWebServiceVoiceMessageSendSingleTextRequest(QString json);
    ~OAIWebServiceVoiceMessageSendSingleTextRequest() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCampaign() const;
    void setCampaign(const QString &campaign);
    bool is_campaign_Set() const;
    bool is_campaign_Valid() const;

    QString getDataField() const;
    void setDataField(const QString &data_field);
    bool is_data_field_Set() const;
    bool is_data_field_Valid() const;

    QString getLanguage() const;
    void setLanguage(const QString &language);
    bool is_language_Set() const;
    bool is_language_Valid() const;

    QString getMessage() const;
    void setMessage(const QString &message);
    bool is_message_Set() const;
    bool is_message_Valid() const;

    QString getRecipientNumber() const;
    void setRecipientNumber(const QString &recipient_number);
    bool is_recipient_number_Set() const;
    bool is_recipient_number_Valid() const;

    qint32 getRetryCount() const;
    void setRetryCount(const qint32 &retry_count);
    bool is_retry_count_Set() const;
    bool is_retry_count_Valid() const;

    qint32 getRetryMaximumInterval() const;
    void setRetryMaximumInterval(const qint32 &retry_maximum_interval);
    bool is_retry_maximum_interval_Set() const;
    bool is_retry_maximum_interval_Valid() const;

    qint32 getRetryMinimumInterval() const;
    void setRetryMinimumInterval(const qint32 &retry_minimum_interval);
    bool is_retry_minimum_interval_Set() const;
    bool is_retry_minimum_interval_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_campaign;
    bool m_campaign_isSet;
    bool m_campaign_isValid;

    QString m_data_field;
    bool m_data_field_isSet;
    bool m_data_field_isValid;

    QString m_language;
    bool m_language_isSet;
    bool m_language_isValid;

    QString m_message;
    bool m_message_isSet;
    bool m_message_isValid;

    QString m_recipient_number;
    bool m_recipient_number_isSet;
    bool m_recipient_number_isValid;

    qint32 m_retry_count;
    bool m_retry_count_isSet;
    bool m_retry_count_isValid;

    qint32 m_retry_maximum_interval;
    bool m_retry_maximum_interval_isSet;
    bool m_retry_maximum_interval_isValid;

    qint32 m_retry_minimum_interval;
    bool m_retry_minimum_interval_isSet;
    bool m_retry_minimum_interval_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIWebServiceVoiceMessageSendSingleTextRequest)

#endif // OAIWebServiceVoiceMessageSendSingleTextRequest_H
